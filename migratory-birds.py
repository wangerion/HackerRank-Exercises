arr = [1, 2, 3, 4, 5, 4, 3, 2, 1, 3, 4] #The answer needs to be 3
r = {}
a = []
for i in arr:
    #We check if i is in the dict, if it's not we add 1 if it is we start counting the occurences.
		if i not in r:
			r[i] = 1
		else:
			r[i] += 1
for i,j in r.items():
    # We select the keys that have the max value (were counted more)
    if max(r.values()) == j:
        a.append(i)
        
print(min(a))