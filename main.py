numbers = list(map(int, input().split()))
average = sum(numbers)/len(numbers)
dist = []

for i in range(len(numbers)):
    dist.append(average - numbers[i])

print (f'{dist:.2f}', end=' ')
# ******************************
# Make your Code
# ******************************


# Use this statement to print out the list element. # Replace the variable 'dist' with your variable
# print (f'{dist:.2f}', end=' ')
