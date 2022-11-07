#https://www.hackerrank.com/challenges/divisible-sum-pairs/problem?isFullScreen=true
"""
Trebuie ca suma a 2 cifre din aceasta lista sa fie divizibila cu valoarea lui k.
"""
ar = [1, 2, 3, 4, 5, 6]
k = 5
n = 6
count = 0 # tinem cont de cate ori suma este divizibila
for i in range(len(ar)): # iteram normal prin lista
	print(f'valaorea lui i este: {i}')
	for j in range(i+1, len(ar)):
		print(f'valaorea lui j este: {j}')
		#iteram valoarea lui i + 1 adica in momentul in care ar[i] este la valoarea ar[0] ar[j] va fi la valoarea ar[1]
		#Astfel niciodata nu se repeta valorile din spate si nu calculam de multe ori aceleasi rezultate
		s = ar[i] + ar[j]
		if s % k == 0:
			count += 1
print(count)