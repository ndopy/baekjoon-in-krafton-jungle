const fs = require('fs');
const path = require('path');

const localPath = path.join(__dirname, 'input.txt');
const filePath = fs.existsSync(localPath)
  ? localPath
  : '/dev/stdin';

const input = fs
  .readFileSync(filePath)
  .toString()
  .trim()
  .split('\n');

const inputNumber = input.map(Number);

const sum = inputNumber.reduce(
  (accumulator, currentValue) => accumulator + currentValue
);

console.log(sum);
