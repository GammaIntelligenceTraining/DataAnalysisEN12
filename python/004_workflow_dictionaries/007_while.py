# 3. While loop

x = 0
while x < 5:
    x += 1
    print(x)

countdown = 5
lst = []

while countdown > 0:
    lst.append(countdown)
    countdown -= 1

print('Blastoff!', lst)

string = 'Python'
index = 0
while index < len(string):
    print(f'Letter {index + 1}: {string[index]}')
    index += 1

num_list = [1, 5, 8, 12, 15, 20]
even_nums = []

while num_list:
    current = num_list.pop(0)
    if current % 2 == 0:
        even_nums.append(current)

print(f'Even numbers extracted: {even_nums}')

x = 0
while True:
    x += 10
    if x == 30:
        continue
    if x > 50:
        break
    print(f'Current value: {x}')