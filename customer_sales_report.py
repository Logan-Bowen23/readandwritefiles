import csv

CSVFILE = "sales.csv"


def main():
    infile = open(CSVFILE, "r")
    reader = csv.reader(infile, delimiter=",")
    fieldrow = next(reader)

    t_id = ""
    sales_data = []
    total = 0

    for row in reader:
        cust_id = row[0]
        order_date = row[1]
        ship_date = row[2]
        sub_total = row[3]
        tax_amount = row[4]
        freight = row[5]

        if cust_id != t_id:
            sales_data.append([t_id, round(total, 2)])
            t_id = cust_id
            total = 0
        total += float(sub_total) + float(tax_amount) + float(freight)
        sales_data.append([t_id, round(total, 2)])
        sales_data.pop(0)
        filename = "salesreport.csv"

        with open(filename, "w") as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(["Customer", "Total"])
            for customer in sales_data:
                writer.writerow([customer[0], customer[1]])

    infile.close()


main()
