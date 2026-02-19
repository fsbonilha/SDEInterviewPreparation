import heapq

"""
CODING INTERVIEW PROBLEMS: DATA MANIPULATION (PURE PYTHON)
---------------------------------------------------------
The following problems test your ability to perform aggregations, 
filtering, and sorting using only Python built-ins.
"""

# PROBLEM 1: THE HIGH-EFFICIENCY REMOTE TEAM
# ------------------------------------------
# You are given a list of employees: [name, department, output_score, hours_worked]
#
# Tasks:
# 1. Calculate the average efficiency (output_score / hours_worked) across the 
#    entire company.
# 2. Identify employees whose individual efficiency is >= 20% higher than the 
#    company average.
# 3. Identify employees who belong to a department with at least 3 people listed 
#    in the input.
# 4. Return the names of employees who meet BOTH conditions (2 and 3), 
#    sorted by their efficiency (highest to lowest).
#
employees = [
    ["Alice", "Engineering", 120, 40],
    ["Bob", "Sales", 100, 50],
    ["Charlie", "Engineering", 150, 35],
    ["David", "Engineering", 80, 40],
    ["Eve", "Sales", 90, 30],
    ["Frank", "Marketing", 110, 40]
]

def get_average_efficiency(employees: list) -> list:
    total_output_score = 0
    total_hours = 0
    for employee in employees:
        total_output_score += employee[2]
        total_hours += employee[3]
    return total_output_score / total_hours

def get_high_efficiency_employee(employees: list) -> list:
    result = []
    efficiency_bar = get_average_efficiency(employees) * 1.2
    for employee in employees:
        if employee[2] / employee[3] >= efficiency_bar:
            result.append(employee)
    return result

def get_people_in_big_departments(employees: list):
    departments = {}
    for employee in employees:
        departments[employee[2]] = departments.get(employee[2]) + employee[2]

    result = []
    for department, employees in departments.items():
        if len(employees) >= 3:
            result.append(employees)
    return result

def get_efficient_team_members(employees: list):
    high_efficient = get_high_efficiency_employee(employees)
    big_departments = set(get_people_in_big_departments(employees))

    result = []
    for employee in high_efficient:
        if employee in big_departments:
            result.append(employee)
    return result



# PROBLEM 2: THE PORTFOLIO RISK ANALYZER
# --------------------------------------
# A financial app provides a list of stocks: 
# [ticker, sector, price_change_percentage, volatility_index]
#
# Tasks:
# 1. Calculate the median price_change_percentage of all stocks.
#    (Note: For odd length, it's the middle; for even, it's the average of the two middle.)
# 2. Find stocks that performed strictly better than the median (higher percentage).
# 3. Find the stocks that have a volatility_index within the bottom 3 (lowest risk) 
#    of the entire list. If there is a tie for the 3rd spot, include all tied items.
# 4. Return the tickers that satisfy both conditions, sorted alphabetically.
#
stocks = [
    ["AAPL", "Tech", 5.2, 12],
    ["TSLA", "Auto", -2.1, 45],
    ["JPM", "Finance", 1.5, 8],
    ["GOOGL", "Tech", 3.8, 15],
    ["XOM", "Energy", 4.1, 20],
    ["KO", "Beverage", 0.5, 5],
    ["PFE", "Health", 2.2, 7]
]

