/**
 * -------------------------------------------------------------------------------------------
 * Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.
 * See License in the project root for license information.
 * -------------------------------------------------------------------------------------------
 */

/**
 * @module BatchRequestContentCollection
 */

import { ErrorMappings, RequestAdapter, RequestInformation } from "@microsoft/kiota-abstractions";
import { BatchRequestStep, convertRequestInformationToBatchItem } from "./BatchRequestStep.js";
import { BatchRequestContent } from "./BatchRequestContent.js";
import { BatchRequestBuilder } from "./BatchRequestBuilder.js";
import { BatchResponseContentCollection } from "./BatchResponseContentCollection.js";

/**
 * The default limit for the number of requests in a single batch.
 */
const DEFAULT_BATCH_LIMIT = 20;

/**
 * Represents the content of a batch request.
 */
export class BatchRequestContentCollection {
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
   * @private
   * @static
   * The maximum number of requests that can be sent in a single batch request
   */
  private readonly batchLimit: number;

  /**
   * @private
   * @static
   * The list of requests to be sent in the batch request
   */
  public readonly batchRequestSteps: BatchRequestStep[] = [];

  /**
   * @public
   * @constructor
   * Creates the BatchRequestContentCollection instance
   * @param {RequestAdapter} requestAdapter - The request adapter to be used for executing the requests
   * @param {ErrorMappings} errorMappings - The error mappings to be used while deserializing the response
   * @param batchLimit - The maximum number of requests that can be sent in a single batch request
   */
  constructor(requestAdapter: RequestAdapter, errorMappings: ErrorMappings, batchLimit: number) {
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

    if (!batchLimit) {
      batchLimit = DEFAULT_BATCH_LIMIT;
    }
    this.batchLimit = batchLimit;
  }

  /**
   * Executes the batch requests asynchronously.
   *
   * @returns {Promise<BatchResponseContent | undefined>} A promise that resolves to the batch response content or undefined.
   * @throws {Error} If the batch limit is exceeded.
   */
  public async postAsync(): Promise<BatchResponseContentCollection | undefined> {
    const requestBuilder = new BatchRequestBuilder(this.requestAdapter, this.errorMappings);
    return await requestBuilder.postBatchRequestContentCollectionAsync(this);
  }

  /**
   * @public
   * Returns the batch request content
   */
  public getBatchResponseContents(): BatchRequestContent[] {
    const batches = this.chunkArray(this.batchRequestSteps, this.batchLimit);
    const batchRequestContent: BatchRequestContent[] = [];
    for (const batch of batches) {
      const requestContent = new BatchRequestContent(this.requestAdapter, this.errorMappings);
      requestContent.addRequests(batch);
      batchRequestContent.push(requestContent);
    }
    return batchRequestContent;
  }

  /**
   * @public
   * Receives a request information object, converts it and adds it to the batch request execution chain
   * @param requestInformation - The request information object
   * @param batchId - The batch id to be used for the request
   */
  public addBatchRequest(requestInformation: RequestInformation, batchId?: string): BatchRequestStep {
    const batchItem = convertRequestInformationToBatchItem(this.requestAdapter, requestInformation, batchId);
    this.batchRequestSteps.push(batchItem);
    return batchItem;
  }

  /**
   * @public
   * Adds multiple requests to the batch request content
   * @param {BatchRequestStep[]} requests - The request value
   */
  public addRequests(requests: BatchRequestStep[]) {
    // loop and add this request
    requests.forEach(request => {
      this.batchRequestSteps.push(request);
    });
  }

  /**
   * @private
   * Splits the array into chunks of the specified size
   * @param array - The array to be split
   * @param chunkSize - The size of each chunk
   */
  private chunkArray<T>(array: T[], chunkSize: number): T[][] {
    const result: T[][] = [];
    for (let i = 0; i < array.length; i += chunkSize) {
      result.push(array.slice(i, i + chunkSize));
    }
    return result;
  }
}
