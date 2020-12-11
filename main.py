from bee_genetic import *
from flower_genetic import *
from bee import *
from genetic_consts import *
import pygame
import random
import copy


flower_generations = []
bee_generations = []

bees = generate_initial_bees()
flowers = generate_initial_flowers()
generations = 100
for _ in range(generations):
    flower_generations.append(copy.copy(flowers))

    fake_flower_search(bees, flowers)

    bees = fitness_bees(bees)
    bee_generations.append(copy.copy(bees))

    select_bees(bees)
    select_flowers(flowers)

    bees = crossover_bees(bees)
    flowers = crossover_flowers(flowers)

    mutate_bees(bees)
    mutate_flowers(flowers)

    add_missing_bees(bees)
    add_missing_flowers(flowers)


grid_cells = 128
grid_cell_size = 7
grid_x_offset = 480
grid_y_offset = 40
grid = []
for i in range(grid_cells): # create flowers grid
    for j in range(grid_cells):
        x = grid_x_offset + grid_cell_size*i
        y = grid_y_offset + grid_cell_size*j
        cell_rect = (x, y, grid_cell_size, grid_cell_size)
        grid.append(cell_rect)


pygame.font.init()
font_flower = pygame.font.Font('segoe.ttf', 8)
for flower_gen in flower_generations: # convert flowers to circles to display
    for i, flower in enumerate(flower_gen):
        x = grid_x_offset + grid_cell_size*flower.x + random.randint(0, 3)
        y = grid_y_offset + grid_cell_size*flower.y -grid_cell_size + random.randint(0, 3)
        pos = (x, y)
        color = [255*bit for bit in flower.color]
        flower_txt = font_flower.render('✿', True, color)
        flower_gen[i] = (pos, flower_txt)


win = pygame.display.set_mode((1400, 950))
pygame.display.set_caption('Genetic Bees')
clock = pygame.time.Clock() # clock used to refresh the display
gen_number = flower_population - 1
bee_number = 0
font_header = pygame.font.Font('segoe.ttf', 30)
font_flower = pygame.font.Font('segoe.ttf', 10)
font_body = pygame.font.Font('segoe.ttf', 23)


def draw_bee_stats():
    bee_number_txt = font_header.render('↑ bee #{} ↓'.format(bee_number+1), True, (250, 250, 250))
    win.blit(bee_number_txt, (190, 20))

    bee = bee_generations[gen_number][bee_number]

    fav_dir_txt = font_body.render('favorite direction: ' + str_dirs[bee.fav_dir], True, (250, 250, 250))
    win.blit(fav_dir_txt, (30, 70))
    fav_color_txt = font_body.render('favorite color: ' + rgb_name(bee.fav_color), True, (250, 250, 250))
    win.blit(fav_color_txt, (30, 100))
    angle_txt = font_body.render('deviation angle: {}°'.format(bee.deviation_angle), True, (250, 250, 250))
    win.blit(angle_txt, (30, 130))
    radius_txt = font_body.render('search radius: {}'.format(bee.search_radius), True, (250, 250, 250))
    win.blit(radius_txt, (30, 160))
    strategy_txt = font_body.render('search strategy: {}'.format(str_search_strategies[bee.search_strategy]), True, (250, 250, 250))
    win.blit(strategy_txt, (30, 190))
    starts_txt = font_body.render('starts at honeycomb: {}'.format(bee.honeycomb_start), True, (250, 250, 250))
    win.blit(starts_txt, (30, 220))
    flowers_txt = font_body.render('pollinated flowers: {}'.format(len(bee.pollinated_flowers)), True, (250, 250, 250))
    win.blit(flowers_txt, (30, 250))
    distance_txt = font_body.render('search distance: {}'.format(bee.traveled_distance), True, (250, 250, 250))
    win.blit(distance_txt, (30, 280))
    mutant_txt = font_body.render('is mutant: {}'.format(bee.is_mutant), True, (250, 250, 250))
    win.blit(mutant_txt, (30, 310))


def redraw_window():
    win.fill((150, 150, 150))
    draw_bee_stats()

    gen_number_txt = font_header.render('← generation #{} →'.format(gen_number+1), True, (250, 250, 250))
    win.blit(gen_number_txt, (grid_x_offset + 400, grid_y_offset - 40))

    for cell_rect in grid: # draw flower grid
        pygame.draw.rect(win, (160, 160, 160), cell_rect, 1)

    for flower_circle in flower_generations[gen_number]: # draw flowers
        pos, flower_txt = flower_circle
        win.blit(flower_txt, pos)


run = True
while run:
    redraw_window()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

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
        gen_number = (flower_population-1) if (gen_number == flower_population) else gen_number

    pygame.display.update()
    clock.tick(60)
