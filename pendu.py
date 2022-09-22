from collections import Counter

chr1 = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','e','e','e','a','a','c','o','i','u']
chr2 = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','é','è','ê','â','à','ç','ô','î','û']

Lf = []
rst = 0 # variable pour recommencer
P = 0 # variable pour la lettre proposée
Vic = 0 # variable utilisée pour tester si toutes les lettres ont été trouvées
X = 0 # variable pour compter le nombre de tentatives
V = 7

def remp(lettre): #remplace les majuscules par des minuscules
    for i in range(len(chr1)):
        if lettre == chr2[i]:
            return chr1[i]
        else:
            pass
    
C = 0 #variables de test pour les boucles while
C2 = 0
C3 = 0
C4 = 0

V6 = '    _____	 _____'

V5 ='''       
              |
              |
              |
              |
              |
              |
    _____	__|__'''

V4 =''' 
            _____________      
              |
              |
              |
              |
              |
              |
    _____	__|__'''
    
V3 =''' 
            _____________      
              |         |  
              |         o
              |
              |
              |
              |
    _____	__|__'''
    
V2 =''' 
            _____________      
              |         |  
              |         o
              |         |
              |         |
              |
              |
    _____	__|__'''
    
V1 =''' 
            _____________      
              |         |  
              |         o
              |        /|\\
              |         |
              |
              |
    _____	__|__'''
    
V0 =''' 
            _____________      
              |         |  
              |         o
              |        /|\\
              |         |
              |        / \\
              |
    _____	__|__'''
    
VL = [V0,V1,V2,V3,V4,V5,V6]

motD = ''

while C4 == 0 :     #test pour recommencer
    
    Lf = []
    rst = 0     #variable pour recommencer
    P = 'zz'   #variable pour la lettre proposée
    Vic = 0     #variable utilisée pour tester si toutes les lettres ont été trouvées
    X = 0   #variable pour compter le nombre de tentatives
    V = 7
    
    C = 0   #variables de test pour les boucles while
    C2 = 0
    C3 = 0
    C4 = 0

    while C == 0 or C2 == 0:    #recommence jusqu'à ce qu'un mot valide soit rentré

        C2 = 1
        motD = ''
        mot = str(input('Proposez un mot secret :'))

        for i in range(len(mot)):
            if mot[i] not in chr1 and mot[i] not in chr2  :    #test si les charactères sont des lettres
                print('Des caractères ne sont pas valides')
                C2 = 0
            if mot[i] in chr1:          #test si les charactères sont des minuscules
                motD = motD + mot[i]
            if mot[i] in chr2:          #remplace les majuscules par des minuscules
                motD = motD + remp(mot[i])        
        if len(motD) < 2:      #vérifie que le mot à deviner contient plus d'une lettre
            C = 0
        else:
            C = 1
            
    for i in range(len(motD)):
        assert motD[i] in chr1
    
    counter = Counter(motD)     #variable pour compter combien de fois une lettre apparait dans le mot        
    print("")
    print("Le mot à trouver est le suivant")

    while C3 == 0:      #recommence jusqu'à ce que toutes les lettres soient trouvées ou que le joueur n'ait plus de vie  
    
        Vic = 1     #variable utilisée pour savoir si toutes les lettres ont été trouvées
    
        for x in range(len(motD)):      #écrit soit un tiret soit une lettre si elle a déja été proposée
            if motD[x] in Lf:
                print(motD[x], end=" ")
            else:
                print('_ ', end=" ")
                Vic = 0     #si Vic = 0 alors toutes les lettres n'ont pas été trouvées
     
        if Vic == 1:
            C3 = 1
        print("")
        print("")
   
        if C3 == 0:
            print("vous avez", V ,"vies")
            if V < 7:
                print(VL[V])        #écrit le dessin correspondant au nombre de vies restantes
            if V > 0:
                tst = str(input('Proposez une lettre :'))
                if len(tst) == 1:       #teste si plus d'une lettre est entrée
                    P = tst
                else:
                    P = '0'
                assert len(P) == 1
            else:
                C3 = 1
            print("")

            if P in chr2:       #remplace les majuscules par des minuscules
                P = remp(P)

            if P in motD:
                print("la lettre est dans le mot il y en a", counter[P])
                Lf.append(P)
            else:
                print("la lettre n’est pas dans le mot")
                V = V - 1
            X = X + 1

    if V < 0:
        print("")
        print("vous avez perdu")
        print("")
    
        while rst != 'y' and rst != 'n':
            rst = str(input("Voulez-vous recommencer ? (y/n):"))
            if rst == 'y':
                C4 = 0
            if rst == 'n':
                C4 = 1
        assert rst == 'y' or rst == 'n'
    else:
        print("vous avez gagné en",X,"coup")
        print("")
    
        while rst != 'y' and rst != 'n':
            rst = str(input("Voulez-vous recommencer ? (y/n):"))
            if rst == 'y':
                C4 = 0
            if rst == 'n':
                C4 = 1
        assert rst == 'y' or rst == 'n'

 





