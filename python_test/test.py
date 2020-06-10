

f = 0
print(f)

def ab():
    global f
    f = 1993
    print(f)


ab()
print(f)

del f
print(f)