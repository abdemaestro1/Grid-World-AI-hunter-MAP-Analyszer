def load_map(filename):
    """
    Reads a grid map file, cleans line whitespace/newlines,
    builds a 2D list (matrix), and locates Start ('S') and Goal ('G').
    
    Returns:
    grid (list of lists): The 2D grid matrix.
    start\_pos (tuple): (row, col) position of 'S'.
    goal\_pos (tuple): (row, col) position of 'G'.
    """
    grid=[]
    start_pos= None
    goal_pos= None

    #1.Open the map text file for reading 
    with open(filename,"r") as infile:
        #Loop through each line with row indexing
        for row_idx , line in enumerate(infile):

            #File Cleaning : Remove trelling newl=ines ('\n') and other whitespace
            clean_line= line.strip()

            #Ignore empty blank lines 
            if not clean_line:
                continue

            # 2. 2D Data Structure: Convert the string into a list of characters
            row= list(clean_line)

            # 3. Start &amp; Goal Tracking: Search for 'S' and 'G' in the current row
            for col_idx, char in enumerate(row):
                if char == 'S':
                    start_pos=(row_idx,col_idx)
                elif char == 'G':
                    goal_pos=(row_idx,col_idx)

            # Append the row list to form our 2D grid matrix
            grid.append(row)
        return grid , start_pos, goal_pos

#Example test  run 
if __name__ == "__main__":
    #load the map file 
    map_grid , start, goal = load_map("map.txt")

    #print diagnostics
    print("--- loading map grid---")
    for r in map_grid:
        print(r)
    print(f"\n Grid Size: {len(map_grid)} rows x {len(map_grid)} cols")
    print(f" Start Position (S): {start}")
    print(f"Goal position: {goal}")
    