import argparse
import random

# Arg Parser
parser = argparse.ArgumentParser()
parser.add_argument('n', help='Number of items to select from a list')
parser.add_argument('-f', help='File with list of items')
args = parser.parse_args()

if args.f is None:
    item_file = 'items.txt'
else:
    item_file = args.f

number_of_items = args.n

# Declare Lists
random_number = []
item_list = []

# Open file and read into list
with open(item_file) as f:
    for line in f:
        item_list.append(line)
    item_list = [x.strip() for x in item_list]

# Variables
last_index = len(item_list) - 1


# Select 4 random values from item_array
def get_items(choices):
    numbers = []
    for x in range(choices):
        value = random.randint(0, last_index)
        numbers.append(value)
    return numbers


def print_selected_items(choices, selected_list):
    for x in range(len(choices)):
        selected = choices[x]
        print('{0}: {1}'.format(selected, selected_list[selected]))


random_number = get_items(int(number_of_items))
print_selected_items(random_number, item_list)
