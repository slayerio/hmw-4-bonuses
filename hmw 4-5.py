IQ = int(input("what's your iq?"));
total: str = ""
students: str = ""
HighestIQ: str = ""

while 30 < IQ < 300:
    if IQ > HighestIQ:
        HighestIQ = IQ
    students = students + 1
    total = total + IQ
    IQ = int(input("what's your iq?"));


avg = total // students
print(f"there are {students} students in the group with the avg of {avg} IQ");
print(f"the highest IQ score: {HighestIQ}")
print("after one year of python studying.....")

IQN = int(input("what's your iq?"));
totalN: str = ""
studentsN: str = ""
HighestIQN: str = ""
while 30 < IQN < 300:
    studentsN = studentsN + 1
    totalN = totalN + IQN
    IQN = int(input("what's your iq?"));
    if IQN > HighestIQN:
        HighestIQN = IQN

avgN = totalN // studentsN
print(f"after a year, there are {studentsN} students in the group with the avg of {avgN} IQ")
print(f"the highest IQ score: {HighestIQN}")
print(f"Highest IQ of all time: {HighestIQN if HighestIQN > HighestIQ else HighestIQ}")
x = avg - avgN
if x < 0:
    print(f"the avg iq went up by {-x} points")
elif x > 0:
    print(f"the avg iq went down by {x} points")
else:
    print(f"the avg iq stayed the same")