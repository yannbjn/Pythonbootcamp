# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    book.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: yabejani <yabejani@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/06/11 10:43:19 by yabejani          #+#    #+#              #
#    Updated: 2024/06/11 14:53:42 by yabejani         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys
from datetime import datetime
from recipe import Recipe

class Book:
    
    def __init__(self, name):
        self.name = name
        self.last_update = datetime.now()
        self.creation_date = datetime.now()
        self.recipes_list = {"starter": [], "lunch": [], "dessert": []}

    def get_recipe_by_name(self, name):
        for recipe_type in self.recipes_list.values():
            for recipe in recipe_type:
                if recipe.name == name:
                    # print(recipe)
                    return recipe
        print(f"Recipe with the name '{name}' not found.")
        return None

    def get_recipes_by_types(self, recipe_type):
        if recipe_type in self.recipes_list:
            return [recipe.name for recipe in self.recipes_list[recipe_type]]
        print(f"Recipe type '{recipe_type}' not found.")
        return []

    def add_recipe(self, recipe):
        if not isinstance(recipe, Recipe):
            raise ValueError("Argument must be an instance of Recipe class.")
        
        if recipe.recipe_type in self.recipes_list:
            self.recipes_list[recipe.recipe_type].append(recipe)
            self.last_update = datetime.now()
        else:
            raise ValueError("Recipe type must be 'starter', 'lunch', or 'dessert'.")


# class Book:
#     def __init__(self, name):
#         if not isinstance(name, str):
#             raise ValueError("Book name must be a string")
#         self.name = name
#         self.last_update = datetime.now()
#         self.creation_date = datetime.now()
#         self.recipes_list = {'starter': [], 'lunch': [], 'dessert': []}
        
#     def get_recipe_by_name(self, name):
#         for recipe_type in self.recipes_list.values():
#             for recipe in recipe_type:
#                 if recipe.name == name:
#                     print(recipe)
#                     return recipe
#         print("Recipe not found.")
#         sys.exit(1)
    
#     def get_recipes_by_types(self, recipe_type):
#         if recipe_type not in self.recipes_list:
#             print("Error: Not a valid Recipe.")
#             return []
#         return [recipe.name for recipe in self.recipes_list[recipe_type]]
    
#     def add_recipe(self, recipe):
#         if not isinstance(recipe, Recipe):
#             raise ValueError("Invalid recipe. Please pass a Recipe object.")
#         self.recipes_list[recipe.recipe_type].append(recipe)
#         self.last_update = datetime.now()