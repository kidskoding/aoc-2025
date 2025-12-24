def prob1_1():
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

def prob1_2():
    pass