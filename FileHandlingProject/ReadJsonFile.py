import json
import zip

def json_equals(jsonA, jsonB):
    if type(jsonA) != type(jsonB):
        # not equal
        return False
    if type(jsonA) == 'dict':
        if len(jsonA) != len(jsonB):
            return False
        for keyA in jsonA:
            if keyA not in jsonB or not json_equals(jsonA[keyA], jsonB[keyA]):
                return False
    elif type(jsonA) == 'list':
        if len(jsonA) != len(jsonB):
            return False
        for itemA, itemB in zip(jsonA, jsonB)
            if not json_equals(itemA, itemB):
                return False
    else:
        return jsonA == jsonB









json_data1=open("D:\\NewTestFolder\\TestJson.json").read()

jsonA = json.loads(json_data1)

json_data2=open("D:\\NewTestFolder\\TestJson.json").read()

jsonB = json.loads(json_data2)

json_equals(jsonA,jsonB)

