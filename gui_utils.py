from gui_consts import font_body
from bee import *
from gui_consts import *
import pygame


def draw_bee_stats(win, bee, x, y):
    line_spacing = 20
    stats_text_color = (250, 250, 250)
    stats_txt = [(font_body.render('original genes:           ' + bee.non_mutated_genes, True, stats_text_color))]
    stats_txt.append(font_body.render('mutated genes:          ' + ''.join(str(gene) for gene in bee.genes()), True, stats_text_color))
    stats_txt.append(font_body.render('fitness:                         {}'.format(bee.fitness), True, stats_text_color))
    stats_txt.append(font_body.render('favorite direction:       ' + str_dirs[bee.fav_dir], True, stats_text_color))
    stats_txt.append(font_body.render('favorite color:             ' + rgb_name(bee.fav_color), True, stats_text_color))
    stats_txt.append(font_body.render('deviation angle:         {}°'.format(bee.deviation_angle), True, stats_text_color))
    stats_txt.append(font_body.render('search radius:             {}'.format(bee.search_radius), True, stats_text_color))
    stats_txt.append(font_body.render('search strategy:          {}'.format(str_search_strategies[bee.search_strategy]), True, stats_text_color))
    stats_txt.append(font_body.render('starts at honeycomb: {}'.format(bee.honeycomb_start), True, stats_text_color))
    stats_txt.append(font_body.render('pollinated flowers:     {}'.format(len(bee.pollinated_flowers)), True, stats_text_color))
    stats_txt.append(font_body.render('search distance:         {}'.format(int(bee.traveled_distance)), True, stats_text_color))
    stats_txt.append(font_body.render('is mutant:                   {}'.format(bee.is_mutant), True, stats_text_color))
    stats_txt.append(font_body.render('has parents:               {}'.format(bee.parents is not None), True, stats_text_color))
    for i, txt in enumerate(stats_txt):
        win.blit(txt, (x, y+line_spacing*i))


def convert_flower_generations_for_display(flower_generations):
    for flower_gen in flower_generations:  # convert flowers to display
        for i, flower in enumerate(flower_gen):
            x = grid_x_offset + grid_cell_size * flower.x + random.randint(0, 3)
            y = grid_y_offset + grid_cell_size * flower.y - grid_cell_size + random.randint(0, 3)
            pos = (x, y)
            color = [255 * bit for bit in flower.color]
            flower_txt = font_flower.render('✿', True, color)
            flower_gen[i] = (pos, flower_txt)
