file = open('file.txt', 'r')
f = file.readlines()

newList = []
#for line in f:
    #if line[-1] == '\n':
     #   newList.append(line[:-1])
    #else:
#       newList.append(line)
#or simpler
for line in f:
    newList.append(line.strip())

print(newList)