// News-image entry, version 2 (Node 22, standard library only).
//
// The entry image is the entry.png next to this file. This program copies
// it to /output/entry.png, after two checks: the file must start with the
// PNG signature (89 50 4E 47 0D 0A 1A 0A) and must fit the 1 MiB limit.
// Anything else fails loudly and writes nothing, so a bad run can never
// leave a broken image behind.
//
// The copy is atomic: bytes go to a temporary file in the output
// directory first, then rename over entry.png. The output directory is
// created when it does not exist yet.
//
// Outside the grader, MAKEFUN_OUTPUT_DIR stands in for /output:
//   mkdir -p out && MAKEFUN_OUTPUT_DIR=out node main.ts

import { existsSync, mkdirSync, readFileSync, renameSync, statSync, writeFileSync } from 'node:fs';
import { join } from 'node:path';

const PNG_MAGIC = Buffer.from([0x89, 0x50, 0x4e, 0x47, 0x0d, 0x0a, 0x1a, 0x0a]);
const MAX_BYTES = 1048576; // 1 MiB

const source = new URL('./entry.png', import.meta.url);
const outDir = process.env.MAKEFUN_OUTPUT_DIR ?? '/output';
const target = join(outDir, 'entry.png');

if (!existsSync(source)) {
  throw new Error('entry.png is missing next to main.ts');
}

const { size } = statSync(source);
if (size > MAX_BYTES) {
  throw new Error(`entry.png is ${size} bytes, over the 1 MiB limit (${MAX_BYTES} bytes)`);
}

const bytes = readFileSync(source);
if (!bytes.subarray(0, PNG_MAGIC.length).equals(PNG_MAGIC)) {
  throw new Error('entry.png is not a PNG: its first bytes do not match the PNG signature');
}

// The gate also caps the image at 1024 by 1024 pixels: read the size
// straight out of the PNG header (IHDR, bytes 16-23) and fail early
// instead of handing the grader an oversized image.
const width = bytes.readUInt32BE(16);
const height = bytes.readUInt32BE(20);
if (width > 1024 || height > 1024) {
  throw new Error(`entry.png is ${width}x${height}, over the 1024x1024 limit`);
}

if (!existsSync(outDir)) {
  mkdirSync(outDir, { recursive: true });
}

const temp = join(outDir, `.entry.png.tmp-${process.pid}`);
writeFileSync(temp, bytes);
renameSync(temp, target);
console.log(`Wrote ${target} (${size} bytes)`);
