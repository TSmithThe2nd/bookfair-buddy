# import


#varibles
studentId=None
first_name=None
last_name=None
grade_level=None
bookId=None

#create new student
new_student= f"""
INSERT INTO student VALUES
('{studentId}','{first_name}','{last_name}','{grade_level}','{bookId})'
"""

#read student
show_all_students="""
SELECT *
FROM student;
"""



show_student_books=f"""
SELECT title
FROM student_books
WHERE student_id="{studentId}"
"""

# update student
update_student=f"""
UPDATE student
SET first_name= '{first_name}', last_name= '{last_name}', grade_level='{grade_level}'
WHERE id = '{studentId}';"""

add_book_to_student=f"""
INSERT INTO student_books VALUES
('{studentId}','{bookId}')
"""

#delete
delete_student=f"""DELETE FROM student
WHERE id = '{studentId}';"""

remove_book_from_student=f"""
DELETE FROM student_books
WHERE book_id='{bookId}' and student_id='{studentId}'
"""