n = 1
r = 101
Fizz = 5
Buzz = 7

while n < r:
    if n % Fizz == 0 and n % Buzz == 0:
        print("FizzBuzz")
        n += 1
    elif n % Fizz == 0:
        print("Fizz")
        n += 1
    elif n % Buzz == 0:
        print("Buzz")
        n += 1
    else:
        print(n)
        n +=1