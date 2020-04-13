function area(shape) {
  if (typeof shape === 'object')
    return shape[0] * shape[1];
  else
    return Math.PI * Math.pow(shape, 2);
}

function sortByArea(array) {
  return array.slice(0).sort((a, b) => area(a) - area(b));
}
