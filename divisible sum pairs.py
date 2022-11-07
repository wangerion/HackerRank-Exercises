#https://www.hackerrank.com/challenges/divisible-sum-pairs/problem?isFullScreen=true
ar = [1, 2, 3, 4, 5, 6]
k = 5
n = 6
count = 0 #We keep track of the divisible sum
for i in range(len(ar)):
	for j in range(i+1, len(ar)):
		#Iterating over the value of i + 1, meaning that as an example when ar[i] is at ar[0], ar[j] will be at ar[1]
		s = ar[i] + ar[j]
		if s % k == 0:
			count += 1
print(count)