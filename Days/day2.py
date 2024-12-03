def part1() -> None:
    with open("./Contents/content2.txt", "r") as file_object:
        lines = file_object.readlines()
        
    correct_reports = 0
        
    for line in lines:
        correct_reports += check_for_number_creasion(list(map(int, line.split(" "))))
        
    print(correct_reports)
    
    
def check_for_number_creasion(numbers) -> int:
    #check if numbers are increasing or decreasing
    first = numbers[0]
    last = numbers[len(numbers) - 1]
    max_variation = 3
    
    idx = 0
    descending = first > last
    for number in numbers:
        if idx == 0:
            idx += 1
            continue
        difference = abs(number - numbers[idx - 1])
        if difference > max_variation or difference < 1 or (descending and numbers[idx] > numbers[idx - 1]) or (not descending and numbers[idx] < numbers[idx - 1]):
            return 0
        idx += 1
        
    return 1
    
def part2() -> None:
    with open("./Contents/content2.txt", "r") as file_object:
        lines = file_object.readlines()
        
    correct_reports = 0
        
    for line in lines:
        correct_reports += check_for_number_creasion_improved(list(map(int, line.split())), True)
        
    print(correct_reports)
    
def check_for_number_creasion_improved(numbers, can_remove) -> int:
    #check if numbers are increasing or decreasing
    first = numbers[0]
    last = numbers[len(numbers) - 1]
    max_variation = 3
    removed_once = False
    
    descending = first > last
    
    for idx in range(len(numbers)):
        if idx == 0:
            continue
        difference = abs(numbers[idx] - numbers[idx - 1])#numbers[] == lastnumber
        if difference > max_variation or difference < 1 or (descending and numbers[idx] > numbers[idx - 1]) or (not descending and numbers[idx] < numbers[idx - 1]):
            if can_remove and not removed_once:
                modified_numbers = numbers[:idx] + numbers[idx + 1:]
                removed_once = True
                return check_for_number_creasion_improved(modified_numbers, False)
            else:
                return 0
    return 1

def is_safe(report):
    """
    Determines if a report is safe based on Part 1 rules.
    """
    # Check if the sequence is strictly increasing or decreasing
    is_increasing = all(1 <= b - a <= 3 for a, b in zip(report, report[1:]))
    is_decreasing = all(1 <= a - b <= 3 for a, b in zip(report, report[1:]))
    return is_increasing or is_decreasing


def count_safe_reports_with_dampener(reports):
    """
    Counts the number of safe reports, including those that can be made safe
    by removing one level.
    """
    safe_count = 0

    for report in reports:
        # Check if the report is already safe
        if is_safe(report):
            safe_count += 1
            continue

        # Try removing each level and check if the remaining sequence is safe
        for i in range(len(report)):
            modified_report = report[:i] + report[i+1:]
            if is_safe(modified_report):
                safe_count += 1
                break  # No need to check further levels for this report

    return safe_count


def process_file(file_path):
    """
    Processes a file where each line contains a space-separated string of levels.
    """
    with open(file_path, 'r') as f:
        reports = [list(map(int, line.split())) for line in f.readlines()]
    return reports

if __name__ == "__main__":
    # part1()
    part2()
    # file_path = "./Contents/content2.txt"  # Replace with your actual file path
    # reports = process_file(file_path)
    # safe_count = count_safe_reports_with_dampener(reports)
    # print(f"Number of safe reports: {safe_count}")