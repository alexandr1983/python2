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


#3

s = {'Winter': (1, 2, 12),
     'Spring': (3, 4, 5),
     'Summer': (6, 7, 8),
     "Autumn": (9, 10, 11)}

m = int(input("Month number: "))
for key in s.keys():
    if m in s[key]:
        print(key)


          
#4

s = input("Enter string ")
m = []
n = 1
for el in range(s.count(' ') + 1):
    m = s.split()
    if len(str(m)) <= 10:
        print(f" {n} {m [el]}")
        n += 1
    else:
        print(f" {n} {m [el] [0:10]}")
        n += 1
 
#5

my_list = [7, 5, 3, 3, 2]
n = int(input("Enter number: "))

for i in range(len(my_list)):
    if my_list[i] == n:
        my_list.insert(i + 1, n)
        break
    elif my_list[0] < n:
        my_list.insert(0, n)
    elif my_list[-1] > n:
        my_list.append(n)
    elif my_list[i] > n and my_list[i + 1] < n:
        my_list.insert(i + 1, n)
print(f"New string  - {my_list}")


