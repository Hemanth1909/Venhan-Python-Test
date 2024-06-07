def is_prime(number):
    if(number == 1):
        return (f"{number} is not a prime")
    elif(number > 1):

        for i in range(2, number):
            if(number % i == 0):
                return (f"{number} is not a prime")
            
        else:
            return(f"{number} is a prime")
    else:
        return(f"{number} is not a prime")
    
print(is_prime(3))