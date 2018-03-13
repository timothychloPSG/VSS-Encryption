"""/*******************************************
 *
 * K out of K Scheme. ( For now. )
 * 
 *
 *  Made by Swagbrina, Superbrina, Romeo.
 *  Supervised by Matthew Rhea.
 *  
 *  Part of the CS Makerspace VSS Project.
 *
 *******************************************/"""

import itertools
# K out of K scheme
# constructs K shares from a black and white image

#returns a list of k elements

"""/**
 * MakeW function.
 * 
 * generates the groundset W.
 *
 * @param k the number of elements in the groundset
 * 
 * @return W the groundset
 */"""
def makeW (k):
   W = []
   i = 1;
   while (i <= k):
      W.append(i)
      i += 1
   return W 

# returns a tuple of pi,sigma as a list based on k
# credit to: http://pythonfiddle.com/a-list-of-subsets-of-a-list/ 
"""/**
 * MakePiSigma function.
 * 
 * generates the pi set (the even cardinality set)
 * and the sigma set (the odd cardinality set) from
 * the ground set.
 *
 * @param W the groundset
 * @return the fullset the set with pi and sigma
 *
 */"""
def makePiSigma (W):
   pi = []
   sigma = []
   for i in xrange(0, len(W)+1):
      listing = [list(subset) for subset in itertools.combinations(W, i)]
      if (len(subset)%2 == 0):
         pi.extend(listing)
      else:
         sigma.extend(listing)

   pi[0] =[0]
   sigma[0]=[0]
   return([pi, sigma])

"""/**
    * Search function.
    *
    * search through the given
    * set for the search target.
    *
    * @param search_space 
    * @retun bool value according to the 
    *
    */"""
def search (target, search_space):
   if target in search_space:
      return True
   else:
      return False

# creates an S0 matrix such that S0 = S0[i,j] = 1 iff ei in pij
"""/**
    * MakeS0 function.
    *
    * generates a S0 set.
    *
    * @param W the groundset
    * @param pi the pi set
    * @return nothing yet
    *
    */"""
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
   print("s0 is: " + str(s0))

# creates an S1 matrix such that S1 = S1[i,j] = 1 iff ei in sigmaj
"""/**
    * MakeS1 function.
    *
    * make S1 set
    *
    * @param sigma the sigma set
    * @return nothing yet!!
    *
    */"""
def makeS1 (sigma): 
   return 0
#given either S0 or S1, randomly permute the matrix 

"""/**
    * PermuteMatrix function.
    *
    * permuting the matrix.
    *
    * @param matrix what is the fucking matrix?????
    * @return nothing yet!!!
    *
    */"""
def permuteMatrix (matrix):
  return 0

# "main" for k out of k

"""/**
    * koutofk function.
    *
    * the main function for carrying out k out of k
    * image secret splitting.
    *
    * @return nothing yet???
    *
    */"""
def koutofk ():
   W = makeW(4)
   fullset = makePiSigma(W)
   pi = fullset[0]
   sigma = fullset[1]
   print("pi is: " + str(pi))
   print("sigma is: " + str(sigma))
   makeS0(W, pi)
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
#W = makeW(4)
#pi = makepi(W)
#makesigma(W)
#makeS0(W,pi)
koutofk()
