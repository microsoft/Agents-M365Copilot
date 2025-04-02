/**
 * -------------------------------------------------------------------------------------------
 * Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.
 * See License in the project root for license information.
 * -------------------------------------------------------------------------------------------
 */

/**
 * @module BatchResponseContentCollection
 */

import { BatchResponseContent } from "./BatchResponseContent.js";
import { BatchResponse } from "./BatchRequestStep.js";
import { Parsable, ParsableFactory, ParseNodeFactoryRegistry } from "@microsoft/kiota-abstractions";

/**
 * Represents a collection of BatchResponseContent.
 */
export class BatchResponseContentCollection {
  /**
   * An array of BatchResponseContent.
   */
  public readonly batchResponseContent: BatchResponseContent[] = [];

  /**
   * Initializes a new instance of the BatchResponseContentCollection class.
   * @param responseContents - An array of BatchResponseContent.
   */
  public constructor(responseContents: BatchResponseContent[]) {
    this.batchResponseContent = responseContents;
  }

  /**
   * Finds the BatchResponseContent containing the specified request ID.
   * @param requestId - The ID of the request.
   * @returns The BatchResponseContent containing the request ID, or undefined if not found.
   */
  private getBatchContentContaining(requestId: string): BatchResponseContent | undefined {
    return this.batchResponseContent.find(batchResponseContent => {
      return batchResponseContent.getResponseById(requestId) !== undefined;
    });
  }

  /**
   * Gets the BatchResponse by the specified request ID.
   * @param requestId - The ID of the request.
   * @returns The BatchResponse with the specified request ID, or undefined if not found.
   */
  private getResponseById(requestId: string): BatchResponse | undefined {
    const batchResponseContent = this.getBatchContentContaining(requestId);
    if (batchResponseContent) {
      return batchResponseContent.getResponseById(requestId);
    }
    return undefined;
  }

  /**
   * Gets the parsable response by the specified request ID.
   * @param requestId - The ID of the request.
   * @param parseNodeFactoryRegistry - The registry to create parse nodes.
   * @param factory - The factory to create the Parsable instance.
   * @returns The parsable response, or undefined if not found.
   */
  public getParsableResponseById<T extends Parsable>(
    requestId: string,
    parseNodeFactoryRegistry: ParseNodeFactoryRegistry,
    factory: ParsableFactory<T>,
  ): T | undefined {
    const res = this.getResponseById(requestId);
    if (res?.body) {
      const result = parseNodeFactoryRegistry.deserializeFromJson(res.body, factory);
      return result as T;
    }
    return undefined;
  }

  /**
   * Gets the status codes of all responses.
   * @returns A promise that resolves to a map of request IDs to status codes.
   */
  public async getResponsesStatusCodes(): Promise<Map<string, number>> {
    const statusCodesArray = await Promise.all(
      this.batchResponseContent.map(batchResponseContent => {
        return batchResponseContent.getResponsesStatusCodes();
      }),
    );
    const mergedStatusCodes = new Map<string, number>();
    statusCodesArray.forEach(map => {
      map.forEach((value, key) => {
        mergedStatusCodes.set(key, value);
      });
    });
    return mergedStatusCodes;
  }
}
