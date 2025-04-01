import { assert, describe, it } from "vitest";
import { PageCollection, PageIterator, PageIteratorCallback } from "../../src";
import { ErrorMappings, Headers, Parsable, ParseNode } from "@microsoft/kiota-abstractions";
// @ts-ignore
import { DummyRequestAdapter } from "../utils/DummyRequestAdapter";

const value = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];

const getPageCollection = () => {
  return {
    value: [...value],
    additionalContent: "additional content",
  };
};

const getPageCollectionWithNext = () => {
  return {
    value: [...value],
    "@odata.nextLink": "nextURL",
    additionalContent: "additional content",
  };
};

export function createPageCollectionFromDiscriminatorValue(
  parseNode: ParseNode | undefined,
): (instance?: Parsable) => Record<string, (node: ParseNode) => void> {
  return deserializeIntoPageCollection;
}

export function deserializeIntoPageCollection(
  baseDeltaFunctionResponse: Partial<PageCollection<number>> | undefined = {},
): Record<string, (node: ParseNode) => void> {
  return {
    backingStoreEnabled: n => {
      baseDeltaFunctionResponse.backingStoreEnabled = true;
    },
    "@odata.deltaLink": n => {
      baseDeltaFunctionResponse.odataDeltaLink = n.getStringValue();
    },
    "@odata.nextLink": n => {
      baseDeltaFunctionResponse.odataNextLink = n.getStringValue();
    },
  };
}

const getEmptyPageCollection = () => {
  return {
    value: [],
  };
};

const getEmptyPageCollectionWithNext = () => {
  return {
    value: [],
    "@odata.nextLink": "nextURL",
  };
};

// eslint-disable-next-line @typescript-eslint/no-unused-vars
const truthyCallback: PageIteratorCallback<number> = data => {
  return true;
};

let halfWayCallbackCounter = 5;
// eslint-disable-next-line @typescript-eslint/no-unused-vars
const halfWayCallback: PageIteratorCallback<number> = data => {
  halfWayCallbackCounter--;
  return halfWayCallbackCounter !== 0;
};

const errorMappings: ErrorMappings = {
  XXX: parseNode => createGraphErrorFromDiscriminatorValue(parseNode),
};

export const createGraphErrorFromDiscriminatorValue = (
  _parseNode: ParseNode | undefined,
): ((instance?: Parsable) => Record<string, (node: ParseNode) => void>) => {
  return deserializeIntoGraphError;
};

/**
 * Deserializes the batch item
 * @param graphError
 */
export const deserializeIntoGraphError = (
  graphError: Partial<Error> | undefined = {},
): Record<string, (node: ParseNode) => void> => {
  return {};
};
const adapter = new DummyRequestAdapter();

describe("PageIterator tests", () => {
  describe("Constructor", () => {
    it("Should create instance", () => {
      const pageIterator = new PageIterator(
        adapter,
        getPageCollection(),
        truthyCallback,
        createPageCollectionFromDiscriminatorValue,
        errorMappings,
      );
      assert(pageIterator instanceof PageIterator);
    });
  });

  describe("iterate", () => {
    it("Should iterate over a complete collection without nextLink", async () => {
      const pageIterator = new PageIterator(
        adapter,
        getPageCollection(),
        truthyCallback,
        createPageCollectionFromDiscriminatorValue,
        errorMappings,
      );
      await pageIterator.iterate();
      assert.equal(pageIterator.getPagingState(), "Complete");
    });
    it("Should execute post with passed headers", async () => {
      const headers = new Headers();
      headers.add("Test", "Value");
      const pageIterator = new PageIterator(
        adapter,
        getPageCollectionWithNext(),
        truthyCallback,
        createPageCollectionFromDiscriminatorValue,
        errorMappings,
        {
          headers,
        },
      );
      await pageIterator.iterate();
      const requests = adapter.getRequests()[0];
      assert.isTrue(requests.headers.has("Test"));
    });

    it("Should not mutate the collection", async () => {
      const collection = getPageCollection();
      const pageIterator = new PageIterator(
        adapter,
        getPageCollection(),
        truthyCallback,
        createPageCollectionFromDiscriminatorValue,
        errorMappings,
      );
      await pageIterator.iterate();
      assert.deepEqual(collection, getPageCollection());
    });

    it("Should not iterate over an empty collection", async () => {
      const pageIterator = new PageIterator(
        adapter,
        getPageCollection(),
        truthyCallback,
        createPageCollectionFromDiscriminatorValue,
        errorMappings,
      );
      halfWayCallbackCounter = 1;
      await pageIterator.iterate();
      assert.equal(halfWayCallbackCounter, 1);
    });

    it("Should break in the middle way", async () => {
      const pageIterator = new PageIterator(
        adapter,
        getPageCollection(),
        halfWayCallback,
        createPageCollectionFromDiscriminatorValue,
        errorMappings,
      );
      halfWayCallbackCounter = 5;
      await pageIterator.iterate();
      assert.equal(pageIterator.getPagingState(), "Paused");
    });
  });

  describe("resume", () => {
    it("Should start from the place where it left the iteration", async () => {
      const pageIterator = new PageIterator(
        adapter,
        getPageCollection(),
        halfWayCallback,
        createPageCollectionFromDiscriminatorValue,
        errorMappings,
      );
      halfWayCallbackCounter = 5;
      await pageIterator.iterate();
      assert.equal(pageIterator.getPagingState(), "Paused");
      await pageIterator.resume();
      assert.equal(pageIterator.getPagingState(), "Complete");
    });
  });

  describe("PagingState", () => {
    it("Should return false for incomplete iteration", async () => {
      const pageIterator = new PageIterator(
        adapter,
        getPageCollection(),
        halfWayCallback,
        createPageCollectionFromDiscriminatorValue,
        errorMappings,
      );
      halfWayCallbackCounter = 5;
      await pageIterator.iterate();
      assert.equal(pageIterator.getPagingState(), "Paused");
    });

    it("Should return delta state when fetching a delta page", async () => {
      const deltaCollection = {
        value: [...value],
        additionalContent: "additional content",
        "@odata.deltaLink": "deltaURL",
      };

      const pageIterator = new PageIterator(
        adapter,
        deltaCollection,
        truthyCallback,
        createPageCollectionFromDiscriminatorValue,
        errorMappings,
      );
      await pageIterator.iterate();
      assert.equal(pageIterator.getPagingState(), "Delta");

      // second iterate call should complete the iteration

      adapter.setResponse(getPageCollection());
      await pageIterator.iterate();
      assert.equal(pageIterator.getPagingState(), "Complete");
    });

    it("Should return true for complete iteration", async () => {
      const pageIterator = new PageIterator(
        adapter,
        getPageCollection(),
        truthyCallback,
        createPageCollectionFromDiscriminatorValue,
        errorMappings,
      );
      await pageIterator.iterate();
      assert.equal(pageIterator.getPagingState(), "Complete");
    });
  });
});
