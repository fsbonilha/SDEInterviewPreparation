from dataclasses import dataclass
from typing import List

@dataclass
class Food:
	name: str
	calories: int
	price: int

def parse_foods(data: List[List[any]]) -> List[Food]:
	parsed = []
	for item in data:
		food = Food(item[0], item[1], item[2])
		parsed.append(food)
	return parsed

def get_average_price(foods: List[Food]) -> float:
	if not foods: return 0.0
	total = 0
	for food in foods:
		total += food.price
	return total / len(foods)

def get_above_average_priced_foods(foods: List[Food]) -> List[Food]:
	average_price = get_average_price(foods)
	above_average = []
	for food in foods:
		if food.price > average_price:
			above_average.append(food)
	return above_average

def get_top_two_calories(foods: List[Food]) -> List[Food]:
	sorted_foods = sorted(foods, key=lambda x: x.calories, reverse=True)
	return sorted_foods[:2]

# Considering that by "qualify for both", you mean the top two OVERALL and at the same time above average price OVERALL
def top_two_calories_and_above_average_price(foods: List[Food]) -> List[Food]:
	top_two_calories = get_top_two_calories(foods)
	above_average_price = get_above_average_priced_foods(foods)
	both = [food for food in top_two_calories if food in above_average_price]
	return sorted(both, key=lambda x: x.name)

input =[
	['ABUELO SUCIO (16oz)',400,26],
	['Chick-fil-A Chicken Sandwich',400,6],
	['Chicken in Lettuce Cups',900,19],
	['Classic French Dip',900,16],
	['Grilled Chicken Teriyaki',400,18],
	['Medium 8 pc Wing Combo',300,10],
	['Pad See You',1000,19],
	['Tea Leaf Rice',400,15],
	['Udon',300,12],
	['Very Cherry Ghirardelli Chocolate Cheesecake',900,10]
]

parsed = parse_foods(input)
result = top_two_calories_and_above_average_price(parsed)
print(result)

