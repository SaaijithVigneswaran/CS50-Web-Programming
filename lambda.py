people = [
    {"name": "harry", "house" : "griffindor"},
    {"name": "Ron ", "house" : "Ravenclaw"},
    {"name": "Draco", "house" : "snake"}
  ]


#def f(person):
 #   return person["name"]


people.sort(key= lambda person: person["name"])

print (people)