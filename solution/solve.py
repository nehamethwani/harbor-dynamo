import csv
import json

INPUT_PATH = "/app/sales.csv"
REPORT_PATH = "/app/report.json"


def main():
    total_revenue = 0.0
    category_counts = {}
    customer_spend = {}
    customer_order = []

    with open(INPUT_PATH, newline="") as f:
        reader = csv.DictReader(f)
        for row in reader:
            amount = float(row["amount"])
            customer_id = row["customer_id"]
            category = row["category"]

            total_revenue += amount
            category_counts[category] = category_counts.get(category, 0) + 1

            if customer_id not in customer_spend:
                customer_spend[customer_id] = 0.0
                customer_order.append(customer_id)
            customer_spend[customer_id] += amount

    top_customer = max(customer_order, key=lambda c: customer_spend[c])

    report = {
        "total_revenue": round(total_revenue, 2),
        "unique_customers": len(customer_spend),
        "orders_by_category": category_counts,
        "top_customer": top_customer,
    }

    with open(REPORT_PATH, "w") as f:
        json.dump(report, f)


if __name__ == "__main__":
    main()
