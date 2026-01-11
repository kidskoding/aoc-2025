def prob3_1():
    def largest_by_pass(lst, prev_len = 0):
        largest = (0 + prev_len, lst[0])
        for i in range(1, len(lst)):
            if lst[i] > largest[1]:
                largest = (i + prev_len, lst[i])
        
        return largest
    
    total = 0
    with open("./input/prob03.txt", 'r') as f:
        for line in f:
            line = line.strip()
            
            lst = [int(x) for x in line]
            largest = largest_by_pass(lst)
            
            if largest[0] == len(lst) - 1:
                second_largest = largest_by_pass(lst[:largest[0]])
            elif largest[0] == 0:
                second_largest = largest_by_pass(lst[largest[0] + 1:], len(lst[:largest[0] + 1]))
            else:
                second_largest = largest_by_pass(lst[largest[0] + 1:], len(lst[:largest[0] + 1]))
            
            largest_num = ""
            if largest[0] > second_largest[0]:
                largest_num = f'{second_largest[1]}{largest[1]}'
            else:
                largest_num = f'{largest[1]}{second_largest[1]}'
            
            total += int(largest_num)
            
    return total

def prob3_2():
    pass