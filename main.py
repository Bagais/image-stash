class Student():
    # [assignment] Skeleton class. Add your code here
    def __init__(self, name, age, tracks, score):
        self.name = name
        self.age = age
        self.tracks = tracks
        self.score = score        
        print('my name is ', name, 'and i am ', age, 'years old.', 'I have chosen the ', tracks, 'track ', 'with a current score of', score)

    def change_name(self, name ):
        self.name = name

    def change_age(self, age ):
        self.age = age

    def add_track(self, tracks):
        self.tracks = tracks

    def get_score(self, score ):
        self.score = score
        
Bob = Student("Bob", 26, ["FE","BE"], 20.90)
Bob.change_name(0)
Bob.change_age(0)
Bob.add_track(0)
Bob.get_score(0)
print('New Student?')
name = str(input ("Please enter name: "))
age = int(input ('age: '))
tracks = input('select a track: ')
score = float(input('final score: '))
print ('New student is ', name, ',', age, 'years old.', 'Assigned to the ', tracks, 'track ', 'with a current score of', score)
