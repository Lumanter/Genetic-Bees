import pygame

pygame.font.init()
font_flower = pygame.font.Font('segoe.ttf', 10)
font_header = pygame.font.Font('segoe.ttf', 30)
font_body = pygame.font.Font('segoe.ttf', 19)

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