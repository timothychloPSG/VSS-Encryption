# K out of K scheme
# constructs K shares from a black and white image


# returns a tuple of pi,sigma as a list based on k 
def makepisigma k:

# creates an S0 matrix such that S0 = S0[i,j] = 1 iff ei in pij
def makeS0 pi:

# creates an S1 matrix such that S1 = S1[i,j] = 1 iff ei in sigmaj
def makeS1 sigma: 

#given either S0 or S1, randomly permute the matrix 
def permuteMatrix matrix:
  

# "main" for k out of k
def koutofk:

   sigma,pi = makepisigma k
   S0 = makeS0 pi
   S1 = makeS1 sigma
   #initialize k shares
   
   #accept commandline input: kofk.py k k image

   for prow in range(image):
      for pcol in range(pixelrow):
         if  image[prow,pcol]== 0:
            C0share = permuteMatrix S0
            #distribute across k shares
         else:
            C1share = permuteMatrix S1

