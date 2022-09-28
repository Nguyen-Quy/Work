s = "DUCQUY"
total = 0
new_lst = []

for c in s:
    print(ord(c))
    total += ord(c)
    new_lst.append(ord(c))

print(total)
print(new_lst)
