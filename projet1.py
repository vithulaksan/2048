'''
    Nous importons random pour utiliser la fonction choice qui va nous permettre de faire des choix de manière aléatoire.
'''

import random

score=0
v=0

######################################################### choix du mode
'''
    La fonction choixmode sera celle qui sera appelle en premier au lancement du jeu elle va permettre de choisir le mode de jeu 
'''
def choixmode() :
    '''
        La fonction nous demande de chosir le mode à laquelle nous voulons jouer.
        Si nous choisissons entre 1 et 3, elle renvoie vers le mode qui correspond sinon elle nous redemande de chosir le mode.
        Si nous avons choisit 1, nous créons un variable n qui vaut 4 et nous renvoie vers la fonction 'debut_game(n)'. 
        Si nous avons choisit 2, nous créons un variable n qui vaut 5 et nous renvoie vers la fonction 'debut_game(n).
        Si nous avons choisit 3, nous allons chercher la dernière ligne du fichier 'tablo_memoire.txt', 
        ceci va nous permettre de retrouver:
        - la valeur de n, qui va nous permettre de savoir la taille du tableau.
        - la valeur de v. 
        - la valeur du score de la  partie enregistrer.
        - le tableau de la partie enregistrer.
    '''
    global score
    global v
    print("Quel mode voulez-vous faire ? \n  1 = 4x4  \n  2 = 5x5 \n  3 = reprendre la partie precedente ")
    niv = int(input())
    if niv == 1 or niv == 2 or niv == 3 :
        print('passage au mode '+str(niv))
    else :
        print("La commande rentrée n'a pas été comprise")
        return(choixmode())
    if niv == 1 : 
        n=4
        return(debut_game(n))
    if niv == 2 :
        n=5
        return(debut_game(n))
    else :
        l = read_file("tablo_memoire.txt")
        l0 = l[-1]
        l1 = l0.split('to')
        n = int(l1[0])
        a = int(l1[1])
        v = int(l1[2])
        l2 = l1[-1]
        l3=l2.split('no')
        tablo1=[l3[i].split('-') for i in range(n)]
        tablo=[]
        for i in range(n):
            tablo.append([])
            for j in range(n):
                tablo[i].append(int(tablo1[i][j]))
        score+=a
        affichage(n,tablo)
        return(direction(n,tablo))
#############################################  mode 3 (transformer le txt en liste)
'''
    La fonction 'read_file' est un élément important pour importer le dernier tableau enregistrer dans un fichier et aussi pour trouver le meilleur score .   
'''
def read_file(filename):
    '''
        La liste 'l' va prendre comme élément chaque ligne du fichier.

    '''
    with open(filename, mode='r', encoding='utf8') as f:
        l=[]
        s = f.readline()
        txt=s.split('\n')
        while s!='' :
            l.append(txt[0])
            s = f.readline()
            txt=s.split('\n')
        return(l)

################################################ meilleur score
'''
    La fonction meilleur_score permet de trouver le meilleur score. 
'''
def meilleur_score(filename):
    '''
        Nous transformons le texte d'un fichier en liste,
        et nous cherchons la plus grande valeur de cette liste. 
    
    '''
    l = read_file(filename)
    m=len(l)
    i=0
    maxi = int(l[0])
    while i<m-1:
        if maxi <= int(l[i+1]):
            maxi=int(l[i+1])
        i+=1
    return(maxi)


################################################ pour nouvo tablo (mode 1 et mode 2)

def debut_game(n):
    '''
        Nous créons un tableau de taille n avec 2 valeurs.
    '''
    tablo=[]
    for i in range(n):
            tablo.append([])
            for j in range(n):
                tablo[i].append(0)
    ajout(tablo)
    ajout(tablo)
    affichage(n,tablo)
    return(direction(n,tablo))

####################################### affichage
def affichage(n,tablo):
    '''
        cette fonctions permet d'afficher le tableau 
    '''
    #trouver la taille du plus grand nombre du tablo
    taille_maxi= len(str(tablo[0][0]))
    for i in range(len(tablo)):
        for j in tablo[int(i)]:
            if len(str(j))>taille_maxi:
                taille_maxi=len(str(j))
    #affichage
    for i in range(n):
        s='|' 
        for j in tablo[i]:
            if j==0:
                s+=" " * taille_maxi + "|"
            else:
                a=taille_maxi - len(str(j))
                s+=" " * a + str(j) + "|"   
        print(s)
    Best_score = meilleur_score('score.txt')
    if score<=Best_score:
        print("\nmeilleur score = "+str(Best_score))
    else:
        print("\nmeilleur score = "+str(score))
    print("\nscore = "+str(score))
    return(' ')



