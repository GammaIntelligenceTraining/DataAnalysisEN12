# 4. Try except

try:
    print(10 / 0)
except ZeroDivisionError:
    print('Error: Cannot divide by zero!')

string_nums = ['15', '42', 'apples', '8', 'bananas', '-3']
valid_nums = []

for item in string_nums:
    try:
        num = int(item)
        valid_nums.append(num)
    except ValueError:
        print(f'Skipped: "{item}" is not a number')

print('Valid numbers are:', valid_nums)

my_dict = {'name': 'Alice', 'age': 25}

try:
    print(my_dict['city'])
except KeyError as e:
    print(f'Missing key: {e}')
else:
    print('Successfully accessed the key!')
finally:
    print('Dictionary lookup attempt finished.')

lst = ['A', 'B', 'C']

for i in range(5):
    try:
        print(f'Index {i} holds: {lst[i]}')
    except IndexError:
        print(f'Index {i} is out of range for this list.')