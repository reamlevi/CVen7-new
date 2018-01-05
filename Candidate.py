import Json
import CloudinaryP
"""CreateCv--------------------------------------------------------------------------------------------------------------------------------------------"""
def CreateCV(name, edu, pic, id, exp):
    data=Json.FetchJson()
    D = {'Name': name, 'Status': "Available", 'Education': edu, 'Picture': CloudinaryP.upload(pic, id)['url'], 'ID': id,'Experience': exp}
    data.append(D)
    Json.SaveJason(data)

"""UploadPic----------------------------------------------------------------------------------------------------------------------------------------------"""
def UploadPic(pic, id):
    CloudinaryP.upload(pic, id)

"""CheckMyStatus------------------------------------------------------------------------------------------------------------------------------------------"""
def CheckMyStatus(id):
    data=Json.FetchJson()
    for c in data:
        if (str(id) == str(c['ID'])):
            print('Name: {}\nID: {}\nEducation: {}\nExperience:{}\nPicture:{}\nStatus: {}\n'.format(c['Name'], str(c['ID']),c['Education'], c['Experience'],c['Picture'], c['Status']))
"""EditCV-------------------------------------------------------------------------------------------------------------------------------------------------"""
def EditCV(id,value,type='n'):
    data = Json.FetchJson()
    for c in data:
        if (str(id)==str(c['ID'])):
            if (type.lower()=='n'):
                c['Name']=value
            elif (type.lower()=='e'):
                c['Education']=value
            elif (type.lower()=='exp'):
                c['Experience']=value
    Json.SaveJason(data)


