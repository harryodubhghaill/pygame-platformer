level_map = [
'                            ',
'                            ',
'                            ',
' XX    XXX            XX    ',
' XX P                       ',
' XXXX         XX         XX ',
' XXXX       XX              ',
' XX    X  XXXX    XX  XX    ',
'       X  XXXX    XX  XXX   ',
'    XXXX  XXXXXX  XX  XXXX  ',
'XXXXXXXX  XXXXXX  XX  XXXX  ']

tile_size = 64

screen_width = 1600
screen_height = tile_size * len(level_map)

screen_limit_right = screen_width - (screen_width * 0.15)
screen_limit_left = screen_width * 0.15
