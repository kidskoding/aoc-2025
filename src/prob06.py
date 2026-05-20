def prob6_1() -> int:
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

def prob6_2() -> int:
    cum_sum = 0
    with open('./input/prob06.txt') as f:
        lines = f.readlines()
    
    grid = []
    for line in lines:
        arr = list(line.rstrip('\n'))
        grid.append(arr)
    
    rows = len(grid)
    cols = len(grid[0])
    
    current_numbers = []
    for c in range(cols - 1, -1, -1):
        num = ''
        
        for r in range(rows - 1):
            if grid[r][c].isdigit():
                num += grid[r][c]
                
        if num:
            current_numbers.append(int(num))
        
        if grid[-1][c] == '+':
            sum = 0
            for num in current_numbers:
                sum += num
                
            cum_sum += sum
            current_numbers = []
        elif grid[-1][c] == '*':
            product = 1
            for num in current_numbers:
                product *= num
            
            cum_sum += product
            current_numbers = []
            
    return cum_sum
