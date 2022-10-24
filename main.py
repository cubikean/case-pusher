import pygame
import sys
from pygame.locals import *

pygame.init()
clock = pygame.time.Clock()


BLACK  = 0, 0, 0
WHITE  = 255, 255, 255
GRIS  = 169 ,169, 169
GRIS2 = 141, 141, 141

FOND   = pygame.image.load("image/hd2.jpg")
sonB = pygame.mixer.Sound('son/bouton3.wav')
sonJ = pygame.mixer.Sound('son/test.wav')
#sonJ.play()

width = pygame.display.Info().current_w
height = pygame.display.Info().current_h

class Bouton:

    def __init__(self, screen, text, couleur, police , coor_x, coor_y):
        
        self.screen = screen
        self.text = text
        self.couleur = couleur
        self.police = police
        self.coor_x = coor_x
        self.coor_y = coor_y
        self.title = self.police.render(self.text, True, (0,0,0))
        text_taille = self.title.get_rect()
        self.bout_wh = text_taille[2]
        self.bout_ht = text_taille[3]
       

    def clique_bouton(self, police, action=None):

        mouse_xy = pygame.mouse.get_pos()
        au_dessus = self.rect.collidepoint(mouse_xy)
        if au_dessus:
            action()

        self.rect = pygame.draw.rect(self.screen, self.couleur,(self.coor_x - self.bout_wh/2,self.coor_y - self.bout_ht/2,self.bout_wh,self.bout_ht))
        self.screen.blit(self.title, (self.coor_x - self.bout_wh/2 ,self.coor_y - self.bout_ht/2))

    def print_bouton(self, screen):
        self.screen = screen
        self.rect = pygame.draw.rect(self.screen, self.couleur, (self.coor_x - self.bout_wh/2,self.coor_y - self.bout_ht/2,self.bout_wh,self.bout_ht))
        self.screen.blit(self.title, (self.coor_x - self.bout_wh/2 ,self.coor_y - self.bout_ht/2))



class Icone:

    def __init__(self, screen, img , coor_x, coor_y):
        
        self.screen = screen
        self.img = img
        self.coor_x = coor_x
        self.coor_y = coor_y
        icone_taille = self.img.get_size()
        self.ico_wh = icone_taille[0]
        self.ico_ht = icone_taille[1]

    def print_icone(self, screen):
        self.rect = pygame.draw.rect(self.screen, (0,0,0), (self.coor_x,self.coor_y,self.ico_wh,self.ico_ht))
        self.screen.blit(self.img, (self.coor_x,self.coor_y,self.ico_wh,self.ico_ht))

    def clique_icone(self,screen,y,action=None):
        mouse_xy = pygame.mouse.get_pos()
        au_dessus = self.rect.collidepoint(mouse_xy)
        print(action)
        if au_dessus:
                action(self.coor_x,self.coor_y, y)
        
class Game:

    def __init__(self):
        self.screen = pygame.display.set_mode((width, height))
        print(width,height)
        self.loop = True

        self.titanous = pygame.font.Font("font/Mur.ttf", 150)
        self.big = pygame.font.Font("font/Mur.ttf", 60)
        self.small = pygame.font.Font("font/Mur.ttf", 40)

        self.creer_background()
        self.creer_bouton()
        
        self.ff = [0,0,0,0,0,0]

    def update_textes(self):
        self.textes = [["Case Pusher", WHITE, self.titanous, (width/2-1360), 100]]


    def creer_background(self):

        self.background = pygame.image.load("image/hd2.jpg")
        pygame.transform.scale(self.background,(width,height))
        self.fond = self.background.convert()
        

    def creer_bouton(self):
        self.start_bouton = Bouton(self.fond, "   Jouer   ", WHITE, self.big, (width/2),(height/3.6))
        self.quit_bouton  = Bouton(self.fond, "   Quitter   ", WHITE, self.big, (width/2),(height/2.5))
        self.credit_bouton  = Bouton(self.fond, "   Credit   ", WHITE, self.big, (width/2),(height/1.9))
        self.aide_bouton  = Bouton(self.fond, "   Aide   ", WHITE, self.big, (width/2),(height/1.5))
        self.commande_bouton  = Bouton(self.fond, "   Commandes   ", WHITE, self.big, (width/2),(height/1.3))

    def display_text(self, text, color, font, dx, dy):

        mytext = font.render(text, True, color)
        textpos = mytext.get_rect()
        textpos.centerx = self.fond.get_rect().centerx + dx
        textpos.centery = dy
        
        self.fond.blit(mytext, textpos)



    def infinite_loop(self):

        fenetre = pygame.display.set_mode((width, height))
        while self.loop:
            self.creer_background()

            self.start_bouton.print_bouton(self.fond)
            self.quit_bouton.print_bouton(self.fond)
            self.credit_bouton.print_bouton(self.fond)
            self.aide_bouton.print_bouton(self.fond)
            self.commande_bouton.print_bouton(self.fond)
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.start_bouton.clique_bouton(self.fond, action = lancer)
                    self.quit_bouton.clique_bouton(self.fond, action = gamequit)
                    self.credit_bouton.clique_bouton(self.fond, action = credit)
                    self.aide_bouton.clique_bouton(self.fond, action = aide)
                    self.commande_bouton.clique_bouton(self.fond, action = commande)

            self.update_textes()
            for text in self.textes:
                
                self.display_text(text[0], text[1], text[2], text[3], text[4])

            self.screen.blit(self.fond, (0, 0))
            pygame.display.update()
            clock.tick(10)

