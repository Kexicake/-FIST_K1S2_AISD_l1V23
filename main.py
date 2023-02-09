lit = ['ноль', 'один', 'два', 'три', 'четыре', 'пять', 'шесть', 'семь', 'восемь', 'девять']
w = open('output.txt', 'w')

with open('input.txt', 'r') as f:
    numbers = f.read()

numbers = numbers.split()
k = int(numbers[0])
numbers.pop(0)
useNum = ''
for i in numbers:
    if int(i, 8) % 2 == 1 and len(i) % 2 == 0 and len(i) > k:
        w.write(i + '  ')
        useNum += i 

w.write('\n')
for i in '0123456789':
    if useNum.find(i) != -1:
        w.write(lit['0123456789'.find(i)] + ' ')

w.close()