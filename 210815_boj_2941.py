string = input()

dic = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

for d in dic:
    string = string.replace(d, 'X')

print(len(string))
