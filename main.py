def heavy_calculation():
    # Simulate heavy CPU work by calculating prime numbers
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    # Find prime numbers up to 100000
    primes = [num for num in range(2, 500) if is_prime(num)]
    return len(primes)

if __name__ == "__main__":
    import time

    start_time = time.time()
    result = heavy_calculation()
    end_time = time.time()

    print(f"Calculated {result} prime numbers in {end_time - start_time:.2f} seconds.")