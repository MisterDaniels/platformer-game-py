level_map = [
    '                           ',
    '                           ',
    '                           ',
    'XX   XXX             XX    ',
    'XX P                       ',
    'XXXX       XX            XX',
    'XXXX     XX                ',
    'XX   X  XXXX    XX   XX    ',
    '     X  XXXX    XX   XXX   ',
    '  XXXX  XXXXXX  XX   XXXX  ',
    'XXXXXX  XXXXXX  XX   XXXXXX'
]

tile_size = 64
screen_width = 1200
screen_height = len(level_map) * tile_size

screen_left_limit = (20 * screen_width) / 100
screen_right_limit = (80 * screen_width) / 100