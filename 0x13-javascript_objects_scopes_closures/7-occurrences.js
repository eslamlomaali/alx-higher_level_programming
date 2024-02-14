#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  let nOccurrences = 0;
  for (let z = 0; z < list.length; z++) {
    if (searchElement === list[z]) {
      nOccurrences++;
    }
  }
  return nOccurrences;
};
