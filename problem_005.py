# 1부터 10까지의 모든 수로 나누어 떨어지는 가장 작은 수는 2520입니다.

# 1부터 20까지의 모든 수로 나누어 떨어지는 가장 작은 양의 정수는 얼마입니까?

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


def lcm(a, b):
    return a * b // gcd(a, b)


def lcm_up_to(n):
    answer = 1
    for i in range(2, n + 1):
        answer = lcm(answer, i)
    return answer


if __name__ == "__main__":
    print(lcm_up_to(20))
