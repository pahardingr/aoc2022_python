with open("input.txt") as aocd1:
    cal_list = aocd1.read().splitlines()

elves=[]
elf=[]

for k in cal_list:
    if k.isdigit():
        elf.append(int(k))
    else:
        elves.append(elf.copy())
        elf.clear()

sum_list = []

for elf in elves:
    sum_list.append(sum(elf))

max(sum_list) #max value in the list

top_3 = sum(sum_list[0:3])