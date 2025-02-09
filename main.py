import pygame

pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
dt = 0
running = True

PLAYER_SPEED = 300
player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # if screen.fill is not used then it won't refresh the screen
        screen.fill('black')
        clock.tick(60)
        player = pygame.draw.aacircle(screen, "red", player_pos, 40)

        # player controls
        key = pygame.key.get_pressed()
        if key[pygame.K_w]:
            player_pos.y += -PLAYER_SPEED * dt
        if key[pygame.K_a]:
            player_pos.x -= PLAYER_SPEED * dt
        if key[pygame.K_s]:
            player_pos.y += PLAYER_SPEED * dt
        if key[pygame.K_d]:
            player_pos.x += PLAYER_SPEED * dt

        # used to draw everything onto the screen
        pygame.display.flip()

        dt = clock.tick(60) / 1000
pygame.quit()