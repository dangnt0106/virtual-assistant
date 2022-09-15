from operator import index, truediv
from pgzero.screen import Screen
#import pygame
import pgzrun
import random


#pygame.mixer.pre_init(frequency=44100, size=-16, channels=2, buffer=512)
#pygame.init()

FONT_COLOR = (255, 255, 255) #màu RGB
WIDTH = 1300
HEIGHT = 700
CENTER_X = WIDTH / 2
CENTER_Y = HEIGHT / 2
CENTER = (CENTER_X, CENTER_Y)
START_SPEED = 10
COLORS =["D:\\Test\\Game\\AmongUs\\images\\orange","D:\\Test\\Game\\AmongUs\\images\\blue"]


current_level = 1
final_level = 5
game_over = False
game_complete = False
impostors = []
animations = []

#score_sound = pygame.mixer.Sound("D:\\Test\\Game\\AmongUs\\sound\\sfx_point.wav")
#die_sound = pygame.mixer.Sound("D:\\Test\\Game\\AmongUs\\sound\\sfx_hit.wav")

def draw():
    global impostors, current_level, game_over, game_complete
    screen.clear()
    screen.blit("D:\\Test\\Game\\AmongUs\\images\\dark.jpg",(0,0))
    if game_over:
        display_message("Game Over", "Press Space to play again")
    elif game_complete:
        display_message("You Won", "Press Space to play again")
    else:
        for im in impostors:
            im.draw()
 

def update():
    global impostors, current_level, game_over, game_complete
    if len(impostors) == 0:
        impostors = make_impostors(current_level)
    if (game_over or game_complete) and keyboard.space:
        impostors = []
        current_level = 1
        game_complete = False
        game_over = False


def make_impostors(number_of_impostors):
    colors_to_create = get_colors_to_create(number_of_impostors)
    new_impostors = create_impostors(colors_to_create)
    layout_impostors(new_impostors)
    animate_impostors(new_impostors)
    return new_impostors


def get_colors_to_create(number_of_impostors):
    colors_to_create = ["D:\\Test\\Game\\AmongUs\\images\\red"]
    for i in range(0,number_of_impostors):
        random_color = random.choice(COLORS)
        colors_to_create.append(random_color)
    return colors_to_create


def create_impostors(colors_to_create):
    new_impostors = []
    for color in colors_to_create:
        impostor = Actor(color + "-im.png")
        new_impostors.append(impostor)
    return new_impostors


def layout_impostors(impostors_to_layout):
    number_of_gaps = len(impostors_to_layout) + 1
    gap_size = WIDTH / number_of_gaps
    random.shuffle(impostors_to_layout)
    for index, impostor in enumerate(impostors_to_layout):
        new_x_pos = (index + 1) * gap_size
        impostor.x = new_x_pos


def animate_impostors(impostors_to_animate):
    for impostor in impostors_to_animate:
        duration = START_SPEED - current_level
        impostor.anchor = ("center", "bottom")
        animation = animate(impostor, duration = duration, on_finished = handle_game_over, y = HEIGHT)
        animations.append(animation) 


def handle_game_over():
    global game_over
    game_over = True


def on_mouse_down(pos):
    global impostors, current_level
    for impostor in impostors:
        if impostor.collidepoint(pos):
            if "D:\\Test\\Game\\AmongUs\\images\\red" in impostor.image:
                red_impostor_click()
                #score_sound.play()
            else:
                handle_game_over()
                #die_sound.play()


def red_impostor_click():
    global current_level, impostors, animations, game_complete
    stop_animations(animations)
    if current_level == final_level:
        game_complete = True
    else:
        current_level = current_level + 1
        impostors = []
        animations = []
  

def stop_animations(animations_to_stop):
    for animation in animations_to_stop:
        if animation.running:
            animation.stop()


def display_message(heading_text, sub_heading_text):
    screen.draw.text(heading_text, fontsize = 60, center = CENTER, color = FONT_COLOR)
    screen.draw.text(sub_heading_text, fontsize = 30, center = (CENTER_X, CENTER_Y + 30), color = FONT_COLOR)


pgzrun.go()
