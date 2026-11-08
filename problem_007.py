# 소수를 크기 순으로 나열하면 2, 3, 5, 7, 11, 13, ... 과 같이 됩니다.
# 여기서 6번째 소수는 13입니다.

# 10001번째 소수를 구하세요.

def get_nth_prime(n):

    import math

    is_prime = [True] * 1_000_000
    is_prime[0] = is_prime[1] = False

    for i in range(2, math.isqrt(1_000_000)+1):
        if is_prime[i]:
            is_prime[i*i::i] = [False] * len(is_prime[i*i::i])

    count = 0
    for number, prime in enumerate(is_prime):
        if prime:
            count += 1
            if count == n:
                return number


if __name__ == "__main__":
    print(get_nth_prime(10001))