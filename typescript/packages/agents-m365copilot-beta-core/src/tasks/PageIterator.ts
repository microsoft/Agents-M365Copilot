/**
 * -------------------------------------------------------------------------------------------
 * Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.
 * See License in the project root for license information.
 * -------------------------------------------------------------------------------------------
 */

/**
 * @module PageIterator
 */

import {
  Parsable,
  RequestAdapter,
  RequestOption,
  RequestInformation,
  HttpMethod,
  ParsableFactory,
  ErrorMappings,
  Headers,
} from "@microsoft/kiota-abstractions";

/**
 * Signature representing PageCollection
 * @property {any[]} value - The collection value
 * @property {string} [@odata.nextLink] - The nextLink value
 * @property {string} [@odata.deltaLink] - The deltaLink value
 * @property {any} Additional - Any number of additional properties (This is to accept the any additional data returned by in the response to the nextLink request)
 */
export interface PageCollection<T> {
  value: T[];
  odataNextLink?: string;
  odataDeltaLink?: string;
  [Key: string]: any;
}

/**
 * Signature representing callback for page iterator
 * @property {Function} callback - The callback function which should return boolean to continue the continue/stop the iteration.
 */
export type PageIteratorCallback<T> = (data: T) => boolean;

/**
 * Signature to define the request options to be sent during request.
 * The values of the GraphRequestOptions properties are passed to the Graph Request object.
 * @property {Headers} headers - the header options for the request
 * @property {RequestOption[]} options - The middleware options for the request
 */
export interface PagingRequestOptions {
  headers?: Headers;
  requestOption?: RequestOption[];
}

/**
 * @typedef {string} PagingState
 * Type representing the state of the iterator
 */
export type PagingState = "NotStarted" | "Paused" | "IntrapageIteration" | "InterpageIteration" | "Delta" | "Complete";

/**
 * Class representing a PageIterator to iterate over paginated collections.
 * @template T - The type of the items in the collection.
 *
 * This class provides methods to iterate over a collection of items that are paginated.
 * It handles fetching the next set of items when the current page is exhausted.
 * The iteration can be paused and resumed, and the state of the iterator can be queried.
 *
 * The PageIterator uses a callback function to process each item in the collection.
 * The callback function should return a boolean indicating whether to continue the iteration.
 *
 * The PageIterator also supports error handling through error mappings and can be configured
 * with custom request options.
 */
export class PageIterator<T extends Parsable> {
  /**
   * @private
   * Member holding the GraphClient instance
   */
  private readonly requestAdapter: RequestAdapter;

  /**
   * @private
   * Member holding the current page
   */
  private currentPage?: PageCollection<T>;

  /**
   * @private
   * Member holding the current position on the collection
   */
  private cursor: number;

  /**
   * @private
   * Member holding the factory to create the parsable object
   */
  private readonly parsableFactory: ParsableFactory<PageCollection<T>>;

  /**
   * @private
   * Member holding the error mappings
   */
  private readonly errorMappings: ErrorMappings;

  /**
   * @private
   * Member holding the callback for iteration
   */
  private readonly callback: PageIteratorCallback<T>;

  /**
   * @private
   * Member holding the state of the iterator
   */
  private pagingState: PagingState;

  /**
   * @private
   * Member holding the headers for the request
   */
  private readonly options?: PagingRequestOptions;

  /**
   * @public
   * @constructor
   * Creates new instance for PageIterator
   * @returns An instance of a PageIterator
   * @param requestAdapter - The request adapter
   * @param pageResult - The page collection result of T
   * @param callback - The callback function to be called on each item
   * @param errorMappings - The error mappings
   * @param parsableFactory - The factory to create the parsable object collection
   * @param options - The request options to configure the request
   */
  public constructor(
    requestAdapter: RequestAdapter,
    pageResult: PageCollection<T>,
    callback: PageIteratorCallback<T>,
    parsableFactory: ParsableFactory<PageCollection<T>>,
    errorMappings: ErrorMappings,
    options?: PagingRequestOptions,
  ) {
    if (!requestAdapter) {
      const error = new Error("Request adapter is undefined, Please provide a valid request adapter");
      error.name = "Invalid Request Adapter Error";
      throw error;
    }
    if (!pageResult) {
      const error = new Error("Page result is undefined, Please provide a valid page result");
      error.name = "Invalid Page Result Error";
      throw error;
    }
    if (!callback) {
      const error = new Error("Callback is undefined, Please provide a valid callback");
      error.name = "Invalid Callback Error";
      throw error;
    }
    if (!parsableFactory) {
      const error = new Error("Parsable factory is undefined, Please provide a valid parsable factory");
      error.name = "Invalid Parsable Factory Error";
      throw error;
    }
    if (!errorMappings) {
      const error = new Error("Error mappings is undefined, Please provide a valid error mappings");
      error.name = "Invalid Error Mappings Error";
      throw error;
    }
    this.requestAdapter = requestAdapter;
    this.currentPage = pageResult;

    this.cursor = 0;
    this.errorMappings = errorMappings;
    this.parsableFactory = parsableFactory;
    this.callback = callback;

    if (!options) {
      options = {};
    }
    this.options = options;
    this.pagingState = "NotStarted";
  }

