from itertools import permutations
test_case = int(input(""))
pattern = []
text_string = []
for i in range(test_case):
    pattern.append(input(""))
    text_string.append(input(""))

i = 0
j = 0
output = ""
for i in range(test_case):
    perms = [''.join(p) for p in permutations(pattern[i])]
    # print(perms)
    for j in range(len(list(perms))):
        if text_string[i].find(perms[j]) > 0:
            output = "YES"
            break
        else:
            output = "NO"


    print(output)
