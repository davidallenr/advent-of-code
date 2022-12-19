# open the file in the folder day1
# with relative path
with open('example.txt', 'r') as f:
    # read the file
    lines = f.readlines()
    
# initialize the total and the list of highest totals
total = 0
highest_totals = []

# loop through the lines
for line in lines:
    # if the line is blank
    if line == '\r' or line == '\n':
        # add the current total to the list of highest totals
        highest_totals.append(total)
        # sort the list in descending order
        highest_totals.sort(reverse=True)
        # keep only the top three highest totals
        highest_totals = highest_totals[:3]
        # reset the total
        total = 0
    # if the line is not blank
    else:
        # add the number to the total
        total += int(line)

# add the last total to the list of highest totals
highest_totals.append(total)
# sort the list in descending order
highest_totals.sort(reverse=True)
# keep only the top three highest totals
highest_totals = highest_totals[:3]

# add the top three highest totals and print the result
result = sum(highest_totals)
print(result)