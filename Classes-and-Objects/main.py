class Student:
    # [assignment] Skeleton class. Add your code here
    def __init__(self, name, age, tracks, score):
        self.name = name
        self.age = age
        self.tracks = tracks
        self.score = score
        
    def change_name(self, new_name):
        print(self.name + ' has been changed to '+ new_name)
        self.name  = new_name
        return self.name
        
        
    def change_age(self, new_age):
        if type(new_age) == int:
            print(str(self.age) + ' has been changed to '+ str(new_age))
            self.age  = new_age
            return self.age
        else:
            print('insert a whole number')
        pass
        
    def add_track(self, new_track):
        self.tracks.append(new_track)
        return self.tracks
        pass
        
    def get_score(self):
        print(self.score)
        



Bob = Student(name="Bob", age=26, tracks=["FE","BE"],score=20.90)

# Expected methods
Bob.change_name("Peter")
print(Bob.name)
Bob.change_age(34)
Bob.add_track("UI/UX")
Bob.get_score()
