# Range: создание списка [18, 14, 10, 6, 2]

# range(start, stop, step)
# stop не включается, поэтому берём 0 (не дойдём до него)
numbers = list(range(18, 0, -4))

print(numbers)   # [18, 14, 10, 6, 2]