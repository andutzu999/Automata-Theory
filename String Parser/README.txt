BLANARU ANDY-ȘTEFAN
332CB

				README TEMA 1 - LFA

	Prima data am implementat o functie care imi afla cel mai lung prefix din cuvantul aux1,
care este si sufix in cuvantul aux2. Functia returneaza lungimea maxima a acestuia.
Pentru a construi matricea delta, sa zicem ca pentru cuvantul "EZER", iau urmatoarele
substringuri : E, EZ, EZE si EZER. Pentru cuvantul EZE de ex, daca urmeaza Z dupa, trecem
in starea 2, deoarece "EZER" si "EZEZ", apelate in functia de prefix_sufix, returneaza 
lungimea maxima 2. Verific si "EZER" cu "EZEE". De fapt, eu in acest caz am concatenat
la EZE fiecare litera anterioara a acestuia, adica E si Z. Analog fac si pentru celelalte
substring-uri. Pentru ultima linie din matrice, aflu cel mai lung prefix din cuvantul meu
care e sufix tot in cuvantul meu.
		Ulterior, folosind matricea delta, in momentul in care parcurc textul, stiu de fiecare
data in ce stare sunt. 	Atunci cand stiu ca starea va coincide cu lungimea cuvantului meu, 
concatenez indexul la un sir de indexi, pe care il afisez la sfarsit.
Citirea si scrierea le fac folosind argumente in linia de comanda.
