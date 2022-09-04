# In computer science, the prefix sum, cumulative sum, inclusive scan, or simply scan of a sequence of numbers x0, 
# x1, x2, ... is a second sequence of numbers y0, y1, y2, ..., the sums of prefixes (running totals) of the input sequence:

#A already exists
A = [a0, a1, a2, ...]
B = []
for i in range(1, len(A)):
  B[i] = B[i-1] + A[i]
  