def gamequit():
    print("Quit")
    pygame.quit()
    sys.exit()


def lancer():
    
    import Game
    Game.jeu()

def text_objects(text, font):
    textSurface = font.render(text, True, BLACK)
    return textSurface, textSurface.get_rect()

def bouton(msg,x,y,w,h,ic,ac,action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(gameDisplay, ac,(x,y,w,h))
        if click[0] == 1 and action != None:
            sonB.play()
            action()
    else:
        pygame.draw.rect(gameDisplay, ic,(x,y,w,h))
    smallText = pygame.font.Font("font/jabjai_light.TTF", 20)
    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = ( (x+(w/2)), (y+(h/2)) )
    gameDisplay.blit(textSurf, textRect)


def credit():
    pygame.init()
    screen = pygame.display.set_mode((width, height))
    myfont = pygame.font.Font(None, 50)    
    text = [myfont.render('Jeu cree par:', True, WHITE),
            myfont.render('- Hugo Chatigny -', True, WHITE),
            myfont.render('- Wendy Alphanor -', True, WHITE),
            myfont.render('- Nikita Manchenko -', True, WHITE),
            myfont.render('- M Li Iman Assoumani -', True, WHITE),
            myfont.render('Jeu intitule -Case Pusher-', True, WHITE),
            myfont.render('L1 Informatique Groupe 5B', True, WHITE),
            myfont.render('En cours de developpement...', True, WHITE)]

    ticks0 = pygame.time.get_ticks()
    while True:
       
        screen.fill(BLACK)
        seconds = int((pygame.time.get_ticks() - ticks0)/2000)
        n_image = seconds%len(text)
        my_image = text[n_image]
        rect = my_image.get_rect()
        rect.center = [width/2, height/2]
        screen.blit(my_image, rect)
        pygame.display.flip()
        
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == MOUSEBUTTONDOWN:
                print("Retour")
                game.infinite_loop()

def aide():
    pygame.init()
    screen = pygame.display.set_mode((width, height))
    myfont = pygame.font.Font(None, 50)    
    text = [myfont.render('Jeu en cours de developpement...', True, WHITE),
            myfont.render(' Veuillez patienter', True, WHITE),
            myfont.render('Disponible le 27/04/20', True, WHITE),
            myfont.render('- Merci !-', True, WHITE)]
           
    ticks0 = pygame.time.get_ticks()
    while True:
        
        screen.fill(BLACK)
        seconds = int((pygame.time.get_ticks() - ticks0)/2000)
        n_image = seconds%len(text)
        my_image = text[n_image]
        rect = my_image.get_rect()
        rect.center = [width/2, height/2]
        screen.blit(my_image, rect)
        pygame.display.flip()
        
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == MOUSEBUTTONDOWN:
                print("Retour")
                game.infinite_loop()

def commande():
    pygame.init()
    screen = pygame.display.set_mode((width, height))
    myfont = pygame.font.Font(None, 50)    
    text = [myfont.render('Commandes:', True, WHITE),
            myfont.render('Déplacement : flèche directionnelle', True, WHITE),
            myfont.render('Touches : ', True, WHITE),
            myfont.render('I : But du jeu', True, WHITE),
            myfont.render('A : Aide', True, WHITE),
            myfont.render('Q : Quitter le jeu', True, WHITE),
            myfont.render('R : Sélection du niveau', True, WHITE)]
    
    ticks0 = pygame.time.get_ticks()
    
    while True:
        
        screen.fill(BLACK)
        seconds = int((pygame.time.get_ticks() - ticks0)/2000)
        n_image = seconds%len(text)
        my_image = text[n_image]
        rect = my_image.get_rect()
        rect.center = [width/2, height/2]
        screen.blit(my_image, rect)
        pygame.display.flip()
        
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == MOUSEBUTTONDOWN:
                print("Retour")
                game.infinite_loop()

        
if __name__ == '__main__':
    game = Game()
    game.infinite_loop()

