def prob01_1() -> int:
    dial = 50
    password = 0
    
    with open('./input/prob01.txt') as f:
        for line in f:    
            direction = line[0]
            amt = int(line[1:])
            
            if direction == 'L':
                dial -= amt
                if dial < 0:
                    dial %= 100
            elif direction == 'R':
                dial += amt
                if dial > 99:
                    dial %= 100
            
            if dial == 0:
                password += 1
    
    return password

def prob01_2() -> int:
    dial = 50
    new_pass = 0
    
    with open('./input/prob01.txt') as f:
        for line in f:
            direction = line[0]
            amt = int(line[1:])
            
            prev_dial = dial
            
            if direction == 'L':
                if prev_dial > 0:
                    crossings = (amt - prev_dial) // 100 + 1 if amt >= prev_dial else 0    
                else:
                    crossings = amt // 100
                
                new_pass += crossings
                
                dial = (prev_dial - amt) % 100
            
            elif direction == 'R':
                if prev_dial > 0:
                    first_hit = 100 - prev_dial
                    crossings = (amt - first_hit) // 100 + 1 if amt >= first_hit else 0
                else:
                    crossings = amt // 100
                    
                new_pass += crossings
                dial = (prev_dial + amt) % 100
            
    return new_pass