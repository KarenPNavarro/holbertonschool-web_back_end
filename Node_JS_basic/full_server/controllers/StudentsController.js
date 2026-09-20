import readDatabase from '../utils';

export default class StudentsController {
  static getAllStudents(request, response) {
    readDatabase(process.argv[2])
      .then((fields) => {
        const output = ['This is the list of our students'];
        const names = Object.keys(fields)
          .sort((a, b) => a.toLowerCase().localeCompare(b.toLowerCase()));

        names.forEach((field) => {
          const list = fields[field];
          output.push(`Number of students in ${field}: ${list.length}. List: ${list.join(', ')}`);
        });

        response.status(200).send(output.join('\n'));
      })
      .catch((error) => {
        response.status(500).send(error.message);
      });
  }

  static getAllStudentsByMajor(request, response) {
    const { major } = request.params;

    if (major !== 'CS' && major !== 'SWE') {
      response.status(500).send('Major parameter must be CS or SWE');
      return;
    }

    readDatabase(process.argv[2])
      .then((fields) => {
        const list = fields[major] || [];
        response.status(200).send(`List: ${list.join(', ')}`);
      })
      .catch((error) => {
        response.status(500).send(error.message);
      });
  }
}
