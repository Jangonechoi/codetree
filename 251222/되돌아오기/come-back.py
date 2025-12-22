N = int(input())
moves = [input().split() for _ in range(N)]

# x, y 좌표 및 경과 시간(초) 초기화
x, y = 0, 0
elapsed_time = 0
ans = -1 # 돌아오지 못할 경우를 대비한 초기값

# 방향에 따른 dx, dy 설정 (x: 가로, y: 세로)
# 북(N), 남(S), 동(E), 서(W)에 따른 이동량
mapper = {
    'N': (0, 1),
    'S': (0, -1),
    'E': (1, 0),
    'W': (-1, 0)
}

# 이동 시작
for direction, dist in moves:
    dist = int(dist)
    dx, dy = mapper[direction]
    
    for _ in range(dist):
        # 1초에 한 칸씩 이동
        x, y = x + dx, y + dy
        elapsed_time += 1
        
        # 처음으로 원점(0, 0)에 돌아왔는지 확인
        if x == 0 and y == 0:
            ans = elapsed_time
            break # 내부 루프 탈출
            
    if ans != -1: # 원점을 찾았다면 외부 루프도 탈출
        break

# 결과 출력
print(ans)
