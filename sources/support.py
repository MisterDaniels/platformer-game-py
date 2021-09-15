from os import walk
import pygame

def import_folder(path):
    surface_list = []

    for _, __, img_files in walk(path):
        for img_file in img_files:
            full_path = path + '/' + img_file
            img_surface = pygame.image.load(full_path).convert_alpha()
            surface_list.append(img_surface)

    return surface_list