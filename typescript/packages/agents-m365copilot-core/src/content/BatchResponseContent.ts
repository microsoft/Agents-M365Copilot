/**
 * -------------------------------------------------------------------------------------------
 * Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.
 * See License in the project root for license information.
 * -------------------------------------------------------------------------------------------
 */

/**
 * @module BatchResponseContent
 */

import { BatchResponseBody, BatchResponse } from "./BatchRequestStep.js";
import { Parsable, ParsableFactory, ParseNodeFactoryRegistry } from "@microsoft/kiota-abstractions";

/**
 * @class
 * Class that handles BatchResponseContent
 */
export class BatchResponseContent {
  /**
   * To hold the responses
   */
  private readonly responses: Map<string, BatchResponse>;

  /**
   * @public
   * @constructor
   * Creates the BatchResponseContent instance
   * @param {BatchResponseBody} response - The response body returned for batch request from server
   * @returns An instance of a BatchResponseContent
   */
  public constructor(response: BatchResponseBody) {
    this.responses = new Map();
    this.update(response);
  }

  /**
   * @private
   * Updates the Batch response content instance with given responses.
   * @param {BatchResponseBody} response - The response json representing batch response message
   * @returns Nothing
   */
  private update(response: BatchResponseBody): void {
    const responses = response.responses;
    for (let i = 0, l = responses.length; i < l; i++) {
      this.responses.set(responses[i].id, responses[i]);
    }
  }

  /**
   * @public
   * To get the response of a request for a given request id
   * @param {string} requestId - The request id value
   * @returns The Response object instance for the particular request
   */
  public getResponseById(requestId: string): BatchResponse | undefined {
    return this.responses.get(requestId);
  }

  /**
   * Retrieves a parsable response by request ID.
   * @template T - The type of the parsable response.
   * @param {string} requestId - The request ID value.
   * @param parseNodeFactoryRegistry - The registry to create parse nodes.
   * @param {ParsableFactory<T>} factory - The factory to create the parsable response.
   * @returns {T | undefined} The parsable response object instance for the particular request, or undefined if not found.
   */
  public getParsableResponseById<T extends Parsable>(
    requestId: string,
    parseNodeFactoryRegistry: ParseNodeFactoryRegistry,
    factory: ParsableFactory<T>,
  ): T | undefined {
    const res = this.responses.get(requestId);
    if (res?.body) {
      const result = parseNodeFactoryRegistry.deserializeFromJson(res.body, factory);
      return result as T;
    }
    return undefined;
  }

  /**
   * @public
   * To get all the responses of the batch request
   * @returns The Map object containing the response objects
   */
  public getResponses(): Map<string, BatchResponse> {
    return this.responses;
  }

  /**
   * @public
   * To get the iterator for the responses
   * @returns The Iterable generator for the response objects
   */
  public *getResponsesIterator(): IterableIterator<[string, BatchResponse]> {
    const iterator = this.responses.entries();
    let cur = iterator.next();
    while (!cur.done) {
      yield cur.value;
      cur = iterator.next();
    }
  }

  /**
   * Retrieves the status codes of all responses in the batch request.
   * @returns {Promise<Map<string, number>>} A promise that resolves to a map of request IDs to their status codes.
   * @throws {Error} If a status code is not found for a request ID.
   */
  public getResponsesStatusCodes(): Promise<Map<string, number>> {
    return new Promise((resolve, reject) => {
      const statusCodes = new Map<string, number>();
      const iterator = this.responses.entries();
      let cur = iterator.next();
      while (!cur.done) {
        const [key, value] = cur.value;
        if (value.status === undefined) {
          reject(new Error(`Status code not found for request ID: ${key}`));
          return;
        }
        statusCodes.set(key, value.status);
        cur = iterator.next();
      }
      resolve(statusCodes);
    });
  }
}
