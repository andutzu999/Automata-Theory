import sys


#caut prexiful in aux1 care este si sufix in aux2
def prefix_sufix(aux1, aux2):
	length = 0
	
	for i in range(1, len(aux1)):
		if aux1[0:i] == aux2[(len(aux2) - i) : len(aux2)]:
			length = i
	return length

#construiesc matricea delta
def build_delta(word):

	matrix = [ [ 0 for i in range(26) ] for j in range(len(word) + 1) ]

	#prima litera a cuvantului
	first_letter = word[0]
	
	#parcurg tot cuvantul
	for i in range(len(word)):
		aux1 = word[0:(i+1)]
		for j in range(i):
			# concatenez fiecare litera anterioara a word-ului la aux2
			aux2 = word[0:i] + word[j]
			if aux1 != aux2:
				#completez matricea delta
				matrix[i][ord(word[j]) - 65] = prefix_sufix(aux1, aux2)

			aux2 = aux2[:-1]

		#completez in matricea delta starea in care ma aflu in cazul in care face match litera
		matrix[i][ord(word[i]) - 65] = i + 1

	#completez ultima linie din matrice
	matrix[len(word)][ord(word[0]) - 65] =  1
	x = prefix_sufix(word,word)
	matrix[len(word)][ord(word[x]) - 65] =  x + 1

	return matrix


def indexes(word, text):
	matrix = build_delta(word)
	stare = 0
	output_file = open(sys.argv[2], "w")

	sir_indexi = ""
	for i in range(len(text)):

		stare = matrix[stare][ord(text[i]) - 65]
		#verific daca am identificat cuvantul cerut in text
		if stare == len(word):
			index = i - len(word) + 1
			sir_indexi = sir_indexi + str(index) + " "
	
	#scriu in fisierul de out
	output_file.write(sir_indexi)
	if sir_indexi != "" :
		output_file.write("\n")

	output_file.close()
	
	return sir_indexi
	

if __name__ == '__main__':

	#citesc cuvintele din fisier
	input_file = open(sys.argv[1], "r")
	word = input_file.readline().strip()
	text = input_file.readline().strip()
	indexes(word, text)
	input_file.close()
