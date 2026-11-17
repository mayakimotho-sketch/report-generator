name=input("enter your name")
print("enter the marks of the following subjects")
math=int(input("math"))
eng=int(input("eng"))
sci=int(input("science"))
agn=int(input("agn"))
total=math+eng+sci+agn
aver=total/4
if aver>=90:
    grade="A"
    comment="Good job"
elif aver>=70:
    grade="B"
    comment="Try harder you are almost there"
elif aver>=50:
    grade="C"
    comment="You can do better"
else:
    grade="D"
    comment="There is all ways next time"
print("Student report")
print("maths:", math)
print("eng:", eng)
print("sci:", sci)
print("agn:", agn)
print("total marks:",total)
print("avarege:",aver)
print("grade:", grade)
print("Teacher's remarks:", comment)