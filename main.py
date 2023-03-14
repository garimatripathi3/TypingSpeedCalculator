import pygame 
import random
import time
import pygame.font
from pygame.locals import *
import sys
pygame.init()
class Typing:
    def __init__(self):
        self.accuracy = '0'
        self.text_gen = ' '
        self.ty_speed = '0'
        self.typed_text = ' '
        self.start_time = time.time()
        self.start = False

    def generate_text(self):
        text = ["You need that pride in yourself as well as a sense when you are sitting on Page 297 ; of a book that the book is going to be read that somebody   is going to care you cant ever be sure about ; that but you need the sense that its important that its not typing its writing", " Communication is a skill that you can learn its like riding a bicycle or typing if you are willing to work at it you can; rapidly improve the quality of evry part of your life" ]
        self.text_gen = random.choice(text)
        return self.text_gen
    def accuracy_calc(self,text, text1):
        if(len(text1)==0):
           self.accuracy = '0'
          
        else:
            str1 = set(text.split())
            str2 = set(text1.split())
            intersection = str1.intersection(str2)
            self.accuracy = str(len(intersection)/len(str1))*100
        return self.accuracy           
    def speed_calc(self, text):
        end_time = time.time()
        total_time = end_time - self.start_time
        speed_ca = len(text) / total_time* 60
        self.ty_speed = speed_ca
        return self.ty_speed
    def take_test(self):
        Typist.text_gen = Typist.generate_text()
        output_lines = Typist.text_gen.split(';')
        total_line = len(output_lines)
        for i1, lines in enumerate(output_lines):
            line_surface_first = font.render(lines, True,(255,255,255))
            pygame.display.update()
            window.blit(line_surface_first,(100,100+i1*100))
            pygame.display.flip()

        self.start = True
size = (800, 800)
WHITE = (255, 255, 255)
GRAY = (128, 128, 128)


title = "Typing Speed Calculator"
color = (43, 78,103)
border = (233, 222,12)
flag = RESIZABLE | DOUBLEBUF
button = pygame.Rect(250, 200, 150, 50)
window = pygame.display.set_mode(size, flag)
window.fill((72, 61, 139))

pygame.display.set_caption(title)

text2 = pygame.font.Font('freesansbold.ttf', 36).render("Test", True, WHITE)
pygame.display.update()
Typist = Typing()
pygame.display.flip()
font = pygame.font.SysFont("Arial", 32)
running = True
while running:
    
  
    for event in pygame.event.get():
        pygame.display.flip()
        mouse = pygame.mouse.get_pos()
        mouse_pressed = pygame.mouse.get_pressed()
        if event.type == QUIT:
            running = False
        if Typist.start == False:
            pygame.draw.rect(window, (0,0,0), button )
            window.blit(text2, (button.x + 15, button.y + 10))
        elif event.type == VIDEORESIZE:
            size = event.size
            
            window = pygame.display.set_mode(size, flag)
            window.fill((50,100,180))
            if Typist.start == True:
                Typist.take_test()
            
     
        if (time.time() - Typist.start_time) >= 60:
            window.fill((0, 0, 0))
            Typist.speed_calc(Typist.typed_text)
            speed_ans = Typist.ty_speed
            screen = font.render(f"Speed : {speed_ans}",True,(255,255,255))
            pygame.display.update()
            window.blit(screen,(10,10))
            speed_accuracy  = Typist.accuracy_calc(Typist.text_gen, Typist.typed_text)
            screen_2 = font.render(f"Accuracy: {speed_accuracy}", True, (255,255,255))
            pygame.display.update()
            pygame.time.delay(3000)
            window.blit(screen_2, (40,40))
            pygame.draw.rect(window, GRAY, button )
            text2 = pygame.font.Font('freesansbold.ttf', 36).render("Test", True, WHITE)
            pygame.display.update()
            window.blit(text2, (button.x + 15, button.y + 10))
            running = False
        if button.collidepoint(mouse) and mouse_pressed[0] and Typist.start == False:

            window.fill((0, 0, 0))
            window.fill((72, 61, 139))
            running = True
            Typist.take_test()
                  
        elif event.type == pygame.KEYDOWN:

            if event.key == pygame.K_BACKSPACE:
                Typist.typed_text = Typist.typed_text[:-1]
            
            elif  len(Typist.text_gen) <= len(Typist.typed_text):
                window.fill((0, 0, 0))
                Typist.speed_calc(Typist.typed_text)
                speed_ans = Typist.ty_speed
                screen = font.render(f"Speed : {speed_ans}",True,(255,255,255))
                # pygame.display.update()
                window.blit(screen,(10,10))
                speed_accuracy  = Typist.accuracy_calc(Typist.text_gen, Typist.typed_text)
                screen_2 = font.render(f"Accuracy: {speed_accuracy}", True, (255,255,255))
                window.blit(screen_2,(100,100))
                # time.sleep(10)
                # pygame.time.delay(1000)
               
                # pygame.display.update()
            else:
                
                # pygame.display.flip()
                Typist.typed_text+=event.unicode
               
    
  
    input_lines = Typist.typed_text.split('\n')
    total_line = len(input_lines)
    for i, line in enumerate(input_lines):
        line_surface = font.render(line, True,(0, 100, 0))

        # pygame.display.update()
        window.blit(line_surface,(100,100+i*100))

        if running ==False:
            window.fill((0,0,0))
            running= True
        
        pygame.display.flip()
pygame.quit()
       
            



