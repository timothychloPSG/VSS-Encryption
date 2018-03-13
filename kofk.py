import itertools
# K out of K scheme
# constructs K shares from a black and white image

#returns a list of k elements
def makeW (k):
   W = []
   i = 1;
   while (i <= k):
      W.append(i)
      i += 1
   return W 

# returns a tuple of pi,sigma as a list based on k
# credit to: http://pythonfiddle.com/a-list-of-subsets-of-a-list/ 
def makepi (W):
   pi = []
   for i in xrange(0, len(W)+1):
      listing = [list(subset) for subset in itertools.combinations(W, i)]
      if (len(subset)%2 == 0):
         pi.extend(listing)
   return(pi)

def makesigma (W):
   sigma = []
   for i in xrange(0, len(W)+1):
      listing = [list(subset) for subset in itertools.combinations(W, i)]
      if (len(subset)%2 != 0):
         sigma.extend(listing)
   return(sigma)

def search (target, search_space):
   for x in search_space:
      if x == target:
         return True
      else:
         return False

# creates an S0 matrix such that S0 = S0[i,j] = 1 iff ei in pij
def makeS0 (W, pi):
   #set size of s0 to be list of lists with sizes k and 2^(k-1)
   k = len(W)
   col = pow(2,(k-1))
   s0 = [[2 for x in range(col)] for y in range(k)]
   for i in range(len(s0)):
      for j in range(len(s0[i])):
         if ( search(W[i],pi[j]) ):
            s0[i][j] = 1
         else:
            s0[i][j] = 0
   #print("s0 is: " + str(s0))

# creates an S1 matrix such that S1 = S1[i,j] = 1 iff ei in sigmaj
def makeS1 (sigma): 
   return 0
#given either S0 or S1, randomly permute the matrix 
def permuteMatrix (matrix):
  return 0

# "main" for k out of k
def koutofk ():
   return 0
   #sigma,pi = makepisigma k
   #S0 = makeS0 pi
   #S1 = makeS1 sigma
   #initialize k shares
   
   #accept commandline input: kofk.py k k image

   #for prow in range(image):
   #   for pcol in range(pixelrow):
   #      if  image[prow,pcol]== 0:
   #         C0share = permuteMatrix S0
            #distribute across k shares
   #      else:
   #         C1share = permuteMatrix S1


###MAIN###
W = makeW(4)
pi = makepi(W)
makesigma(W)
makeS0(W,pi)
