# -*- coding: utf-8 -*-
"""Fibonacci.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Xo9mAScaOTXtFIPe0cww3HdO7ctSX9ck
"""

def fibonacci():
  result = [0,1]
  print("Entrez un nombre :")
  n = int(input())
  for i in range(2, n + 1):
    next = result[-1] + result[-2]
    result.append(next)
  result = ", ".join([str(i) for i in result])
  print(f"La suite fibonacci est :\n {result}")

fibonacci()