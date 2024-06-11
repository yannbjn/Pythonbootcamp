# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    recipe.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: yabejani <yabejani@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/06/11 10:50:29 by yabejani          #+#    #+#              #
#    Updated: 2024/06/11 13:37:52 by yabejani         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import string
import sys

class Recipe:
    def __init__(self, name, cooking_lvl, cooking_time, ingredients, recipe_type, description=""):
        
        
        if not isinstance(name, str) or not name:
            raise ValueError("Name must be a non-empty string.")
        self.name = name
        
        if not isinstance(cooking_lvl, int) or not (1 <= cooking_lvl <= 5):
            raise ValueError("Cooking level must be an integer between 1 and 5.")
        self.cooking_lvl = cooking_lvl
        
        if not isinstance(cooking_time, int) or cooking_time < 0:
            raise ValueError("Cooking time must be a non-negative integer.")
        self.cooking_time = cooking_time
        
        if not isinstance(ingredients, list) or not all(isinstance(ingredient, str) for ingredient in ingredients):
            raise ValueError("Ingredients must be a list of strings.")
        self.ingredients = ingredients
        
        if recipe_type not in ["starter", "lunch", "dessert"]:
            raise ValueError("Recipe type must be 'starter', 'lunch', or 'dessert'.")
        self.recipe_type = recipe_type
        
        if not isinstance(description, str):
            raise ValueError("Description must be a string.")
        self.description = description

    def __str__(self):
        txt = (f"Recipe for {self.name}:\n"
            f"Cooking level: {self.cooking_lvl}\n"
            f"Cooking time: {self.cooking_time} minutes\n"
            f"Ingredients: {', '.join(self.ingredients)}\n"
            f"Description: {self.description}\n"
            f"Type: {self.recipe_type}")
        return txt

def main():
    try:
        cake = Recipe(
            name="Cake",
            cooking_lvl=5,
            cooking_time=60,
            ingredients=["flour", "sugar", "eggs"],
            recipe_type="dessert",
            description="A delicious cake."
		)
        toprint = str(cake)
        print(toprint)
    except ValueError as e:
        print(f"ERROR: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()