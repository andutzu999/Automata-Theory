                                            Tema 2 - Subset Construction

                Tema consta in transformarea unui NFA intr-un DFA. Pentru inceput, citesc din fisierele de 
        intrare fiecare linie aferenta starilor din care plec si ajung, linii pe care le voi retine intr-un dictionar. 
        Ulterior, urmeaza sa aflu inchiderile initiale pentru fiecare stare, asa ca extrag din dictionarul NFA-ului 
        starile ce au ca si cale de tranzitie un Epsilon. Dupa, le stochez intr-un dictionar ce are ca si cheie 
        fiecare stare din care plec. 
                Aceasta structura a Epsilonului initial ma va ajuta sa aflu Epsilon final, adica practic inchiderile 
        pentru fiecare stare din NFA. Asa ca eu pentru fiecare stare din Epsilon inital, trebuie sa aflu calea
        maxima cu Epsilon-uri pe care se poate ajunge. 
        De exemplu daca am E_initial(0) = {0,1}, E_initial(1) = {1, 3} , atunci E_final(0) = {0,1,3}, deoarece 
        avem cai cu Epsilon pe ruta 0-1-3.
                Mai departe, ca sa construim DFA-ul, practic forma primei stari este data de concatenarea cifrelor
        din rezultatul multimii E_final(0) si aflam formele starilor noi. Cand nu vom mai obtine stari noi, practic
        DFA-ul se termina de construit. Din el mai aflam care dintre acele stari sunt finale. Apoi, asociem o valoare
        fiecarei stari de la 0 la numarul de stari obtinute. Avem nevoie de asta cnd vom scrie DFA-ul in fisier.
                Cum aflam care dintre starile obtinute este finala? Va contine in multime minim o stare finala din NFA.
                Cum determinam noi stari din DFA? Incepand cu prima stare a DFA-ului, vedem cu fiecare tranzitie pe 
        rand pentru fiecare valoarea din multimea primei stari a DFA-ului, unde ajungem. Apoi, aflam inchiderea finala
        pentru rezultat, reunim toate rezultatele si eliminam duplicatele. Asa va arata multimea unei noi stari din DFA.
                In final, DFA-ul afisat in output este corect.
