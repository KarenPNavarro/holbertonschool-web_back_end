export default function appendToEachArrayValue(array, appendString) {
  const result = [];

  // eslint-disable-next-line space-in-parens
  for ( const value of array ) {
    result.push(appendString + value);
  }

  return result;
}
