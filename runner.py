# -*- coding: utf-8 -*-
"""
Created on Mon Mar 17 00:04:31 2025

@author: kaosa
"""
#%%%
import os
print(os.getcwd())
#os.chdir('E:\\Python\\OS\\Runner')

#%%%

import pygame as pg
from sys import exit
from random import randint, choice



class Player(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()
        
        player_walk_1 = pg.image.load('E://Python//OS//Runner/graphics/player_walk_1.png').convert_alpha()
        player_walk_2 = pg.image.load('E://Python//OS//Runner/graphics/player_walk_2.png').convert_alpha()
        self.player_index = 0
        self.player_walk = [player_walk_1, player_walk_2]

        self.player_jump = pg.image.load('E://Python//OS//Runner/graphics/jump.png').convert_alpha()
      
        self.image = self.player_walk[self.player_index]
        self.rect = self.image.get_rect(midbottom=(80, 300))
        self.player_duck = pg.transform.rotozoom(self.player_jump, angle=2.0, scale= 0.5)
                                            
        self.gravity = 0
        self.ducked = False
        self.player_duck_offset = 20
        self.jump_sound = pg.mixer.Sound('E://Python//OS//Runner//sound//jump.mp3')
        self.jump_sound.set_volume(0.4)
    
    def player_input(self):
        keys = pg.key.get_pressed()
        
        if keys[pg.K_UP] and self.rect.bottom >= 300:
            self.gravity = -20
            self.jump_sound.play() 
        if keys[pg.K_DOWN]:
            self.ducked = True
            self.jump_sound.play()
        else:
            self.ducked = False
         
    
    def apply_gravity(self):
        self.gravity += 1
        self.rect.y += self.gravity
        if self.rect.bottom >= 300:
            self.rect.bottom = 300
    
    def animation_state(self):
        
        if self.ducked:
            self.image = self.player_duck
            self.rect.y += self.player_duck_offset
        else:
            self.image = self.player_walk[int(self.player_index)]
        
        if self.rect.bottom < 300:
            self.image = self.player_jump
        
        else:
            self.player_index += 0.1
            if self.player_index >= len(self.player_walk):
                self.player_index = 0
            self.image = self.player_walk[int(self.player_index)]
        
        
        
            
    def update(self):
        self.player_input()
        self.apply_gravity()
        self.animation_state()

class Obstacle(pg.sprite.Sprite):
    def __init__(self, type):
        super().__init__()
        
        if type == 'fly':
            fly_1 = pg.image.load('E://Python//OS//Runner/graphics/fly1.png').convert_alpha()
            fly_2 = pg.image.load('E://Python//OS//Runner/graphics/fly2.png').convert_alpha()
            self.frames = [fly_1, fly_2]
            y_pos = 220
        else:
            snail_1 = pg.image.load('E://Python//OS//Runner/graphics/snail1.png').convert_alpha()
            snail_2 = pg.image.load('E://Python//OS//Runner/graphics/snail2.png').convert_alpha()
            self.frames = [snail_1, snail_2]
            y_pos = 300
        
        self.frames[0] = pg.transform.rotozoom(self.frames[0], angle=0, scale=0.7)
        self.frames[1] = pg.transform.rotozoom(self.frames[1], angle=0, scale=0.7)
        self.animation_index = 0
        self.image = self.frames[self.animation_index]
        self.rect = self.image.get_rect(midbottom=(randint(900, 1100), y_pos))
        
        
        
    def animation_state(self):
        self.animation_index += 0.1
        if self.animation_index >= len(self.frames): self.animation_index = 0
        else: self.image = self.frames[int(self.animation_index)]
    def update(self):
        self.animation_state()
        self.rect.x -= 6
        self.destro_obstacle()
    
    def destro_obstacle(self):
        if self.rect.x <= -100:
            self.kill()
    
    
    
    
    
def display_score() -> int:
    t = int((pg.time.get_ticks()-start_time)/100)
    score_surface = font.render(f'Score: {t}', False, (64, 64, 64))
    score_rect = score_surface.get_rect(center=(400, 50))
    screen.blit(score_surface, score_rect)
    return t


def collision():
      if pg.sprite.spritecollide(player.sprite, obstacle, False):
          obstacle.empty()
          return False
      else: return True




pg.init()
screen = pg.display.set_mode((800, 400)) #w:800, h:400
pg.display.set_caption('Runner')
clock = pg.time.Clock()
font = pg.font.Font('E://Python//OS//Runner/font/Pixeltype.ttf', 50)
sky_surface = pg.image.load('E://Python//OS//Runner/graphics/sky.png').convert() #background surface
ground_surface = pg.image.load('E://Python//OS//Runner/graphics/ground.png').convert()
text_surface = font.render('Jump Master Runner', False, (128, 64, 64))
text_rect = text_surface.get_rect(center = (400, 50))
instruction_surface = font.render('Enter press to start', False, (64, 64, 128))
instruction_rect = instruction_surface.get_rect(center = (400, 90))
game_over_surface = font.render('Game Over! Press enter to start again', False, (255, 100, 50))
game_over_rect = game_over_surface.get_rect(center = (400, 70))





player = pg.sprite.GroupSingle()
player.add(Player())

obstacle = pg.sprite.Group() #obstacle is grouped by fly and snails








#intro
player_stand  = pg.image.load('E:/Python/OS/Runner/graphics/player_stand.png').convert_alpha()
player_stand = pg.transform.scale2x(player_stand)
player_stand_rect = player_stand.get_rect(center=(400, 200))


text_rect = text_surface.get_rect(center = (400, 50))




#timer
obstacle_timer = pg.USEREVENT + 1
pg.time.set_timer(obstacle_timer, 1500)

snail_animation_timer = pg.USEREVENT + 2
pg.time.set_timer(snail_animation_timer, 500)

fly_animation_timer = pg.USEREVENT + 3
pg.time.set_timer(fly_animation_timer, 100)

player_gravity = 0
start_time = 0
player_x_pos = 0
score = 0
game_active = False

bg_sound = pg.mixer.Sound('E://Python//OS//Runner/sound/music.wav')
bg_sound.set_volume(0.1)
bg_sound.play(loops=-1)

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            exit()
              
            
          
        else:
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_SPACE:
                    game_active = True
                    start_time = pg.time.get_ticks()
                        
        if game_active:
            if event.type == obstacle_timer:
                obstacle.add(Obstacle(choice(['fly', 'snail', 'snail', 'snail'])))
          
                    
              
    if game_active:
        
        
    
        screen.blit(sky_surface, (0, 0))
        screen.blit(ground_surface, (0, 300))
        
        score = display_score()
        
      
        player.draw(screen)
        player.update()
        
        obstacle.draw(screen)
        obstacle.update()
        
        game_active = collision()
            
            
            
            
    else:
        
        screen.fill((94, 130, 162))
        screen.blit(player_stand, player_stand_rect)
        player_gravity = 0
        score_message = font.render(f'Your Score: {score}', False, (250, 220, 155))
        score_message_rect = score_message.get_rect(center=(400, 330))
     
        
        if score == 0:
            
            screen.blit(text_surface, text_rect)
            screen.blit(instruction_surface, instruction_rect)
        
        else:
            screen.blit(game_over_surface, game_over_rect)
            screen.blit(score_message, score_message_rect)
   
        
    pg.display.update()       
    clock.tick(60)  #60 frame i.e while will execute 60 times in a sec
