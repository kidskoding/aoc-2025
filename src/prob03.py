def prob3_1():
    total = 0
    
    with open("./input/prob03_sample.txt", 'r') as f:
        for line in f:
            line = line.strip()
            
            lst = [int(x) for x in line]
            largest = (0, lst[0])
            diff = abs(largest[1] - lst[1])
            second_largest = (1, lst[1])
            
            for i, x in enumerate(lst, 1):
                if x > largest[1]: 
                    largest = (i, x)
                
                diff = abs(largest[1] - x)
                if diff > second_largest[1]:
                    second_largest = (i, x)
                    
            print(largest, second_largest)
            
    return total