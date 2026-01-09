# sample test problem

def prob00():
    with open('./input/prob00.txt') as f:
        lines = 0
        # 1. Grab each line in the file
        for line in f:
            # 2. Count the number of lines in the file
            lines += 1
            
        return lines