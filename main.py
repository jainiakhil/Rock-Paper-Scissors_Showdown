# -*- coding: utf-8 -*-
"""
Created on Fri Dec 23 14:41:22 2022

@author: Akhil Jaini

Rock Paper Scissors Simulator
A Pygame-based battle royale simulation where Rock, Paper, and Scissors autonomous entities collision-convert each other until one faction conquers the arena!
"""

import pygame
import random
import math
import time
import os

# Base directory for loading assets reliably
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ASSET_DIR = os.path.join(BASE_DIR, "assets")

def get_asset_path(filename):
    return os.path.join(ASSET_DIR, filename)

# Initializing the pygame module
pygame.init()
pygame.font.init()

# Defining window size
WIDTH, HEIGHT = 800, 800

# Defining colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Defining frame rate
FPS = 200

# Defining number of participants per faction
NUM = 20

# Initializing window
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Rock Paper Scissors Simulator")

# Defining font
FONT = pygame.font.SysFont("Calibri", 50)

def blit_text_center(win, font, text):
    render = font.render(text, 1, BLACK)
    win.blit(render, (win.get_width()/2 - render.get_width()/2,
                      win.get_height()/2 - render.get_height()/2))
    pygame.display.update()

# Scaling image assets
def scale_image(img, factor):
    size = round(img.get_width() * factor), round(img.get_height() * factor)
    return pygame.transform.scale(img, size)

# Initializing surfaces and objects
RING = scale_image(pygame.image.load(get_asset_path("ring.jpg")), 0.5)
RING_BORDER = scale_image(pygame.image.load(get_asset_path("ring_border_2_bg.png")), 0.5)
RING_BORDER_MASK = pygame.mask.from_surface(RING_BORDER)

OLYMPICS = scale_image(pygame.image.load(get_asset_path("olympics_tr.png")), 0.3)

ROCK = scale_image(pygame.image.load(get_asset_path("rock.png")), 0.08); ROCK.set_colorkey(WHITE)
PAPER = scale_image(pygame.image.load(get_asset_path("paper.png")), 0.08); PAPER.set_colorkey(WHITE)
SCISSORS = scale_image(pygame.image.load(get_asset_path("scissors.png")), 0.08)

# Defining attributes for objects
class RPS:
    VEL = 0.7
    
    def __init__(self, start_pos):
        self.img = self.IMG
        self.vel = self.VEL
        self.x, self.y = start_pos
        self.width = self.img.get_width()
        self.height = self.img.get_height()
        
    def draw(self, win):
        win.blit(self.img, (self.x, self.y))
    
    def move(self):
        radians = random.uniform(0, 2*math.pi)
            
        horizontal = math.cos(radians) * self.VEL
        vertical = math.sin(radians) * self.VEL
        
        self.y -= vertical
        self.x -= horizontal
        
    def attract(self, obj):
        radians = math.atan2(self.y - obj.y, self.x - obj.x)
        horizontal = math.cos(radians) * self.vel
        vertical = math.sin(radians) * self.vel
        
        self.y -= vertical
        self.x -= horizontal
        
    def repel(self, obj):
        radians = math.atan2(self.y - obj.y, self.x - obj.x)
        horizontal = math.cos(radians) * self.vel
        vertical = math.sin(radians) * self.vel
        
        self.y += vertical
        self.x += horizontal
    
    def collide(self, obj):
        if not (obj.x <= self.x + self.width and obj.x >= self.x):
            return False
        if not (obj.y <= self.y + self.height and obj.y >= self.y):
            return False
        
        return True

    def bounce(self):
        self.vel = -self.vel
        self.move()
        
    def speedup(self, obj):
        self.vel = self.VEL + (NUM - min(NUM, len(obj))) * 0.1
    
    def reset(self, start_pos):
        self.x, self.y = start_pos
        
class Rock(RPS):
    IMG = ROCK

class Paper(RPS):
    IMG = PAPER
    
class Scissor(RPS):
    IMG = SCISSORS

# Drawing on screen
def draw(win, images, rocks, papers, scissors):
    for img, pos in images:
        win.blit(img, pos)
    
    for _, rock in enumerate(rocks):
        rock.draw(WIN)
    for _, paper in enumerate(papers):
        paper.draw(WIN)
    for _, scissor in enumerate(scissors):
        scissor.draw(WIN)
    
    pygame.display.update()

