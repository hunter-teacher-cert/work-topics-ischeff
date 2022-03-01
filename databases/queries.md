# Homework:

Write a SQL query that retrieves the following records: https://drive.google.com/file/d/1Vy6VDlqOZy8aV7zceGFSJNbbpFH06z1G/view?usp=sharing
Your SQL JOIN query will retrieve from the tables shared with you the records of all of the unexcused period attendance absences in the school for the week of 1-24-22 sorted by student last name ascending. You will use the resulting table of results, which you can call allCuts, in the async assignment. Consider a cut to be any instance of a student scanning into the building and being marked absent in a class. You will retrieve only the first name, last name, student ID, grade, scanTime, status, date, courseSection, attendance, period, and teacher.

```sql
SELECT s.first, s.last, s.studentID,s.grade,s.scantime, s.status,p.date,p.coursesection, p.attendance,p.teacher,p.period
FROM scan AS s
INNER JOIN periodAtt as p
ON s.studentID=p.studentID AND SUBSTR(s.scantime, 1, 9)=p.date
WHERE p.attendance = "A"
ORDER BY s.last ASC
```

# Async Work: