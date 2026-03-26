import  pygame
import random
import sys

pygame.init()
# Pantalla
WIDTH=400
HEIGHT=600
pantalla = pygame.display.set_mode((WIDTH,HEIGHT))

#Colores
WHITE = (255,255,255)
GREEN = (0,200,0)
BLUE = (135,206,235)

# Bird
bird_x = 50
bird_y = 300
bird_velocity = 0
gravity = 0.5
jump = -8

# Pipes
pipe_width = 60
pipe_gap = 150
pipes = []

# Score
score = 0
font = pygame.font.SysFont(None, 40)

clock = pygame.time.Clock()

def create_pipe():
    height = random.randint(100, 400)
    top = pygame.Rect(WIDTH, 0, pipe_width, height)
    bottom = pygame.Rect(WIDTH, height + pipe_gap, pipe_width, HEIGHT)
    return top, bottom
pipes.append(create_pipe())

running = True
while running:
    clock.tick(60)
    pantalla.fill(BLUE)

    # Eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bird_velocity = jump

    # Bird physics
    bird_velocity += gravity
    bird_y += bird_velocity

    bird = pygame.Rect(bird_x, bird_y, 30, 30)

    pygame.draw.rect(pantalla, WHITE, bird)

    # Pipes
    for pipe in pipes:
        pipe[0].x -= 3
        pipe[1].x -= 3

        pygame.draw.rect(pantalla, GREEN, pipe[0])
        pygame.draw.rect(pantalla, GREEN, pipe[1])

        # Colisión
        if bird.colliderect(pipe[0]) or bird.colliderect(pipe[1]):
            running = False

    # Añadir pipes
    if pipes[-1][0].x < 200:
        pipes.append(create_pipe())
        score += 1

    # Borrar pipes
    if pipes[0][0].x < -pipe_width:
        pipes.pop(0)

    # Suelo o techo
    if bird_y > HEIGHT or bird_y < 0:
        running = False

    # Score
    text = font.render(f"Score: {score}", True, WHITE)
    pantalla.blit(text, (10,10))

    pygame.display.update()

pygame.quit()
sys.exit()