import re 
with open('./input.txt', 'r') as f:
    input_file = f.read().splitlines()

    
def isValid(passport):   
    byr = int(passport['byr']) >= 1920 and int(passport['byr']) <= 2002
    iyr = int(passport['iyr']) >= 2010 and int(passport['iyr']) <= 2020
    eyr = int(passport['eyr']) >= 2020 and int(passport['eyr']) <= 2030
    
    hgt = False
    if passport['hgt'] != '':
        res = re.findall("[\d]*", passport['hgt'])[0] 
        if passport['hgt'].lower().endswith('in'):
            hgt = int(res) >= 59 and int(res) <= 76
        elif passport['hgt'].lower().endswith('cm'):
            hgt = int(res) >=150 and int(res) <= 193
    
    hcl = False
    if passport['hcl'] != '':
        if passport['hcl'].startswith('#'):
            res = re.findall("[\dA-Fa-f]*", passport['hcl'][1:])
            if len(res) == 2 and len(res[0]) == 6:
                hcl = True

    ecl = False
    if passport['ecl'] != '':
        if passport['ecl'].lower() in ('amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'):
            ecl = True
    
    pid = False
    if len(str(passport['pid'])) == 9:
        if int(passport['pid']):
            pid = True

    return byr and iyr and eyr and hgt and hcl and ecl and pid 

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
    

    