# 1부터 10까지 자연수를 각각 제곱해 더하면 다음과 같습니다(제곱의 합).
# 1^2 + 2^2 + ... + 10^2 = 385

# 1부터 10을 먼저 더한 다음에 그 결과를 제곱하면 다음과 같습니다(합의 제곱).
# (1 + 2 + ... + 10)^2 = 55^2 = 3025

# 따라서 1부터 10까지 자연수에 대해 합의 제곱과 제곱의 합의 차이는 3025 - 385 = 2640이 됩니다.

# 그러면 1부터 100까지 자연수에 대해 합의 제곱과 제곱의 합의 차이는 얼마입니까?

def sum_of_squares(n):
    return n * (n + 1) * (2 * n + 1) // 6


def square_of_sum(n):
    return (n * (n+1) // 2) ** 2


def square_sum_gap(n):
    return abs(sum_of_squares(n) - square_of_sum(n))


if __name__ == "__main__":
    print(square_sum_gap(100))