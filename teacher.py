# import


#varibles
teacherId=None
first_name=None
last_name=None
grade_level=None
prefix=None
bookId=None

#create new teacher
new_teacher= f"""
INSERT INTO teacher VALUES
('{teacherId}','{first_name}','{last_name}','{grade_level}','{prefix}')
"""

#read teacher
show_all_teachers="""
SELECT *
FROM teacher;
"""

show_students_in_teacher=f"""
SELECT first_name, last_name
FROM student
WHERE teacher_id="{teacherId}"
"""

show_teacher_books=f"""
SELECT title
FROM teacher_books
WHERE teacher_id="{teacherId}"
"""

# update teacher
update_teacher=f"""
UPDATE teacher
SET first_name= '{first_name}', last_name= '{last_name}', grade_level='{grade_level}',
prefix='{prefix}'
WHERE id = '{teacherId}';"""

add_book_to_teacher=f"""
INSERT INTO teacher_books VALUES
('{teacherId}','{bookId}')
"""

#delete
delete_teacher=f"""DELETE FROM teacher
WHERE id = '{teacherId}';"""

remove_book_from_teacher=f"""
DELETE FROM teacher_books
WHERE book_id='{bookId}' and teacher_id='{teacherId}'
"""