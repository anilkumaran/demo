
def get_digit_sum(num):
    sum = 0
    if len(str(num)) == 1:
        return num
    else:
        for char in str(num):
            sum += int(char)
        return sum

def is_multiple_of_3(num):
    return get_digit_sum(num) in (3, 6, 9)
    
def is_multiple_of_5(num):
    return str(num)[-1] in ('0', '5')

def fizzBuzz(n):
    i = n
    # Write your code here
    # for i in range(1, n+1):
    if is_multiple_of_3(i) and is_multiple_of_5(i):
        # print(f'I i: {i}')
        print('FizzBuzz')
    elif is_multiple_of_3(i) and not is_multiple_of_5(i):
        # print(f'II i: {i}')
        print('Fizz')
    elif is_multiple_of_5(i) and not is_multiple_of_3(i):
        # print(f'III i: {i}')
        print('Buzz')
    else:
        # print(f'IV i: {i}')
        print(i)

a=1
b=2
c=a+b
fizzBuzz(57)

print('i')