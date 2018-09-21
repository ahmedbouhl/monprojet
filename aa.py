
import pygame
pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((1250, 1000))
pygame.draw.rect(screen, (10,120,200), pygame.Rect(0, 0, 1250, 1000)) 
carImg = pygame.image.load('/home/ahmed/Images/canvas.png')





done = False
#i= 0
#k=0

col3=(40, 40, 40)

def lire(i):
      f = open("/home/ahmed/test.txt", "r");
      font = pygame.font.SysFont("comicsansms", 23)
      for line in f.readlines():
                
     
                text = font.render(line.rstrip(), True,col3)
     
                screen.blit(text, (10, i*20))
                if line.rstrip() == "Fin":
                         
                         screen.blit(carImg, (0,(i+1)*20)) 
                         i=i+20
                i = i +1
      f.close() 
lire(0)
n= 0
while not done:
        
        for event in pygame.event.get():
               if event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN:
                         pygame.draw.rect(screen, (10,120,200), pygame.Rect(0, 0, 1250, 1000)) 
                         lire(n)
                         n= n-1
                         print n
               if event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
                         pygame.draw.rect(screen, (10,120,220), pygame.Rect(0, 0, 1250, 1000)) 
                         lire(n)
                         n= n+1
               if event.type == pygame.KEYDOWN and event.key == pygame.K_b:
                         pygame.draw.rect(screen,(10,120,220), pygame.Rect(0, 0, 1250, 1000)) 
                         lire(-17)
               if event.type == pygame.KEYDOWN and event.key == pygame.K_a:
                         pygame.draw.rect(screen, (10,122,220), pygame.Rect(0, 0, 1250, 1000)) 
                         lire(-4)
                         n=-4
               if event.type == pygame.KEYDOWN and event.key == pygame.K_c:
                         pygame.draw.rect(screen, (10,122,220), pygame.Rect(0, 0, 1250, 1000)) 
                         lire(-72) 
                         n=-72
               if event.type == pygame.KEYDOWN and event.key == pygame.K_d:
                         pygame.draw.rect(screen, (10,122,220), pygame.Rect(0, 0, 1250, 1000)) 
                         lire(-100) 
                         n=-100           
               if  int(event.type)==12:
                    done =True
               
        pygame.display.flip()







