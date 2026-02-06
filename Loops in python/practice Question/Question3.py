num = int(input("Enter any number: "))

if num < 2:
    print(f"{num} is not prime.")
else:
    is_prime = True

    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            is_prime = False
            break

    if is_prime:
        print(f"{num} is prime.")
    else:
        print(f"{num} is not prime.")
