// A working news-image-daily entry (Node 22, standard library only): its image is the entry.png beside this file, and
// the program copies it to /output/entry.png. The gate takes a whole PNG or JPEG of at most 1 MiB and 1024 by 1024
// pixels, and the judge sees exactly the bytes copied.
//
// Before copying, the program validates the source: it must start with the PNG signature (89 50 4E 47 0D 0A 1A 0A)
// and be at most 1 MiB (1048576 bytes); anything else fails with a clear error and writes nothing. The output is
// written atomically — the bytes go to a temporary file in the output directory first, then rename over entry.png,
// so a partial or failed run can never leave a truncated image behind.
//
// Outside the grader's container, MAKEFUN_OUTPUT_DIR stands in for /output:
//   mkdir -p out && MAKEFUN_OUTPUT_DIR=out node main.ts

import { renameSync, statSync, readFileSync, writeFileSync } from 'node:fs';
import { join } from 'node:path';

const PNG_SIGNATURE = Buffer.from([0x89, 0x50, 0x4e, 0x47, 0x0d, 0x0a, 0x1a, 0x0a]);
const MAX_BYTES = 1048576; // 1 MiB

const sourcePath = new URL('./entry.png', import.meta.url);
const outputDir = process.env.MAKEFUN_OUTPUT_DIR ?? '/output';
const outputPath = join(outputDir, 'entry.png');

const { size } = statSync(sourcePath);
if (size > MAX_BYTES) {
  throw new Error(`entry.png is ${size} bytes, over the 1 MiB limit (${MAX_BYTES} bytes)`);
}

const bytes = readFileSync(sourcePath);
if (!bytes.subarray(0, PNG_SIGNATURE.length).equals(PNG_SIGNATURE)) {
  throw new Error('entry.png is not a PNG: first 8 bytes do not match the PNG signature');
}

const tempPath = join(outputDir, `.entry.png.tmp-${process.pid}`);
writeFileSync(tempPath, bytes);
renameSync(tempPath, outputPath);
console.log(`Wrote ${outputPath} (${size} bytes)`);
