change_amount=float(input("change amount?"))
bill_mount={'twenties':0,'tens':0,'fives':0,'ones':0,'quarters':0,'dimes':0,'nickles':0,'pannies':0}
def change(n):
	if n>=20:
		n-=20
		bill_mount['twenties']+=1
		change(n)
	elif n>=10 and n<20:
		n-=10
		bill_mount['tens']+=1
		change(n)
	elif n>=5 and n<10:
		n-=5
		bill_mount['fives']+=1
		change(n)
	elif n>=1 and n<5:
		n-=1
		bill_mount['ones']+=1
		change(n)
	elif n>=0.25 and n<1:
		n-=0.25
		bill_mount['quarters']+=1
		change(n)
	elif n>=0.1 and n<0.25:
		n-=0.1
		bill_mount['dimes']+=1
		change(n)
	elif n>=0.05 and n<0.1:
		n-=0.05
		bill_mount['nickles']+=1
		change(n)
	elif n>=0.01 and n<0.05:
		n-=0.01
		bill_mount['pannies']+=1
		change(n)


if __name__ == '__main__':
	change(change_amount) 
	print("The bills or the change should be:")
	print(bill_mount)