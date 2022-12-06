#We calculate the sum minus the item that Anna didn't eat and then we just split the bill to see how much Anna should really pay.
def bonAppetit(bill, k, b):
	b_act = int((sum(bill) - bill[k])/2)
	if b == b_act:
		print("Bon Appetit")
	else:
		print(b - b_act)

if __name__ == '__main__':

	bill = [3, 10, 2, 9]
	k = 1
	b = 12
	bonAppetit(bill, k, b)