def prob04_1() -> int:
    grid = []
    
    with open('./input/prob04.txt') as f:
        for line in f:
            grid.append(list(line.strip()))
    
    directions = [
        (-1, 1), (-1, 0), (-1, -1),
        (0, -1),          (0, 1),
        (1, -1),  (1, 0), (1, 1)
    ]
    rows = len(grid)
    cols = len(grid[0])
    
    accessible_rolls = 0
    
    for r in range(rows):
        for c in range(cols):
            neighbor_count = 0
            
            if grid[r][c] == '@':
                for dr, dc in directions:
                    nr = r + dr
                    nc = c + dc
                    
                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == '@':
                        neighbor_count += 1
                        
                if neighbor_count < 4:
                    accessible_rolls += 1
            
    return accessible_rolls

def prob04_2() -> int:
    grid = []
    
    with open('./input/prob04.txt') as f:
        for line in f:
            grid.append(list(line.strip()))
    
    directions = [
        (-1, 1), (-1, 0), (-1, -1),
        (0, -1),          (0, 1),
        (1, -1),  (1, 0), (1, 1)
    ]
    rows = len(grid)
    cols = len(grid[0])
    
    accessible_rolls = 0
    while True:
        to_remove = []
        
        for r in range(rows):
            for c in range(cols):
                neighbor_count = 0
                
                if grid[r][c] == '@':
                    for dr, dc in directions:
                        nr = r + dr
                        nc = c + dc
                        
                        if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == '@':
                            neighbor_count += 1
                            
                    if neighbor_count < 4:
                        to_remove.append((r, c))
                        
        if not to_remove:
            break
        
        accessible_rolls += len(to_remove)
        
        for (r, c) in to_remove:
            grid[r][c] = '.'
            
    return accessible_rolls
