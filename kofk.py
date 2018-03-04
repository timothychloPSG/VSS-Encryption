import itertools
# K out of K scheme
# constructs K shares from a black and white image

#returns a list of k elements
def makeW (k):
   return [1,2,3,4]

# returns a tuple of pi,sigma as a list based on k
# credit to: http://pythonfiddle.com/a-list-of-subsets-of-a-list/ 
def makepi (W):
   pi = []
   for i in xrange(0, len(W)+1):
      listing = [list(subset) for subset in itertools.combinations(W, i)]
      if (len(subset)%2 == 0):
         pi.extend(listing)

   print(pi)

def makesigma (W):
   sigma = []
   for i in xrange(0, len(W)+1):
      listing = [list(subset) for subset in itertools.combinations(W, i)]
      if (len(subset)%2 != 0):
         sigma.extend(listing)

   print(sigma)

# creates an S0 matrix such that S0 = S0[i,j] = 1 iff ei in pij
def makeS0 (pi):
   return 0
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
#print (makepi(4))
W = makeW(4)
makepi(W)
makesigma(W)
