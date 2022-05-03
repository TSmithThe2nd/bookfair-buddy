#imports


#varibles
first_name=None
last_name=None
authorID=None

# todo create basic crud functions each should be SQL queries
#with varibles ready for user input. 
#create new author
new_author= f"""
INSERT INTO author VALUES
(10, '{first_name}','{last_name}')
"""


#read (all authors, all books from author)
show_authors= """
SELECT *
FROM author;
"""
show_books_by_author=f"""
SELECT title
FROM book
WHERE author_id="{authorID}"
"""

#update(change authors name)
update_author=f"""
UPDATE author
SET first_name= '{first_name}', last_name= '{last_name}'
WHERE id = 10;"""


#delete
delete_author=f"""
DELETE FROM author
WHERE id = '{authorID}';"""
