N=int(input("take input(>=2):"))
def primes(N):
	primes_list=[2]
	for i in range(2,N):
		for j in range(2,i):
			if i%j==0:
				break
			else:
				primes_list.append(i)
				break
	print(primes_list)
if __name__ == '__main__':
	primes(N)