def get_median_price_change_perc(stocks: list) -> float:
    price_changes = sorted([stock[2] for stock in stocks])
    count = len(price_changes)
    if count % 2 == 0:
        return (price_changes[count//2] + price_changes[count//2 - 1])/2
    else:
        return price_changes[count//2]

def get_better_than_median(stocks: list) -> list:
    median = get_median_price_change_perc(stocks)
    return [stock for stock in stocks if stock[2] > median]

def get_low_volatility_stocks(stocks: list) -> list:
    return sorted(stocks, key=lambda stock: stock[3])[:3]

def get_low_risk_performers(stocks: list) -> list:
    low_volatility = {stock[0]: stock for stock in get_low_volatility_stocks(stocks)}
    performers = {stock[0]: stock for stock in get_better_than_median(stocks)}
    
    result = []

    for stock_name, stock in low_volatility.items():
        if stock_name in performers:
            result.append(stock)

    return sorted(result, key=lambda stock: stock[0])



# PROBLEM 3: THE WAREHOUSE STOCK OPTIMIZER
# ----------------------------------------
# You have inventory data: [product_id, category, stock_count, unit_cost]
#
# Tasks:
# 1. For each category, find the maximum unit_cost within that category.
# 2. Filter for products that have a unit_cost equal to their specific 
#    category's maximum cost.
# 3. Of those items, filter further for those where the total inventory value 
#    (stock_count * unit_cost) is strictly greater than 1000.
# 4. Return a list of product_ids, sorted by their total inventory value 
#    in descending order.

inventory = [
    ["PROD_01", "Electronics", 10, 150],
    ["PROD_02", "Electronics", 8, 200],
    ["PROD_03", "Furniture", 2, 600],
    ["PROD_04", "Furniture", 10, 300],
    ["PROD_05", "Grocery", 100, 5],
    ["PROD_06", "Grocery", 150, 12]
]

ID = 0
CATEGORY = 1
STOCK_COUNT = 2
UNIT_COST = 3

def get_max_unit_cost_within_category(inventory) -> dict[str, int]:
    max_costs = {}
    for product in inventory:
        category = product[CATEGORY]
        cost = product[UNIT_COST]
        max_costs[category] = max(max_costs.get(category, -1), cost)
    return max_costs

def get_premium_high_value_stock(inventory):
    max_costs = get_max_unit_cost_within_category(inventory)
    return [product for product in inventory if product[UNIT_COST] == max_costs[product[CATEGORY]]]

def get_inventory_value(product):
    return product[STOCK_COUNT] * product[UNIT_COST]

def get_high_inventory_value(inventory):
    return [product for product in inventory if get_inventory_value(product) > 1000]

def get_total_inventory_value_ranking(inventory):
    ranking = sorted(inventory, key=get_inventory_value, reverse=True)
    return [product[ID] for product in rakin]


# PROBLEM 4: THE ENERGY EFFICIENT FLEET
# --------------------------------------
# You have a list of vehicles: [vin, model, fuel_type, mpg, range_miles]
# 
# Tasks:
# 1. Calculate the average 'mpg' (miles per gallon) of all vehicles.
# 2. Identify vehicles that have an 'mpg' strictly higher than the average.
# 3. Among all vehicles, find those that have a 'range_miles' in the top 3.
#    (If there is a tie for the 3rd spot, include all tied items).
# 4. Return a list of 'vin' strings for vehicles that satisfy BOTH 
#    conditions (2 and 3), sorted alphabetically by model name.

vehicles = [
    ["V1", "Model S", "Electric", 120, 400],
    ["V2", "Civic", "Gas", 35, 350],
    ["V3", "Prius", "Hybrid", 55, 500],
    ["V4", "Bolt", "Electric", 110, 250],
    ["V5", "Lucid", "Electric", 130, 500],
    ["V6", "Hummer", "Gas", 15, 400]
]

VIN=0
MODEL=1
FUEL_TYPE=2
MPG=3
RANGE_MILES=4

def get_average_mpg(vehicles):
    mpgs = [vehicle[MPG] for vehicle in vehicles]
    return sum(mpgs)/len(mpgs)

def get_above_average_mpg(vehicles):
    average_mpg = get_average_mpg(vehicles)
    return [vehicle for vehicle in vehicles if vehicle[MPG] > average_mpg]

def get_top_3_range_miles(vehicles):
    unique_ranges = {vehicle[RANGE_MILES] for vehicle in vehicles}
    sorted_unique = sorted(list(unique_ranges), reverse=True)

    cutoff_idx = min(2, len(sorted_unique) - 1)
    threshold = sorted_unique[cutoff_idx]

    return [vehicle for vehicle in vehicles if vehicle[RANGE_MILES] >= threshold]

def get_both_conditions(vehicles):
    above_average_mpg = set([vehicle[VIN] for vehicle in get_above_average_mpg(vehicles)])
    top_3_range_miles = get_top_3_range_miles(vehicles)
    both_conditions = [vehicle for vehicle in top_3_range_miles if vehicle[VIN] in above_average_mpg]
    return sorted(both_conditions, key=lambda vehicle: vehicle[MODEL])


# PROBLEM 5: THE CLASSROOM STAR PERFORMERS
# ----------------------------------------
# Data: [student_name, subject, score, attendance_percentage]
#
# Tasks:
# 1. Find the maximum 'score' achieved across all students and subjects.
# 2. Identify students who have at least one score within 5 points of 
#    that maximum (e.g., if max is 100, score >= 95).
# 3. Identify students who have an 'attendance_percentage' higher than 
#    the average attendance of the whole group.
# 4. Return the unique names of students who meet BOTH conditions, 
#    sorted by their highest score (descending).
#
# classroom = [
#     ["Alice", "Math", 95, 90],
#     ["Bob", "Math", 80, 95],
#     ["Charlie", "Science", 100, 70],
#     ["Alice", "Science", 88, 90],
#     ["David", "Math", 92, 85]
# ]


# PROBLEM 6: THE LOW-STOCK ADVISOR
# --------------------------------
# Data: [item_id, category, current_stock, restock_threshold]
#
# Tasks:
# 1. Calculate the 'urgency_ratio' for each item: (restock_threshold / current_stock).
#    (Note: If current_stock is 0, treat the ratio as restock_threshold * 2).
# 2. Find the average 'urgency_ratio' for the entire inventory.
# 3. Filter for items where the 'urgency_ratio' is greater than the average.
# 4. Out of those, return only the item_ids that belong to a category 
#    containing more than 1 item in this list.
# 5. Sort the final item_ids by the urgency_ratio (highest to lowest).
#
# inventory = [
#     ["ID01", "Produce", 10, 20],   # Ratio: 2.0
#     ["ID02", "Produce", 5, 5],     # Ratio: 1.0
#     ["ID03", "Dairy", 0, 10],      # Ratio: 20.0
#     ["ID04", "Bakery", 20, 10],    # Ratio: 0.5
#     ["ID05", "Dairy", 15, 10]      # Ratio: 0.66
# ]

def main():
    print(get_top_3_range_miles(vehicles))
    print(get_both_conditions(vehicles))

if __name__ == '__main__':
    main()