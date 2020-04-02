
# STABLE MATCHING PROBLEM
# solution with the Gale-Shapely algorithm off the top of my head
# using the classic stable marriage question

'''
INPUTS: 
men_pref: nxn array of men's preferences of women
e.g. [0][2] is the first man's third-most preferred woman
women_pref: nxn array of women's preferences of men

OUTPUT:
list of all (man, woman) pairs for a stable matching
'''

def gs(men_pref, women_pref):
	# let n be the number of men and women. 
	# In this basic exercise we suppose num men == num women
	n = len(women_pref[0])

	# DATA STRUCTURE: unmatched_men
	# queue of unmatched men left to process. Popping off end is O(1)
	unmatched_men = []
	for i in range(n):
		unmatched_men.append(i)

	# DATA STRUCTURE: men_next_choice
	# length n array of integers
	# men_next_choice[m] == index of next woman in preference list of man m whom has not been proposed to yet
	men_next_choice = [0] * n

	# DATA STRUCTURE: match[w]
	# length n array of matches. index: woman number -> contains man number
	# -1 if woman is unmatched
	match = [-1] * n

	# DATA STRUCTURE: rank[w][m]
	# 2D array where for each woman, contains array with index: man number -> man ranking on w's list
	# EXAMPLE: if woman has preferences [0th pref: 2, first pref: 0, second pref: 1] this creates ranking [m0:1, m1:2, m2:0]
	# DANGER: [[-1] * n * n] creates n shallow copies of an array
	rank = [[-1 for woman in range(n)] for man in range(n)]
	for w in range(n):
		for ranking in range(n):
			man_id = women_pref[w][ranking]
			rank[w][ man_id ] = ranking

	# MAIN LOOP:
	# while there exists unmatched man m, find match for man m
	while len(unmatched_men) > 0:
		m = unmatched_men.pop() 
		w = men_pref[m][ men_next_choice[m] ]

		# if woman is unmatched, match with man m
		if match[w] == -1:
			match[w] = m
		# if woman prefers m to current partner, switch to m
		else:
			current_partner = match[w]
			if rank[w][m] < rank[w][current_partner]:
				match[w] = m
				unmatched_men.append(current_partner)
			# otherwise the man is still unmatched and will propose to the next woman on his list
			else:
				unmatched_men.append(m)
		# we increment the man's next preferred pointer and loop again
		# even if the man is matched, we increment his next preferred pointer since he may be unmatched later
		men_next_choice[m] += 1
		print("match iteration:",match)


	for w in range(n):
		print((match[w], w))

# small sanity check
gs([[0,1,2],[1,2,0], [1,2,0]],
	[[2,0,1],[2,1,0], [1,2,0]]
	)
