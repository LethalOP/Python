n=int(input())
num_list = list(int(num) for num in input().strip().split())
num_list.sort()
a=num_list[-1]
b=n-1
for i in range(1,b):
    if(num_list[-1]==a):
      del num_list[-1]
print(num_list[-1])