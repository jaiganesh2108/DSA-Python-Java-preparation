import json

print(json.dumps({"name" : "jai", "age": 22})) #dictionary
print(json.dumps(["apple", "banana"])) #list
print(json.dumps(("apple", "banana"))) #tuple
print(json.dumps("hello")) #string
print(json.dumps(42)) #int
print(json.dumps(50.2)) #float
print(json.dumps(True)) #boolean
print(json.dumps(False)) #boolean
print(json.dumps(None)) #Null