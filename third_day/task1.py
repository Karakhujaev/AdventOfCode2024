import re

def calculate_mul_sum(memory):
    pattern = r"mul\((\d{1,3}),(\d{1,3})\)"
    matches = re.findall(pattern, memory)
    print(matches[:10])
    total = 0
    for x, y in matches:
        total += int(x) * int(y)
    
    return total

def main():
    try:
        with open('/Users/freelancer/Desktop/AdventOfCode2024/third_day/input1.txt', 'r') as file:
            memory = file.read()
        
        result = calculate_mul_sum(memory)
        print("Sum of all valid multiplications:", result)
    except FileNotFoundError:
        print("Error: The file 'input1.txt' was not found.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
