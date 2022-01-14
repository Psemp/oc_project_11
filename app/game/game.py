import pygame
import time

from pathlib import Path

from app.models.position_nt import Position


def game(ai: bool, ai_path, game_map, characters, items):
    # 32 px is the size of the sprites, so pos*32 is position to sprite position
    counter = 0
    game_map.make_map()
    pygame.init
    game_over = False
    consciousness = False

    lenght = len(game_map.box) * 32
    height = len(game_map.box[0]) * 32
    win = pygame.display.set_mode((lenght, height + 32))

    ford = characters[0]
    bernard = characters[1]

    tablet = items[0]
    glasses = items[1]
    toy = items[2]

    def get_path(file_name):
        return str(Path(__file__).parent.parent.joinpath("images", file_name))

    def get_image(file_name):
        return pygame.image.load(get_path(file_name)).convert()

    def get_image_alpha(file_name):
        return pygame.image.load(get_path(file_name)).convert_alpha()

    known_images = ['floor.png', 'wall.png']
    known_alpha_images = [
            "bernard.png",
            "consciousness.png",
            "ford.png",
            "defeat.png",
            "glasses.png",
            "maze.png",
            "tablet.png",
            "victory.png",
        ]

    images = {}

    for known_image in known_images:
        loaded_image = get_image(known_image)
        images[known_image] = loaded_image

    for known_image in known_alpha_images:
        loaded_image = get_image_alpha(known_image)
        images[known_image] = loaded_image

    run = True

    while run:

        pygame.time.delay(100)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

    # GAME "RULES"

        if bernard.alive and ford.alive and bernard.position == ford.position and not consciousness:
            bernard.alive = False
            game_over = True
        if bernard.alive and ford.alive and bernard.position == ford.position and consciousness:
            ford.alive = False
            game_over = True
        if bernard.alive and tablet.gathered and toy.gathered and glasses.gathered:
            consciousness = True
        if bernard.alive and not tablet.gathered and bernard.position == tablet.position:
            tablet.gathered = True
        if bernard.alive and not glasses.gathered and bernard.position == glasses.position:
            glasses.gathered = True
        if bernard.alive and not toy.gathered and bernard.position == toy.position:
            toy.gathered = True

    # /GAME "RULES"

    # DRAW

        win.fill((255, 255, 255))

        for i in range(0, len(game_map.floors)):
            win.blit(images["floor.png"], (game_map.floors[i]))

        for i in range(0, len(game_map.walls)):
            win.blit(images["wall.png"], (game_map.walls[i]))

        if not glasses.gathered:
            win.blit(images["glasses.png"], ((glasses.position.x_axis * 32, glasses.position.y_axis * 32)))
        else:
            win.blit(images["glasses.png"], (0, height))

        if not tablet.gathered:
            win.blit(images["tablet.png"], ((tablet.position.x_axis * 32, tablet.position.y_axis * 32)))
        else:
            win.blit(images["tablet.png"], (32, height))

        if not toy.gathered:
            win.blit(images["maze.png"], ((toy.position.x_axis * 32, toy.position.y_axis * 32)))
        else:
            win.blit(images["maze.png"], (64, height))

        if bernard.alive:
            win.blit(images["bernard.png"], ((bernard.position.x_axis * 32, bernard.position.y_axis * 32)))

        if ford.alive:
            win.blit(images["ford.png"], ((ford.position.x_axis * 32, ford.position.y_axis * 32)))

        if game_over and bernard.alive:
            win.blit(images["victory.png"], (0, 0))

        if game_over and not bernard.alive:
            win.blit(images["defeat.png"], (0, 0))

        if consciousness:
            win.blit(images["consciousness.png"], (lenght - 32, height))

    # /DRAW

    # PLAYER MOVEMENT
        if not ai:
            player_action = pygame.key.get_pressed()

            if player_action[pygame.K_LEFT] and not game_over:

                new_position = Position(bernard.position.y_axis, bernard.position.x_axis - 1)

                if not ((new_position.x_axis * 32, new_position.y_axis * 32)) in game_map.walls:
                    bernard.position = new_position

            if player_action[pygame.K_RIGHT] and not game_over:

                new_position = Position(bernard.position.y_axis, bernard.position.x_axis + 1)

                if not ((new_position.x_axis * 32, new_position.y_axis * 32)) in game_map.walls:
                    bernard.position = new_position

            if player_action[pygame.K_UP] and not game_over:

                new_position = Position(bernard.position.y_axis - 1, bernard.position.x_axis)

                if not ((new_position.x_axis * 32, new_position.y_axis * 32)) in game_map.walls:
                    bernard.position = new_position

            if player_action[pygame.K_DOWN] and not game_over:

                new_position = Position(bernard.position.y_axis + 1, bernard.position.x_axis)

                if not ((new_position.x_axis * 32, new_position.y_axis * 32)) in game_map.walls:
                    bernard.position = new_position

    # /MOVEMENT

    # AI MOVEMENT
        # uses the while loop and counter to loop over ai_path list which is supposed to be the shortest sol
        if ai:
            try:
                new_position_tuple = ai_path[counter]
            except IndexError:
                new_position_tuple = ((bernard.position.y_axis, bernard.position.x_axis))
            new_position = Position(y_axis=new_position_tuple[0], x_axis=new_position_tuple[1])
            bernard.position = new_position
            time.sleep(0.50)
    # /AI MOVEMENT
        pygame.display.flip()
        try:
            counter += 1
        except IndexError:
            pass
