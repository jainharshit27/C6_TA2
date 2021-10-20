import pygame

pygame.init()

screen = pygame.display.set_mode((1200, 400))

#Create a variable game_state and assign value "play" to it.

score = 0
score_font = pygame.font.Font("freesansbold.ttf", 16)

dino_rect = pygame.Rect(100, 250, 64, 64)
cactus_rect = pygame.Rect(1100, 300, 32, 32)
ground_rect = pygame.Rect(0, 330, 1200, 2)

dino_y_change = 0

while True:
    screen.fill((255, 255, 255))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            
        #Add play state here. Indent the following 6 lines. This will make the keys work for gameplay.
        if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    dino_y_change = -1
        if event.type == pygame.KEYUP:
                if event.key == pygame.K_SPACE:
                    dino_y_change = 1
        
        #Add the over state code block here. This will make the keys run for restarting the game.
            #if event.type == pygame.KEYDOWN:
                #if event.key == pygame.K_SPACE:
                    #Reset game_state = "play"
                    #Reset cactus_rect.x = 1200
                    #Reset score = 0
                    #Reset dino_y_change = 1
    
    #Add play game_state. Indent the next 22 lines. This will ensure that the code indented in this block runs only when game is in play state.
    dino_rect.y += dino_y_change
    if dino_rect.y > 250:
        dino_rect.y = 250
    if dino_rect.y < 100:
        dino_rect.y = 100
    
    cactus_rect.x = cactus_rect.x - 1
    if cactus_rect.x <= -30:
        cactus_rect.x = 1200
    
    score += 1
    show_score = round(score/100)
    score_show = score_font.render("Score: " + str(show_score), True, (0, 0, 0))
    screen.blit(score_show, (10, 10))   
    
    pygame.draw.rect(screen, (100, 100, 100), dino_rect)
    pygame.draw.rect(screen, (100, 100, 100), cactus_rect)
    pygame.draw.rect(screen, (100, 100, 100), ground_rect)
    
    if dino_rect.colliderect(cactus_rect):
        pygame.time.delay(2000)
        pygame.quit()   #Change this line to set game_state to over.
        
    #Add the over state code block here. This will ensure that the code indented in this block runs only when game is in over state.
        #pygame.time.delay(500)
        #game_state = "over"
    
    pygame.display.update()
    
    
    
    
    
