/**
 * -------------------------------------------------------------------------------------------
 * Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.
 * See License in the project root for license information.
 * -------------------------------------------------------------------------------------------
 */

import {
  ErrorMappings,
  Headers,
  HttpMethod,
  Parsable,
  ParsableFactory,
  RequestAdapter,
  RequestInformation,
  type AdditionalDataHolder,
} from "@microsoft/kiota-abstractions";
import { HeadersInspectionOptions } from "@microsoft/kiota-http-fetchlibrary";
import { UploadResult, UploadSession } from "./LargeFileUploadTask.js";
import { SeekableStreamReader } from "./SeekableStreamReader.js";

const binaryContentType = "application/octet-stream";

/**
 * @class
 * Represents a slice of a file to be uploaded.
 *
 * @template T - The type of the parsable object.
 */
export class UploadSlice<T extends Parsable> {
  /**
   * Constructs an instance of the UploadSlice class.
   *
   * @param {RequestAdapter} requestAdapter - The request adapter to use for making HTTP requests.
   * @param {string} sessionUrl - The URL of the upload session.
   * @param {number} rangeBegin - The beginning byte position of the slice.
   * @param {number} rangeEnd - The ending byte position of the slice.
   * @param {number} totalSessionLength - The total length of the upload session.
   * @param {ParsableFactory<T>} parsableFactory - The factory to create parsable objects.
   * @param {ErrorMappings} errorMappings - The mappings for handling errors.
   * @param {SeekableStreamReader} seekableStreamReader - The stream reader to read the file slice.
   */
  constructor(
    readonly requestAdapter: RequestAdapter,
    readonly sessionUrl: string,
    readonly rangeBegin: number,
    readonly rangeEnd: number,
    readonly totalSessionLength: number,
    readonly parsableFactory: ParsableFactory<T>,
    readonly errorMappings: ErrorMappings,
    readonly seekableStreamReader: SeekableStreamReader,
  ) {}

  /**
   * Uploads a slice of the file to the server.
   *
   * @returns {Promise<UploadResult<T> | undefined>} - The result of the upload operation.
   */
  public async uploadSlice(): Promise<UploadResult<T> | UploadSession | undefined> {
    const data = await this.seekableStreamReader.readSection(this.rangeBegin, this.rangeEnd);
    const requestInformation = new RequestInformation(HttpMethod.PUT, this.sessionUrl);
    requestInformation.headers = new Headers([
      ["Content-Range", new Set([`bytes ${this.rangeBegin}-${this.rangeEnd}/${this.totalSessionLength}`])],
      ["Content-Length", new Set([`${this.rangeEnd - this.rangeBegin}`])],
    ]);
    requestInformation.setStreamContent(data, binaryContentType);

    const headerOptions = new HeadersInspectionOptions({ inspectResponseHeaders: true });
    requestInformation.addRequestOptions([headerOptions]);

    const itemResponse = await this.requestAdapter.send<T>(
      requestInformation,
      this.parsableFactory,
      this.errorMappings,
    );

    const locations = headerOptions.getResponseHeaders().get("location");

    if (itemResponse) {
      let sessionResponse = this.isUploadSessionResponse(itemResponse);
      if (sessionResponse) {
        return sessionResponse;
      }
      const { additionalData } = itemResponse as Partial<AdditionalDataHolder>;
      if (additionalData) {
        sessionResponse = this.isUploadSessionResponse(additionalData);
        if (sessionResponse) {
          return sessionResponse;
        }
      }
    }

    return {
      itemResponse,
      location: locations ? (locations as unknown as string[])[0] : undefined,
    };
  }

  private isUploadSessionResponse(item: Parsable | AdditionalDataHolder): UploadSession | null {
    const { expirationDateTime, nextExpectedRanges } = item as Partial<UploadSession>;
    if (nextExpectedRanges) {
      return {
        expirationDateTime,
        nextExpectedRanges,
      };
    }
    return null;
  }
}
