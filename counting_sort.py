def counting_sort(numbers):
    """Sort given numbers (integers) by counting occurrences of each number,
    then looping over counts and copying that many numbers into output list.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Find range of given numbers (minimum and maximum integer values)
    # TODO: Create list of counts with a slot for each number in input range
    # TODO: Loop over given numbers and increment each number's count
    # TODO: Loop over counts and append that many numbers into output list
    # Stretch: Improve this to mutate input instead of creating new output list
numbers = [3,2,5,3]

new_array = [0] * (max(numbers) + 1)
print(new_array)

for num in numbers:
    if new_array[num] == 0:
        new_array[num] = 1
    else:
        new_array[num] += 1
print(new_array)

final = []
for num in range(len(new_array)):
    if new_array[num] != 0:
        for x in range(new_array[num]):
            final.append(num)

print(final)
    #TODO: Write some test cases