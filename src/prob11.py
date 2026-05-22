def prob11_1() -> int:
    graph = {}
    
    with open('./input/prob11.txt') as f:
        for line in f:
            line = line.rstrip('\n')
            lst = line.replace(':', '').split()
        
            graph[lst[0]] = lst[1:]
            
    def dfs(node: str) -> int:
        if node == "out":
            return 1
        
        total = 0
        for neighbor in graph[node]:
            total += dfs(neighbor)
            
        return total
    
    return dfs("you")

def prob11_2() -> int:
    graph = {}
    
    with open('./input/prob11.txt') as f:
        for line in f:
            line = line.rstrip('\n')
            lst = line.replace(':', '').split()
            
            graph[lst[0]] = lst[1:]

    memo = {}            
    def dfs(node: str, seen_dac: bool, seen_fft: bool) -> int:
        if node == 'dac':
            seen_dac = True
        
        if node == 'fft':
            seen_fft = True
        
        if node == 'out':
            return 1 if seen_dac and seen_fft else 0
        
        key = (node, seen_dac, seen_fft)
        if key in memo:
            return memo[key]
        
        total = 0
        for neighbor in graph[node]:
            total += dfs(neighbor, seen_dac, seen_fft)
            
        memo[key] = total
        return total
    
    return dfs("svr", False, False)
