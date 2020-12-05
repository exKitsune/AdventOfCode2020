with open('./input.txt', 'r') as f:
    input_file = f.read().splitlines()

    
def isValid(passport):
    return passport['byr'] != -1 and \
        passport['iyr'] != -1 and \
        passport['eyr'] != -1 and \
        passport['hgt'] != '' and \
        passport['hcl'] != '' and \
        passport['ecl'] != '' and \
        passport['pid'] != -1 

passport_list = []
current_passport = { 'byr':-1, 'iyr':-1, 'eyr':-1, 'hgt':'', 'hcl':'', 'ecl':'', 'pid':-1, 'cid':-1 }



for line in input_file:
    if line == '':
        passport_list.append(current_passport)
        current_passport = { 'byr':-1, 'iyr':-1, 'eyr':-1, 'hgt':'', 'hcl':'', 'ecl':'', 'pid':-1, 'cid':-1 }
    else:
        entries = line.split(" ")
        for entry in entries:
            key, value = entry.partition(":")[::2]
            current_passport[key] = value
passport_list.append(current_passport)

valid_pp = 0
for pp in passport_list:
    if isValid(pp):
        valid_pp += 1

print(valid_pp)
    

    