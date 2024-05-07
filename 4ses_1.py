# 1. FizzBuzz

# Izdrukāt virknīti 1,2,3,4,Fizz,6,Buzz,8,.....34,FizzBuzz,36,....līdz  97,Buzz, 99,Fizz 

# Tātad ja skaitlis dalās ar 5 tad Fizz

# Ja dalās ar 7 tad Buzz,

# Ja dalās ar 5 UN 7 tad Fizzbuzz

# savādāk pats skaitlis

# Piezīme: šads uzdevums kļuva populārs kā pirmais uzdevums, ko uzdot, lai noteiktu vai cilvēks vispār zina par programmēšanu :)

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