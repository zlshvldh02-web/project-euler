# 어떤 수를 소수의 곱으로만 나타내는 것을 소인수분해라 하고,
# 이 소수들을 그 수의 소인수라고 합니다.
# 예를 들면 13195의 소인수는 5, 7, 13, 29 입니다.

# 600851475143의 소인수 중에서 가장 큰 수를 구하세요.

def find_prime_factor(n):
    answer = set()
    for i in range(2, n+1):
        while n % i == 0:
            n //= i
            answer.add(i)
        if i * i > n:
            if n > 1 : answer.add(n)
            break
    return [sorted(answer), max(answer)]

print(find_prime_factor(600851475143))

