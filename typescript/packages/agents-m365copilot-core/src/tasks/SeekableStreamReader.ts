/**
 * -------------------------------------------------------------------------------------------
 * Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.
 * See License in the project root for license information.
 * -------------------------------------------------------------------------------------------
 */

/**
 *  @class
 *
 * A class that provides seekable read access to a `ReadableStream` of `Uint8Array`.
 * This class allows reading specific sections of a stream without seeking backwards.
 */
export class SeekableStreamReader {
  private readonly reader: ReadableStreamDefaultReader<Uint8Array>;
  private cachedChunk?: Uint8Array | null;
  private cachedPosition = 0;
  private cachedOffset = 0; // Track where we are within the cached chunk

  /**
   * Creates an instance of SeekableStreamReader.
   * @param {ReadableStream<Uint8Array>} stream - The readable stream to read from.
   */
  constructor(private readonly stream: ReadableStream<Uint8Array>) {
    this.reader = stream.getReader();
  }

  /**
   * Reads a section of the stream from the specified start position to the end position.
   *
   * This method reads data from the stream starting at the `start` position and ending at the `end` position.
   * It ensures that the read operation does not seek backwards and handles chunked reading from the stream.
   * The read data is collected into a single `ArrayBuffer` and returned.
   *
   * @param {number} start - The starting position of the section to read. Must be non-negative.
   * @param {number} end - The ending position of the section to read. Must be greater than the start position.
   * @returns {Promise<ArrayBuffer>} A promise that resolves to an `ArrayBuffer` containing the read section.
   * @throws {Error} If the start position is negative, the end position is not greater than the start position, or if seeking backwards.
   */
  public async readSection(start: number, end: number): Promise<ArrayBuffer> {
    if (start < 0 || end <= start) {
      throw new Error("Invalid range: start must be non-negative and end must be greater than start.");
    }
    if (start < this.cachedPosition) {
      throw new Error("Cannot seek backwards.");
    }

    const chunks: Uint8Array[] = [];
    let totalLength = 0;
    let position = this.cachedPosition;

    while (position < end) {
      if (!this.cachedChunk) {
        const { done, value } = await this.reader.read();
        if (done) break;
        if (!value) continue;
        this.cachedChunk = value;
        this.cachedOffset = 0; // Reset the offset since it's a new chunk
      }

      const chunk = this.cachedChunk;
      const chunkLength = chunk.byteLength;

      // Skip chunks that are entirely before `start`
      if (position + chunkLength - this.cachedOffset <= start) {
        position += chunkLength - this.cachedOffset;
        this.cachedChunk = null;
        this.cachedOffset = 0;
        continue;
      }

      // Calculate the section of the chunk to return
      const startIndex = Math.max(0, start - position - 1) + this.cachedOffset;
      const endIndex = Math.min(chunkLength, end - position + this.cachedOffset + 1);

      const sliced = chunk.slice(startIndex, endIndex);
      chunks.push(sliced);
      totalLength += sliced.byteLength;

      // Update position correctly
      position += sliced.byteLength;

      // Store remaining unread data for future reads
      if (endIndex < chunkLength) {
        this.cachedOffset = endIndex;
      } else {
        this.cachedChunk = null;
        this.cachedOffset = 0;
      }
    }

    this.cachedPosition = position; // Ensure position is updated

    // Combine collected chunks into a single buffer
    const result = new Uint8Array(totalLength);
    let offset = 0;
    for (const chunk of chunks) {
      result.set(chunk, offset);
      offset += chunk.byteLength;
    }

    return result.buffer;
  }
}
