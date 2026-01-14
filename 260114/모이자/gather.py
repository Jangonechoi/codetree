N = int(input())
people_at_home = list(map(int, input().split()))

# 1. 전체 인원수 계산
total_people = sum(people_at_home)
median_index = (total_people - 1) // 2 # 중앙값에 해당하는 인덱스 (0부터 시작)

# 2. 중앙값 위치 찾기
count = 0
for i in range(N):
    count += people_at_home[i]
    if count > median_index:
        # 현재 집 i의 위치가 중앙값 위치임
        optimal_home_location = i + 1 # 문제에서 x=1부터 시작하므로 +1
        break

# 3. 최소 이동 거리의 합 계산
min_distance_sum = 0
for i in range(N):
    distance = abs((i + 1) - optimal_home_location) # 각 집 위치와 최적 위치 간의 거리
    min_distance_sum += distance * people_at_home[i] # 거리에 인원수 곱하여 합산

print(min_distance_sum)
