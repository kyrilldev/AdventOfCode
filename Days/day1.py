def part1():
    with open("./Contents/content1.txt", "r") as file_object:
        lines = file_object.readlines()
    
    listone = []
    listtwo = []
    for line in lines:
        temp = line.split("   ")
        listone.append(int(temp[0]))
        listtwo.append(int(temp[1]))
        
    listone.sort()
    listtwo.sort()

    totalDistance = 0

    idx = 0
    for digit in listone:
        distance = abs(digit - listtwo[idx])
        totalDistance += distance
        idx += 1
        
    print(totalDistance)
    
def part2():
    with open("./Contents/content1.txt", "r") as file_object:
        lines = file_object.readlines()
        
    total_score = 0
        
    listone = []
    listtwo = []
    for line in lines:
        temp = line.split("   ")
        listone.append(int(temp[0]))
        listtwo.append(int(temp[1]))
    
    for number in listone:
        total_score += number * listtwo.count(number)
        
    print(total_score)
    
if __name__ == "__main__":
    part1()
    part2()