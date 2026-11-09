# 10보다 작은 소수를 모두 더하면 2 + 3 + 5 + 7 = 17입니다.

# 200만(2,000,000)보다 작은 소수를 모두 더하면 얼마입니까?

import math

limit = 2_000_000

is_prime = [True] * limit
is_prime[0] = is_prime[1] = False

for i in range(2, math.isqrt(limit)+1):
    if is_prime[i]:
        is_prime[i*i::i] = [False] * len(is_prime[i*i::i])

print(sum(number for number, prime in enumerate(is_prime) if prime))