#################################### ajouter apres chaque deplacement
'''
    La fonction 'ajout' va être utilisé après chaque déplacement pour mettre une valeur dans le tableau,
    et au début de chaque partie pour mettre 2 valeurs au tableau vide.
'''
def ajout(tablo):
    '''
        Nous créons une liste 'vides' qui va nous donner toutes les positions où nous avons des zéros.
        Nous choisissons deux positions de manières aléatoires parmis celles où nous avons des zéros, 
        pour transformer les zéros en 2 ou en 4 avec une probabilité de 3/4 d'avoir un 2 et une probabilité de 1/4 d'avoir un 4.  
    
    '''
    vides=[]
    for i in range(len(tablo)):
        for j,x in enumerate(tablo[i]):
            if x==0:
                vides+=[( str(i) , str(j) )]
    if len(vides)!=0:
        (a,b)= random.choice(vides)
        tablo[int(a)][int(b)]= random.choice([2,2,2,4])

##################################### deplacement vers la gauche
'''
    L'ensemble de ces fonctions vont permettre de se déplacer à gauche lorsque nous cliquons z et le button entrer.
'''
def gauche(n,ligne):
    '''
        Nous créons une liste qui va prendre les valeurs non nul d'une liste donner en argument
        et on va le compléter avec des 0. 
        Exemple : si on a [2,0,4,0] ça renvoie [2,4,0,0]
    '''
    l=[]
    for i in ligne:
        if i!=0:
            l.append(i)
    for j in range(n):
        l.append(0)
    return(l[:n])

def simp(n,ligne):
    '''
        Nous prenons une liste, nous mettons les valeurs non nul à gauche et nous la complètons avec des zéros.
        Nous comparons de gauche à droite pour voir si nous avons pas la même valeur, si c'est le cas nous multiplions par
        2 celle qui se trouve à gauche parmi les 2 valeurs comparé et nous mettons 0 pour celle qui se trouver à gauche.
        Et pour finir, nous met les valeurs non nul à gauche et nous la complètons avec des zéros. 
        Exemple: [4,2,0,2,0,4] -> [4,2,2,4,0,0] -> [4,4,0,4,0,0] -> [4,4,4,0,0,0] 

    '''
    global score
    ligne = gauche(n,ligne)
    for i in range(1,n):
        if ligne[i] == ligne[i-1]:
            score += ligne[i]*2
            ligne[i-1] *= 2
            ligne[i] = 0
    return(gauche(n,ligne))


def deplacement_gauche(n,tablo):
    '''
        Nous fesons exactement la même chose que dans la fonction vu précèdement, ligne par ligne du tableau.
    '''
    for i in range(n):
        tablo[i]=simp(n,tablo[i])
    return(tablo)

#######################################  deplacement vers la droite
'''
    L'ensemble de ces fonctions vont permettre de se deplacer à droite lorsque nous cliquons sur la flèche droite.
'''
def deplacement_droite(n,tablo):
    for i in range(n):
        tablo[i]=gauche(n,tablo[i])
        tablo[i].reverse()
        tablo[i]=simp(n,tablo[i])
        tablo[i].reverse()
    return(tablo)

######################################  deplacement vers le haut
'''
    L'ensemble de ces fonctions vont permettre de se deplacer en haut lorsque nous cliqueons sur la flèche haut.
'''
def transformation(n,tablo):
    '''
        cette fonction renvoie la tanslation de la matrice mit en argument.
    '''
    l=[]
    for i in range(n):
        l.append([tablo[j][i] for j in range(n)])
    return(l)


def deplacement_haut(n,tablo):
    tablo = transformation(n,tablo)
    tablo = deplacement_gauche(n,tablo)
    tablo = transformation(n,tablo)
    return(tablo)

#####################################   deplacement vers le bas
'''
    L'ensemble de ces fonctions vont permettre de se deplacer en bas lorsque nous cliquons sur la fleche bas.
'''
def deplacement_bas(n,tablo):
    tablo = transformation(n,tablo)
    tablo = deplacement_droite(n,tablo)
    tablo = transformation(n,tablo)
    return(tablo)

####################################   victoire

def victoire(n,tablo):
    '''
        Renvoie 'vous avez gg' lorsque nous retrouvons un 2048 dans le tableau
    '''
    a=0
    for i in range(n):
        for j in range(n):
            if tablo[i][j]==2048:
                a=1
                break
    if a==1:
        return('vous avez gg') 
    else:
        return(' ')

####################################  défaite
'''
    La fonction défaite permet de savoir si on a perdu ou pas,
'''
def defaite(n,tablo):
    a=0
    for i in range(n):
        for j in range(n):
            if tablo[i][j]==0:
                return(' ')
    for i in range(n-1):
        for j in range(n-1):
            if tablo[i][j] == tablo[i][j+1] or tablo[i][j] == tablo[i+1][j]:
                a=1
                break
    for i in range(n-1):
        if tablo[n-1][i]==tablo[n-1][i+1]:
            a=1
            break
    for i in range(n-1):
        if tablo[i][n-1]==tablo[i+1][n-1]:
            a=1
            break
    if a==0:
        return("Vous avez perdu")
    else:
        return(' ')

