'''
    Nous importons tous les éléments de Tkinder, pour l'interface graphique.
    Nous importons random pour utiliser la fonction choice qui va nous permettre de faire des choix de manière aléatoire.

'''

from tkinter import *
import random

################################## creation de fenetre
'''
    Nous créons une fenêtre. 
    Nous l'appelons 2048. La fenêtre apparaît avec une taille de 800x800. 
    Nous lui mettons un logo et une couleur de fond.    

'''
window = Tk()
window.title("2048")
window.geometry("800x800")
window.iconbitmap('logo.ico')
window.config(background='#faf8ef')

#################################### les variables
'''
    Ici contrairement au programme fait pour l'affichage sur le terminal.
    Nous allons créer plus de variables pour les appeler ensuite dans les fonctions, au lieu 
    d'encombrer les arguments des fonctions. 

'''
canvas=None
canvas1=None
n=0
tablo=[]
score = 0
s1 = 0
s2 = 0
Best_score=0
b1 = None
b2 = None
b3 = None
v = 0

##################### ajout
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

################### transformer le txt en liste

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

######################### meilleur score
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

########## debut
'''
    La fonction 'choixmode' sera celle qui sera appellée en premier au lancement du jeu, elle va permettre de choisir le mode de jeu.  
'''
def choixmode():
    '''

        Nous appelons tous les variables globales,
        Nous supprimons tous les éléments affichés ( cette partie est importante lorsque nous avons un jeu en cours 
        et qu'on clique 'menu' pour revenir au choix du mode, sans cette partie nous allons superposer la partie précédente au dessus de la nouvelle ).
        Après avoir supprimé les éléments afficher si cela existe, nous créons 3 boutons:
        - le bouton '4x4' nous renvoie vers la fonction debut4x4 lorsque nous cliquons dessus.
        - le bouton '5x5' nous renvoie vers la fonction debut5x5 lorsque nous cliquons dessus.
        - le bouton 'Reprendre la partie précédente' nous renvoie vers la fonctions 'partie_precedent' lorsque nous cliquons dessus.

    '''

    global canvas
    global canvas1
    global b1
    global b2
    global b3

    if canvas1 != None:
        canvas1.destroy()
    if canvas != None:
        canvas.destroy()
    if b1 != None:
        b1.destroy()
    if b2 != None:
        b2.destroy()
    if b3 != None:
        b3.destroy()       
    canvas1 = Canvas(window,width=600, height=100, background="#faf8ef")
    canvas1.pack(expand=YES)

    button=Button(canvas1,text="4x4", font=("helvetica Neue", 25), background="#faf8ef", command = debut4x4)
    button.pack()
    button=Button(canvas1,text="5x5", font=("helvetica Neue", 25), background="#faf8ef", command = debut5x5)
    button.pack()
    button=Button(canvas1,text="Reprendre la partie précédente", font=("helvetica Neue", 25), background="#faf8ef", command = partie_precedent)
    button.pack()
    return

'''
    La fonction 'debut4x4' permet de créer un tableau de taille 4x4 avec deux valeurs. 
'''

