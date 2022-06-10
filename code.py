#!/usr/bin/env python3

# Created by Paterry Baptichon
# Created on 2022-06-09

import stage
import ugame

def game_scene():
    # this funciton is the main game scene

    # image banks for circuit python
    image_bank_background = stage.Bank.from_bmp16("space_aliens_background.bmp")

    # set background to imgae 0 in the image bank
    # and the size (10x8 tiles of size 16x16)
    background = stage.Grid(image_bank_background, 10, 8)

    # set frame rate to 60 fps
    game = stage.Stage(ugame.display, 60)

    # set the layter of all sprites to show up in order
    game.layers = [background]

    # render all sprites
    # most likely will only render background once per game scnece
    game.render_block()

     # repeat forever, game loop
    while True:
        pass

if __name__=="__main__":
    game_scene()
