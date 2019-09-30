mylist = [1,2,3,4,5,6,7,8,9,10]
for num in mylist:
    print("hello")
for num in mylist:
    if num % 2 == 0:
        print(num)
    else:
        print(f'oddnum {num}')

list_sum = 0
for num in mylist:
    list_sum = list_sum + num
    print(f'sum of {num}={list_sum}')

print(f'total sum = {list_sum}')


name = "srini"
for letter in name:
    if letter == 'i':
        continue
    print(letter)


for letter in name:
    if letter == 'i':
        break
    print(letter)

