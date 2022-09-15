# Game flappy bird
import pygame
import sys
import random
from pygame.constants import USEREVENT


# Tạo hàm cho trò chơi

def draw_floor():
    screen.blit(floor, (floor_x_pos, 650))
    screen.blit(floor, (floor_x_pos + 432, 650))


def create_pipe():
    random_pipe_pos = random.choice(pipe_height)
    bottom_pipe = pipe_surface.get_rect(midtop=(500, random_pipe_pos))
    top_pipe = pipe_surface.get_rect(
        midtop=(500, random_pipe_pos - 750))  # 650 thì hơi khó qua
    return bottom_pipe, top_pipe


def move_pipe(pipes):
    for pipe in pipes:
        pipe.centerx -= 5
    return pipes


def draw_pipe(pipes):
    for pipe in pipes:
        if pipe.bottom >= 650:
            screen.blit(pipe_surface, pipe)
        else:
            flip_pipe = pygame.transform.flip(pipe_surface, False, True)
            screen.blit(flip_pipe, pipe)


def check_collision(pipes):
    for pipe in pipes:
        if bird_rect.colliderect(pipe):
            hit_sound.play()
            return False
    if bird_rect.top <= -75 or bird_rect.bottom >= 650:
        die_sound.play()
        return False
    return True


def rotate_bird(bird1):
    new_bird = pygame.transform.rotozoom(bird1, -bird_movement*3, 1)
    return new_bird


def bird_animation():
    new_bird = bird_list[bird_index]
    new_bird_rect = new_bird.get_rect(center=(100, bird_rect.centery))
    return new_bird, new_bird_rect


def score_display(game_stage):
    if game_stage == "main game":
        score_surface = game_font.render(
            str(int(score)), True, (255, 255, 255))
        score_rect = score_surface.get_rect(center=(216, 100))
        screen.blit(score_surface, score_rect)
    if game_stage == "game_over":
        score_surface = game_font.render(
            f"Score: {int(score)}", True, (255, 255, 255))
        score_rect = score_surface.get_rect(center=(216, 100))
        screen.blit(score_surface, score_rect)

        high_score_surface = game_font.render(
            f"High Score: {int(high_score)}", True, (255, 255, 255))
        high_score_rect = high_score_surface.get_rect(center=(216, 630))
        screen.blit(high_score_surface, high_score_rect)


def update_score(score, high_score):
    if score > high_score:
        high_score = score
    return high_score


pygame.mixer.pre_init(frequency=44100, size=-16, channels=2, buffer=512)
pygame.init()
screen = pygame.display.set_mode((400, 700))  # 432, 768
pygame.display.set_caption("Flappy Bird")
clock = pygame.time.Clock()
game_font = pygame.font.Font(
    "D:\\Test\\Game\\FalppyBird\\FileGame\\04B_19.ttf", 40)


# Tạo các biến cho trò chơi
gravity = 0.25
bird_movement = 0
game_active = True
score = 0
high_score = 0


# Chèn background
bg = pygame.image.load(
    "D:\\Test\\Game\\FalppyBird\\FileGame\\assets\\background-night.png").convert()
bg = pygame.transform.scale2x(bg)


# Chèn sàn
floor = pygame.image.load(
    "D:\\Test\\Game\\FalppyBird\\FileGame\\assets\\floor.png").convert()
floor = pygame.transform.scale2x(floor)
floor_x_pos = 0


# Tạo chim
bird_down = pygame.transform.scale2x(pygame.image.load(
    "D:\\Test\\Game\\FalppyBird\\FileGame\\assets\\yellowbird-downflap.png").convert_alpha())
bird_mid = pygame.transform.scale2x(pygame.image.load(
    "D:\\Test\\Game\\FalppyBird\\FileGame\\assets\\yellowbird-midflap.png").convert_alpha())
bird_up = pygame.transform.scale2x(pygame.image.load(
    "D:\\Test\\Game\\FalppyBird\\FileGame\\assets\\yellowbird-upflap.png").convert_alpha())
bird_list = [bird_down, bird_mid, bird_up]
bird_index = 0
bird = bird_list[bird_index]
bird_rect = bird.get_rect(center=(100, 384))


# Tạo timer cho chim
birdflap = pygame.USEREVENT + 1
pygame.time.set_timer(birdflap, 200)


# Tạo ống
pipe_surface = pygame.image.load(
    "D:\\Test\\Game\\FalppyBird\\FileGame\\assets\\pipe-green.png").convert()
pipe_surface = pygame.transform.scale2x(pipe_surface)
pipe_list = []


# Tạo timer
spawnpipe = pygame.USEREVENT
pygame.time.set_timer(spawnpipe, 1200)
pipe_height = [200, 300, 400]


# Tạo màn hình kết thúc
game_over_surface = pygame.transform.scale2x(pygame.image.load(
    "D:\\Test\\Game\\FalppyBird\\FileGame\\assets\\message.png").convert_alpha())
gmae_over_rect = game_over_surface.get_rect(center=(216, 384))


# Chèn âm thanh
flap_sound = pygame.mixer.Sound(
    "D:\\Test\\Game\\FalppyBird\\FileGame\\sound\\sfx_wing.wav")
hit_sound = pygame.mixer.Sound(
    "D:\\Test\\Game\\FalppyBird\\FileGame\\sound\\sfx_hit.wav")
score_sound = pygame.mixer.Sound(
    "D:\\Test\\Game\\FalppyBird\\FileGame\\sound\\sfx_point.wav")
die_sound = pygame.mixer.Sound(
    "D:\\Test\\Game\\FalppyBird\\FileGame\\sound\\sfx_die.wav")
score_sound_countdown = 100


# Vòng lập của trò chơi
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and game_active:
                bird_movement = 0
                bird_movement = - 11
                flap_sound.play()
            if event.key == pygame.K_SPACE and game_active == False:
                game_active = True
                pipe_list.clear()
                bird_rect.center = (100, 384)
                bird_movement = 0
                score = 0
        if event.type == spawnpipe:
            pipe_list.extend(create_pipe())
        if event.type == birdflap:
            if bird_index < 2:
                bird_index += 1
            else:
                bird_index = 0
            bird, bird_rect = bird_animation()
    screen.blit(bg, (0, 0))
    if game_active:

        # Hành động của chim
        bird_movement += gravity
        rotated_bird = rotate_bird(bird)
        bird_rect.centery += bird_movement
        screen.blit(rotated_bird, bird_rect)
        game_active = check_collision(pipe_list)

        # Hành động của ống
        pipe_list = move_pipe(pipe_list)
        draw_pipe(pipe_list)
        score += 0.01
        score_display("main game")
        score_sound_countdown -= 1
        if score_sound_countdown <= 0:
            score_sound.play()
            score_sound_countdown = 100
    else:
        screen.blit(game_over_surface, gmae_over_rect)
        high_score = update_score(score, high_score)
        score_display("game_over")

    # Hành động của sàn
    floor_x_pos -= 1
    draw_floor()
    if floor_x_pos <= -432:
        floor_x_pos = 0
    pygame.display.update()
    clock.tick(120)