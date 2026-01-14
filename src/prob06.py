def prob6_1():
    cum_sum = 0
    with open("./input/prob06.txt") as f:
        lines = f.readlines()
        lst = []
        
        for line in lines[:-1]:
            line = line.strip()
            arr = [int(x) for x in line.split()]
            lst.append(arr)
            
        ops = list(lines[-1].strip().split())
        
        i, j = 0, 0
        rows, cols = len(lst), len(lst[0])
        while j < cols:
            op = ops[j]
            product = 1
            total = 0
            i = 0
            
            while i < rows:
                match op:
                    case '*':
                        product *= lst[i][j]
                    case '+':
                        total += lst[i][j]
                i += 1
            
            match op:
                case '*':
                    cum_sum += product
                case '+':
                    cum_sum += total
            j += 1
            
    return cum_sum

# test commit
# test commit #2