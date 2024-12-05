def part1():
    with open("./Contents/content4.txt", "r") as file_object:
        lines = file_object.readlines()
    
    total_sum = 0
    
    for i in range(len(lines)):
        for j in range(len(lines)):
            currentChar = lines[i][j]
            if currentChar == 'X':
                total_sum += check_neighbours((i, j), lines, 1)
                
    print(total_sum)
                
# Currently struggling with the problem that xmas can be spelled any direction as long as it connects. even in circle. We need to somehow give a direction to keep checking in. When we start checking diagonally we need to keep checking diagonally.
def check_neighbours(array_pos, lines, letter_index) -> int:
    #this function has to be recursive
    print("entering recursive neighbour checking function")
    
    characters = ['X', 'M', 'A', 'S']
    
    checking_positions = [
        (-1, 0), 
        (-1, 1), 
        (0, -1), 
        (0, 1) , 
        (1, -1), 
        (1, 0) , 
        (1, 1) , 
        (-1, -1)
    ]
    
    neighbour_characters = []
    
    for dx, dy in checking_positions:
        ni, nj = array_pos[0] + dx, array_pos[1] + dy
        
        if 0 <= ni < len(lines) and 0 <= nj < len(lines[0]):
            neighbour_characters.append((lines[ni][nj], (ni, nj)))
    
    for char in neighbour_characters:
        if char[0] == characters[3] and letter_index == 3:# doesn't work because an X can stand next to a S
            return 1
        elif char[0] == characters[letter_index]:
            letter_index += 1
            return check_neighbours(char[1], lines, letter_index)
        else:
            continue
    
    return 0

    
if __name__ == "__main__":
    part1()