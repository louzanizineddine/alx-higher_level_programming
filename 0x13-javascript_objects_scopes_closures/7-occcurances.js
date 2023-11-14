#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  let occ = 0;
  list.map(
    (x) => {
      if (x === searchElement) {
        occ += 1;
        return 1;
      } else {
        return 0;
      }
    }
  );
  return occ;
};
