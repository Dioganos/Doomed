import pygame as pg
import os
DOOM_konum = os.path.expanduser('~/Doomed/DOOM')

class Sound:
    def __init__(self, game):
        self.game = game
        pg.mixer.init()
        self.path = DOOM_konum+'/resources/sound/'
        self.crowbar = pg.mixer.Sound(self.path + 'cbar_miss1.wav')
        self.crowbar.set_volume(0.5)
        self.hitsound = pg.mixer.Sound(self.path + 'cbar_hitbod1.wav')
        self.hitsound.set_volume(0.2)
        self.npc_pain = pg.mixer.Sound(self.path + 'npc_pain.wav')
        self.npc_pain.set_volume(0.2)
        self.npc_death = pg.mixer.Sound(self.path + 'npc_death.wav')
        self.npc_death.set_volume(0.2)
        self.npc_shot = pg.mixer.Sound(self.path + 'npc_attack.wav')
        self.npc_shot.set_volume(0.2)
        self.player_pain = pg.mixer.Sound(self.path + 'player_pain.wav')
        self.player_pain.set_volume(0.2)
        self.theme = pg.mixer.music.load(self.path + 'theme.mp3')
        pg.mixer.music.set_volume(0.2)