import json
import re

print(json.dumps({"name" : "jai", "age": 22})) #dictionary
print(json.dumps(["apple", "banana"])) #list
print(json.dumps(("apple", "banana"))) #tuple
print(json.dumps("hello")) #string
print(json.dumps(42)) #int
print(json.dumps(50.2)) #float
print(json.dumps(True)) #boolean
print(json.dumps(False)) #boolean
print(json.dumps(None)) #Null


x = {
  "name": "John",
  "age": 30,
  "married": False,
  "divorced": False,
  "children": ("Ann","Billy"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}

# use . and a space to separate objects, and a space, a = and a space to separate keys from their values:
print(json.dumps(x, indent=4, separators=(". ", " = ")))
print("-----------------------------")

#Check if the string starts with "The" and ends with "Spain":

txt = "The rain in Spain"
x = re.search("^The.*Spain$", txt)

if x:
  print("YES! We have a match!")
else:
  print("No match")