import fn
f = "Failed"
t = "This is people stupid"
if fn.salary(2, 10) != 40:
    print(f)
elif fn.hellp_who("Max") != "Hello Max":
    print(f)
else:
    print(t)
if fn.salary(1, 10) != 20:
    print(f)
elif fn.hellp_who('People stupid') != "Hello People stupid":
    print(f)
else:
    print(t)