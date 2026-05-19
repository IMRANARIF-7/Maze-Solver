# Assignment 3 
#281157456

# Wall representation 
right , bottom, left, top = 0, 1, 2, 3

def defining_maze(filename):
    with open(filename, 'r') as file:
        r, c = map(int, file.readline().split()) # to fetch the first line from txt file 
        end_r, end_c = map(int, file.readline().split()) # to fetch the second line for end coordinates 
        
        grid =[] # empty list which will eventually hold 4 int for the walls
        for i in range(r):
            row =[]
            third_line = file.readline().split()
            for x in range(c):
                sq = [int(y) for y in third_line[x]]
                row.append(sq)
            grid.append(row)
        
    return grid, (end_r, end_c)

def exploremaze(maze, c_pos, d_pos, path, prev_pos):
    row, col = c_pos
    if c_pos == d_pos:
        return path + [c_pos]
    
    prev_pos.add(c_pos)
    
    directions = [
        (0, 1, right, left),    # right
        (1, 0, bottom, top),    # down
        (0, -1, left, right),   # left
        (-1, 0, top, bottom)    # up
    ]
    
    for dr, dc, wall_from, wall_to in directions:
        new_row, new_col = row + dr, col + dc
        if 0 <= new_row < len(maze) and 0 <= new_col < len(maze[0]):
            if maze[row][col][wall_from] == 0 and maze[new_row][new_col][wall_to] == 0:
                if (new_row, new_col) not in prev_pos:
                    result = exploremaze(maze, (new_row, new_col), d_pos, path + [c_pos], prev_pos)
                    if result:
                        return result

    return None

def main():
    filename = input("maze1.txt or maze2.txt ").strip()
    maze, d_pos = defining_maze(filename)
    rows, cols = len(maze), len(maze[0])

    while True:
        try:
            start_row = int(input(f"Enter start row (0 to {rows - 1}): "))
            start_col = int(input(f"Enter start col (0 to {cols - 1}): "))
            if 0 <= start_row < rows and 0 <= start_col < cols:
                break
            else:
                print("coordinates are invalid. Try again.")
        except ValueError:
            print("You are allowed to enter integers.")

    path = exploremaze(maze, (start_row, start_col), d_pos, [], set())

    if path:
        print("The path is found:")
        for step in path:
            print(step)
        print("Finish:", d_pos)
    else:
        print("path could not be found ")

if __name__ == "__main__":
    main() 