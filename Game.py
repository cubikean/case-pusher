from __future__ import absolute_import, division, print_function
from itertools import cycle
import os
import pygame
import time
import sys
from pygame.locals import *
from tkinter import*

"""
 author: 
 date:
 version:
"""
pygame.init()
# Recupère la taille de votre écran
width = pygame.display.Info().current_w
height = pygame.display.Info().current_h

# Importation des sons
sonP = pygame.mixer.Sound('son/G.wav')
sonV = pygame.mixer.Sound('son/exit.wav')

# Importation des images pour les differents élements
image_wall = pygame.image.load('image/Wall.jpg')
image_block = pygame.image.load('image/box42x42.png')
image_end = pygame.image.load('image/end.jpg')
image_perso = pygame.image.load('image/perso.jpg')

# Couleurs
blank = (0,0,155)                                    
black = (0,0,0)

# Font police
arial_font = pygame.font.Font("font/font.otf",40)        
arial_font2 = pygame.font.Font("font/font.otf",98)

def jeu():
    st = time.time()# start timer
        
    # Les maps.

    level1 =  [
            "WWWWWWWWWWWWWWWWWWWWWWWWWWWW",
            "WP   O O   W          W    W",
            "W  W W      O WWWWW W W WW W",
            "WO WWW WO  W     W OW  O W W",
            "W OW   W   WWW W W  WOWWWW W",
            "W  W  OW  O W  W W     W WWW",
            "WO WWW    WWWW   WWWW  W O W",
            "W   O   O  O WW  O  OW    WW",
            "WWWWWWWOOWWWWWWWWWO W  O O W",
            "W  W  W  W   W W W OWWW WWWW",
            "W OWW W  W  WW   WO W   O  W",
            "W  O  W  O  WEWW W OW  W   W",
            "WWWW  O  WWWW  W    O  WWW W",
            "W    W   W     O W     W   W",
            "WWWWWWWWWWWWWWWWWWWWWWWWWWWW",
            ]
    
       
    level2 = [
            "WWWWWWWWWWWWWWWWWWWWWWWWWWWW",
            "WPW   W  W  W   O  W   W   W",
            "W W W WW WW WWWWW  WWW W W W",
            "W W W W  O  W      W O  Ow W",
            "W   O  O  O    WWWO    W O W",
            "WWWWWW  WWWW   W   W   W   W",
            "W  W    W  W  O    W WOW W W",
            "W  W OWWW  WOO WWWWW W WOW W",
            "W  W  O   OW         WOW W W",
            "WO O WWWWWWWWWWWWWWWWW W O W",
            "W  WWW     W    W  W O WW WW",
            "W  WW O  O EWW OW OW   W O W",
            "WO    OWWWWWO   OO    O    W",
            "W  W O         W O O O W O W",
            "WWWWWWWWWWWWWWWWWWWWWWWWWWWW",
            ]
    level3 = [
            "WWWWWWWWWWWWWWWWWWWWWWWWWWWW",
            "WP  O   OO W   W W W   W   W",
            "W   O O  OWW WWW   WWWWWW  W",
            "WO WWWWO  O OO W  WW O  W  W",
            "W  WO  O    OWWWW O  W  O  W",
            "W WWW  WWWW O O  O   WO WWWW",
            "WO OWOO   W W O   O  W     W",
            "W O W   O W O WWW WWWWWO O W",
            "W O WWW WWW O W WWW O W    W",
            "WO  O W O W   W W O   WWWOOW",
            "WWW  OWO  WWWWW W   OOW O  W",
            "W W O  O WW O    O W  W   OW",
            "W W   WWWW O WWW O W OW O  W",
            "W  O  W   O   EW   W  O    W",
            "WWWWWWWWWWWWWWWWWWWWWWWWWWWW",
            ]
      

            
    def select(niveau): #choix des niveaux
        choix_niv.destroy()        
            
        class Player(object):
             
            def __init__(self):
                self.rect = pygame.Rect(45, 45, 45, 45)  # position initial du joueur(carre blanc)
           
            def move(self, dx, dy):
                if dx != 0:
                    self.move_single_axis(dx, 0)
                if dy != 0: 
                    self.move_single_axis(0, dy)                   
            """
            Fonction collision entre blocks
            dx : la position x 
            dy : la position y          
            """
            
            def move_single_axis(self, dx, dy):
                
                # deplacement du rectangle
                self.rect.x += dx
                self.rect.y += dy

                # If you collide with a wall, move out based on velocity
                for wall in walls:
                    if self.rect.colliderect(wall.rect):
                        if dx > 0:                               # Moving right; Hit the left side of the wall
                            self.rect.right = wall.rect.left
                        if dx < 0:                               # Moving left; Hit the right side of the wall
                            self.rect.left = wall.rect.right
                        if dy > 0:                               # Moving down; Hit the top side of the wall
                            self.rect.bottom = wall.rect.top
                        if dy < 0:                               # Moving up; Hit the bottom side of the wall
                            self.rect.top = wall.rect.bottom

                for block in blocks:
                    if self.rect.colliderect(block.rect):
                        
                        if dx > 0:      
                            block.move(45, 0)                    # mouvement du block déplaçable à droite
                        if dx < 0: 
                            block.move(-45, 0)                   # mouvement du block déplaçable à gauche
                        if dy > 0: 
                            block.move(0, 45)                    # mouvement du block déplaçable en haut
                        if dy < 0: 
                            block.move(0, -45)                   # mouvement du block déplaçable en bas

                

        #-------------------------------------------------------------Fin de "class Player"--------------------------------------------------------------------------#
                            
        # Fonction creation Wall
        class Wall(object):
            
            def __init__(self, pos):
                walls.append(self)
                self.rect = pygame.Rect(pos[0], pos[1], 45, 45)

        #--------------------------------------------------------------Fin de "class Wall"----------------------------------------------------------------------------#
                
        
        # Fonction creation Block 
        class Block(object):
            
            def __init__(self, pos):
                blocks.append(self)
                self.rect = pygame.Rect(pos[0], pos[1], 45, 45)

            def move(self, dx, dy):
                    
                    # Move each axis separately. Note that this checks for collisions both times.
                    if dx != 0:
                        self.move_single_axis(dx, 0)
                    if dy != 0:
                        self.move_single_axis(0, dy)
                        
            def move_single_axis(self, dx, dy):
                
                # Move the rect
                self.rect.x += dx
                self.rect.y += dy

        #----------------------------------------------------------------Fin de "class Block"-------------------------------------------------------------------------#
                
        # Initialise pygame
        pygame.init()
  
        # Initialisation des variables
        pygame.display.set_caption("Atteindre le carré vert !") # Nom de la fenêtre
        screen = pygame.display.set_mode((width, height))       # Taille de l'écran
        walls = []                                              # Liste walls
        blocks =[]                                              # Liste blocks
        player = Player()                                       # player
        pygame.key.set_repeat(400,30)                           # Avance en continue si la touche déplacement est True
        compteur = 0                                            # Nombre de déplacements
                
        # Analyser le level et crée les blocks correspondants. W = Wall, E = exit, O = Movable block
        x = y = 0
        for i in niveau:
            for j in i:
                if j == "W":                                    # création du block mur
                    Wall((x, y))
                    
                if j =="O":                                     # création du block déplaçable
                    Block((x,y))
                    
                if j == "E":                                    # création du block sortie
                    end_rect = pygame.Rect(x, y, 45, 45)
                x += 45
            y += 45
            x = 0

        def Convers(a): #Fonction qui converti les maps "level1 level12 level13" en tableau [[ ]]
            l=[0]*len(a[0])
            for i in range(len(a)):
                l[i]=[]*len(a[0])
                for j in range(len(a[i])):    
                    l[i].append(a[i][j])
            v = l.count(0)
            x =0
            while x < v:           
                l.remove(0)
                x+=1  
            return l
        
        def Mur(a): #Recupère les positions des murs dans le tableau
            lisMur = []
            for i in range(len(a)):
                for j in range(len(a[i])):
                    if a[i][j] == "W":
                        lisMur.append((i,j))
            return lisMur

        def Caisse(a): #Recupère les positions des caisses dans le tableau
            lisCaisse = []
            for i in range(len(a)):
                for j in range(len(a[i])):
                    if a[i][j] == "O":
                        lisCaisse.append((i,j))
            return lisCaisse

        def Player(a): #Recupère la position du joueur dans le tableau
            lisPlayer = []
            for i in range(len(a)):
                for j in range(len(a[i])):
                    if a[i][j] == "P":
                        lisPlayer.append((i,j))
            return lisPlayer[0]

        carte = Convers(niveau)
        mur = Mur(carte)
        joueur = Player(carte)
        caisse = Caisse(carte)     

        continuer = True
        while continuer: 
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    continuer=0       
                elif event.type==pygame.KEYDOWN:
                    
                    if event.key==K_LEFT: # deplacement du personnage à gauche
                        
                        dr = [0,-1]
                        if (joueur[0]+dr[0],joueur[1]+dr[1]) not in mur: # Condiction qui permet de faire les colisions
                            if (joueur[0]+dr[0],joueur[1]+dr[1]) in caisse:
                                if (joueur[0]+dr[0]+dr[0],joueur[1]+dr[1]+dr[1]) not in caisse:
                                    if (joueur[0]+dr[0]+dr[0],joueur[1]+dr[1]+dr[1]) not in mur:
                                        carte[joueur[0]][joueur[1]]= " "
                                        carte[joueur[0]+dr[0]][joueur[1]+dr[1]] = "P"
                                        carte[joueur[0]+dr[0]+dr[0]][joueur[1]+dr[1]+dr[1]] = "O"
                                        caisse.remove((joueur[0]+dr[0],joueur[1]+dr[1]))
                                        caisse.append((joueur[0]+dr[0]+dr[0],joueur[1]+dr[1]+dr[1]))
                                        joueur = (joueur[0]+dr[0],joueur[1]+dr[1])
                                        player.move(-45, 0)
                                        sonP.play()
                                        compteur = compteur + 1 # incrementation du compteur
                                        
                            else:
                                carte[joueur[0]][joueur[1]]= " "
                                carte[joueur[0]+dr[0]][joueur[1]+dr[1]] = "P"
                                joueur = (joueur[0]+dr[0],joueur[1]+dr[1])
                                player.move(-45, 0)
                                sonP.play()
                                compteur = compteur + 1
                                                 
                    if event.key==K_RIGHT:  # deplacement du personnage à droite
                        
                        dr = [0,1]
                        if (joueur[0]+dr[0],joueur[1]+dr[1]) not in mur:
                            if (joueur[0]+dr[0],joueur[1]+dr[1]) in caisse:
                                if (joueur[0]+dr[0]+dr[0],joueur[1]+dr[1]+dr[1]) not in caisse:
                                    if (joueur[0]+dr[0]+dr[0],joueur[1]+dr[1]+dr[1]) not in mur:
                                        carte[joueur[0]][joueur[1]]= " "
                                        carte[joueur[0]+dr[0]][joueur[1]+dr[1]] = "P"
                                        carte[joueur[0]+dr[0]+dr[0]][joueur[1]+dr[1]+dr[1]] = "O"
                                        caisse.remove((joueur[0]+dr[0],joueur[1]+dr[1]))
                                        caisse.append((joueur[0]+dr[0]+dr[0],joueur[1]+dr[1]+dr[1]))
                                        joueur = (joueur[0]+dr[0],joueur[1]+dr[1])
                                        player.move(45, 0)
                                        sonP.play()
                                        compteur = compteur + 1
                                        
                            else:
                                carte[joueur[0]][joueur[1]]= " "
                                carte[joueur[0]+dr[0]][joueur[1]+dr[1]] = "P"
                                joueur = (joueur[0]+dr[0],joueur[1]+dr[1])
                                player.move(45, 0)
                                sonP.play()
                                compteur = compteur + 1                

                    if event.key==K_UP:  # deplacement du personnage en haut
                        
                        dr = [-1,0]
                        if (joueur[0]+dr[0],joueur[1]+dr[1]) not in mur:
                            if (joueur[0]+dr[0],joueur[1]+dr[1]) in caisse:
                                if (joueur[0]+dr[0]+dr[0],joueur[1]+dr[1]+dr[1]) not in caisse:
                                    if (joueur[0]+dr[0]+dr[0],joueur[1]+dr[1]+dr[1]) not in mur:
                                        carte[joueur[0]][joueur[1]]= " "
                                        carte[joueur[0]+dr[0]][joueur[1]+dr[1]] = "P"
                                        carte[joueur[0]+dr[0]+dr[0]][joueur[1]+dr[1]+dr[1]] = "O"
                                        caisse.remove((joueur[0]+dr[0],joueur[1]+dr[1]))
                                        caisse.append((joueur[0]+dr[0]+dr[0],joueur[1]+dr[1]+dr[1]))
                                        joueur = (joueur[0]+dr[0],joueur[1]+dr[1])
                                        player.move(0, -45)
                                        sonP.play()
                                        compteur = compteur + 1
                                        
                            else:
                                carte[joueur[0]][joueur[1]]= " "
                                carte[joueur[0]+dr[0]][joueur[1]+dr[1]] = "P"
                                joueur = (joueur[0]+dr[0],joueur[1]+dr[1])
                                player.move(0, -45)
                                sonP.play()
                                compteur = compteur + 1
                                                 
                    if event.key==K_DOWN: # deplacement du personnage en bas
                        
                        dr = [1,0]
                        if (joueur[0]+dr[0],joueur[1]+dr[1]) not in mur:
                            if (joueur[0]+dr[0],joueur[1]+dr[1]) in caisse:
                                if (joueur[0]+dr[0]+dr[0],joueur[1]+dr[1]+dr[1]) not in caisse:
                                    if (joueur[0]+dr[0]+dr[0],joueur[1]+dr[1]+dr[1]) not in mur:
                                        carte[joueur[0]][joueur[1]]= " "
                                        carte[joueur[0]+dr[0]][joueur[1]+dr[1]] = "P"
                                        carte[joueur[0]+dr[0]+dr[0]][joueur[1]+dr[1]+dr[1]] = "O"
                                        caisse.remove((joueur[0]+dr[0],joueur[1]+dr[1]))
                                        caisse.append((joueur[0]+dr[0]+dr[0],joueur[1]+dr[1]+dr[1]))
                                        joueur = (joueur[0]+dr[0],joueur[1]+dr[1])
                                        player.move(0, 45)
                                        sonP.play()
                                        compteur = compteur + 1
                            else:
                                carte[joueur[0]][joueur[1]]= " "
                                carte[joueur[0]+dr[0]][joueur[1]+dr[1]] = "P"
                                joueur = (joueur[0]+dr[0],joueur[1]+dr[1])
                                player.move(0, 45)
                                sonP.play()
                                compteur = compteur + 1 
                    
                    if event.key==K_q: # quiter le jeu
                        quitter = Tk()
                        quitter.title('Case-Pusher')
                        
                        def delete():
                            pygame.quit()
                            sys.exit()

                        quitter_text = Label(quitter, text="Voulez vous quitter ?")
                        boutonN = Button(quitter, text="NON", width=20, bd=10, bg='Skyblue2', activeforeground='red' , fg='red' , command=quitter.destroy)
                        boutonY = Button(quitter, text="OUI", width=20, bd=10, bg='Skyblue2', activeforeground='red' , fg='red' ,command=delete)
                        quitter_text.pack()                     # Affichage texte
                        boutonY.pack()                          # Affichage bouton
                        boutonN.pack()                          # Affichage bouton
                        quitter.mainloop()     
                    
                    if event.key==K_r:                          # retour à la selection du niveau
                        jeu()
                        
                    if event.key==K_a:                          # aide pour le joueur
                        aide = Tk()
                        aide.title('Case-Pusher')
                        def aide1():
                            reponse.pack()
                        def aide2():
                            reponse2.pack()
                        def aide3():
                            reponse3.pack()
                            
                        titre = Label(aide, text='Quel aide voulez vous ?')
                        niv1 = Button(aide, text='Aide du niveau 1',width=20, bd=10, bg='Skyblue2', activeforeground='red' , fg='red' ,command=aide1)       # Creation bouton
                        niv2 = Button(aide, text='Aide du niveau 2',width=20, bd=10, bg='Skyblue2', activeforeground='red' , fg='red' ,command=aide2)       # Creation bouton
                        niv3 = Button(aide, text='Aide du niveau 3',width=20, bd=10, bg='Skyblue2', activeforeground='red' , fg='red' ,command=aide3)       # Creation bouton
                        reponse=Label(aide, text="aide niv 1")
                        reponse2=Label(aide, text="aide niv 2")
                        reponse3=Label(aide, text="aide niv 3")
                        titre.pack()                            # Affichage texte
                        niv1.pack()                             # Affichage bouton
                        niv2.pack()                             # Affichage bouton
                        niv3.pack()                             # Affichage bouton
                        aide.mainloop()
                        
                    if event.key==K_i:                          # affichage but du jeu
                        jeu_tk = Tk()
                        jeu_tk.title('Case-Pusher')
                        titre = Button(jeu_tk, text='BUT DU JEU : Vous devez aller au carré vert en poussant ou non les caisses', width=70 ,font="Verdana 19 bold", height=3, bd=10, bg='Skyblue2', activeforeground='red' , fg='red' ,command=jeu_tk.destroy) #Creation text
                        titre.pack()
                        jeu_tk.mainloop()

                # check la collision avec le carré vert pour la sortie
                if player.rect.colliderect(end_rect):
                    sonV.play()
                    compteur = compteur - 1                     # prise en compte du déplacement pour aller au carré vert
                    affichage_time_big = arial_font2.render('Temps : '+str(ftt)+str('  s'),True,blank)   # affichage du timer             
                    affichage = arial_font2.render('Déplacements : '+str(compteur),True,blank)          # affichage du compteur    
                    pygame.draw.rect(screen,black,(150,140,950,420))   # creation d'un écran noir
                    screen.blit(affichage,[190,400])            # placement du compteur de fin 
                    screen.blit(affichage_time_big,[310,200])   # placement du timer de fin 
                    pygame.time.delay(700)                      # delay 700ms 
                    pygame.display.flip()                       # actualisation de la fenetre                 
                    replay = Tk()
                
                    def yes():
                        replay.destroy()
                        jeu()
                        
                    def no():
                        pygame.quit()
                        sys.exit()

                        
                    titre = Label(replay, text='voulez vous rejouer')
                    titre.pack()
                    yes = Button(replay, text='oui', width=20, bd=10, bg='Skyblue2', activeforeground='red' , fg='red' ,command=yes) # Creation bouton
                    no = Button(replay, text='non', width=20, bd=10, bg='Skyblue2', activeforeground='red' , fg='red' ,command=no)   # Creation bouton
                    yes.pack()                                  # Affichage bouton
                    no.pack()                                   # Affichage bouton
                    replay.mainloop()
                #------------------------------------------------------------Fin du  for----------------------------------------------------------------------------------#
            
            # Draw the scene
            screen.fill((0, 0, 0))
            
            #image_floor = pygame.image.load('floor.png')
            
            for wall in walls:
                screen.blit(image_wall, wall.rect)              # wall sprite 
                
            for block in blocks:
                screen.blit(image_block, block.rect)            # block sprite
                
            screen.blit(image_end, end_rect)                    # end sprite
            screen.blit(image_perso, player.rect)               # player sprite

            ft = (time.time() - st)                             # timer 
            ftt = round(ft,2)                                   # round timer
            
            affichage = arial_font.render('Déplacements : '+str(compteur),True,blank)        # affichage du compteur
            affichage_time = arial_font.render('Temps : '+str(ftt),True,blank)
            pygame.draw.rect(screen,black,(200,4,375,39))
            pygame.draw.rect(screen,black,(790,4,300,39))
            screen.blit(affichage,[210,-4])                     # placement du compteur
            screen.blit(affichage_time,[800,-4])               # placement du timer
            
            pygame.display.flip()                               # actualisation de la fenetre
            
        #------------------------------------------------------------Fin de la boucle-----------------------------------------------------------------------------------#


    #----------------------------------------------------------------Fin de "def select"--------------------------------------------------------------------------------#


    choix_niv = Tk()
    choix_niv.title('Case-Pusher')                              # Nom da la fenetre


    # Definition des images du niveau
    image_niv1 = PhotoImage(file="image/niveau1.png")           
    image_niv2 = PhotoImage(file="image/niveau2.png")
    image_niv3 = PhotoImage(file="image/niveau3.png")
    
    titre = Label(choix_niv , text='Quel niveau voulez vous ?',font="Verdana 19 bold", height=3,)                                                                                            # Definition du titre
    bouton1 = Button(choix_niv, text='niveau 1', width=200, image=image_niv1, compound = BOTTOM ,bd=10, bg='Skyblue2' , fg='red' ,font="Verdana 12 bold" ,command=lambda: select(level1))     # appel du niveau 1
    bouton2 = Button(choix_niv, text='niveau 2', width=200, image=image_niv2, compound = BOTTOM ,bd=10, bg='Skyblue2',  fg='red' ,font="Verdana 12 bold" ,command=lambda: select(level2))     # appel du niveau 2
    bouton3 = Button(choix_niv, text='niveau 3', width=200, image=image_niv3, compound = BOTTOM ,bd=10, bg='Skyblue2',  fg='red' ,font="Verdana 12 bold" ,command=lambda: select(level3))     # appel du niveau 3

    titre.pack()
    bouton1.pack(side=LEFT)                                     # Affichage bouton à gauche
    bouton2.pack(side=LEFT)                                     # Affichage bouton à gauche         # Disposition des boutons en ligne 
    bouton3.pack(side=LEFT)                                     # Affichage bouton à gauche
    
    
    choix_niv.mainloop()     
        
#--------------------------------------------------------------------Fin de "def jeu"--------------------------------------------------------------------------------#      
jeu()


