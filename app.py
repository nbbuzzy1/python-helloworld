numbers = [5, 2, 1, 7, 4]
numbers2 = numbers.copy()
numbers.append(20)
print(numbers)

numbers.insert(0, 10)
print(numbers)

numbers.remove(5)
print(numbers)

numbers.pop()
print(numbers)

print(numbers.index(7))  # or use 7 in numbers

print(numbers.count(1))

numbers.sort()
numbers.reverse()
print(numbers)

numbers.clear()
print(numbers)
print(numbers2)






