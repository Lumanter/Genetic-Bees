from bee_genetic import *
from search import *
from gui_consts import *
from gui_utils import *
import os
import pygame


flower_generations, bee_generations, goal_fitness_reached = run_genetic_generations()
display_flowers = to_display_flowers(flower_generations)

os.environ['SDL_VIDEO_CENTERED'] = '1' # center window
win = pygame.display.set_mode((1400, 950))
pygame.display.set_caption('Genetic Bees')

gen_number = len(bee_generations) - 1
bee_number = 0
view_pollinated_flowers = False
for i, bees in enumerate(bee_generations): # set gen_number to best fitness gen
    if (avg_fitness(bee_generations[i]) > avg_fitness(bee_generations[gen_number])):
        gen_number = i

selected_bee = bee_generations[gen_number][bee_number]
parent_bee = selected_bee


def redraw_window():
    win.fill((175, 175, 175))
    dark_grey = (80, 80, 80)
    white = (250, 250, 250)

    gen_number_txt = font_header.render('← generation #{} →'.format(gen_number + 1), True, dark_grey)
    win.blit(gen_number_txt, (grid_x_offset + 350, grid_y_offset - 43))

    average_fitness_txt = font_header.render('average fitness: {}'.format(avg_fitness(bee_generations[gen_number])), True, dark_grey)
    win.blit(average_fitness_txt, (120, 0))

    goal_fitness_txt = font_body.render('goal {} reached: {}'.format(goal_avg_gen_fitness, goal_fitness_reached), True, dark_grey)
    win.blit(goal_fitness_txt, (140, 40))

    bee_number_txt = font_header.render('↑ bee #{} ↓'.format(bee_number + 1), True, white)
    win.blit(bee_number_txt, (190, 80))

    parent_bee_txt = font_header.render('parent bee', True, white)
    win.blit(parent_bee_txt, (170, 420))

    parent_bee_options = ['left parent             - key Q', 'right parent          - key E','reset parent          - key R', 'first gen                - key S', 'last gen                - key W', 'show pollination - SPACE']
    for i, option in enumerate(parent_bee_options):
        win.blit(font_body.render(option, True, dark_grey), (50, 750+30*i))

    draw_bee_stats(win, selected_bee, 30, 120)
    if parent_bee != selected_bee:
        draw_bee_stats(win, parent_bee, 30, 460)

    for cell_rect in grid: # draw flower grid
        pygame.draw.rect(win, (160, 160, 160), cell_rect, 1)

    for flower_circle in display_flowers[gen_number]: # draw flowers
        pos, flower_txt = flower_circle
        win.blit(flower_txt, pos)
    pygame.display.update()


run = True
while run:
    redraw_window()

    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q and parent_bee.parents: # events to change bee parent
                parent_bee = parent_bee.parents[0]
            if event.key == pygame.K_e and parent_bee.parents:
                parent_bee = parent_bee.parents[1]
            if event.key == pygame.K_w:
                gen_number = len(bee_generations)-1
            if event.key == pygame.K_s:
                gen_number = 0
            if event.key == pygame.K_SPACE:
                view_pollinated_flowers = not view_pollinated_flowers
                display_flowers = to_display_flowers(flower_generations, view_pollinated_flowers)



    key_pressed = pygame.key.get_pressed() # arrow events to change generation and bee
    if key_pressed[pygame.K_UP]:
        bee_number -= 1
        bee_number = 0 if (bee_number < 0) else bee_number
    if key_pressed[pygame.K_DOWN]:
        bee_number += 1
        bee_number = (bee_population - 1) if (bee_number == bee_population) else bee_number

    if key_pressed[pygame.K_LEFT]:
        gen_number -= 1
        gen_number = 0 if (gen_number < 0) else gen_number
    if key_pressed[pygame.K_RIGHT]:
        gen_number += 1
        gen_number = (len(bee_generations)-1) if (gen_number == len(bee_generations)) else gen_number

    if key_pressed[pygame.K_DOWN] or key_pressed[pygame.K_UP] or key_pressed[pygame.K_LEFT] or key_pressed[pygame.K_RIGHT] or key_pressed[pygame.K_r] or key_pressed[pygame.K_w] or key_pressed[pygame.K_s]:
        selected_bee = bee_generations[gen_number][bee_number]
        parent_bee = selected_bee