# Main event loop
if __name__ == "__main__":   
    run = True
    clock = pygame.time.Clock()
    
    images = [(RING, (0,0)), (RING_BORDER, (0,0)), (OLYMPICS, (WIN.get_width()/2 - OLYMPICS.get_width()/2, 
                                                               WIN.get_height()/2 - OLYMPICS.get_height()/2))]
    
    rocks = []
    papers = []
    scissors = []
    
    # Adding objects to the scene
    for _ in range(NUM):
        rocks.append(Rock((random.randint(130,350),random.randint(130,350))))
        papers.append(Paper((random.randint(450,630),random.randint(130,400))))
        scissors.append(Scissor((random.randint(300,500),random.randint(450,630))))
    
    start = time.time()
    z1, z2, z3 = True, True, True
    
    while run:
        clock.tick(FPS)
        
        draw(WIN, images, rocks, papers, scissors)
        
        rocks_del = []
        papers_del = []
        scissors_del = []
        
        # Moving objects and detecting collisions
        for rock in rocks:
            rock.move(); rock.speedup(rocks)
            if len(scissors):
                rock.attract(scissors[random.randint(0,len(scissors)-1)])
            if len(papers):
                rock.repel(papers[random.randint(0,len(papers)-1)])    
            if rock.x < 130 or rock.x > 630 or rock.y < 130 or rock.y > 630:
                rock_k = rocks[random.randint(0,len(rocks)-1)]
                rock.x, rock.y = rock_k.x, rock_k.y
                rock.bounce()
            
            for i in range(len(scissors)):
                if rock.collide(scissors[i]):
                    scissors_del.append(scissors[i])
                           
        for paper in papers:
            paper.move(); paper.speedup(papers)
            if len(rocks):
                paper.attract(rocks[random.randint(0,len(rocks)-1)])
            if len(scissors):
                paper.repel(scissors[random.randint(0,len(scissors)-1)])
            if paper.x < 130 or paper.x > 630 or paper.y < 130 or paper.y > 630:
                paper_k = papers[random.randint(0,len(papers)-1)]
                paper.x, paper.y = paper_k.x, paper_k.y
                paper.bounce()
               
            for i in range(len(rocks)):
                if paper.collide(rocks[i]):
                    rocks_del.append(rocks[i])
   
        for scissor in scissors:
            scissor.move(); scissor.speedup(scissors)
            if len(papers):
                scissor.attract(papers[random.randint(0,len(papers)-1)])
            if len(rocks):
                scissor.repel(rocks[random.randint(0,len(rocks)-1)])
            if scissor.x < 130 or scissor.x > 630 or scissor.y < 130 or scissor.y > 630:
                scissor_k = scissors[random.randint(0,len(scissors)-1)]
                scissor.x, scissor.y = scissor_k.x, scissor_k.y
                scissor.bounce()
        
            for i in range(len(papers)):
                if scissor.collide(papers[i]):
                    papers_del.append(papers[i])
                    
        # Converting objects upon collision
        for j in range(len(rocks_del)):
            try:
                papers.append(Paper((rocks[j].x, rocks[j].y)))
                rocks.remove(rocks[j])
            except IndexError:
                print("Rock IndexError"); break
            
        for j in range(len(papers_del)):
            try:
                scissors.append(Scissor((papers[j].x, papers[j].y)))
                papers.remove(papers[j])
            except IndexError:
                print("Paper IndexError"); break
            
        for j in range(len(scissors_del)):
            try:
                rocks.append(Rock((scissors[j].x, scissors[j].y)))
                scissors.remove(scissors[j])
            except IndexError:
                print("Scissor IndexError"); break
        
        # Counting time
        if len(rocks) == 0 and z1 == True:
            rock_stop = time.time() - start
            z1 = False
            print(f"Rocks lasted for {rock_stop:.2f} seconds only")
        if len(papers) == 0 and z2 == True:
            paper_stop = time.time() - start
            z2 = False
            print(f"Paper lasted for {paper_stop:.2f} seconds only")
        if len(scissors) == 0 and z3 == True:
            scissors_stop = time.time() - start
            z3 = False
            print(f"Scissors lasted for {scissors_stop:.2f} seconds only")
         
        # Declaring winner
        if len(papers) == 0 and len(scissors) == 0:
            run = False
            print("Rocks won!")
            blit_text_center(WIN, FONT, "ROCKS WON!")
            time.sleep(3)
        elif len(rocks) == 0 and len(scissors) == 0:
            run = False
            print("Papers won!")
            blit_text_center(WIN, FONT, "PAPERS WON!")
            time.sleep(3)
        elif len(rocks) == 0 and len(papers) == 0:
            run = False
            print("Scissors won!")
            blit_text_center(WIN, FONT, "SCISSORS WON!")
            time.sleep(3)
        
        for event in pygame.event.get():            
            # Quit application using escape key
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN 
                                             and event.key == pygame.K_ESCAPE):
                run = False
                print("Rock Paper Scissors Simulator exited successfully!")
                
    pygame.quit()
