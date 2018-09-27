def MinimumEditDistance(s1, s2):
	""" (str, str) -> int
		Calculates the edit distance between two strings,
		s1 and s2.
		Based on the pseudocode in 
		https://web.stanford.edu/~jurafsky/slp3/2.pdf
		[p. 24]
	"""
	# Ignore casing
	s1 = s1.lower()
	s2 = s2.lower()

	# Edit costs
	deletion_cost = 1
	insertion_cost = 1
	substitution_cost = 2

	n = len(s1)
	m = len(s2)

	# Initialize distance matrix
	D = [[0 for j in range(m+2)] for i in range(n+2)]

	for i in range(1, n+1):
		D[i][0] = D[i-1][0] + deletion_cost

	for j in range(1, m+1):
		D[0][j] = D[0][j-1] + insertion_cost

	# Compute cost
	for i in range(1, n+1):
		for j in range(1, m+1):
			del_cost = D[i-1][j] + deletion_cost
			ins_cost = D[i][j-1] + insertion_cost
			sub_cost = D[i-1][j-1]

			if s1[i-1] != s2[j-1]: sub_cost += substitution_cost
			
			D[i][j] = min([del_cost, ins_cost, sub_cost])

	return D[n][m]

# Top 10 rated imdb movies
movies = ["Fight Club", "The Godfather", "Schindler's List", "The Dark Knight", "The Lord of the Rings: The Return of the King", "The Shawshank Redemption", "The Godfather: Part II ", "Pulp Fiction", "12 Angry Men", "The Good, the Bad and the Ugly"]

ratings = [8.8, 9.2, 8.9, 9.0, 8.9, 9.2, 9.0, 8.9, 8.9, 8.8]
stopword = "quit"

while True:
	ui = input("Indtast en filmtitel (og '"+stopword+"' for at stoppe): ")

	if ui.lower() == stopword.lower():
		break

	if ui.lower() not in [m.lower() for m in movies]:
		
		distances = []

		# Calculate the distances between ui and known movies
		for movie in movies:
			med = MinimumEditDistance(movie, ui)
			distances.append(med)

		# Find the movie title most similar to ui
		most_similar_i = distances.index(min(distances))
		most_similar_title = movies[most_similar_i]
		most_similar_rating = ratings[most_similar_i]

		print("Filmen '"+most_similar_title+"' har fået en rating på "+str(most_similar_rating))

	else:
		movie_i = movies.index(ui)
		movie_rating = ratings[movie_i]
		print("Filmen '"+ui+"' har fået en rating på "+str(movie_rating))

	print()
