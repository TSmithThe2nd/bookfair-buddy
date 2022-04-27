# imports
from pythonCrudFunctions import create_db_connection, execute_query

#varibles
title="manning the mutt"
authorId=3
bookId=25
genre="readers"

pw="Lacyk#18"
connection = create_db_connection("localhost", "root",pw, "bookfairbuddy")

#create new book
new_book=f"""
INSERT INTO book VALUES
('{bookId}','{genre}','{title}','{authorId}')
"""


#read ()
show_all_books=f"""
SELECT *
FROM book
"""

show_book_by_genre=f"""
SELECT title
FROM book
WHERE genre='{genre}'
"""
        #dulplicate function consider removing (found in authors)
show_book_by_author="""
SELECT title
FROM book
WHERE author_id='{authorId}'
"""
#update
update_book=f"""
UPDATE book
SET title='{title}', genre='{genre}', author_id='{authorId}'
WHERE id= '{bookId}'
"""

#delete
delete_book=f"""DELETE FROM book
WHERE id = '{bookId}';"""
