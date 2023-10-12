import pygame as pg
from random import randrange 

pg.init()

screen_width = 1000
screen_height = 750
TILE_SIZE = 50 #since our map will take the form of a grid we need to define tile sizes
FONT = pg.font.Font("MontserratAlternates-BlackItalic.otf", TILE_SIZE*2)



screen = pg.display.set_mode((screen_width,screen_height))
pg.display.set_caption("Snake game")
clock = pg.time.Clock() #to set the framerate


class Snake:
    def __init__(self):
        self.x = TILE_SIZE
        self.y = TILE_SIZE
        self.xdir = 1 #our snake is gonna be able to move in direction 1 for right, -1 for left (x axis)
        self.ydir = 0 #1 for down, -1 for up (y axis)
        self.head = pg.Rect(self.x,self.y, TILE_SIZE, TILE_SIZE ) # the head runs on different logic 
        #then the body because the head is used to detect collisions for example 
        self.body = [pg.Rect(self.x-TILE_SIZE,self.y, TILE_SIZE, TILE_SIZE)] #the body of the snake is gonna be 
        # an array constaining a succession of rectangles with coordinates that corespond to our snake
        self.dead = False 


#for the update movement method the logic is simple, for the body we just give for each square starting
#from the tail, the position of the square that comes after.
    def update(self):
        global apple

        for square in self.body:
            if self.head.x == square.x and self.head.y == square.y:
                self.dead = True 
            if self.head.x not in range(0, screen_width) or self.head.y not in range(0, screen_height):
                self.dead = True

        if self.dead:
            self.x = TILE_SIZE
            self.y = TILE_SIZE
            self.xdir = 1 
            self.ydir = 0
            self.head = pg.Rect(self.x,self.y, TILE_SIZE, TILE_SIZE )
            self.body = [pg.Rect(self.x-TILE_SIZE,self.y, TILE_SIZE, TILE_SIZE)] 
            self.dead = False
            apple = Apple()
        #we append the head so when we enter the loop we take into consideration the head as part
        #of the entire body, so we move we can take the position of the head, then after that,
        #we increase the position of our head and then we remove it of from the body
        self.body.append(self.head)
        for i in range(len(self.body)-1):
            self.body[i].x = self.body[i+1].x
            self.body[i].y = self.body[i+1].y
        self.head.x += self.xdir * TILE_SIZE
        self.head.y += self.ydir * TILE_SIZE 
        self.body.remove(self.head)
             

class Apple:
    def __init__(self):
        #we have a problem and that is that the apple is not on the grid, so all we have to do is divide
        #by the TILE SIZE and then convert that to an int the multiply it by TILE SIZE
        self.x = int(randrange(0,screen_width)/TILE_SIZE)*TILE_SIZE
        self.y = int(randrange(0,screen_height)/TILE_SIZE)*TILE_SIZE
        self.rect = pg.Rect(self.x, self.y, TILE_SIZE, TILE_SIZE) 
    
    def update(self):
        pg.draw.rect(screen,('red'), self.rect)  



def draw_tiles():
    for x in range(0,screen_width,TILE_SIZE):
        for y in range(0, screen_height, TILE_SIZE):
            tile_rect = pg.Rect(x, y, TILE_SIZE, TILE_SIZE)
            pg.draw.rect(screen,('white'), tile_rect, 1)


#for the score
score = FONT.render("1", True, "white")
score_rect = score.get_rect(center = (screen_width/2,screen_height/20))


# draw_tiles()
snake = Snake()
apple = Apple()

run = True
while run:
    

    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False

        #now here we implement the user input
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_DOWN:
                snake.ydir = 1 
                snake.xdir = 0
            elif event.key == pg.K_UP:
                snake.ydir = -1
                snake.xdir = 0
            elif event.key == pg.K_RIGHT:
                snake.ydir = 0
                snake.xdir = 1
            elif event.key == pg.K_LEFT:
                snake.ydir = 0
                snake.xdir = -1
            elif event.key == pg.K_a:
                run = False


    
    snake.update()

    screen.fill('black')
    # draw_tiles()

    apple.update()

    score = FONT.render(f"{len(snake.body) + 1}", True, "white")

    pg.draw.rect(screen,('cyan'), snake.head)

    for square in snake.body:
        pg.draw.rect(screen,('green'), square)
    
    screen.blit(score, score_rect)

    #we check if the apple is being eaten
    if snake.head.x == apple.x and snake.head.y == apple.y:
        snake.body.append(pg.Rect(square.x, square.y, TILE_SIZE, TILE_SIZE))
        apple = Apple()

    pg.display.flip() 
    clock.tick(15)

pg.quit()





# #example OOP

# class Dog:
#     def __init__(self, name, age):  # Constructor method, fonction pour initialiser une instance
#         self.name = name           # Attribute
#         self.age = age             # Attribute

#     def bark(self):                # Method
#         print(f"{self.name} barks!")

# # Create an instance of the Dog class
# dog1 = Dog("Buddy", 3)

# # Access attributes and methods
# print(dog1.name)  # Output: Buddy
# dog1.bark()       # Output: Buddy barks!


#what i learnet:
# . OOP (the init function, instances, update function for the movement)
# . KEYDOWN inputs, how to work with user input 
# . initialise a classes attributes like coordinates for example
# .
# .
# .
# .
# .
# .