###################################### Enregistrement et quitter

'''
    La fonction 'enregistrer2' est utilisée lorsque nous cliquons sur le bouton 'quitter sans sauvegarder'
    et lorsque nous perdons une partie. 
'''
def enregistrer(n,tablo):
    '''
        Nous enregistrons la valeur du score dans le fichier 'score.txt'.
    '''
    with open("score.txt",mode='a',encoding='utf8') as g:
        g.write('\n')
        g.write(str(score))
    with open("tablo_memoire.txt", mode='a', encoding='utf8') as f:
        f.write(str(n))
        f.write("to")
        f.write(str(score))
        f.write("to")
        f.write(str(v))
        f.write("to")
        for i in range(n):
            for j in range(n):
                if j!=(n-1):
                    f.write(str(tablo[i][j]))
                    f.write('-')
                else:
                    f.write(str(tablo[i][j]))
            if i!=(n-1):
                f.write('no')
        f.write("\n")
    return('STOP') 

################################ choix continuer
'''
    permet de chosir si on continue ou pas après avoir atteint la valeur 2048.
'''
def continu(e,n,tablo):
    while e!='1' and e!='2' and e!='3':
            print('Bien jouer')
            print('Cliquez sur : \n 1 : Enregistrer et quitter \n 2 : Quitter sans enregistrer \n 3 : continuer ')
            e = input()
    if e=='2':
            with open("score.txt",mode='a',encoding='utf8') as g:
                g.write('\n')
                g.write(str(score))
            return("STOP")
    if e=='1':
        enregistrer(n,tablo)
        return('STOP') 
    if e=='3':
        return(direction(n,tablo))

################################### choix direction

def direction(n,tablo):
    '''
        Nous mettons le tableau en mémoire.
        Nous choissisons entre:
        - z pour déplacer le tableau vers le haut.
        - s pour déplacer le tableau vers le bas.
        - d pour déplacer le tableau vers la droite.
        - q pour déplacer le tableau vers la gauche. 
        - nous cliquons sur espace pour pouvoir:
            - enregister et quitter.
            - quitter sans enregistrer.
        Nous comparons le nouveau tableau avec le tableau mit en mémoire:
        - Si c'est pas le même, nous remplaçons un 0 par un 2 ou 4.
        Nous regardons si nous avons gagner c'est a dire si on a un 2048,
        si c'est le cas on a 3 choix:
        - enregistrer et quitter 
        - quitter sans enregistrer
        - continuer: c'est ici que le v intervient et empeche une repetion de demande pour savoir si nous voulons continer ou pas.
          En effet une fois que nous décidons de continuer pour arreter il faut que nous cliquons sur la touche espace.
        Nous regardons si nous avons perdu c'est à dire si on ne peu plus se deplacer,
        si c'est le cas le score et enregistrer dans le fichier 'score.txt'.  
        
    '''
    global v
    global score
    tablo1=tablo[:]
    print("dans quelle direction voulez-vous aller ? \n  z = haut \n  d = droite  \n  s = bas \n  q = gauche \n espace = Enregistrer ou Stop \n ")
    dir = input()
    if dir ==' ':
        print("Cliquez sur : \n 1 : Enregistrer et quitter \n 2 : Quitter sans enregistrer \n ")
        d = int(input())
        if d == 1 :
            enregistrer(n,tablo)
            return('STOP')
        if d == 2 :
            with open("score.txt",mode='a',encoding='utf8') as g:
                g.write('\n')
                g.write(str(score))
            return('STOP')
        else :
            return(direction(n,tablo))
    if dir == "z" :
        print('Vous vous êtes déplacés vers le haut\n')
        tablo = deplacement_haut(n,tablo)
    elif dir == "d" :
        print('Vous vous êtes déplacés vers la droite\n')
        tablo = deplacement_droite(n,tablo)
    elif dir == "s" :
        print('Vous vous êtes déplacés vers le bas\n')
        tablo = deplacement_bas(n,tablo)
    elif dir == "q" :
        print('Vous vous êtes déplacés vers la gauche\n')
        tablo = deplacement_gauche(n,tablo)
    else:
        print('choix de direction invalide\n')
        return(direction(n,tablo))
    if tablo!=tablo1:
        ajout(tablo)
    print(affichage(n,tablo))
    vict=victoire(n,tablo)
    if vict=='vous avez gg'and v==0 :
        v = 1
        print('Bien jouer')
        print('Cliquez sur : \n 1 : Enregistrer et quitter \n 2 : Quitter sans enregistrer \n 3 : continuer ')
        e=input()
        continu(e,n,tablo)
        return('STOP')
    defai=defaite(n,tablo)
    if defai == "Vous avez perdu":
        with open("score.txt",mode='a',encoding='utf8') as g:
            g.write('\n')
            g.write(str(score))
        print('vous avez perdu')
        return('perdu')
    return(direction(n,tablo))

choixmode()