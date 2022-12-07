import json

g_json_big_data=[]

with open('ITT_Student.json', encoding='UTF8') as json_file:
 json_object = json.load(json_file)
 json_string = json.dumps(json_object)
 g_json_big_data = json.loads(json_string)

pass