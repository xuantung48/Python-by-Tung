import pygame, sys, random
pygame.init()

def draw_floor():
    screen.blit(floor, (floor_x_pos, 600))
    screen.blit(floor, (floor_x_pos + 432, 600))

def create_pipe():
    random_pipe = random.choice(pipe_height)
    bottom_pipe = pipe_face.get_rect(midtop = (500, random_pipe))
    top_pipe = pipe_face.get_rect(midtop = (500, random_pipe - 650))
    return bottom_pipe, top_pipe 

def move_pipe(pipes):
    for pipe in pipes:
        pipe.centerx -= 5
    return pipes

def draw_pipe(pipes):
    for pipe in pipes:
        if pipe.bottom >= 768:
            screen.blit(pipe_face, pipe)
        else:
            flip_pipe = pygame.transform.flip(pipe_face, False, True)
            screen.blit(flip_pipe, pipe)

screen = pygame.display.set_mode((432, 768))
clock = pygame.time.Clock()
gravity = 0.25
bird_moverment = 0

bg = pygame.image.load('filegame/background-night.png').convert()
bg = pygame.transform.scale2x(bg)

floor = pygame.image.load('filegame/floor.png').convert()
floor = pygame.transform.scale2x(floor)
floor_x_pos = 0

bird = pygame.image.load('filegame/minhtrang2.png').convert()
bird = pygame.transform.scale2x(bird)
bird_rect = bird.get_rect(center = (100, 384))

pipe_face = pygame.image.load('filegame/pipe-green.png').convert()
pipe_face = pygame.transform.scale2x(pipe_face)
pipe_list = []

#tạo timer:
spawpipe = pygame.USEREVENT 
pygame.time.set_timer(spawpipe, 1200)
pipe_height = [200, 300, 400]

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit() 
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bird_moverment = 0
                bird_moverment = -11
        if event.type == spawpipe:
            pipe_list.extend(create_pipe())

    screen.blit(bg, (0,0))

    bird_moverment += gravity
    bird_rect.centery += bird_moverment
    screen.blit(bird, bird_rect)

    floor_x_pos -= 1
    draw_floor()

    pipe_list = move_pipe(pipe_list)
    draw_pipe(pipe_list)
    if floor_x_pos <= -432:
        floor_x_pos = 0
    pygame.display.update()
    clock.tick(120)