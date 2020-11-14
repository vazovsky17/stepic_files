data = ''
with open('file.txt', 'r') as file:
    all = file.read().split('\n')
    math, phiz, rus, count = [], [], [], 0
    for line in all:
        if len(line) > 1:
            lst = [int(i) for i in line.split(';') if i.isdigit()]
            data += f'{sum(lst)/3}\n'
            math.append(lst[0])
            phiz.append(lst[1])
            rus.append(lst[2])
            count += 1
    data += f'{sum(math)/count} {sum(phiz)/count} {sum(rus)/count}\n'

with open('new.txt', 'w') as new:
    new.write(data)
