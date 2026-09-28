import pygame
import random


pygame.init()


WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Neon Racer - Pro")


DARK_BG = (10, 10, 20)
ROAD_COLOR = (30, 30, 40)
NEON_YELLOW = (255, 230, 0)
NEON_CYAN = (0, 255, 255)
NEON_PINK = (255, 20, 147)
WHITE = (255, 255, 255)
RED = (255, 50, 50)
BLUE = (0, 150, 255)

lane = 1
score = 0
speed = 7
lanes = [280, 400, 520]

traffic = []
spawn_timer = 0
game_over = False

clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 45)
large_font = pygame.font.SysFont(None, 70)

running = True
while running:
    screen.fill(ROAD_COLOR)
    
    
    pygame.draw.line(screen, NEON_CYAN, (200, 0), (200, HEIGHT), 6)
    pygame.draw.line(screen, NEON_CYAN, (600, 0), (600, HEIGHT), 6)
     
    pygame.draw.line(screen, NEON_YELLOW, (340, 0), (340, HEIGHT), 4)
    pygame.draw.line(screen, NEON_YELLOW, (460, 0), (460, HEIGHT), 4)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
          
        if event.type == pygame.KEYDOWN:
            if game_over and event.key == pygame.K_SPACE:
                game_over = False
                score = 0
                speed = 7
                traffic.clear()
                lane = 1

    if not game_over:
        
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and lane > 0:
            lane -= 1
            pygame.time.delay(120)
        if keys[pygame.K_RIGHT] and lane < 2:
            lane += 1
            pygame.time.delay(120)

        player_x = lanes[lane]
        player_y = 450
        player_rect = pygame.Rect(player_x, player_y, 50, 90)

        
        spawn_timer += 1
        if spawn_timer > 35:
            spawn_timer = 0
            enemy_lane = random.randint(0, 2)
            traffic.append(pygame.Rect(lanes[enemy_lane], -100, 50, 90))

        
        for car in traffic[:]:
            car.y += speed
            
 
            pygame.draw.rect(screen, RED, car, border_radius=10)
        
        
        
            if car.y > HEIGHT:
                traffic.remove(car)
                
             
            if player_rect.colliderect(car):
                game_over = True

 
        pygame.draw.rect(screen, BLUE, player_rect, border_radius=10)
         
        pygame.draw.rect(screen, NEON_PINK, (player_x + 10, player_y + 30, 30, 30), border_radius=5)

 
        score += int(speed)

         
        score_text = font.render(f"Score: {score}", True, WHITE)
        screen.blit(score_text, (20, 20))

    else:
        
        overlay = pygame.Surface((WIDTH, HEIGHT))
        overlay.set_alpha(180)
        overlay.fill(DARK_BG)
        screen.blit(overlay, (0, 0))

      
        over_text = large_font.render("GAME OVER", True, RED)
        final_score_text = font.render(f"Final Score: {score}", True, WHITE)
        restart_text = font.render("Press SPACE to Restart", True, NEON_YELLOW)

        screen.blit(over_text, (WIDTH // 2 - 140, HEIGHT // 2 - 80))
        screen.blit(final_score_text, (WIDTH // 2 - 110, HEIGHT // 2 - 10))
        screen.blit(restart_text, (WIDTH // 2 - 160, HEIGHT // 2 + 50))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()