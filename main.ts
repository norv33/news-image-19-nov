// News-image entry, version 3 (Node 22, standard library only).
//
// The image is the entry.png sitting next to this file. This program
// checks it and copies it to /output/entry.png. The checks are the
// ones the gate applies: the first 8 bytes must be the PNG signature,
// the file must be no bigger than 1 MiB, and the IHDR header must say
// at most 1024 by 1024 pixels. A file that fails any of them is
// refused loudly and nothing is written, so a bad run can never leave
// a broken image behind.
//
// The write is atomic: bytes land in a temporary file inside the
// output directory first and are then renamed over entry.png. The
// output directory is created when it is missing.
//
// Outside the grader, MAKEFUN_OUTPUT_DIR stands in for /output:
//   mkdir -p out && MAKEFUN_OUTPUT_DIR=out node main.ts

import { existsSync, mkdirSync, readFileSync, renameSync, statSync, writeFileSync } from 'node:fs';
import { join } from 'node:path';

const PNG_MAGIC = Buffer.from([0x89, 0x50, 0x4e, 0x47, 0x0d, 0x0a, 0x1a, 0x0a]);
const MAX_BYTES = 1048576; // 1 MiB
const MAX_SIDE = 1024;

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

const width = bytes.readUInt32BE(16);
const height = bytes.readUInt32BE(20);
if (bytes.subarray(12, 16).toString('latin1') !== 'IHDR' || bytes.readUInt32BE(8) !== 13) {
  throw new Error('entry.png has no valid IHDR chunk, so its size cannot be trusted');
}
if (width > MAX_SIDE || height > MAX_SIDE) {
  throw new Error(`entry.png is ${width}x${height}, over the ${MAX_SIDE}x${MAX_SIDE} limit`);
}

if (!existsSync(outDir)) {
  mkdirSync(outDir, { recursive: true });
}

const temp = join(outDir, `.entry.png.tmp-${process.pid}`);
writeFileSync(temp, bytes);
renameSync(temp, target);
console.log(`Wrote ${target} (${size} bytes, ${width}x${height})`);
