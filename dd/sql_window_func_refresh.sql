/*

1. The "Top N" Problem (Window Functions)

Scenario: You have a sales table with salesperson_id, department, and amount.

Task: Write a query to find the top 2 highest-earning salespeople in each department.

*/

with ranking as (
	SELECT
		DENSE_RANK() OVER (PARTITION BY department ORDER BY amount DESC) as rank,
		salesperson_id,
		department,
		amount
	FROM sales
)

SELECT 
	rank,
	salesperson_id,
	department,
	amount
FROM 
	ranking
WHERE 
	rank <= 2;

/*

2. Handling Gaps (Joins/Edge Cases)

Scenario: You have a users table and a logins table.

Task: Identify users who have never logged in.

*/

WITH logged_in as (
	SELECT
		user_id
	FROM logins
)

SELECT
	u.user_id
FROM users u
LEFT JOIN logged_in l
	ON l.user_id = u.user_id
WHERE l.user_id IS NULL;

/*
1.Find item name and price with highest price(in case of ties, return all)
2.Show all menu ids where there are more than 30 items with each item price not
greater than $20. Please display the result by item count in descending order.
3.Find total number of menus that have menu items from either highest calories or
highest price.

Questions: 

- Are there any duplicate names in the table?
- High Price overall?

*/


-- Question 1:
WITH price_ranking AS (
	SELECT
		name,
		price,
		DENSE_RANK() OVER (ORDER BY price DESC) AS rank
	FROM items
)

SELECT 
	name,
	price
FROM price_ranking 
WHERE rank = 1;


-- Question 2:
SELECT
	menu_id,
	COUNT(id) as item_count
FROM items
WHERE price <= 20.0
GROUP BY menu_id
HAVING item_count > 30
ORDER BY item_count DESC;


-- Question 3:
WITH high_cal_or_price AS (
	SELECT
		id,
		menu_id,
		DENSE_RANK() OVER (ORDER BY price DESC) as price_rank,
		DENSE_RANK() OVER (ORDER BY calories DESC) as cal_rank
	FROM items
)

SELECT
	COUNT(DISTINCT menu_id) as menus_with_top_cal_or_price
FROM high_cal_or_price
WHERE price_rank = 1 OR cal_rank = 1;

