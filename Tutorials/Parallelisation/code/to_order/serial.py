import time
import random

SIZE = 2
MAXRAND = 10000

def rand_vec():

   random_ = []

   for i in range(SIZE):
      random_.append(random.randint(0,MAXRAND-1))

   return random_

def cmp_vec(random):
   
   is_sorted = 0
   last_value = None
   for value in random:
      if last_value is not None:
         is_sorted = is_sorted + (last_value < value)
      last_value = value

   return is_sorted


if __name__ == '__main__':

   random.seed(int(time.time())) # init random generator

   random_ = rand_vec()
   is_sorted = cmp_vec(random_)

   print("%d neighbouring sorted pairs found!" % (is_sorted))




