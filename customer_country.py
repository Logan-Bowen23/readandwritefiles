import csv

CSVFILE = "customers.csv"


def main():
    infile = open(CSVFILE, "r")
    outfile = open("customer_country.csv", "w", newline="")
    writer = csv.writer(outfile, delimiter=",")
    reader = csv.reader(infile)

    next(reader)
    fieldnames = ["Name:", "Country:"]
    writer.writerow(fieldnames)
    for row in reader:
        name = row[1] + " " + row[2]
        country = row[4]

        total_customers += 1
        output = [name, format(country, "20")]
        writer.writerow(output)
        print("Total Customers: ")

    infile.close()
    outfile.close()


main()
