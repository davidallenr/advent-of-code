def calculate_badge_priorities(filename):
  # Read the rucksack lists from the file
  with open(filename) as f:
    rucksack_lists = [line.strip() for line in f]

  # Initialize the sum of the badge priorities to 0
  badge_priorities_sum = 0

  # Iterate over the rucksack lists in groups of three
  for i in range(0, len(rucksack_lists), 3):
    group_rucksacks = rucksack_lists[i:i+3]
    # Find the item type that appears in all three rucksacks
    common_item_type = None
    for item_type in set(''.join(group_rucksacks)):
      if all(item_type in rucksack for rucksack in group_rucksacks):
        common_item_type = item_type
        break

    # Calculate the priority of the common item type
    if common_item_type.islower():
      priority = ord(common_item_type) - ord('a') + 1
    else:
      priority = ord(common_item_type) - ord('A') + 27

    # Add the priority to the sum of the badge priorities
    badge_priorities_sum += priority

  return badge_priorities_sum

# Test the function with the example data
print(calculate_badge_priorities('input.txt')) # should print 70