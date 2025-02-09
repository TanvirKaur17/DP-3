#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 30 09:20:42 2019

@author: tanvirkaur
"""

# time complexity = O(n*n)
# space complexity = O(1)
class Solution:
    def minFallingPathSum(self, A: List[List[int]]) -> int:
        for i in range(1,len(A)):
            for j in range(len(A)):
                if j == 0:
                    A[i][j] = A[i][j] + min(A[i-1][j],A[i-1][j+1])
                elif j == len(A)-1:
                    A[i][j] = A[i][j] + min(A[i-1][j],A[i-1][j-1])
                else:
                    A[i][j] = A[i][j] + min(A[i-1][j],A[i-1][j-1],A[i-1][j+1])
        return min(A[-1])
                    