a = 1
b = 0
if a == b:
    print(f"was True for {a} {b}")
else:
    print(f"was False for {a} {b}")

##always true
a = 1
b = -2
c = 3
d = 4
if a + b and c + d:
    print(f"was True for {a} {b} {c} {d}")
else:
    print(f"was False for {a} {b} {c} {d}")

a = 2
b = 3
c = 4
d = 5
if a >= b or c > d:
    print(f"was True for {a} {b} {c} {d}")
else:
    print(f"was False for {a} {b} {c} {d}")

a = 1
b = 6
c = 5
d = 4
if a >= b or c < d:
    print(f"was True for {a} {b} {c} {d}")
else:
    print(f"was False for {a} {b} {c} {d}")

a = 4
b = 8
c = 5
d = 2
if a == b and c <= d:
    print(f"was True for {a} {b} {c} {d}")
else:
    print(f"was False for {a} {b} {c} {d}")

##always true except a=b=c=d=0
a = 0
b = 0
c = 0
d = 0
if True and a + b + c + d:
    print(f"was True for {a} {b} {c} {d}")
else:
    print(f"was False for {a} {b} {c} {d}")

a = 5
b = 5
if a != b:
    print(f"was True for {a} {b}")
else:
    print(f"was False for {a} {b}")

##always true
a = 0
b = 0
c = 0
if a != b and a <= c or a <= b or True:
    print(f"was True for {a} {b} {c}")
else:
    print(f"was False for {a} {b} {c}")

##always true, cant be false because of a paradox with a and b
a = 3
b = 3
c = 4
if a != b and a <= c or a <= b or False:
    print(f"was True for {a} {b} {c}")
else:
    print(f"was False for {a} {b} {c}")

a = 4
b = 3
c = 2
d = 1
if a % b == 0 and c % d == 1:
    print(f"was True for {a} {b} {c} {d}")
else:
    print(f"was False for {a} {b} {c} {d}")