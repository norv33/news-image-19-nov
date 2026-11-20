// main.ts — news-image-20261119 v4 (Swiss typography poster).
// Node 22, standard library only. Copies entry.png from this repository
// to $MAKEFUN_OUTPUT_DIR (or /output) as entry.png, after validating it
// is a real PNG within the competition's size limits. The write is
// atomic: bytes go to a temp file in the output directory, then rename
// over entry.png, so a failed run never leaves a truncated image.

import { mkdirSync, readFileSync, renameSync, writeFileSync } from "node:fs";
import { join } from "node:path";

const PNG_SIGNATURE = Buffer.from([
  0x89, 0x50, 0x4e, 0x47, 0x0d, 0x0a, 0x1a, 0x0a,
]);
const MAX_BYTES = 1048576; // 1 MiB
const MAX_DIMENSION = 1024;

const source = new URL("./entry.png", import.meta.url);
const data = readFileSync(source);

if (data.length > MAX_BYTES) {
  throw new Error(
    `entry.png is ${data.length} bytes, over the 1 MiB limit`,
  );
}
if (!data.subarray(0, 8).equals(PNG_SIGNATURE)) {
  throw new Error("entry.png does not start with the PNG signature");
}
if (data.toString("ascii", 12, 16) !== "IHDR") {
  throw new Error("entry.png has no IHDR chunk where one is expected");
}
const width = data.readUInt32BE(16);
const height = data.readUInt32BE(20);
if (width > MAX_DIMENSION || height > MAX_DIMENSION) {
  throw new Error(
    `entry.png is ${width}x${height}, over the 1024x1024 limit`,
  );
}
// A whole PNG ends with its IEND chunk: 4-byte length 0, the letters
// IEND, and its CRC. Refuse a file cut short before it.
const IEND_TAIL = Buffer.from([
  0x00, 0x00, 0x00, 0x00, 0x49, 0x45, 0x4e, 0x44, 0xae, 0x42, 0x60, 0x82,
]);
if (!data.subarray(data.length - 12).equals(IEND_TAIL)) {
  throw new Error("entry.png does not end with a complete IEND chunk");
}

const outDir = process.env.MAKEFUN_OUTPUT_DIR ?? "/output";
mkdirSync(outDir, { recursive: true });
const tmpPath = join(outDir, `.entry.png.${process.pid}.tmp`);
writeFileSync(tmpPath, data);
const outPath = join(outDir, "entry.png");
renameSync(tmpPath, outPath);
// Read the written file back: it must be exactly what was validated.
if (!readFileSync(outPath).equals(data)) {
  throw new Error("written entry.png does not match the validated bytes");
}
