#ASSERT WITHOUT ERROR MSG

#if assertion is True -> does nothing, goes to new line
#if assertion is False -> throws assertion error

def avg(marks):
    assert len(marks) != 0
    return sum(marks)/len(marks)

mark1 = [11, 22, 33]
print(avg(mark1)) #22.0

mark2 = []
print(avg(mark2)) #AssertionError
