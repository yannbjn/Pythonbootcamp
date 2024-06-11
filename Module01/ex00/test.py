# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    test.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: yabejani <yabejani@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/06/11 10:50:38 by yabejani          #+#    #+#              #
#    Updated: 2024/06/11 15:08:18 by yabejani         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from book import Book
from recipe import Recipe

try:
	cake = Recipe(
		name="Cake",
		cooking_lvl=5,
		cooking_time=60,
		ingredients=["flour", "sugar", "eggs"],
		recipe_type="dessert",
		description="A delicious cake."
		)
except ValueError as e:
    print(f"Error: {e}")

try:
	olive = Recipe(
		name="tarte aux olives",
		cooking_lvl=3,
		cooking_time=26,
		ingredients=["Quelques olives", "Beaucoup de farine", "3 oeufs"],
		recipe_type="lunch",
		description="Une delicieuse tarte aux olives simple a realiser :)"
		)
except ValueError as e:
    print(f"Error: {e}")

try:
	jambon = Recipe(
		name="tarte au jambon",
		cooking_lvl=3,
		cooking_time=26,
		ingredients=["Un peu de jambon", "Beaucoup de farine", "3 oeufs"],
		recipe_type="lunch",
		description="Une delicieuse tarte au jambon simple a realiser"
		)
except ValueError as e:
    print(f"Error: {e}")

# Create a book and add recipes
my_book = Book("Family Recipes")
my_book.add_recipe(olive)
my_book.add_recipe(cake)
my_book.add_recipe(jambon)

# Fetch and print a recipe by name
print(my_book.get_recipe_by_name("tarte aux olives"))
print(my_book.get_recipe_by_name("Cake"))
print(my_book.get_recipe_by_name("tarte au jambon"))

# Print all dessert recipes
print(my_book.get_recipes_by_types("lunch"))
