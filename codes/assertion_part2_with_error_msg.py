#ASSERT WITH ERROR MSG

def avg(marks):
    assert len(marks) != 0, 'list is empty' #assertion with err msg
    return sum(marks)/len(marks)

mark1 = [11, 22, 33]
print(avg(mark1)) #22.0

mark2 = []
print(avg(mark2)) #AssertionError: list is empty

#assertion err msg is optional