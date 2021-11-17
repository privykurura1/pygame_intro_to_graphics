import pygame

pygame.init()

# define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

PI = 3.141592653

size = (400, 500)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Eng Privy's cool game")

# Loop until the user clicks close button

done = False
clock = pygame.time.Clock()

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done == True
    screen.fill(WHITE)
    
    pygame.draw.line(screen, GREEN, [0, 0], [100, 100],5)
    
    for y_offset in range(0, 100, 10):
        pygame.draw.line(screen, RED, [0, 10 + y_offset], [100, 110 + y_offset],5)
        
    pygame.draw.rect(screen, BLACK, [20, 20, 250, 100],2)
    
    pygame.draw.ellipse(screen, BLACK, [20, 20, 250, 100],2)
    
    pygame.draw.arc(screen, BLACK, [20, 220, 250, 200], 0, PI / 2, 2)
    pygame.draw.arc(screen, GREEN, [20, 220, 250, 200], PI / 2, PI, 2)
    pygame.draw.arc(screen, BLUE, [20, 220, 250, 200], PI, 3 * PI / 2, 2)
    pygame.draw.arc(screen, BLACK, [20, 220, 250, 200], 3 * PI / 2, 2 * PI, 2)
    
    pygame.draw.polygon(screen, BLACK, [[100, 100], [0, 200], [200,200]],5)
    
    font = pygame.font.SysFont('calibri', 25, True, False)
    
    text = font.render("My best", True, BLACK)
    
    screen.blit(text, [250, 250])
    
    pygame.display.flip()
    
    clock.tick(60)
    
pygame.quit()
    
    
    

    
    