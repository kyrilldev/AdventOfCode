import re

def part1():
    with open("./Contents/content3.txt", "r") as file_object:
        lines = file_object.readlines()
    
    total_count = 0
    
    for line in lines:
        results = re.findall(r"mul\(\d{1,3},\d{1,3}\)", line)
        for result in results:
            # print("statement: " + result)
            super_result = re.findall(r"\d{1,3},\d{1,3}", result)
            temp = str(super_result)
            temp = temp.split(",")
            total_count += int(temp[0].removeprefix("['")) * int(temp[1].removesuffix("']"))
    
    print(total_count)
    
def part2():
    print("temp")
    with open("./Contents/content3.txt", "r") as file_object:
        lines = file_object.readlines()
    
    total_count = 0    
    execute = True
        
    for line in lines:
        results = [match.group() for match in re.finditer(r"mul\(\d{1,3},\d{1,3}\)|do\(\)|don't\(\)", line)]
        for result in results:
            if re.search(r"do\(\)", result):
                execute = True
            elif re.search(r"don't\(\)", result):
                execute = False
            elif execute and re.search(r"mul\(\d{1,3},\d{1,3}\)", result):
                super_result = re.findall(r"\d{1,3},\d{1,3}", result)
                temp = str(super_result)
                temp = temp.split(",")
                total_count += int(temp[0].removeprefix("['")) * int(temp[1].removesuffix("']"))
    
    print(total_count)
    
if __name__ == "__main__":
    part2()