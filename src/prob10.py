from collections import deque

def prob10_1() -> int:
    sum = 0
    with open('./input/prob10.txt') as f:
        for line in f:
            parts = line.split()
            
            target = parts[0]
            schematics = parts[1:-1]

            target = target.strip("[]")
            parsed_schematics = []
            for schematic in schematics:
                schematic = schematic.strip("()")
                nums = list(map(int, schematic.split(",")))
                parsed_schematics.append(nums)

            target_mask = 0
            for i, ch in enumerate(target):
                if ch == '#':
                    target_mask |= (1 << i)

            queue = deque([(0, 0)])
            visited = {0}
            while queue:
                curr_mask, presses = queue.popleft()
                if curr_mask == target_mask:
                    sum += presses

                for schematic in parsed_schematics:
                    button_mask = 0

                    for idx in schematic:
                        button_mask |= (1 << idx)

                    next_mask = curr_mask ^ button_mask
                    if next_mask not in visited:
                        visited.add(next_mask)
                        queue.append((next_mask, presses + 1))

    return sum
