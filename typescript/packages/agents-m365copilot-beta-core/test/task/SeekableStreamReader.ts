import { assert, describe, it } from "vitest";
import { SeekableStreamReader } from "../../src";

function createRandoReadableStream(value: string): ReadableStream<Uint8Array> {
  return new ReadableStream<Uint8Array>({
    start: controller => {
      const encoder = new TextEncoder();
      const chunk = encoder.encode(value);
      controller.enqueue(chunk);
      controller.close();
    },
  });
}

describe("SeekableStreamReader tests", () => {
  it("should read the sections of the stream", async () => {
    const value = veryLongRandomText;
    const stream = createRandoReadableStream(value);

    const reader = new SeekableStreamReader(stream);

    // split the stream into pairs 20 pairs of start and end
    const pairs = [];
    const size = new TextEncoder().encode(veryLongRandomText).length;
    const units = 4;

    const batchSize = Math.round(size / units);
    for (let i = 0; i < value.length; i += batchSize) {
      const start: number = pairs.length === 0 ? i : pairs[pairs.length - 1][1] + 1;
      pairs.push([start, Math.min(start + batchSize, value.length)]);
    }

    const decoder = new TextDecoder();
    let reconstructedString = "";
    for (const [start, end] of pairs) {
      const section = await reader.readSection(start, end);
      reconstructedString += decoder.decode(section);
    }
    assert.equal(value, reconstructedString, "Reconstructed string should match the original");
  });
});

const veryLongRandomText = "This is a very long text that will be used to test the SeekableStreamReader class.".repeat(
  20,
); //.split('').sort(() => 0.5 - Math.random()).join('');
