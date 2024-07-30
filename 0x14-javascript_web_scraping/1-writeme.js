#!/usr/bin/node

const fs = require('fs');
const file = process.argv[2];
const str = process.argv[3];
try {
  fs.writeFileSync(file, str, { encoding: 'utf-8' });
} catch (err) {
  console.err(err);
}