  /**
   * @public
   * Getter to get the deltaLink in the current response
   * @returns A deltaLink which is being used to make delta requests in future
   */
  public getOdataDeltaLink(): string | undefined {
    const deltaLink = this.currentPage?.["@odata.deltaLink"] as string | undefined;
    return this.currentPage?.odataDeltaLink ?? deltaLink;
  }

  /**
   * @public
   * Getter to get the nextLink in the current response
   * @returns A nextLink which is being used to make requests in future
   */
  public getOdataNextLink(): string | undefined {
    const nextLink = this.currentPage?.["@odata.nextLink"] as string | undefined;
    return this.currentPage?.odataNextLink ?? nextLink;
  }

  /**
   * @public
   * @async
   * Iterates over the collection and kicks callback for each item on iteration. Fetches next set of data through nextLink and iterates over again
   * This happens until the nextLink is drained out or the user responds with a red flag to continue from callback
   */
  public async iterate() {
    while (true) {
      if (this.pagingState === "Complete") {
        return;
      }

      if (this.pagingState === "Delta") {
        const nextPage = await this.fetchNextPage();
        if (!nextPage) {
          this.pagingState = "Complete";
          return;
        }
        this.currentPage = nextPage;
      }

      const advance = this.enumeratePage();
      if (!advance) {
        return;
      }

      const nextLink = this.getOdataNextLink();
      const deltaLink = this.getOdataDeltaLink();
      const hasNextPageLink = nextLink || deltaLink;

      const pageSize = this.currentPage?.value.length ?? 0;
      const isEndOfPage = !hasNextPageLink && this.cursor >= pageSize;
      if (isEndOfPage) {
        this.pagingState = "Complete";
        return;
      }

      if (hasNextPageLink && this.cursor >= pageSize) {
        this.cursor = 0;
        if (deltaLink) {
          this.pagingState = "Delta";
          return;
        }
        const nextPage = await this.fetchNextPage();
        if (!nextPage) {
          this.pagingState = "Complete";
          return;
        }
        this.currentPage = nextPage;
      }
    }
  }

  /**
   * @public
   * Getter to get the state of the iterator
   */
  public getPagingState(): PagingState {
    return this.pagingState;
  }

  /**
   * @private
   * @async
   * Helper to make a get request to fetch next page with nextLink url and update the page iterator instance with the returned response
   * @returns A promise that resolves to a response data with next page collection
   */
  private async fetchNextPage(): Promise<PageCollection<T> | undefined> {
    this.pagingState = "InterpageIteration";

    const nextLink = this.getOdataNextLink();
    const deltaLink = this.getOdataDeltaLink();

    if (!nextLink && !deltaLink) {
      throw new Error("NextLink and DeltaLink are undefined, Please provide a valid nextLink or deltaLink");
    }

    const requestInformation = new RequestInformation();
    requestInformation.httpMethod = HttpMethod.GET;
    requestInformation.urlTemplate = nextLink ?? deltaLink;
    if (this.options) {
      if (this.options.headers) {
        requestInformation.headers.addAll(this.options.headers);
      }
      if (this.options.requestOption) {
        requestInformation.addRequestOptions(this.options.requestOption);
      }
    }

    return await this.requestAdapter.send<PageCollection<T>>(
      requestInformation,
      this.parsableFactory,
      this.errorMappings,
    );
  }

  /**
   * @public
   * @async
   * To resume the iteration
   * Note: This internally calls the iterate method, It's just for more readability.
   */
  public async resume() {
    return this.iterate();
  }

  /**
   * @private
   * Iterates over a collection by enqueuing entries one by one and kicking the callback with the enqueued entry
   * @returns A boolean indicating the continue flag to process next page
   */
  private enumeratePage(): boolean {
    this.pagingState = "IntrapageIteration";

    let keepIterating = true;

    const pageItems = this.currentPage?.value;

    // pageItems should never be undefined at this point
    if (!pageItems) {
      throw new Error("Page items are undefined, Please provide a valid page items");
    }

    if (pageItems.length === 0) {
      return true;
    }

    // continue iterating from cursor
    for (let i = this.cursor; i < pageItems.length; i++) {
      keepIterating = this.callback(pageItems[i]);
      this.cursor = i + 1;
      if (!keepIterating) {
        this.pagingState = "Paused";
        break;
      }
    }

    return keepIterating;
  }
}
