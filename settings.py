# level_map = [
# '                            ',
# '                            ',
# '                            ',
# ' XX    XXX            XX    ',
# ' XX P                       ',
# ' XXXX         XX         XX ',
# ' XXXX       XX              ',
# ' XX    X  XXXX    XX  XX    ',
# '       X  XXXX    XX  XXX   ',
# '    XXXX  XXXXXX  XX  XXXX  ',
# 'XXXXXXXX  XXXXXX  XX  XXXX  ']

tile_size = 64
vertical_tile_number = 11 #from tiled data

screen_width = 1600
screen_height = tile_size * vertical_tile_number

screen_limit_right = screen_width - (screen_width * 0.15)
screen_limit_left = screen_width * 0.15
