# pylint:disable=C0111,C0103

<<<<<<< HEAD

def students_from_city(db, city):
    """return a list of students from a specific city"""

    request = """
        SELECT *
        FROM students
        WHERE birth_city = ?
    """

    db.execute(request, (city,))
    results = db.fetchall()
    return results
=======
def students_from_city(db, city):
    """return a list of students from a specific city"""
    pass
>>>>>>> 0782c767536f39d257c82e4fa630528b55d96c35


# To test your code, you can **run it** before running `make`
#   => Uncomment the following lines + run:
<<<<<<< HEAD
# $python school.py

import sqlite3

conn = sqlite3.connect("data/school.sqlite")
db = conn.cursor()
print(students_from_city(db, "Paris"))
=======
#   $ python school.py
#
# import sqlite3
# conn = sqlite3.connect('data/school.sqlite')
# db = conn.cursor()
# print(students_from_city(db, 'Paris'))
>>>>>>> 0782c767536f39d257c82e4fa630528b55d96c35
