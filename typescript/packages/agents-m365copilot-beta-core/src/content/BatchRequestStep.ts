/**
 * -------------------------------------------------------------------------------------------
 * Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.
 * See License in the project root for license information.
 * -------------------------------------------------------------------------------------------
 */

/**
 * @module BatchItem
 */

/**
 * @interface
 * Signature represents key value pair object
 */
import {
  Parsable,
  ParseNode,
  SerializationWriter,
  createUntypedNodeFromDiscriminatorValue,
  RequestInformation,
  createGuid,
  RequestAdapter,
} from "@microsoft/kiota-abstractions";
import { defaultUrlReplacementPairs } from "../utils/Constants.js";

/**
 * @interface
 * Signature represents payload structure for batch request and response
 */
export interface BatchRequestStep {
  readonly id: string;
  method: string;
  url: string;
  headers?: Record<string, string> | Record<string, string[]> | null;
  body?: ArrayBuffer | null;
  dependsOn?: string[];
}

/**
 * @interface
 * Signature represents unwrapped payload structure for batch response
 */
export interface BatchResponse {
  id: string;
  headers?: Record<string, string> | null;
  body?: ArrayBuffer | null;
  status?: number;
}

/**
 * @interface
 * Signature representing Batch request body
 */
export interface BatchRequestBody {
  requests: BatchRequestStep[];
}

/**
 * @interface
 * Signature representing Batch response body
 */
export interface BatchResponseBody {
  responses: BatchResponse[];
}

/**
 * Serializes the batch request body
 * @param writer
 * @param batchRequestBody
 */
export const serializeBatchRequestBody = (
  writer: SerializationWriter,
  batchRequestBody: Partial<BatchRequestBody> | undefined | null = {},
): void => {
  if (batchRequestBody) {
    writer.writeCollectionOfObjectValues("requests", batchRequestBody.requests, serializeBatchItem);
  }
};

/**
 * Serializes the batch item
 * @param writer
 * @param batchRequestData
 */
export const serializeBatchItem = (
  writer: SerializationWriter,
  batchRequestData: Partial<BatchRequestStep> | undefined | null = {},
): void => {
  if (batchRequestData) {
    writer.writeStringValue("id", batchRequestData.id);
    writer.writeStringValue("method", batchRequestData.method);
    writer.writeStringValue("url", batchRequestData.url);
    writer.writeObjectValue("headers", batchRequestData.headers);
    // get contentType from headers
    // N:B watch out for text encoding as it might not be utf-8
    const body = batchRequestData.body;
    if (body) {
      const contentType = batchRequestData.headers?.["Content-Type"];
      if (contentType === "application/json") {
        // convert body to json
        writer.writeObjectValue("body", JSON.parse(new TextDecoder().decode(body)));
      } else {
        writer.writeByteArrayValue("body", body);
      }
    }
    writer.writeCollectionOfPrimitiveValues("dependsOn", batchRequestData.dependsOn);
  }
};

/**
 * BatchResponseCollection ParsableFactory
 * @param _parseNode
 */
export const createBatchResponseContentFromDiscriminatorValue = (
  _parseNode: ParseNode | undefined,
): ((instance?: Parsable) => Record<string, (node: ParseNode) => void>) => {
  return deserializeIntoBatchResponseContent;
};

/**
 * Deserializes the batch response body
 * @param batchResponseBody
 */
export const deserializeIntoBatchResponseContent = (
  batchResponseBody: Partial<BatchResponseBody> | undefined = {},
): Record<string, (node: ParseNode) => void> => {
  return {
    responses: n => {
      batchResponseBody.responses = n.getCollectionOfObjectValues(createBatchResponseFromDiscriminatorValue);
    },
  };
};

/**
 * BatchRequestStep ParsableFactory
 * @param _parseNode
 */
export const createBatchResponseFromDiscriminatorValue = (
  _parseNode: ParseNode | undefined,
): ((instance?: Parsable) => Record<string, (node: ParseNode) => void>) => {
  return deserializeIntoBatchResponse;
};

/**
 * Deserializes the batch item
 * @param batchResponse
 */
export const deserializeIntoBatchResponse = (
  batchResponse: Partial<BatchResponse> | undefined = {},
): Record<string, (node: ParseNode) => void> => {
  return {
    id: n => {
      batchResponse.id = n.getStringValue();
    },
    headers: n => {
      batchResponse.headers = n.getObjectValue<Record<string, string>>(createUntypedNodeFromDiscriminatorValue);
    },
    body: n => {
      batchResponse.body = n.getByteArrayValue();
    },
    status: n => {
      batchResponse.status = n.getNumberValue();
    },
  };
};

/**
 * Converts a `RequestInformation` object to a `BatchRequestStep`.
 * @param {RequestAdapter} requestAdapter - The request adapter containing the base URL.
 * @param {RequestInformation} requestInformation - The request information to convert.
 * @param {string} [batchId] - Optional batch ID to use for the `BatchRequestStep`.
 * @returns {BatchRequestStep} The converted `BatchRequestStep`.
 */
export const convertRequestInformationToBatchItem = (
  requestAdapter: RequestAdapter,
  requestInformation: RequestInformation,
  batchId?: string,
): BatchRequestStep => {
  if (requestInformation.pathParameters && requestInformation.pathParameters.baseurl === undefined) {
    requestInformation.pathParameters.baseurl = requestAdapter.baseUrl;
  }

  let uriString = requestInformation.URL;

  Object.keys(defaultUrlReplacementPairs).forEach(replacementKey => {
    uriString = uriString.replace(replacementKey, defaultUrlReplacementPairs[replacementKey]);
  });

  const body = requestInformation.content;

  let headers: Record<string, any> | undefined;
  if (headers !== undefined) {
    headers = Object.fromEntries(requestInformation.headers.entries()) as unknown as Record<string, string>;
  }

  const url = uriString.replace(requestAdapter.baseUrl, "");

  const method = requestInformation.httpMethod?.toString();

  return {
    id: batchId ?? createGuid(),
    method: method!,
    url,
    headers,
    body,
  };
};
