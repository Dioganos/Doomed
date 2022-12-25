from sprite_object import *
import os
DOOM_konum = os.path.expanduser('~/Doomed/DOOM')

class Weapon(AnimatedSprite):
    def __init__(self, game, path=DOOM_konum+'/resources/sprites/weapon/crowbar/0.png', scale=1, animation_time=90):
        super().__init__(game=game, path=path, scale=scale, animation_time=animation_time)
        self.images = deque(
            [pg.transform.smoothscale(img, (self.image.get_width() * scale, self.image.get_height() * scale))
             for img in self.images])
        self.weapon_pos = (HALF_WIDTH * 1.58 - self.images[0].get_width() // 2, HEIGHT - self.images[0].get_height())
        self.shooting = False
        self.num_images = len(self.images)
        self.frame_counter = 0
        self.damage = 100

    def animate_shot(self):
        if self.shooting:
            self.game.player.shot = False
            if self.animation_trigger:
                self.images.rotate(-1)
                self.image = self.images[0]
                self.frame_counter += 1
                if self.frame_counter == self.num_images:
                    self.shooting = False
                    self.frame_counter = 0

    def draw(self):
        self.game.screen.blit(self.images[0], self.weapon_pos)

    def update(self):
        self.check_animation_time()
        self.animate_shot()