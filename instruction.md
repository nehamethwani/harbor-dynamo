There's a CSV file at /app/sales.csv containing sales transactions from an online store, one order per row, with columns order_id, customer_id, category, and amount.

Write a script that reads /app/sales.csv and produces a single JSON report at /app/report.json summarizing the data. The output must be a UTF-8 JSON object with exactly these four keys:

1. total_revenue: a number, the sum of the amount column across all rows, rounded to 2 decimal places.
2. unique_customers: an integer, the count of distinct customer_id values in the file.
3. orders_by_category: an object mapping each category value that appears in the file to the integer number of orders in that category. Do not include categories that don't appear in the data.
4. top_customer: a string, the customer_id with the highest total amount spent, summed across all of their orders. If two customers are tied for the highest total, use whichever of them placed their first order earlier in the file.

Write only these four keys to /app/report.json — no extra fields, no wrapper array.
