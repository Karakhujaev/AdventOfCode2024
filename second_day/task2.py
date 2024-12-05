class RedNosedReports:
    def __init__(self, reports):
        self.reports = reports

    def is_ordered(self, report):
        """Check if a report is ordered."""
        for i in range(len(report) - 1):
            if report[i] >= report[i + 1] or report[i] + 3 < report[i + 1]:
                return False
        return True

    def is_unordered(self, report):
        """Check if a report is unordered."""
        for i in range(len(report) - 1):
            if report[i] <= report[i + 1] or report[i] - 3 > report[i + 1]:
                return False
        return True

    def ordered_check(self, report):
        """Check ordered report allowing one bad level."""
        for i in range(len(report)):
            modified_report = report[:i] + report[i + 1:]  # Remove one level
            if self.is_ordered(modified_report):
                return True
        return self.is_ordered(report)  # Check without removing a level

    def unordered_check(self, report):
        """Check unordered report allowing one bad level."""
        for i in range(len(report)):
            modified_report = report[:i] + report[i + 1:]  # Remove one level
            if self.is_unordered(modified_report):
                return True
        return self.is_unordered(report)  # Check without removing a level

    def get_result(self):
        """Calculate the number of safe reports."""
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


