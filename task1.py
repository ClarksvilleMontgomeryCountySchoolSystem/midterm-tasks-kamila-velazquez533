total_slices = party_pizza_mini + large + medium + people
print(f'Total number of slices: {total_slices}')

people += 1
share = total_slices // people
leftover = total_slices % people
print(f'Each person gets: {share}')
print(f'Leftover slices: {leftover}')

people += 2
share = total_slices // people
leftover = total_slices % people
print(f'Each person gets: {share}')
print(f'Leftover slices: {leftover}')

slices += party_pizza_mini
share = slices // people
leftover = slices % people
print(f'Each person gets: {share}')
print(f'Leftover slices: {leftover}')
print("...for Mr. Hollow Leg")
