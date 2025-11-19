import sys
import pygame
from constants import *
from logger import log_state, log_event
from player import *
from asteroid import *
from asteroidfield import AsteroidField
from circleshape import *

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
    print("Starting Asteroids!")
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2
    clock = pygame.time.Clock()
    dt = 0
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    Shot.containers = (shots, updatable, drawable)
    AsteroidField.containers = (updatable)
    player = Player(x,y)
    asteroidfield = AsteroidField()
    while True:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        #player.update(dt)
        updatable.update(dt)
        for aster in asteroids:
            if CircleShape.collide_with(aster,player):
                log_event("player_hit")
                print("Game over!")
                sys.exit()
            for shot in shots:
                if CircleShape.collide_with(aster,shot):
                    log_event("asteroid_shot")
                    shot.kill()
                    aster.split()
        for d in drawable:
            d.draw(screen)
        #player.draw(screen)
        pygame.display.flip()
        dt = clock.tick(60)/1000
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")


if __name__ == "__main__":
    main()
