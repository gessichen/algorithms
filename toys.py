# Enter your code here. Read input from STDIN. Print output to STDOUT
def max_toys(prices, rupees):
  #Compute and return final answer over here

  prices.sort()
#  print str(prices) 
  psum = 0 
  for answer in xrange (0, len(prices)):
  	psum += prices[answer]
  	if psum > rupees:
  		return answer
  return answer

if __name__ == '__main__':
  n, k = map(int, raw_input().split())
  prices = map(int, raw_input().split())
  print max_toys(prices, k)
