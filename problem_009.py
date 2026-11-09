# 세 자연수 a, b, c가 피타고라스 정리 a² + b² = c²를 만족하면 피타고라스 수라고 부릅니다(여기서 a < b < c).
# 예를 들면 3² + 4² = 9 + 16 = 25 = 5²이므로 3, 4, 5는 피타고라스 수입니다.

# a + b + c = 1000인 피타고라스 수 a, b, c는 한 가지뿐입니다. 이때 a × b × c는 얼마입니까?

def find_triplet():
    for a in range(1, 334):
        for b in range(a+1,500):
            c = 1000 - a - b
            if a < b < c and a ** 2 + b ** 2 == c ** 2:
                return a * b * c

print(find_triplet())