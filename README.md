
A faculty stores information about:
Student: studentID, name
Discipline: disciplineID, name
Grade: disciplineID, studentID, gradeID

The application allows to:
1. Manage the list of students and available disciplines. The application must allow the user to
add, remove, update, and list both students and disciplines.
2. Grade students at a given discipline. The program must allow only those students who are
enrolled at a given discipline to receive any number of grades.
3. Search for disciplines/students based on their ID or name/title. The search must work using
case-insensitive, partial string matching, and must return all matching disciplines/students.
4. Create statistics:
o All students enrolled at a given discipline, sorted alphabetically or by descending order
of average grade.
o All students failing at one or more disciplines (students having an average <5 for a
discipline are considered to be failing)
o Students with the best school situation, sorted in descending order of their aggregated
average (the average between their average grades per discipline).
o All disciplines at which there is at least one grade, sorted in descending order of the
average grade received by all students enrolled at that discipline.
5. Unlimited undo/redo functionality. Each step will undo/redo the previous operation
performed by the user.
