import { describe, it, assert, expect } from "vitest";
import { coreVersion } from "src";
import { readFile } from "node:fs/promises";

/**
 * Reads the package.json content and returns the value as a JSON object.
 * @returns current package.json version value
 */
const getPackageVersion = async (): Promise<string> => {
  try {
    const filePath = new URL("../../package.json", import.meta.url);
    const contents = await readFile(filePath, { encoding: "utf8" });
    // eslint-disable-next-line @typescript-eslint/no-unsafe-assignment
    const { version } = JSON.parse(contents);
    // eslint-disable-next-line @typescript-eslint/no-unsafe-return
    return Promise.resolve(version);
  } catch (err) {
    const message = (err.message as string) ?? "";
    return Promise.reject(message);
  }
};

describe("version", () => {
  it("should be written after build", () => {
    assert(coreVersion, "version is not written");
  });
  it("should equal the package.json version", async () => {
    const version = await getPackageVersion();
    expect(coreVersion).toEqual(version);
  });
});
