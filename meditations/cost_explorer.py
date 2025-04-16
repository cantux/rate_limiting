#!/usr/bin/env python

from datetime import datetime
from dateutil.relativedelta import relativedelta

# products
# plans
# customers
# concept of a purchase
# billing cycle
# will there be updates? do we allow returns?
product_plans_costs = {"jira": {
        "basic": 20,
        "standard": 60,
        "premium": 250
        },
      "confluence": {
        "basic": 10,
        "standard": 16,
        "premium": 30
        }
}

customer_purchase = collections.defaultdict(list)
customer_purchase = {
        "microsoft": [["jira", "basic"],["confluence", "premium"]],
        "google": [["confluence", "standard"], ["jira", "standard", ]]
}

def customer_purchase(uniq_customer_name, product, plan):
    # check if there are previous purchases under the same name
    # check if dates overlap
    customer_purchase[uniq_customer_name].append([product, plan])


def calc_annual_cost():
    product_earnings = collections.defaultdict(int)
    for c, p_l in customer_purchase.items():
        for product, plan in p_l:
            product_earnings[product] += product_plans_costs[product][plan] * 12
    return product_earnings



customer_purchase = {
        "microsoft": [["jira", "basic", "2023-10-23"],["confluence", "premium", "2021-5-30"]],
        "google": [["confluence", "standard"], ["jira", "standard", ]]
}

def customer_purchase(uniq_customer_name, product, plan, end_date=None):
    if not end_date:
        end_date = datetime.now() + relativedelta(year=1)
    customer_purchase[uniq_customer_name].append([product, plan, end_date.strftime("%Y-%m-%d")])

# is there a recurring plan?
# how do we let customers know of their renewal?
# how do we quickly query about a specific purchase
# how do we update plans,, should we then recalculate?
# there must be a billing cycle

def test():
    assert fnc() == None

if __name__ == "__main__":
    test()

