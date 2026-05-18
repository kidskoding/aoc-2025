def prob5_1() -> int:
    fresh_ingredients = 0
    with open('./input/prob05.txt') as f:
        ranges = []
        line = f.readline().strip()
        while line != '':
            ranges.append(line)
            line = f.readline().strip()
        
        for line in f:
            ingredient_id = int(line.strip())
            for x in ranges:
                if ingredient_id >= int(x[0:x.index('-')]) and ingredient_id <= int(x[x.index('-') + 1:]):
                    fresh_ingredients += 1
                    break
            
    return fresh_ingredients

def prob5_2() -> int:
    ranges = []
    with open('./input/prob05.txt') as f:
        line = f.readline().strip()
        while line != '' and '-' in line:
            start = int(line[0:line.index('-')])
            end = int(line[line.index('-') + 1:])
            
            ranges.append((start, end))
            line = f.readline().strip()
    
    ranges.sort()
    merged = []
    for start, end in ranges:
        if merged and start <= merged[-1][1] + 1:
            merged[-1] = (merged[-1][0], max(merged[-1][1], end))
        else:
            merged.append((start, end))
    
    return sum(end - start + 1 for start, end in merged)
