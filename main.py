import time

def heavy_calculation():
    # Simulate heavy CPU work by calculating prime numbers
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    start_time = time.time()
    primes = [num for num in range(2, 5000000) if is_prime(num)]
    end_time = time.time()
    print(f"Calculated {len(primes)} prime numbers in {end_time - start_time:.2f} seconds.")
