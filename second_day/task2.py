class RedNosedReports:
    def __init__(self, reports):
        self.reports = reports

    def is_ordered(self, report):
        for i in range(len(report) - 1):
            if report[i] >= report[i + 1] or report[i] + 3 < report[i + 1]:
                return False
        return True

    def is_unordered(self, report):
        for i in range(len(report) - 1):
            if report[i] <= report[i + 1] or report[i] - 3 > report[i + 1]:
                return False
        return True

    def ordered_check(self, report):
        for i in range(len(report)):
            modified_report = report[:i] + report[i + 1:]  
            if self.is_ordered(modified_report):
                return True
        return self.is_ordered(report)  

    def unordered_check(self, report):
        for i in range(len(report)):
            modified_report = report[:i] + report[i + 1:] 
            if self.is_unordered(modified_report):
                return True
        return self.is_unordered(report) 

    def get_result(self):
        result = 0
        for report in self.reports:
            if self.ordered_check(report) or self.unordered_check(report):
                result += 1
        return result

    

def main():
    with open('/Users/freelancer/Desktop/AdventOfCode2024/second_day/input2.txt', 'r') as file:
        lines = file.readlines()

    reports = []
    for line in lines:
        if line.strip(): 
            report = list(map(int, line.strip().split()))
            reports.append(report)

    red_nodes = RedNosedReports(reports)
    print("Result:", red_nodes.get_result())

if __name__ == "__main__":
    main()


