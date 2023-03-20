# import
import student as student


# new create new student
def create_student(first_name, last_name, grade_level, teacher_id):
    return f"""Insert Into student values
(0, '{first_name}','{last_name}','{grade_level}',{teacher_id})"""


# update student
def update_student(first_name, last_name, grade_level, student_id):
    return f"""
UPDATE student
SET first_name= '{first_name}', last_name= '{last_name}', grade_level='{grade_level}'
WHERE id = '{student_id}';"""


# read student
show_all_students = """
SELECT *
FROM student;
"""


def show_student_books(student_id):
    return f"""
SELECT title
FROM student_books
WHERE student_id="{student_id}"
"""

# todo join statements will be needed to retrieve data related to this function.
def add_book_to_student(student_id, book_id):
    return f"""
INSERT INTO student_books VALUES
('{student_id}','{book_id}')
"""

# TODO join statement needed here
# delete
def delete_student(student_id):
    return f"""DELETE FROM student
WHERE id = '{student_id}';"""

# TODO this will need to be made into an join statement to be of any use
def remove_book_from_student(book_id, student_id):
    return f"""
DELETE FROM student_books
WHERE book_id='{book_id}' and student_id='{student_id}'
"""
