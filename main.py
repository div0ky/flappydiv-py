import random
import pygame, sys, time
from sprites import *
from settings import *


# Flappy bird remake with drawn geometric shapes instead of images
class Game:
    def __init__(self):
        # setup
        pygame.init()
        self.score = 0
        self.game_started = False
        self.display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption(TITLE)
        self.clock = pygame.time.Clock()
        
        self.pipes = []
        
        self.font = pygame.font.SysFont(None, 36)  # Choose a desired font and size

        
        # sprite groups
        self.all_sprites = pygame.sprite.Group()
        self.collision_sprites = pygame.sprite.Group()
        
        self.bird = Bird()
        self.bird.rect.centery = WINDOW_HEIGHT // 2 # Vertically center the bird
        self.all_sprites.add(self.bird)
        
        # create pipes periodically (every PIPE_ADD_INTERVAL seconds)
        self.pipe_timer = 0
        
    def run(self):
        last_time = time.time()
        
        def pause(display_surface, score):
            font = pygame.font.SysFont(None, 56)
            game_over_surface = font.render('Game Over', True, (255, 0, 0))  # Red color
            score_surface = font.render(f'Score: {score - 1}', True, (0, 0, 0))  # Black color

            game_over_rect = game_over_surface.get_rect(center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2 - 50))
            score_rect = score_surface.get_rect(center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2 + 50))

            display_surface.blit(game_over_surface, game_over_rect)
            display_surface.blit(score_surface, score_rect)
            pygame.display.flip()
            
            while True:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_n:
                            return
    

        while True:            
            # delta time
            dt = time.time() - last_time
            last_time = time.time()
            
            # event loop
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                    
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        if not self.game_started:
                            self.game_started = True
                            self.bird.flap()
                        else:
                            self.bird.flap()
                    
            
            # Add pipes periodically
            self.pipe_timer += dt
            if self.pipe_timer > PIPE_ADD_INTERVAL:
                gap_start = random.randint(PIPE_MIN_Y, WINDOW_HEIGHT - PIPE_MAX_Y)
                upper_pipe = Pipe(WINDOW_WIDTH, gap_start, True)
                lower_pipe = Pipe(WINDOW_WIDTH, gap_start + PIPE_GAP, False)
                self.all_sprites.add(upper_pipe, lower_pipe)
                self.collision_sprites.add(upper_pipe, lower_pipe)
                self.pipes.append(upper_pipe)
                self.pipes.append(lower_pipe)
                self.pipe_timer = 0
            
            # Update and draw sprites
            self.all_sprites.update(self.game_started)
            
            reward = 0.1 # default reward for survival
            
            # Check for collisions
            pipe_collisions = pygame.sprite.spritecollide(self.bird, self.collision_sprites, False)
            if pipe_collisions:
                reward = -100
                # Handle collision (e.g., end game, reset bird position, etc.)
                print("Collision detected!")
                pause(self.display_surface, self.score)
                self.__init__()
                # For now, let's just end the game when a collision is detected
                # pygame.quit()
                # sys.exit()
                
            # Check if the bird passed a pipe
            next_pipe = self.get_next_pipe()
            if next_pipe and self.bird.rect.left > next_pipe.rect.right:
                reward += 5.0
                print("Passed a pipe!")
            
            self.display_surface.fill(WHITE)
            self.all_sprites.draw(self.display_surface)
            
            # Display the score
            score_surface = self.font.render(f"Score: {self.score}", True, (0, 0, 0))  # Render in black color
            score_rect = score_surface.get_rect(topleft=(10, 10))  # Position at the top-left corner
            self.display_surface.blit(score_surface, score_rect)
            
            if self.game_started:
                self.score += 1
            
            # game logic (updating the display and setting the frame rate)
            pygame.display.update()
            self.clock.tick(FPS)
            
    def get_next_pipe(self):
        bird_right_edge = self.bird.rect.right
        next_pipe = None
        for pipe in self.pipes:
            
            # Find the pipe that is closest to the bird
            if pipe.rect.left > bird_right_edge:
                if not next_pipe or pipe.rect.left < next_pipe.rect.left:
                    next_pipe = pipe
            
            # Clean up pipes that have moved off-screen
            if pipe.rect.right < 0:
                self.pipes.remove(pipe)
                    
        return next_pipe
        

    def get_state(self):
        next_pipe = self.get_next_pipe()
        if next_pipe:
            gap_center = (next_pipe.rect.top + next_pipe.rect.bottom) / 2
            vertical_distance_to_gap = self.bird.rect.centery - gap_center
            horizontal_distance_to_pipe = next_pipe.rect.left - self.bird.rect.right
            return (self.bird.rect.centery, vertical_distance_to_gap, horizontal_distance_to_pipe, self.bird.y_speed)
        else:
            return None

        
        


if __name__ == '__main__':
    game = Game()
    game.run()