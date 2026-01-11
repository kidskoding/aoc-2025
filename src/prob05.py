def prob5_1():
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