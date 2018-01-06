import sqlite3
import datetime
import time
now = datetime.datetime.now()
"""RegistrationC-------------------------------------------------------------------------------------------------------------------------------------------"""
def RegistrationC(username, password):

    """
    >>> RegistrationC('AdminC', 1234)
    This username exist in the system!
    False
    """

    if CheckIfNotExistC(username):
        db = sqlite3.connect('CVen7.db')
        CVen = db.cursor()

        def CreateTable():
            CVen.execute('CREATE TABLE IF NOT EXISTS CVen7Candidate(username TEXT,password REAL,loged_in REAL)')

        def DataEntry():
            CVen.execute("INSERT INTO CVen7Candidate(username,password,loged_in) VALUES(?,?,?)",(username, password, 0))
            db.commit()
            CVen.close()
            db.close()

        CreateTable()
        DataEntry()
        return True
    else:
        print ("This username exist in the system!")
        return False

"""RegistrationHR------------------------------------------------------------------------------------------------------------------------------------------"""

def RegistrationHR(username, password):

    """
    >>> RegistrationHR('AdminHR', 1234)
    This username exist in the system!
    False
    """

    if (CheckIfNotExistHR(username)):
        db = sqlite3.connect('CVen7.db')
        CVen = db.cursor()

        def CreateTable():
            CVen.execute('CREATE TABLE IF NOT EXISTS CVen7HR(username TEXT,password REAL,loged_in REAL)')

        def DataEntry():
            CVen.execute("INSERT INTO CVen7HR(username,password,loged_in) VALUES(?,?,?)", (username, password, 0))
            db.commit()
            CVen.close()
            db.close()

        CreateTable()
        DataEntry()
        return True
    else:
        print("This username exist in the system!")
        return False

"""Login-------------------------------------------------------------------------------------------------------------------------------------------"""
def Login(username, password,type):

    """
    >>> Login ('AdminC',1234,'c')
    WELCOME AdminC
    True
    >>> Login ('AdminC',1234,'hr')
    Username or Password not recognised
    False
    >>> Login ('AdminHR',1234,'HR')
    WELCOME AdminHR
    True
    >>> Login ('AdminHR',1234,'c')
    Username or Password not recognised
    False
    """

    while True:
        with sqlite3.connect("CVen7.db") as db:
            cursor = db.cursor()
        if (type=='c'):
            find_user = ("SELECT * FROM CVen7Candidate WHERE username =? AND password =?")
            cursor.execute(find_user, [(username), (password)])
            result = cursor.fetchall()
            if result:
                for i in result:
                    print("WELCOME " + i[0])
                    cursor.execute("UPDATE CVen7Candidate SET loged_in='{}' ".format(time.time()))
                    db.commit()
                    break
                return True
            else:
                print("Username or Password not recognised")
                return False
        elif (type.lower()=='hr'):
            find_user = ("SELECT * FROM CVen7HR WHERE username =? AND password =?")
            cursor.execute(find_user, [(username), (password)])
            result = cursor.fetchall()
            if result:
                for i in result:
                    print("WELCOME " + i[0])
                    cursor.execute("UPDATE CVen7HR SET loged_in='{}' ".format(time.time()))
                    db.commit()
                    break
                return True
            else:
                print("Username or Password not recognised")
                return False
        else:
            print ("The type is not recognised")

"""CheckIfLoginC-------------------------------------------------------------------------------------------------------------"""
def CheckIfLoginC(username):

    """
    >>> CheckIfLoginC('AdminC')
    True
    """

    with sqlite3.connect("CVen7.db") as db:
        cursor = db.cursor()
    my_sq = "SELECT loged_in FROM CVen7Candidate WHERE username = ?"
    cursor.execute(my_sq, [(username)])
    result = cursor.fetchall()
    if result==[]:
        return False
    if (time.time()- int(result[0][0])<3600):
        return True
    else:
        print("Please login!")
        return False

"""checkIfLoginHR------------------------------------------------------------------------------------------------------------"""
def CheckIfLoginHR(username):

    """
    >>> CheckIfLoginHR('AdminHR')
    True
    """

    with sqlite3.connect("CVen7.db") as db:
        cursor = db.cursor()
    my_sq = "SELECT loged_in FROM CVen7HR WHERE username = ?"
    cursor.execute(my_sq, [(username)])
    result = cursor.fetchall()
    if result==[]:
        return False
    if (time.time()- int(result[0][0])<3600):
        return True
    else:
        print ("Please login!")
        return False

"""CheckIfNotExistC----------------------------------------------------------------------------------------------------------------"""
def CheckIfNotExistC(username):
    with sqlite3.connect("CVen7.db") as db:
        cursor = db.cursor()
    my_sq = "SELECT username FROM CVen7Candidate WHERE username = ?"
    cursor.execute(my_sq, [(username)])
    result = cursor.fetchall()
    if result==[]:
        return True
    else:
        return False

"""CheckIfNotExistHR---------------------------------------------------------------------------------------------------------------"""
def CheckIfNotExistHR(username):
    with sqlite3.connect("CVen7.db") as db:
        cursor = db.cursor()
    my_sq = "SELECT username FROM CVen7HR WHERE username = ?"
    cursor.execute(my_sq, [(username)])
    result = cursor.fetchall()
    if result==[]:
        return True
    else:
        return False