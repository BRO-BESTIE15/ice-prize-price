import pygame

# Settings
SCREEN_SIZE = (1280, 720)
FPS = 60
BACKGROUND = "blue"

radius = 100
width = 10
position = [200, 500]
speed = 5


# Movement directions
direction_x = None
direction_y = None
mouse_direction_x = None
mouse_direction_y = None

run = True

pygame.init()

screen = pygame.display.set_mode(SCREEN_SIZE)
clock = pygame.time.Clock()

# Mouse edge areas
EDGE_X = SCREEN_SIZE[0] * 0.1
EDGE_Y = SCREEN_SIZE[1] * 0.1

while run:
    
    # ---------------- EVENTS ----------------
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            run = False

        elif event.type == pygame.MOUSEBUTTONDOWN:

            x, y = event.pos

            # Vertical movement
            if y <= EDGE_Y:
                mouse_direction_y = "up"
            elif y >= SCREEN_SIZE[1] - EDGE_Y:
                mouse_direction_y = "down"

            # Horizontal movement
            if x <= EDGE_X:
                mouse_direction_x = "left"
            elif x >= SCREEN_SIZE[0] - EDGE_X:
                mouse_direction_x = "right"

        elif event.type == pygame.MOUSEBUTTONUP:
            mouse_direction_x = None
            mouse_direction_y = None

    # ---------------- KEYBOARD ----------------
    keys = pygame.key.get_pressed()
    
    keyboard_direction_x = None
    keyboard_direction_y = None

    if keys[pygame.K_w] or keys[pygame.K_UP]:
        keyboard_direction_y = "up"
    elif keys[pygame.K_s] or keys[pygame.K_DOWN]:
        keyboard_direction_y = "down"

    if keys[pygame.K_a] or keys[pygame.K_LEFT]:
        keyboard_direction_x = "left"
    elif keys[pygame.K_d] or keys[pygame.K_RIGHT]:
        keyboard_direction_x = "right"

    # ---------------- MOVEMENT ----------------
    
    # Vertical
    if keyboard_direction_y is not None:
        direction_y = keyboard_direction_y
    else:
        direction_y = mouse_direction_y
    
    # Horizontal
    if keyboard_direction_x is not None:
        direction_x = keyboard_direction_x
    else:
        direction_x = mouse_direction_x
    
    
    # Actually move
    if direction_y == "up":
        position[1] -= speed
    elif direction_y == "down":
        position[1] += speed
    
    if direction_x == "left":
        position[0] -= speed
    elif direction_x == "right":
        position[0] += speed
        
    # ---------------- SCREEN BOUNDARIES ----------------
    if position[0] - radius <= 0:
        position[0] = radius
    elif position[0] + radius >= SCREEN_SIZE[0]:
        position[0] = SCREEN_SIZE[0] - radius

    if position[1] - radius <= 0:
        position[1] = radius
    elif position[1] + radius >= SCREEN_SIZE[1]:
        position[1] = SCREEN_SIZE[1] - radius

    # ---------------- DRAW ----------------
    screen.fill(BACKGROUND)

    pygame.draw.circle(
        screen,
        "white",
        position,
        radius,
        width
    )

    pygame.display.update()

    # Keep game running at 60 FPS
    clock.tick(FPS)

pygame.quit()

