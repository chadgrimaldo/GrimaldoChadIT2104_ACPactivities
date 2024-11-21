def perfect_number(n):
   
    if n <= 0:
        return False 

    divisors = [i for i in range(1, n) if n % i == 0]
    
    return sum(divisors) == n

while True:
    try:
        number = int(input("Enter a number: "))
        
        if perfect_number(number):
            print(f"{number} is a perfect number.")
        else:
            print(f"{number} is not a perfect number.")
        break
    except ValueError:
        print("Please enter a valid integer.")
