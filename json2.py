import json

input1 = '''[
  { "id" : "001",
    "x" : "2",
    "name" : "Chuck"
  } ,
  { "id" : "009",
    "x" : "7",
    "name" : "Chuck"
  }
]''' 

info = json.loads(input1)
print('User count: ', len(info))
for item in info:
    print('Name:', item['name'])
    print('Id', item['id'])
    print('Attribute', item['x'])