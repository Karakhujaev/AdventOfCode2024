def is_increasing(data):
    if data[0]  <  data[-1]:
        return True

    elif data[0] > data[-1]:
        return False

def ordered_check(report):
    prev = report[0]
    for num in report[1:]:
        if prev >= num or prev + 3 < num:
            return False
        prev = num

    return True

def unordered_check(report):
    prev = report[0]
    for num in report[1:]:
        print(prev==num)
        if prev <= num or prev - 3 > num:
            return False
        
        prev = num

    return True

#686
def issafe(reports):
    result = 0
    for report in reports:
        if is_increasing(report):
            if ordered_check(report):
                result +=1
        
        else:
            if unordered_check(report):
                print(unordered_check(report))
                result += 1
    
    return result

def main():
    with open('input1.txt', 'r') as file:
        lines = file.readlines()

    reports = []
    for line in lines:
        if line.strip(): 
            report = list(map(int, line.strip().split()))
            reports.append(report)

    result = issafe(reports)
    print("Result:", result)

if __name__ == "__main__":
    main()


