# 백준 - 5와 6의 차이 -> 프로그래머스 로또 문제랑 비슷한듯 이거 풀고 로또 풀어보자
# 2863 의 6을 5랑 헷갈림

a,b = input().split()

# 5를 6으로 볼수도 있지만, 6을 5로 볼수도 있다.
# 최소값을 구하려면 모든 6이 5로 낮아져야하고
ans1 = int(a.replace('6','5')) + int(b.replace('6','5'))
# 최대값을 구하려면 모든 5가 6으로 커져야한다.
ans2 = int(a.replace('5','6')) + int(b.replace('5','6'))

print(ans1, ans2)