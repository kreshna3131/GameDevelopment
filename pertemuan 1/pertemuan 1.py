import random
import pygame

class DrawDemo:
    def do_draw_demo():
        init_result = pygame.init()
        if init_result[1] != 0:
            print('pygame not installed properly')
            return
        
        width = 800
        height = 600
        size = (width,height)
        
        def get_random_coordinate():
            X = random.randint(0, width-1)
            Y = random.randint(0, height-1)
            return (X,Y)
        
        def get_random_color():
            red = random.randint(0,255)
            green = random.randint(0,255)
            blue = random.randint(0,255)
            return (red, green, blue)
        
        surface = pygame.display.set_mode(size)
        pygame.display.set_caption("Drawing Example")
        
        red = (255,0,0)
        green = (0,255,0)
        blue = (0,0,255)
        black = (0,0,0)
        yellow = (255,255,0)
        magenta = (255,0,255)
        cyan = (0,255,255)
        white = (255,255,255)
        gray = (128,128,128)
        
        surface.fill(white)
        
        for count in range(100):
            start = get_random_coordinate()
            end = get_random_coordinate()
            color = get_random_color()
            pygame.draw.line(surface, color, start, end)
            
        dot_radius = 10
        for count in range(100):
            pos = get_random_coordinate()
            color = get_random_color()
            radius = random.randint(5,50)
            pygame.draw.circle(surface, color, pos, radius)
            
        pygame.display.flip()
        
DrawDemo.do_draw_demo()