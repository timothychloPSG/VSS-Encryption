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
    * @param ps pi or sigma
    * @return nothing yet
    *
    */"""
def makeS (W, ps):
   #set size of s0 to be list of lists with sizes k and 2^(k-1)
   k = len(W)
   col = pow(2,(k-1))
   s = [[2 for x in range(col)] for y in range(k)]
   for i in range(len(s)):
      for j in range(len(s[i])):
         if ( search(W[i],ps[j]) ):
            s[i][j] = 1
         else:
            s[i][j] = 0
   return s

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
   # creates an S0 matrix such that S0 = S0[i,j] = 1 iff ei in pij
   s0 = makeS(W, pi)
   # creates an S1 matrix such that S1 = S1[i,j] = 1 iff e1 in sigmaj
   s1 = makeS(W, sigma)
   return 0
   
   #accept commandline input: kofk.py k k image

   #for prow in range(image):
   #   for pcol in range(pixelrow):
   #      if  image[prow,pcol]== 0:
   #         C0share = permuteMatrix S0
            #distribute across k shares
   #      else:
   #         C1share = permuteMatrix S1


###MAIN###
koutofk()
