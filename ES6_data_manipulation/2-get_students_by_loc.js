// Function: getStudentsByLocation
// Purpose: Return students whose location matches the specified city
// Params:
//   students (Array) - list of student objects
//   city (String) - location to filter by
// Returns: Array of student objects filtered by location

export default function getStudentsByLocation(students, city) {
  if (!Array.isArray(students)) {
    return [];
  }

  return students.filter((student) => student.location === city);
}