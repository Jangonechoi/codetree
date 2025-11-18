import sys

N = int(sys.stdin.read())
# # print(N)
# for i in range(1,N+1):
#     if i % 2 == 0:
#         print('* '* i)
#     else:
#         print('*')

#i가 짝수인 경우 별을 1개, 홀수인 경우 i+1개를 출력합니다
for i in range(N):
	if i % 2 == 0:
		print("*", end="")
	else:
		for _ in range(i + 1):
			print("*", end=" ")
	print()


