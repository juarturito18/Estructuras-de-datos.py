numbers = [1,2,3,4,5,6,7,8,9,10]
pairs = []

for num in numbers:
    if num % 2 == 0:
        pairs.append(num)

def is_pair(num:int) -> bool:
    if num % 2 == 0:
        return True
    return False

pair_filter = list(filter(is_pair,numbers))

print(pair_filter)