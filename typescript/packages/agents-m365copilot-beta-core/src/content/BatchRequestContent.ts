import { RequestAdapter, RequestInformation, ErrorMappings } from "@microsoft/kiota-abstractions";
import { BatchRequestStep, BatchRequestBody, convertRequestInformationToBatchItem } from "./BatchRequestStep.js";
import { BatchResponseContent } from "./BatchResponseContent.js";
import { BatchRequestBuilder } from "./BatchRequestBuilder.js";

/**
 * -------------------------------------------------------------------------------------------
 * Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.
 * See License in the project root for license information.
 * -------------------------------------------------------------------------------------------
 */

/**
 * @module BatchRequestContent
 */

/**
 * Represents the content of a batch request.
 */
export class BatchRequestContent {
  /**
   * @private
   * @static
   * Limit for number of requests {@link - https://developer.microsoft.com/en-us/graph/docs/concepts/known_issues#json-batching}
   */
  private static get requestLimit() {
    return 20;
  }

  /**
   * @public
   * To keep track of requests, key will be id of the request and value will be the request json
   */
  public requests: Map<string, BatchRequestStep>;

  /**
   * @private
   * @static
   * Executes the requests in the batch request content
   */
  private readonly requestAdapter: RequestAdapter;

  /**
   * @private
   * @static
   * Error mappings to be used while deserializing the response
   */
  private readonly errorMappings: ErrorMappings;

  /**
   * Creates an instance of BatchRequestContent.
   * @param {RequestAdapter} requestAdapter - The request adapter to be used for executing the requests.
   * @param {ErrorMappings} errorMappings - The error mappings to be used while deserializing the response.
   * @throws {Error} If the request adapter is undefined.
   * @throws {Error} If the error mappings are undefined.
   */
  constructor(requestAdapter: RequestAdapter, errorMappings: ErrorMappings) {
    this.requests = new Map<string, BatchRequestStep>();
    if (!requestAdapter) {
      const error = new Error("Request adapter is undefined, Please provide a valid request adapter");
      error.name = "Invalid Request Adapter Error";
      throw error;
    }
    this.requestAdapter = requestAdapter;
    if (!errorMappings) {
      const error = new Error("Error mappings are undefined, Please provide a valid error mappings");
      error.name = "Invalid Error Mappings Error";
      throw error;
    }
    this.errorMappings = errorMappings;
  }

  /**
   * @private
   * @static
   * Validates the dependency chain of the requests
   *
   * Note:
   * Individual requests can depend on other individual requests. Currently, requests can only depend on a single other request, and must follow one of these three patterns:
   * 1. Parallel - no individual request states a dependency in the dependsOn property.
   * 2. Serial - all individual requests depend on the previous individual request.
   * 3. Same - all individual requests that state a dependency in the dependsOn property, state the same dependency.
   * As JSON batching matures, these limitations will be removed.
   * @see {@link https://developer.microsoft.com/en-us/graph/docs/concepts/known_issues#json-batching}
   *
   * @param {Map<string, BatchRequestStep>} requests - The map of requests.
   * @returns The boolean indicating the validation status
   */
  private static validateDependencies(requests: Map<string, BatchRequestStep>): boolean {
    const isParallel = (reqs: Map<string, BatchRequestStep>): boolean => {
      const iterator = reqs.entries();
      let cur = iterator.next();
      while (!cur.done) {
        const curReq = cur.value[1];
        if (curReq.dependsOn !== undefined && curReq.dependsOn.length > 0) {
          return false;
        }
        cur = iterator.next();
      }
      return true;
    };
    const isSerial = (reqs: Map<string, BatchRequestStep>): boolean => {
      const iterator = reqs.entries();
      let cur = iterator.next();
      if (cur.done || cur.value === undefined) return false;
      const firstRequest: BatchRequestStep = cur.value[1];
      if (firstRequest.dependsOn !== undefined && firstRequest.dependsOn.length > 0) {
        return false;
      }
      let prev = cur;
      cur = iterator.next();
      while (!cur.done) {
        const curReq: BatchRequestStep = cur.value[1];
        if (
          curReq.dependsOn === undefined ||
          curReq.dependsOn.length !== 1 ||
          curReq.dependsOn[0] !== prev.value[1].id
        ) {
          return false;
        }
        prev = cur;
        cur = iterator.next();
      }
      return true;
    };
    const isSame = (reqs: Map<string, BatchRequestStep>): boolean => {
      const iterator = reqs.entries();
      let cur = iterator.next();
      if (cur.done || cur.value === undefined) return false;
      const firstRequest: BatchRequestStep = cur.value[1];
      let dependencyId: string;
      if (firstRequest.dependsOn === undefined || firstRequest.dependsOn.length === 0) {
        dependencyId = firstRequest.id;
      } else {
        if (firstRequest.dependsOn.length === 1) {
          const fDependencyId = firstRequest.dependsOn[0];
          if (fDependencyId !== firstRequest.id && reqs.has(fDependencyId)) {
            dependencyId = fDependencyId;
          } else {
            return false;
          }
        } else {
          return false;
        }
      }
      cur = iterator.next();
      while (!cur.done) {
        const curReq = cur.value[1];
        if ((curReq.dependsOn === undefined || curReq.dependsOn.length === 0) && dependencyId !== curReq.id) {
          return false;
        }
        if (curReq.dependsOn !== undefined && curReq.dependsOn.length !== 0) {
          if (curReq.dependsOn.length === 1 && (curReq.id === dependencyId || curReq.dependsOn[0] !== dependencyId)) {
            return false;
          }
          if (curReq.dependsOn.length > 1) {
            return false;
          }
        }
        cur = iterator.next();
      }
      return true;
    };
    if (requests.size === 0) {
      const error = new Error("Empty requests map, Please provide at least one request.");
      error.name = "Empty Requests Error";
      throw error;
    }
    return isParallel(requests) || isSerial(requests) || isSame(requests);
  }

