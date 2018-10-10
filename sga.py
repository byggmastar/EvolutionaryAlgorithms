# Simple Generic Algorithm
# Property of Fredrik

import numpy as np
import math
import random as rand

class sga:

    def __init__( self , len = 0, size = 0 ):
        self.init( len, size )

    def init(self, len, size):
        self.len = len
        self.size = size
        self.pop = np.zeros( (size, len ), np.int8 )
        for i in np.nditer( self.pop, op_flags=['readwrite'] ):
            i[...] = math.floor( rand.random() + 0.5 )

    def eval(self, eval_func):
        np.apply_along_axis( eval_func, axis=1, arr=self.pop );

    def display(self):
        print( "Chromozome length: " + str( self.len ) )
        print( "Population size: " + str( self.size ) )
        print( self.pop )

    @staticmethod
    def toInt( x ):
        return x.dot( 2 ** np.arange(x.size)[::-1])

