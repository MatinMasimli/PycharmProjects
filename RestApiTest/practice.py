"""
    Python RestApi Connection Practice
"""

import random  # https://docs.python.org/3.6/library/random.html
import sqlite3  # https://docs.python.org/3.6/library/sqlite3.html
import string  # https://docs.python.org/3.6/library/string.html

import requests

def generate_password(length: int, complexity: int) -> str:
    """Generate a random password with given length and complexity

    Complexity levels:
        Complexity == 1: return a password with only lowercase chars
        Complexity ==  2: Previous level plus at least 1 digit
        Complexity ==  3: Previous levels plus at least 1 uppercase char
        Complexity ==  4: Previous levels plus at least 1 punctuation char

    :param length: number of characters
    :param complexity: complexity level
    :returns: generated password
    """

    if complexity == 1:
        password = ''.join([random.choice(string.ascii_lowercase)
                          for i in range(length)])
    elif complexity==2:
        password = ''.join([random.choice(string.ascii_lowercase + string.digits)
                            for i in range(length)])
    elif complexity==3:
        password = ''.join([random.choice(string.ascii_letters + string.digits)
                            for i in range(length)])
    elif complexity==4:
        password = ''.join([random.choice(string.ascii_letters + string.digits + string.punctuation)
                            for i in range(length)])

    return password


def check_password_level(password: str) -> int:
    """Return the password complexity level for a given password

    Complexity levels:
        Return complexity 1: If password has only lowercase chars
        Return complexity 2: Previous level condition and at least 1 digit
        Return complexity 3: Previous levels condition and at least 1 uppercase char
        Return complexity 4: Previous levels condition and at least 1 punctuation

    Complexity level exceptions (override previous results):
        Return complexity 2: password has length >= 8 chars and only lowercase chars
        Return complexity 3: password has length >= 8 chars and only lowercase and digits

    :param password: password
    :returns: complexity level
    """

    if (all(ch.islower() for ch in password) and not any(ch.isdigit() for ch in password)):
        return 1
    elif (any(ch.islower() for ch in password) and any(ch.isdigit() for ch in password)
         and not any(ch.isupper() for ch in password)):
        return 2
    elif (any(ch.islower() for ch in password) and any(ch.isdigit() for ch in password)
        and any(ch.isupper() for ch in password) and
          not any(ch in "!\"#$%&'()*+,-./:;<=>?@[\]^_`{|}~" for ch in password)):
        return 3
    elif (any(ch.islower() for ch in password) and any(ch.isdigit() for ch in password)
        and any(ch.isupper() for ch in password) and
          any(ch in "!\"#$%&'()*+,-./:;<=>?@[\]^_`{|}~" for ch in password)):
        return 4


    return None

def step_4():

    string1 = generate_password(4, 1)
    string2 = generate_password(6, 2)
    string3 = generate_password(6, 3)
    string4 = generate_password(6, 4)

def create_user(db_path: str) -> None:  # you may want to use: http://docs.python-requests.org/en/master/
    """Retrieve a random user from https://randomuser.me/api/
    and persist the user (full name and email) into the given SQLite db

    :param db_path: path of the SQLite db file (to do: sqlite3.connect(db_path))
    :return: None
    """

    r = requests.get('https://randomuser.me/api/')
    data = r.json()

    print("FName: ", data['results'][0]['name']['first'])
    print("LName: ", data['results'][0]['name']['last'])
    print("email: ", data['results'][0]['email'])

    firstName = data['results'][0]['name']['first']
    lastName = data['results'][0]['name']['last']
    email = data['results'][0]['email']

    conn = sqlite3.connect(db_path)
    c = conn.cursor()

    c.execute('''CREATE TABLE IF NOT EXISTS users
                 (Fname, Lname, email)''')

    sql = "INSERT INTO users VALUES ('%s','%s','%s')" % \
              (firstName, lastName, email)

    c.execute(sql)
    conn.commit()
    conn.close()

def step_6(db_path: str):

    conn = sqlite3.connect(db_path)
    c = conn.cursor()

    c.execute('SELECT * FROM users')

    #c.execute("ALTER TABLE users ADD Password")

    for i in range(10):
        print(c.fetchone())
        length = random.randrange(6, 13)
        complexity = random.randrange(1, 5)
        password = generate_password(length, complexity)
    #    addColumn = "INSERT INTO users (Password) VALUES ('%s')" % password
    #    c.execute(addColumn)

    c.close()


generate_password(10, 4)
step_4()
create_user('TestDB18.db')
step_6('TestDB18.db')