def debut4x4():
    '''
        Nous mettons 'score = 0' car elle permet de remettre le score à 0 après qu'on a cliqué 'menu'.
        Nous detruisons le canevas1 pour enlever l'affichage des boutons du choix de mode.
        Nous créons le canavas1 et le canevas, pour ajouter du textes dans le canevas1.
        Nous créons s1 et s2 pour mettre le score et le meilleur score. Nous créons de cette manière pour 
        pouvoir le supprimer et le réécrire plus facilement après chaque déplacement.
        Nous créons 3 boutons:
        - enregistrer et quitter en bas à gauche 
        - quitter sans enregistrer en bas à droite
        - menu pour revenir au choix de mode
        Nous mettons à jour la valeur de n qui vaut 4 et le tableau qui est un tableau de taille 4x4 avec que des zéros.
        Nous mettons deux valeurs dans le tableau.
        Nous renvoyons vers la fonction 'rectangle1'.

    '''
    global n
    global tablo
    global canvas1
    global canvas
    global score
    global s1
    global s2
    global Best_score
    global b1
    global b2
    global b3

    score = 0
    Best_score=meilleur_score('score.txt')
    canvas1.destroy()
    canvas1 = Canvas(window,width=600, height=100, background="#faf8ef")
    canvas1.pack(expand=YES)
    canvas = Canvas(window,width=600, height=600, background="#bbada0")
    canvas.pack(expand=YES)
    texte = canvas1.create_text(65, 40, text="2048", font=("helvetica Neue", 40))
    texte = canvas1.create_text(200, 90, text="Reliez les nombres et obtenez la tuile 2048 !", font=("helvetica Neue", 15))
    texte = canvas1.create_text(475, 15, text="Score :", font=("helvetica Neue", 15))
    texte = canvas1.create_text(475, 40, text="Record :", font=("helvetica Neue", 15))
    s1 = canvas1.create_text(550, 10, text=str(score), font=("helvetica Neue", 15))
    s2 = canvas1.create_text(550, 40, text=str(Best_score), font=("helvetica Neue", 15))
    b1 = Button(window, text="Menu", font=("helvetica Neue", 8), background="#faf8ef", command = choixmode)
    b1.pack()
    b2 = Button(window, text="Sauvegarder et quitter", font=("helvetica Neue", 8), background="#faf8ef", command = enregistrer )
    b2.pack(side=LEFT)
    b3 = Button(window, text="Quitter sans sauvegarder", font=("helvetica Neue", 8), background="#faf8ef", command = enregistrer2)
    b3.pack(side=RIGHT)
    n=4
    tablo=[[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
    ajout(tablo)
    ajout(tablo)
    rectangle1(n,tablo)
    return

'''
    La fonction 'debut5x5' permet de créer un tableau de taille 5x5 avec deux valeurs. 
'''

def debut5x5():
    '''
        Nous mettons 'score = 0' car elle permet de remettre le score à 0 après que nous avons cliqué 'menu'.
        Nous détruisons le canevas1 pour enlever l'affichage des boutons du choix de mode.
        Nous créons le canavas1 et le canevas, pour ajouter du textes dans le canevas1.
        Nous créons s1 et s2 pour mettre le score et le meilleur score. Nous créons de cette maniere pour 
        pouvoir le supprimer et le réécrire plus facilement après chaque déplacement.
        Nous créons 3 boutons:
        - enregistrer et quitter en bas à gauche. 
        - quitter sans enregistrer en bas à droite.
        - menu pour revenir au choix de mode.
        Nous mettons à jour la valeur de n qui vaut 4 et le tableau qui est un tableau de taille 5x5 avec que des zéros.
        Nous mettons deux valeurs dans le tableau.
        Nous renvoyons vers la fonction 'rectangle2'.
    '''
    global n
    global tablo
    global canvas1
    global canvas
    global score
    global s1
    global s2
    global Best_score
    global b1
    global b2
    global b3
    score = 0 
    Best_score=meilleur_score('score.txt')
    canvas1.destroy()
    canvas1 = Canvas(window,width=600, height=100, background="#faf8ef")
    canvas1.pack(expand=YES)
    canvas = Canvas(window,width=600, height=600, background="#bbada0")
    canvas.pack(expand=YES)
    texte = canvas1.create_text(65, 40, text="2048", font=("helvetica Neue", 40))
    texte = canvas1.create_text(200, 90, text="Reliez les nombres et obtenez la tuile 2048 !", font=("helvetica Neue", 15))
    texte = canvas1.create_text(475, 15, text="Score :", font=("helvetica Neue", 15))
    texte = canvas1.create_text(475, 40, text="Record :", font=("helvetica Neue", 15))
    s1 = canvas1.create_text(550, 10, text=str(score), font=("helvetica Neue", 15))
    s2 = canvas1.create_text(550, 40, text=str(Best_score), font=("helvetica Neue", 15))
    b1 = Button(window, text="Menu", font=("helvetica Neue", 8), background="#faf8ef", command = choixmode)
    b1.pack()
    b2 = Button(window, text="Sauvegarder et quitter", font=("helvetica Neue", 8), background="#faf8ef", command = enregistrer )
    b2.pack(side=LEFT)
    b3 = Button(window, text="Quitter sans sauvegarder", font=("helvetica Neue", 8), background="#faf8ef", command = enregistrer2)
    b3.pack(side=RIGHT)
    n=5
    tablo=[[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]
    ajout(tablo)
    ajout(tablo)
    rectangle2(n,tablo)
    return

'''
    La fonction 'partie_precedent' permet de reprendre la dernière partie que nous avons enregistré.
'''
def partie_precedent():
    '''
        Nous mettons 'score = 0' car elle permet de remettre le score à 0 après que nous avons cliqué 'menu'.
        Nous allons chercher la dernière ligne du fichier 'tablo_memoire.txt', 
        ceci va nous permettre de retrouver:
        - la valeur de n, qui va nous permettre de savoir la taille du tableau
        - la valeur de v, pour ce programme la valeur de v ne sert a rien, nous n'avons pas besoin de lui pour le programme sur le terminal
        - la valeur du score de la  partie enregistrer
        - le tableau de la partie enregistrer
        Nous détruisons le canevas1 pour enlever l'affichage des boutons du choix de mode.
        Nous créons le canavas1 et le canevas, pour ajouter du textes dans le canevas1.
        Nous créons s1 et s2 pour mettre le score et le meilleur score. Nous créons de cette manière pour 
        pouvoir le supprimer et le reéécrire plus facilement après chaque déplacement.
        Nous créons 3 boutons:
        - enregistrer et quitter en bas à gauche. 
        - quitter sans enregistrer en bas à droite.
        - menu pour revenir au choix de mode.
        Nous comparons la valeur de n :
        - si n = 4, nous renvoyons vers la fonction 'rectangle1'.
        - si n = 5, nous renvoyons vers la fonction 'rectangle2'.

    '''
    global n
    global tablo
    global canvas1
    global canvas
    global score
    global s1
    global s2
    global Best_score
    global b1
    global b2
    global b3
    global v
    score = 0
    l = read_file("tablo_memoire.txt")
    l0 = l[-1]
    l1 = l0.split('to')
    n = int(l1[0])
    score = int(l1[1])
    v = int(l1[2])
    l2 = l1[-1]
    l3=l2.split('no')
    tablo1=[l3[i].split('-') for i in range(n)]
    tablo=[]
    for i in range(n):
        tablo.append([])
        for j in range(n):
            tablo[i].append(int(tablo1[i][j]))
    Best_score=meilleur_score('score.txt')
    canvas1.destroy()
    canvas1 = Canvas(window,width=600, height=100, background="#faf8ef")
    canvas1.pack(expand=YES)
    canvas = Canvas(window,width=600, height=600, background="#bbada0")
    canvas.pack(expand=YES)
    texte = canvas1.create_text(65, 40, text="2048", font=("helvetica Neue", 40))
    texte = canvas1.create_text(200, 90, text="Reliez les nombres et obtenez la tuile 2048 !", font=("helvetica Neue", 15))
    texte = canvas1.create_text(475, 15, text="Score :", font=("helvetica Neue", 15))
    texte = canvas1.create_text(475, 40, text="Record :", font=("helvetica Neue", 15))
    s1 = canvas1.create_text(550, 10, text=str(score), font=("helvetica Neue", 15))
    s2 = canvas1.create_text(550, 40, text=str(Best_score), font=("helvetica Neue", 15))
    b1 = Button(window, text="Menu", font=("helvetica Neue", 8), background="#faf8ef", command = choixmode)
    b1.pack()
    b2 = Button(window, text="Sauvegarder et quitter", font=("helvetica Neue", 8), background="#faf8ef", command = enregistrer )
    b2.pack(side=LEFT)
    b3 = Button(window, text="Quitter sans sauvegarder", font=("helvetica Neue", 8), background="#faf8ef", command = enregistrer2)
    b3.pack(side=RIGHT)
    if n==4:
        rectangle1(n,tablo)
    else:
        rectangle2(n,tablo)
    return

#################  Affichage
lrx1=[9,154.5,304.5,454.5]
lrx2=[145.5,295.5,445.5,595.5]
ltx1=[75,225,378.25,525]
lty1=[81.75,225,375,525]

'''
    La fonction 'retangle1' va permettre l'affichage de la partie 4x4.
'''
def rectangle1(n,tablo):
    '''
        Nous supprimons le texte qui renvoie la valeur du score et celui du meilleur score.
        Nous recréons le texte qui va permettre d'afficher le score et le meilleur score, après les avoir comparés:
        - si le score est plus grand que le meilleur score alors dans les deux textes, nous allons mettre la valeur du score.
        - si le score est plus petit que le meilleur score alors dans s2 nous renvoyons le meilleur score du fichier 'score.txt' et 
        dans s1 nous renvoyons le score.
        Nous créons 16 rectangles dans lesquels nous allons afficher les valeurs du tableau.
        Nous regardons si on a perdu,si c'est le cas y aura écrit en haut 'vous avez perdu'.  

    '''
    global canvas1
    global s1
    global s2
    global canvas
    canvas1.delete(s1)
    canvas1.delete(s2)
    if score<=Best_score:
        s1 = canvas1.create_text(550, 10, text=str(score), font=("helvetica Neue", 15))
        s2 = canvas1.create_text(550, 40, text=str(Best_score), font=("helvetica Neue", 15))
    else:
        s1 = canvas1.create_text(550, 10, text=str(score), font=("helvetica Neue", 15))
        s2 = canvas1.create_text(550, 40, text=str(score), font=("helvetica Neue", 15))
    for i in range(n):
        for j in range(n):
            rect = canvas.create_rectangle(lrx1[j],lrx1[i],lrx2[j],lrx2[i],width=2, fill =couleur(tablo[i][j]))
    for i in range(n):
        for j in range(n):
            if tablo[i][j] != 0 and  tablo[i][j] <= 2048 :
                texte = canvas.create_text(ltx1[j],lty1[i],text=str(tablo[i][j]),font=("helvetica Neue", 30))
            if tablo[i][j] > 2048:
                texte = canvas.create_text(ltx1[j],lty1[i],text=str(tablo[i][j]),font=("helvetica Neue", 30), fill="#edc22e")
    if defaite(n,tablo)==0:
        with open("score.txt",mode='a',encoding='utf8') as g:
            g.write('\n')
            g.write(str(score))
        b2.destroy()
        b3.destroy()
        text = canvas1.create_text(300, 40, text="Vous avez perdu ", font=("helvetica Neue", 15))    
    return()

lry1=[9,125,245,365,485]
lry2=[115,235,355,475,595]
ltx2=[60,180,300,420,540]
lty2=[60,180,300,420,540]

'''
    La fonction 'rectangle2' va permettre l'affichage de la partie 5x5.
'''

def rectangle2(n,tablo):
    '''
        Nous fesons exactement la même chose que dans 'rectangle1'  mais pour n=5. 
    '''
    global canvas1
    global s1
    global s2
    global canvas
    canvas1.delete(s1)
    canvas1.delete(s2)
    if score<=Best_score:
        s1 = canvas1.create_text(550, 10, text=str(score), font=("helvetica Neue", 15))
        s2 = canvas1.create_text(550, 40, text=str(Best_score), font=("helvetica Neue", 15))
    else:
        s1 = canvas1.create_text(550, 10, text=str(score), font=("helvetica Neue", 15))
        s2 = canvas1.create_text(550, 40, text=str(score), font=("helvetica Neue", 15))
    for i in range(n):
        for j in range(n):
            rect = canvas.create_rectangle(lry1[j],lry1[i],lry2[j],lry2[i],width=2, fill =couleur(tablo[i][j]))
    for i in range(n):
        for j in range(n):
            if tablo[i][j] != 0 and  tablo[i][j] <= 2048 :
                texte = canvas.create_text(ltx2[j],lty2[i],text=str(tablo[i][j]),font=("helvetica Neue", 30))
            if tablo[i][j] > 2048:
                texte = canvas.create_text(ltx2[j],lty2[i],text=str(tablo[i][j]),font=("helvetica Neue", 30), fill="#edc22e")
    if defaite(n,tablo)==0:
        with open("score.txt",mode='a',encoding='utf8') as g:
            g.write('\n')
            g.write(str(score))
        b2.destroy()
        b3.destroy()
        text = canvas1.create_text(300, 40, text="Vous avez perdu ", font=("helvetica Neue", 15))
    return()

####################### Enregistrer et quitter
'''
    La fonction 'enregistrer' sert à enregister la partie en cours lorsque nous cliquons sur le bouton 'enregistrer et quitter'.
'''
def enregistrer():
    '''
        Nous regardons si nous avons une valeur qui vaut 2048 ou plus, si c'est le cas v vaut 1 (ceci est utile pour le programme sur le terminal et non ici ).
        Nous enregistrons la valeur du score dans le fichier 'score.txt'.
        Nous enregistrons la valeur de n, le score et le tableau dans le fichier 'tablo_memoire.txt'.

    '''
    global n
    global tablo
    global v
    for i in range(n):
        for j in range(n):
            if tablo[i][j]>=2048:
                v = 1
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
    return(window.destroy()) 

###################### Quitter sans sauvegarder

'''
    La fonction 'enregistrer2' est utilisée lorsque nous cliquons sur le bouton 'quitter sans sauvegarder'
    et lorsque nous perdons une partie. 
'''
def enregistrer2():
    '''
        Nous enregistrons la valeur du score dans le fichier 'score.txt'.
    '''
    global n 
    global tablo
    with open("score.txt",mode='a',encoding='utf8') as g:
        g.write('\n')
        g.write(str(score))
    return(window.destroy())

##############################  couleur

'''
    La fonction' couleur' sert à donner des couleurs dans les carrés en fonction des valeurs.
'''
def couleur(k):
    if k == 0:
        return("#bbada0")
    if k == 2:
        return("#eee4da")
    if k == 4:
        return("#ede0c8")
    if k == 8:
        return("#f2b179")
    if k == 16:
        return("#f59563")
    if k == 32:
        return("#f67c5f")
    if k == 64:
        return("#f65e3b")
    if k == 128:
        return("#edcf72")
    if k == 256:
        return("#edcc61")
    if k == 512:
        return("#edc850")
    if k == 1024:
        return("#edc53f")
    if k == 2048:
        return("#edc22e")
    else :
        return("black")

################################# défaite
'''
    La fonction défaite permet de savoir si on a perdu ou pas, 
    elle renvoie 0 si on a perdu.  
'''
def defaite(n,tablo):
    '''
        Nous regardons si nous avons pas de 0 dans le tableau, s'il y en a, nous renvoyons 1 pour dire que nous avons pas perdu. 
        Nous comparons ensuite les valeurs pour voir si nous avons pas de valeur côte à côte qui ont la même valeur, 
        si nous avons des valeurs côte à côte qui ont la même valeur nous renvoyons 1 également. 
    '''
    a=0
    for i in range(n):
        for j in range(n):
            if tablo[i][j]==0:
                a=1
                return(a)
    for i in range(n-1):
        for j in range(n-1):
            if tablo[i][j] == tablo[i][j+1] or tablo[i][j] == tablo[i+1][j]:
                a=1
                return(a)
    for i in range(n-1):
        if tablo[n-1][i]==tablo[n-1][i+1]:
            a=1
            return(a)
    for i in range(n-1):
        if tablo[i][n-1]==tablo[i+1][n-1]:
            a=1
            return(a)
    return(a)

##################################### déplacement vers la gauche
'''
    L'ensemble de ces fonctions vont permettre de se déplacer à gauche lorsque nous cliquons sur la flèche gauche.
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

def deplacement_gauche_clavier(event):
    '''
        Nous mettons en mémoire le tableau.
        Nous appliquons le deplacement gauche au tableau.
        Nous comparons avec celle que nous avons mit en mémoire:
        - si c'est pas le même, nous rajoutons une valeur parmi les 0 et nous renvouons vers les fonctions 'rectangle1' ou 'rectangle2' 
        en fonction de la valeur de n.
        - si c'est le même, nous renvoyons vers les fonctions 'rectangle1' ou 'rectangle2' en fonction de n. 

    '''
    global n 
    global tablo
    tablo1=tablo[:]
    tablo = deplacement_gauche(n,tablo)
    if tablo!=tablo1:
        ajout(tablo)
    if n==4:
        rectangle1(n,tablo)
    else:
        rectangle2(n,tablo)
    
#######################################  déplacement vers la droite
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

def deplacement_droit_clavier(event):
    global n 
    global tablo
    tablo1=tablo[:]
    tablo = deplacement_droite(n,tablo)
    if tablo!=tablo1:
        ajout(tablo)
    if n==4:
        rectangle1(n,tablo)
    else:
        rectangle2(n,tablo)    

######################################  déplacement vers le haut
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

def deplacement_haut_clavier(event):
    global n 
    global tablo
    tablo1=tablo[:]
    tablo = deplacement_haut(n,tablo)
    if tablo!=tablo1:
        ajout(tablo)
    if n==4:
        rectangle1(n,tablo)
    else:
        rectangle2(n,tablo)

#####################################   déplacement vers le bas
'''
    L'ensemble de ces fonctions vont permettre de se deplacer en bas lorsque nous cliquons sur la fleche bas.
'''
def deplacement_bas(n,tablo):
    tablo = transformation(n,tablo)
    tablo = deplacement_droite(n,tablo)
    tablo = transformation(n,tablo)
    return(tablo)

def deplacement_bas_clavier(event):
    global n 
    global tablo
    tablo1=tablo[:]
    tablo = deplacement_bas(n,tablo)
    if tablo!=tablo1:
        ajout(tablo)
    if n==4:
        rectangle1(n,tablo)
    else:
        rectangle2(n,tablo)

############################## exécution

choixmode()

'''
    Permet au code de comprendre quoi faire lorsque nous cliquons sur les flèches.
'''
window.bind("<Left>",deplacement_gauche_clavier)
window.bind("<Up>",deplacement_haut_clavier)
window.bind("<Down>",deplacement_bas_clavier)
window.bind("<Right>",deplacement_droit_clavier)


window.mainloop() 