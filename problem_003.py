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

if __name__ == "__main__":
    print(find_prime_factor(600851475143))


# 참고: 숫자가 아주 클 때(예: 30자리 이상)는 하나씩 나눠 보는 방법이 너무 느리다.
# - 폴라드 로(Pollard's rho) 알고리즘: 수열을 돌리다가 소인수가 걸려 나오게 해서 빠르게 찾는다.
# - 밀러-라빈(Miller-Rabin) 소수 판정: 남은 수가 소수인지 빠르게 검사한다.
# - 실제로는 이 알고리즘들이 들어 있는 sympy.factorint()를 쓴다.
