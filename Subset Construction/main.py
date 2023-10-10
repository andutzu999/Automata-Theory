import sys
import itertools
from queue import Queue


# citirea datelor din fisierele de intrare si aflarea AFN-ului
def AFN():
    # dictionar nfa
    AFN_dict = dict()
    # input file
    input_file = open(sys.argv[1], "r")
    Lines = input_file.readlines()

    number_of_states = Lines[0].strip()
    list_of_final_states = Lines[1].strip().split()
    Lines = Lines[2:]

    #construim un dictionar cu inputul
    for line in Lines:
        l = line.strip().split()
        AFN_dict[(l[0], l[1])] = l[2:]

    input_file.close()
    return AFN_dict, number_of_states, list_of_final_states

# aflam Epsilon initial
def epsilon_initial(AFN_dict,  AFN_stari):

    E_initial = dict()
    for i in range(len(AFN_stari)):
        #iau fiecare stare din AFN cu legaturi epsilon
        if (AFN_stari[i],'eps') in AFN_dict: 
            E_initial[i] = AFN_dict[(AFN_stari[i],'eps')]
            E_initial[i].append(str(i))

        else:
            E_initial[i] = [str(i)]
        
    
    return E_initial

## stiind Epsilon initial, putem sa aflam Epsilon final
## fac oarecum o parcurgere in latime pentru fiecare 
## stare din Epsilon initial
def epsilon_final(E_initial, AFN_stari):

    E_final = dict()
    for key in E_initial:

        list = []
        queue = []
        visited = [0]*int(number_of_states)
        visited[key] = 1
        queue.append(key)
        list.append(str(key))
    
        while queue:
            s = queue.pop(0)

            for neighbour in E_initial[s]:
                if visited[int(neighbour)] == 0:
                    visited[int(neighbour)] = 1
                    queue.append(int(neighbour))
                    list.append(neighbour)

            E_final[key] = sorted(list)
       
    return E_final

# returnam noua stare in care se va ajunge in DFA (sub forma de lista)
def stare(stare_curenta, AFN_dict, litera):

    list_of_list = []
    for i in range(len(stare_curenta)):

        if (stare_curenta[i], litera) in AFN_dict:
            x = AFN_dict[(stare_curenta[i], litera)]

            for j in range(len(x)):
                # epsilon final pentru fiecare stare in care ajunge o litera
                lista = E_final[int(x[j])]
                list_of_list.append(lista)
            
    final_list = [item for sublist in list_of_list for item in sublist]        
    final_list = sorted(list(dict.fromkeys(final_list)))


    return final_list  

# construire DFA
def construire_DFA(E_final, AFN_dict, l):

    DFA_dict = dict()
    queue = []
    visited = dict()
    lista = []

    visited[tuple(E_final[0])] = 1
    queue.append(E_final[0])
    lista.append(E_final[0])

# pentru fiecare stare nou aflata a DFA-ului, mai aflu inca o stare noua
# atunci cand coada mea va fi goala, inseamna ca deja am obtinut toate starile DFA-ului
    while queue:
        s = queue.pop(0)

        #aflam stari noi pentru fiecare litera din lista cu costuri din NFA
        for i in range(len(l)):
            #noua stare
            final_list = []
            final_list = stare(s, AFN_dict, l[i])

            if final_list != []:
                DFA_dict[(tuple(s), l[i])] = final_list

                if tuple(final_list) not in visited:
                    visited[tuple(final_list)] = 1
                    queue.append(final_list)
                    lista.append(final_list)

            # daca nu se ajunge in nicio stare in DFA, atunci adaugam un sink state in DFA ul nostru 
            if final_list == []:
                DFA_dict[tuple(s), l[i]] = ["sink"]
                visited["sink"] = 1
                for j in range(len(l)):
                    DFA_dict[("sink",l[j])] = ["sink"]
                lista.append(["sink"])
    
        
    return DFA_dict,lista

# aflam din lista noastra cu stari DFA
# care dintre ele este o stare finala
def check_stari_finale(list_of_final_states, lista):
    l_fin = []
    for i in range(len(lista)):    
        if lista[i] != ['sink']:
            for j in range(len(list_of_final_states)):

                if list_of_final_states[j] in lista[i]:
                    l_fin.append(i)
                    break
    
    return sorted(l_fin)

            
    
if __name__ == '__main__':

    # dictionar NFA
    AFN_dict, number_of_states, list_of_final_states = AFN()

    # lista cu starile NFA-ului
    AFN_stari = [0] * int(number_of_states)
    for i in range(int(number_of_states)):
        AFN_stari[i] = str(i)
    

    #aflam epsilon initial
    E_initial = epsilon_initial(AFN_dict, AFN_stari)

    #aflam epsilon final
    E_final = epsilon_final(E_initial, AFN_stari)

    #aflam literele de tranzitie din AFN
    rows = AFN_dict.keys()
    l = [x[1] for x in rows]
    l = list(dict.fromkeys(l))
    if 'eps' in l:
        l.remove('eps')

    #construim DFA-ul
    DFA_dict, lista = construire_DFA(E_final, AFN_dict, l)
    lista = sorted(lista)
    lista = list(lista for lista,_ in itertools.groupby(lista))

    ##facem o lista cu cheile din dictionarul DFA-ului
    ##si inca una cu valorile din dictionarul DFA-ului
    DFA_keys = list(DFA_dict.keys())
    DFA_values = list(DFA_dict.values())

    for i in range(len(DFA_keys)):

        t = DFA_keys[i]
        lst = list(t)
        if lst[0] != 'sink':
            lst[0] = lista.index(list(lst[0]))

        else: lst[0] = len(lista) - 1
        t = tuple(lst)
        DFA_keys[i] = t

    #inlocuim in lista de valori a DFA-ului 
    #cu indexii fiecarei stari a DFA-ului stocat in "lista"
    DFA_values = list(map(lambda x: lista.index(x), DFA_values))

    # lista cu stari finale
    l_fin = check_stari_finale(list_of_final_states, lista)

    # scrierea in fisier
    output_file = open(sys.argv[2], "w")
    output_file.write(str(len(lista)) + "\n")

    output_file.write(str(l_fin[0]))
    for i in range(1,len(l_fin)):
        output_file.write(" " + str(l_fin[i]))
    
    output_file.write("\n")

    for i in range(len(DFA_values)):
        output_file.write(str(DFA_keys[i][0]) + " " + DFA_keys[i][1] + " " + str(DFA_values[i]) + "\n")
    output_file.close()
    
  
  
  


    







