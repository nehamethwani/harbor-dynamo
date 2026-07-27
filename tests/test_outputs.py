import json

REPORT_PATH = "/app/report.json"


def load_report():
    with open(REPORT_PATH) as f:
        return json.load(f)


def test_total_revenue():
    """instruction.md criterion 1: total_revenue is the sum of amount, rounded to 2 decimal places."""
    report = load_report()
    assert report["total_revenue"] == 686.99


def test_unique_customers():
    """instruction.md criterion 2: unique_customers is the count of distinct customer_id values."""
    report = load_report()
    assert report["unique_customers"] == 4


def test_orders_by_category():
    """instruction.md criterion 3: orders_by_category maps every category seen to its exact order count, with no extra categories."""
    report = load_report()
    assert report["orders_by_category"] == {"electronics": 4, "books": 3, "clothing": 3}


def test_top_customer():
    """instruction.md criterion 4: top_customer is the customer_id with the highest total spend, first-seen tiebreak."""
    report = load_report()
    assert report["top_customer"] == "C001"
