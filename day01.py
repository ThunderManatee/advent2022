from aocd import get_data
data = get_data(day=1)
dn = [d for d in data.splitlines()]

def part1(data):
    most = 0
    elf = 0
    for x in data:
        if elf > most:
            most = elf
        if x == '':
            elf = 0
        else:
            elf = elf + int(x)    
    return most
def part2(data):
    first = 0
    second = 0
    third = 0
    elf = 0
    for x in data:
        if x == '':
            if elf > first:
                third = second
                second = first
                first  = elf
            elif elf > second:
                third = second
                second = elf
            elif elf > third:
                third = elf
            elf = 0
        else:
            elf = elf + int(x)    
    return first + second + third

print(part1(dn))
print(part2(dn))
