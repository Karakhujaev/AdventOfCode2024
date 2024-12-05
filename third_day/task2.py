import re

def calculate_mul_sum_second(data):
    mul_pattern = re.compile(r"mul\((\d{1,3}),(\d{1,3})\)")
    is_enabled = True 
    total_sum = 0

    for match in re.finditer(r"do\(\)|don't\(\)|mul\((\d{1,3}),(\d{1,3})\)", data):
        print(match.group())
        instruction = match.group(0)

        if instruction == "do()":
            is_enabled = True
        elif instruction == "don't()":
            is_enabled = False
        elif "mul" in instruction and is_enabled:
            x, y = map(int, mul_pattern.match(instruction).groups())
            total_sum += x * y

    return total_sum

def main():
    try:
        with open('/Users/freelancer/Desktop/AdventOfCode2024/third_day/input2.txt', 'r') as file:
            memory = file.read()
        
        result = calculate_mul_sum_second(memory)
        print("Sum of all valid multiplications:", result)
    except FileNotFoundError:
        print("Error: The file 'input1.txt' was not found.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
