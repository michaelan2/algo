'''
string alignment problem
Given string X and string Y, find the minimum cost to transform string X into string Y.
Valid operations include insertions (match _, a), deletions (match a, _), and substitutions (match a,b)
Assume inserts, deletes cost d and substitutions cost a


Approach: Use dynamic programming
Recursively break down the problem into alignment problems of substrings
Let OPT(i, j) == minimum cost for aligning x1, x2, ... xi and y1, y2, ... yj
We have three ways of finding OPT(i,j):
1. Match xi, yj. Use a substitution.
OPT(i,j) = OPT(i-1,j-1) + a
2. xi is unmatched. Use a deletion.
OPT(i,j) = OPT(i-1, j) + d
3. yj is unmatched. Use an insertion.
OPT(i,j) = OPT(i, j-1) + d

Then our algorithm to find OPT(i,j) simply uses the minimum cost of the above three options.

Base cases:
OPT(0, 0) = 0
OPT(0, j) = d*j (just j insertions)
OPT(i, 0) = d*i (just i deletions)

Suppose X has length m and Y has length n
We can visualize the solving of this problem with a 2D matrix.
The matrix is [null, y1, y2, y3, ... yn] x [null, x1, x2, x3, ... xm]
Solving for entry (x,y) requires (x-1,y-1), (x-1,y), and (x,y-1)

'''

# bottom up solution
def sequence_alignment(X, Y, m, n, d, a):
	M = [[0 for i in range(m+1)] for j in range(n+1)]
	for i in range(m+1):
		M[0][i] = d*i
	for j in range(n+1):
		M[j][0] = d*j

	for i in range(1, m+1):
		for j in range(1, n+1):
			M[j][i] = min(
				M[j-1][i] + d,
				M[j][i-1] + d,
				M[j-1][i-1] + cost_a(X[i-1], Y[j-1], a)
				)
	return M[n][m]

# cost function for substitiution
def cost_a(x, y, a):
	return 0 if (x==y) else a