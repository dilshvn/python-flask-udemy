class VotersEligibility(Exception): #inherited from 'Exception' superclass
    def __init__(self):
        super().__init__() #calls the superclass constructor -> 'Exception' class constructor

try:
    age = 12
    if age < 18:
        raise VotersEligibility
except VotersEligibility:
    print('underaged')
else:
    print('adult') #runs if except doesn't run
finally:
    print('end') #runs for sure