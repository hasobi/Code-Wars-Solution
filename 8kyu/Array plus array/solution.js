function arrayPlusArray(arr1, arr2) {
  let result = 0; 
  arr1.forEach(number => {result += number});
  arr2.forEach(number => {result += number});
  return result;
}
