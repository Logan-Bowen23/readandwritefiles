import csv

CSVFILE = "EmployeePay.csv"


def main():
    infile = open(CSVFILE, "r")

    reader = csv.reader(infile)

    next(reader)
    print("ID", format("Employee Name", ">4s"), "Payment")
    print("-" * 70)
    for row in reader:
        emp_id = row[0]
        name = row[1] + " " + row[2]
        total_pay = float(row[3]) * (1 + float(row[4]))
        print(emp_id, format(name, ">4s"), format(total_pay, ".2f"))
        input("-" * 70)

    infile.close()


main()
