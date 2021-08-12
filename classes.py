class Point():
    def __init__(self,input1,input2):
        self.x=input1
        self.y=input2

p = Point(2,8)

print(p.x)
print(p.y)    

class Flight():
    def __init__(self,capacity):
        self.capacity = capacity
        self.passesengers=[]

    def add_passengers(self,name):
        if not self.open_seats():
            return False
        self.passesengers.append(name)
        return True

    def open_seats(self):
        return self.capacity-len(self.passesengers)

flight= Flight(3)

people = ["harry","ron","bob", "tom"]
for person in people:
    success= flight.add_passengers(person)
    if success:
        print(f"Add {person} to flight ")
    else:
        print (f"full no seats for {person}")
