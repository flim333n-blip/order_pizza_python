#pizza parameters

# size
def size():
    while True:
        print('select size:')
        print('1. 20 cm +$8')
        print('2. 30 cm +$11')
        print('3. 40 cm +$14')
        size_choice = int(input("choose pizza size (1-3): "))
        if size_choice in [1, 2, 3]:
            return size_choice
        else:
            print('invalid option!')
            exit()
result_size = size()
time_choice = 0
if result_size == 1:
    time_choice = time_choice + 3
elif result_size == 2:
    time_choice = time_choice + 4
elif result_size == 3:
    time_choice = time_choice + 5
# dough
def dough():
    while True:
        print('choose dough:')
        print('1. regular +$0')
        print('2. thick +$2')
        dough_choice = int(input('choose dough (1-2): '))
        if dough_choice in [1, 2]:
            return dough_choice
        else:
            print('invalid option!')
            exit()
result_dough = dough()
time_dough = 0
if result_dough == 1:
    time_dough = time_dough
elif result_dough == 2:
    time_dough = time_dough + 3

# filling (toppings)
def filling():
    toppings_list = []
    while True:
        print('choose toppings:')
        print('1. pepperoni +$2.5')
        print('2. mushrooms +$2')
        print('3. olives +$1.5')
        print('4. bacon +$3')
        print('5. finish choice')
        topping_choice = int(input('choose topping (1-4) or 5 to finish: '))
        if topping_choice in [1, 2, 3, 4]:
            toppings_list.append(topping_choice)
            print('added!')
        elif topping_choice == 5:
            return toppings_list
        else:
            print('invalid option!')
            exit()
result_toppings = filling()
topping_time = 0
for topping in result_toppings:
    if topping in [1,2,3,4]:
        topping_time = topping_time + 1
# sauce
def sauce():
    while True:
        print('choose sauce:')
        print('1. tomato +$0')
        print('2. creamy +$1')
        print('3. spicy +$1.5')
        sauce_choice = int(input('choose sauce (1-3): '))
        if sauce_choice in [1, 2, 3]:
            return sauce_choice
        else:
            print('invalid option!')
            exit()
result_sauce = sauce()
time_sauce = 1

# cheese
def cheese():
    while True:
        print('choose cheese:')
        print('1. regular +$0')
        print('2. double +$2.5')
        cheese_choice = int(input('choose cheese (1-2): '))
        if cheese_choice in [1, 2]:
            return cheese_choice
        else:
            print('invalid option!')
            exit()
result_cheese = cheese()
time_cheese = 0
if result_cheese == 2:
    time_cheese = time_cheese + 1

# prices

# size price
price_per_size = 0
if result_size == 1:
    price_per_size = price_per_size + 8
    final_size = '20 cm'
elif result_size == 2:
    price_per_size = price_per_size + 11
    final_size = '30 cm'
elif result_size == 3:
    price_per_size = price_per_size + 14
    final_size = '40 cm'

# dough price
price_per_dough = 0
if result_dough == 1:
    price_per_dough = price_per_dough + 0
    final_dough = 'regular dough'
elif result_dough == 2:
    price_per_dough = price_per_dough + 2
    final_dough = 'thick dough'

# toppings price
price_per_filling = 0
for topping in result_toppings:          # loop through each chosen topping
    if topping == 1:
        price_per_filling += 2.5
    elif topping == 2:
        price_per_filling += 2
    elif topping == 3:
        price_per_filling += 1.5
    elif topping == 4:
        price_per_filling += 3
final_toppings_list = []
for toppung in result_toppings:
    if toppung == 1:
        final_toppings_list.append('pepperoni')
    elif toppung == 2:
        final_toppings_list.append('mushrooms')
    elif toppung == 3:
        final_toppings_list.append('olives')
    elif toppung == 4:
        final_toppings_list.append('bacon')


# sauce price
price_per_sauce = 0
if result_sauce == 1:
    price_per_sauce = price_per_sauce + 0
    final_sauce = 'tomato sauce'
elif result_sauce == 2:
    price_per_sauce = price_per_sauce + 1
    final_sauce = 'creamy sauce'
elif result_sauce == 3:
    price_per_sauce = price_per_sauce + 1.5
    final_sauce = 'spicy sauce'

# cheese price
price_per_cheese = 0
if result_cheese == 1:
    price_per_cheese = price_per_cheese + 0
    final_cheese = 'regular cheese'
elif result_cheese == 2:
    price_per_cheese = price_per_cheese + 2.5
    final_cheese = 'double cheese'


# time, final price and pizza order

pizza_time = time_choice + time_dough + topping_time + time_sauce + time_cheese

total_price = price_per_size + price_per_dough + price_per_filling +price_per_sauce + price_per_cheese
print('your final pizza:' 
      f'\nsize: {final_size}'
      f'\ndough: {final_dough}'
      f'\ntoppings: {final_toppings_list}'
      f'\nsauce: {final_sauce}'
      f'\ncheese: {final_cheese}')
print(f'total price: {total_price} $')
print(f'cooking time: {pizza_time} minutes')