str = ''
with open('file.txt','r') as file:
    line = file.readline()
    for i, n in enumerate(line):
        if n.isalpha():
            if line[i+1].isdigit() and line[i+2].isdigit():
                str += n*int(line[i+1]+line[i+2])
            elif line[i+1].isdigit():
                str += n*int(line[i+1])
        if n.isdigit():
            continue

with open('new.txt','w') as f:
    f.write(str)
