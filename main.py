# enter 5 subject marks
m1 = int(input("enter mark 1: "))
m2 = int(input("enter mark 2: "))
m3 = int(input("enter mark 3: "))
m4 = int(input("enter mark 4: "))
m5 = int(input("enter mark 5: "))

# calculate average
avg = (m1 + m2 + m3 + m4 + m5) / 5

print("average =", avg)

# decide grade
if avg >= 91 and avg <= 100:
    print("grade: A1")
elif avg >= 81:
    print("grade: A2")
elif avg >= 71:
    print("grade: B1")
elif avg >= 61:
    print("grade: B2")
elif avg >= 51:
    print("grade: C1")
elif avg >= 41:
    print("grade: C2")
elif avg >= 33:
    print("grade: D")
elif avg >= 21:
    print("grade: E1")
else:
    print("grade: E2")