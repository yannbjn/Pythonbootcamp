# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    recipe.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: yabejani <yabejani@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/06/10 14:27:29 by yabejani          #+#    #+#              #
#    Updated: 2024/06/10 16:13:43 by yabejani         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

cookbook = {
    'Sandwich': {
        'ingredients': ['ham', 'bread', 'cheese', 'tomatoes'],
        'meal': 'lunch',
        'prep_time': 10
    },
    'Cake': {
        'ingredients': ['flour', 'sugar', 'eggs'],
        'meal': 'dessert',
        'prep_time': 60
    },
    'Salad': {
        'ingredients': ['avocado', 'arugula', 'tomatoes', 'spinach'],
        'meal': 'lunch',
        'prep_time': 15
    }
}

def	delete_recipe(recipe_name):
    if recipe_name in cookbook:
        del cookbook[recipe_name]
        print(f"{recipe_name} has been deleted")
    else:
        print(f"Recipe {recipe_name} does not exist")

def print_all_recipes():
    for	recipe in cookbook:
        #print(f"Recipe name: {recipe}")
        print_recipe(recipe)

def	print_recipe(recipe_name):
    if recipe_name in cookbook:
        recipe = cookbook[recipe_name]
        print(f"Recipe for {recipe_name}:")
        print(f"   Ingredients list: {', '.join(recipe['ingredients'])}")
        print(f"   To be eaten for {recipe['meal']}.")
        print(f"   Takes {recipe['prep_time']} minutes of cooking.")
    else:
        print(f"Recipe {recipe} does not exist")

def	add_recipe():
    name = input("Enter a name")
    ingredient = []
    print("Enter ingredients (press enter on empty line to stop)")
    while True:
        ingredient = input()
        if not ingredient:
            break
        ingredient.append(ingredient)
    meal_type = input("Input a meal type:")
    prep_time = input("Enter a preparation time:")
    cookbook[name] = {
        'ingredients': ingredient,
        'meal': meal_type,
        'prep_time': prep_time
    }
    print(f"{name} has been added to the cookbook.")

def main():
    print("Welcome to the Python Cookbook!")
    options = {
        '1' : add_recipe,
        '2'	: delete_recipe,
		'3' : print_recipe,
	    '4' : print_all_recipes,
		'5' : exit
	}
    while True:
        print("List of available option:")
        print("   1: Add a recipe")
        print("   2: Delete a recipe")
        print("   3: Print a recipe")
        print("   4: Print the cookbook")
        print("   5: Quit")
        print("Please select an option between 1 and 5:")
        choice = input(">> ")
        if choice in options:
            if choice == '5':
                print("Cookbook closed. Goodbye !")
                break
            if choice == '3':
                recipe_name = input("Please enter a recipe name to get its details :")
                options[choice](recipe_name)
            elif choice in ['1', '2', '4']:
                if choice == '2' or choice == '3':
                    recipe_name = input("PLease enter a recipe name: ")
                    options[choice](recipe_name)
                else:
                    options[choice]()
            else:
                print("Sorry, this option does not exist.")
                continue  

if __name__ == "__main__":
    main()