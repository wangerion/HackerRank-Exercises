arr = [1, 4, 4, 4, 5, 3]
x = arr.count(arr[0])
r = []
for i in arr:
	if arr.count(i) >= x: #We count each value of i and if it's greather than the last value of x we assign it to x.
		x = arr.count(i)
		r.append(i)
print(min(r))
