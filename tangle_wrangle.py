import pygame
import time
import random

def run_tangle_wrangle():

    # Initialize pygame
    pygame.init()

    # Display settings
    width = 1200
    height = 800
    display = pygame.display.set_mode((width, height))
    pygame.display.set_caption('Snake Game')

    # Snake settings
    snake_block = 40
    snake_speed = 15
    snake_over = 1.5

    clock = pygame.time.Clock()

    font_style = pygame.font.SysFont("haettenschweiler", 35)
    score_font = pygame.font.SysFont("haettenschweiler", 35)

    snake_image = pygame.image.load("images/PIRIB.png")
    snake_image = pygame.transform.scale(snake_image, (snake_block * snake_over, snake_block * snake_over))

    food_image = pygame.image.load("images/glob.png")
    food_image = pygame.transform.scale(food_image, (snake_block * snake_over, snake_block * snake_over))
    

    def your_score(score):
        value = score_font.render("Your Score: " + str(score), True, [233, 169, 71])
        display.blit(value, [0, 0])

    def snake(snake_block, snake_list):
        for x in snake_list:
            display.blit(
                snake_image, 
                (x[0] - snake_block // 2, x[1] - snake_block // 2)
            )

    def is_snake_out_of_bounds(x, y, width, height):
        return x >= width or x < 0 or y >= height or y < 0

    def message(msg, color):
        mesg = font_style.render(msg, True, color)
        display.blit(mesg, [width / 6, height / 3])

    def gameLoop():
        game_over = False
        game_close = False

        x1 = width / 2
        y1 = height / 2

        x1_change = 0
        y1_change = 0

        snake_list = []
        length_of_snake = 1

        # Random food position
        foodx = round(random.randrange(0, width - snake_block) / snake_block) * snake_block
        foody = round(random.randrange(0, height - snake_block) / snake_block) * snake_block

        while not game_over:

            while game_close == True:
                display.fill([11, 127, 126])
                message("You Lost! Press Q-Quit or C-Play Again", [255, 10, 0])
                your_score(length_of_snake - 1)
                pygame.display.update()

                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_q:
                            game_over = True
                            game_close = False
                        if event.key == pygame.K_c:
                            gameLoop()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_over = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        x1_change = -snake_block
                        y1_change = 0
                    elif event.key == pygame.K_RIGHT:
                        x1_change = snake_block
                        y1_change = 0
                    elif event.key == pygame.K_UP:
                        y1_change = -snake_block
                        x1_change = 0
                    elif event.key == pygame.K_DOWN:
                        y1_change = snake_block
                        x1_change = 0

            if is_snake_out_of_bounds(x1, y1, width, height):
                game_close = True
            x1 += x1_change
            y1 += y1_change
            display.fill([0, 0, 0])

            display.blit(
                food_image, 
                (foodx - snake_block // 2, foody - snake_block // 2)
            )
            
            snake_head = []
            snake_head.append(x1)
            snake_head.append(y1)
            snake_list.append(snake_head)
            if len(snake_list) > length_of_snake:
                del snake_list[0]

            for x in snake_list[:-1]:
                if x == snake_head:
                    game_close = True

            snake(snake_block, snake_list)
            your_score(length_of_snake - 1)

            pygame.display.update()

            if x1 == foodx and y1 == foody:
                foodx = round(random.randrange(0, width - snake_block) / snake_block) * snake_block
                foody = round(random.randrange(0, height - snake_block) / snake_block) * snake_block
                length_of_snake += 1

            clock.tick(snake_speed)

        pygame.quit()

    gameLoop()
