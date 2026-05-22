def prob02_1() -> int:
    total = 0
    
    with open('./input/prob02.txt', 'r') as f:
        lst = f.readline().split(',')
        
        for rnge in lst:
            start = int(rnge[:rnge.index('-')])
            end = int(rnge[rnge.index('-') + 1:])
            
            for x in range(start, end + 1):
                temp = str(x)
                
                first_half = temp[:len(temp) // 2]
                second_half = temp[len(temp) // 2:]
                
                if first_half == second_half:
                    total += x
        
    return total

def prob02_2() -> int:
    total = 0
    
    def has_repeated_sequence(num_str):
        n = len(num_str)
        dp = [False] * (n + 1)
        dp[0] = True
        
        for i in range(1, n + 1):
            for pattern_len in range(1, i // 2 + 1):
                if i % pattern_len == 0:
                    pattern = num_str[:pattern_len]
                    
                    if pattern * (i // pattern_len) == num_str[:i]:
                        dp[i] = True
                        break
                    
        return dp[n]
    
    with open('./input/prob02.txt', 'r') as f:
        lst = f.readline().split(',')
        
        for rnge in lst:
            start = int(rnge[:rnge.index('-')])
            end = int(rnge[rnge.index('-') + 1:])
            
            for x in range(start, end + 1):
                if has_repeated_sequence(str(x)):
                    total += x
        
    return total
