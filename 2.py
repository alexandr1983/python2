#1

a = [35, 'list', 77, True, None, 45.3, '33',
     (3 + 4j), (5, 43, 6), {44, 55, 33, 8}, frozenset(),
     {"k1": 500, 2: 400, "k2": True, 4: None}, bytearray(b'some text')]

for ind, i in enumerate(a, 1):
    print(f"{ind} {i} {type(i)}")


#2

a = list(input("Enter numbers:"))

for i in range(1, len(a), 2)
     a[i - 1], a[i] = a[i], a[i - 1]
     
print(a)