  /**
   * @public
   * Adds a request to the batch request content
   * @param {BatchRequestStep} request - The request value
   * @returns The id of the added request
   */
  private addRequest(request: BatchRequestStep): string {
    const limit = BatchRequestContent.requestLimit;
    if (request.id === "") {
      const error = new Error(`Id for a request is empty, Please provide an unique id`);
      error.name = "Empty Id For Request";
      throw error;
    }
    if (this.requests.size === limit) {
      const error = new Error(`Maximum requests limit exceeded, Max allowed number of requests are ${limit}`);
      error.name = "Limit Exceeded Error";
      throw error;
    }
    if (this.requests.has(request.id)) {
      const error = new Error(`Adding request with duplicate id ${request.id}, Make the id of the requests unique`);
      error.name = "Duplicate RequestId Error";
      throw error;
    }
    this.requests.set(request.id, request);
    return request.id;
  }

  /**
   * @public
   * Adds multiple requests to the batch request content
   * @param {BatchRequestStep[]} requests - The request value
   */
  public addRequests(requests: BatchRequestStep[]) {
    // loop and add this request
    requests.forEach(request => {
      this.addRequest(request);
    });
  }

  /**
   * @public
   * Receives a request information object, converts it and adds it to the batch request execution chain
   * @param requestInformation - The request information object
   * @param batchId - The batch id to be used for the request
   */
  public addBatchRequest(requestInformation: RequestInformation, batchId?: string): BatchRequestStep {
    const batchItem = convertRequestInformationToBatchItem(this.requestAdapter, requestInformation, batchId);
    this.addRequest(batchItem);
    return batchItem;
  }

  /**
   * @public
   * Gets the content of the batch request
   * @returns The batch request collection
   */
  public readonly getContent = (): BatchRequestBody => {
    const content = {
      requests: Array.from(this.requests.values()),
    };
    if (!BatchRequestContent.validateDependencies(this.requests)) {
      const error = new Error("Invalid dependency chain found in the requests, Please provide valid dependency chain");
      error.name = "Invalid Dependency Chain Error";
      throw error;
    }
    return content;
  };

  /**
   * @public
   * @async
   * Executes the batch request
   */
  public async postAsync(): Promise<BatchResponseContent | undefined> {
    const requestBuilder = new BatchRequestBuilder(this.requestAdapter, this.errorMappings);
    return await requestBuilder.postBatchResponseContentAsync(this);
  }
}
