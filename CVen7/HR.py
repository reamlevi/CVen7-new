import Json
"""Serach----------------------------------------------------------------------------------------------------------------------------------"""
def Serach(value):

    """
        >>> Serach(123456789)
        Name: TestName
        ID: 123456789
        Education: TestEducation
        Experience: TestExp
        Picture: TestPic
        Status: TestStatus
        Note: TestNotes
        <BLANKLINE>
        <BLANKLINE>
    """

    data=Json.FetchJson()
    for c in data:
        if (str(value)==str(c['ID'])):
            print('Name: {}\nID: {}\nEducation: {}\nExperience: {}\nPicture: {}\nStatus: {}'.format(c['Name'], str(c['ID']),c['Education'],c['Experience'],c['Picture'],c['Status'],end='\n'))
            if c['Notes']:
                print  ("Note:",c['Notes'])
            print('\n')
        if (str(value)==str(c['Education'])):
            print('Name: {}\nID: {}\nEducation: {}\nExperience: {}\nPicture: {}\nStatus: {}'.format(c['Name'], str(c['ID']),c['Education'],c['Experience'],c['Picture'],c['Status'], end='\n'))
            if c['Notes']:
                print  ("Note:",c['Notes'])
            print('\n')
        if (str(value)==str(c['Experience'])):
            print('Name: {}\nID: {}\nEducation: {}\nExperience: {}\nPicture: {}\nStatus:{}'.format(c['Name'], str(c['ID']),c['Education'],c['Experience'],c['Picture'],c['Status'], end='\n'))
            if c['Notes']:
                print  ("Note:",c['Notes'])
            print('\n')

"""UpdateStatus---------------------------------------------------------------------------------------------------------------------------------------"""
def UpdateStatus(id,status):

    """
    >>> UpdateStatus(123456789,"TestStatus")
    TestName status is update
    """

    data=Json.FetchJson()
    for c in data:
        if (str(id)==str(c['ID'])):
            print(c['Name']+" status is update")
            c["Status"]=status
    Json.SaveJason(data)

"""AddNotes-------------------------------------------------------------------------------------------------------------------------------------------"""
def AddNotes(id,note):

    """
    >>> AddNotes(123456789,"TestNotes")
    Note added to TestName
    """

    data=Json.FetchJson()
    for c in data:
        if (str(id)==str(c['ID'])):
            c["Notes"]=note
            print ("Note added to "+c['Name'])

    Json.SaveJason(data)