string = input()
_last_index = -2
for index in range(len(string)):
    if string[index] == 'a':
        _last_index = index

print(_last_index+1)
