import Json
"""Serach----------------------------------------------------------------------------------------------------------------------------------"""
def Serach(value):
    data=Json.FetchJson()
    for c in data:
        if (str(value)==str(c['ID'])):
            print('Name: {}\nID: {}\nEducation: {}\nExperience:{}\nPicture:{}\nStatus: {}'.format(c['Name'], str(c['ID']),c['Education'],c['Experience'],c['Picture'],c['Status'],end='\n'))
            if c['Notes']:
                print  ("Note: ",c['Notes'])
        if (str(value)==str(c['Education'])):
            print('Name: {}\nID: {},Education: {}\nExperience:{}\nPicture:{}\nStatus: {}'.format(c['Name'], str(c['ID']),c['Education'],c['Experience'],c['Picture'],c['Status'], end='\n'))
            if c['Notes']:
                print  ("Note: ",c['Notes'])
        if (str(value)==str(c['Experience'])):
            print('Name: {}\nID: {}\nEducation: {}\n Experience:{}\nPicture:{}\nStatus:{}\n'.format(c['Name'], str(c['ID']),c['Education'],c['Experience'],c['Picture'],c['Status'], end='\n'))
            if c['Notes']:
                print  ("Note: ",c['Notes'])

"""UpdateStatus---------------------------------------------------------------------------------------------------------------------------------------"""
def UpdateStatus(id,status):
    data=Json.FetchJson()
    for c in data:
        if (str(id)==str(c['ID'])):
            print(c['Name']+" status is update")
            c["Status"]=status
    Json.SaveJason(data)
"""AddNotes-------------------------------------------------------------------------------------------------------------------------------------------"""
def AddNotes(id,note):
    data=Json.FetchJson()
    for c in data:
        if (str(id)==str(c['ID'])):
            c["Notes"]=note
    Json.SaveJason(data)