from collections import Counter

# 23082277
def similarity_score(left_list, right_list):
    data = Counter(right_list)
    for idx, value in enumerate(left_list):
      if value in data:
        left_list[idx] = value * data[value]
        continue
      left_list[idx] = 0

    return sum(left_list)

def main():
    with open("input2.txt", "r") as file:
        lines = file.readlines()

    left_list = []
    right_list = []
    for line in lines:
        left, right = map(int, line.split())
        left_list.append(left)
        right_list.append(right)

    result = similarity_score(left_list, right_list)
    print(result)  

if __name__ == "__main__":
    main()