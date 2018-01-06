import json
"""FetchJson------------------------------------------------------------------------------------------------------------"""
def FetchJson():
    jsonFile = open('CVen7db.json', 'r')
    jsonData = json.load(jsonFile)
    jsonFile.close()
    return jsonData

"""SaveJason------------------------------------------------------------------------------------------------------------"""
def SaveJason(jsonData):
    f = open('CVen7db.json', 'w')
    newJson = json.dumps(jsonData)
    f.write(newJson)
    f.close()

