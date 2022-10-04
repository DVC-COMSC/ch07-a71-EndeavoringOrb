numbers = list(map(int, input().split()))
average = sum(numbers)/len(numbers)
dist = []

for i in range(len(numbers)):
    dist.append(abs(average - numbers[i]))

#print(f'{dist:.2f}', end=' ')
#This does not work, cannot pass a list type to this

for i in range(len(dist)):
    print (f'{dist[i]:.2f}', end=' ')
# ******************************
# Make your Code
# ******************************


# Use this statement to print out the list element. # Replace the variable 'dist' with your variable
# print (f'{dist:.2f}', end=' ')
