def return_intersection_of_sets_from_file(filename):
  # Read the sets from the file
  with open(filename) as f:
    lines = f.readlines()

  count_of_sets_containing_eachother = 0
  # Create a list of sets
  for line in lines:
    sets = []
    # Split the line into the bounds of the sets
    bounds = line.split(',')
    # Create a set for each bound
    for bound in bounds:
      # Split the bound into the lower and upper bounds
      lower, upper = bound.split('-')
      # Create set in increasing value order and add it to the list of sets
      sets.append(set(range(int(lower), int(upper)+1)))
      
    try:
      if sets[0].issubset(sets[1]) or sets[1].issubset(sets[0]):
        count_of_sets_containing_eachother += 1
    except:
      pass
  


  

  return count_of_sets_containing_eachother

# Test the function with the example data
print(return_intersection_of_sets_from_file('input.txt')) # should print 2