def prob09_1() -> int:
    max_area = 0
    area = 0
    coords = []
    with open('./input/prob09.txt') as f:
        lines = f.readlines()
        for line in lines:
            coord_str = line.strip()
            coord = coord_str.split(',')
            coord = (int(coord[0]), int(coord[1]))
            
            coords.append(coord)

    for i in range(len(coords)):
        for j in range(i, len(coords)):
            first = coords[i]
            second = coords[j]

            area = (abs(second[0] - first[0]) + 1) * (abs(second[1] - first[1]) + 1)
            max_area = max(max_area, area)
            
    return max_area
