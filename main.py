import pgzrun,random, math, pygame
from PIL import Image
"""
You cannot collide a rectangle with an actor since actor doesn't inherit rectangle attributes 
"""


SIZE=25

image = Image.open('images/snake.png')
image = image.resize((SIZE,SIZE))
image.save(fp='images/snake_modified.png')

WIDTH = 600
HEIGHT = 600
CENTER = (WIDTH/2,HEIGHT/2)
MOVE_DIST = 2


game_over = False
new_rectangle=False

rectangle_list = []
#snake_head = Actor('snake_modified',topleft=(50,50))
snake_head = Rect((50,50),(SIZE,SIZE))
rectangle_list.append(snake_head)
snake_direction = pygame.math.Vector2() #[x,y] [-1,1] player is going < and v
rectangle = Rect(CENTER,(SIZE,SIZE))


def draw():
    global rectangle
    screen.clear()
    screen.draw.filled_rect(snake_head,'white')

    if new_rectangle:
        rectangle = spawn_rectangle()

    screen.draw.filled_rect(rectangle,'yellow')

    for rect in rectangle_list:
        screen.draw.filled_rect(rect,'white')

    # if len(rectangle_list) !=0:
    #     rectangle_list[0].x = snake_head.x
    #     rectangle_list[0].bottom = snake_head.top
    #     screen.draw.filled_rect(rectangle_list[0],'green')

    # for i in range (len(rectangle_list)):
    #     rectangle_list[i+1].x = rectangle_list[i].x
    #
    #
    #
    # for rect in rectangle_list:
    #     rect.x = snake_head.x-26
    #     rect.y = snake_head.y
    #     screen.draw.filled_rect(rect,'green')

    #screen.draw.filled_rect(rectangle,'green')

def update():
    global snake_direction
    if not game_over:
        if keyboard.up:
           # snake_direction = (0,-1)
            snake_direction.x=0
            snake_direction.y=-1
        if keyboard.right:
            #snake_direction=(1,0)
            snake_direction.x = 1
            snake_direction.y = 0
        if keyboard.down:
            #snake_direction=(0,1)
            snake_direction.x = 0
            snake_direction.y = 1
        if keyboard.left:
            #snake_direction=(-1,0)
            snake_direction.x = -1
            snake_direction.y = 0

        snake_head.x += snake_direction.x * MOVE_DIST
        snake_head.y += snake_direction.y * MOVE_DIST

        #how to update the position of the list of rectangles supposedly behind
        for i in range(1,len(rectangle_list)):
            prev_coord = (rectangle_list[i-1].x,rectangle_list[i-1].y)
            rectangle_list[i].x = prev_coord[0]
            rectangle_list[i].y = prev_coord[1]
            print(rectangle_list[i].center)
            # rectangle_list[i-1]+= snake_direction.x * MOVE_DIST
            # rectangle_list[i-1] += snake_direction.x * MOVE_DIST

        check_collision(rectangle)


def spawn_rectangle():
    global new_rectangle, rectangle
    rectangle = Rect((random.randint(0, WIDTH-SIZE), random.randint(0, HEIGHT-SIZE)), (SIZE, SIZE))
    new_rectangle=False
    return rectangle

def check_collision(rect):
    global new_rectangle
    #if the distance between the center of each rectangle is

    rectangle_center = rect.center
    snake_head_center = snake_head.center
    dist = math.dist(rectangle_center,snake_head_center) #distance formula sqrt((x2-x1)^2+(y2=y1)^2)

    l = 2*(math.sqrt((2*(SIZE/2)**2)))

    if dist<=l:
        print('collided!')
        #objects have collided
        rectangle_list.append(rect)
        new_rectangle=True

    # if rect.colliderect(snake_head):
    #     rectangle_list.append(rect)
    # new_rectangle=True



pgzrun.go()