"""
 This example shows having multiple balls bouncing around the screen at the
 same time. You can hit the space bar to spawn more balls.
 
 Sample Python/Pygame Programs
 Simpson College Computer Science
 http://programarcadegames.com/
 http://simpson.edu/computer-science/
"""
 
import pygame
import random
from operator import itemgetter 
 
# Define some colors
BLACK = (0, 0, 0)
 
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
BALL_SIZE = 25
 
 
class Ball:
    """
    Class to keep track of a ball's location and vector.
    """
    def __init__(self):
        self.x = 0
        self.y = 0
        self.change_x = 0
        self.change_y = 0
        self.color = self.gen_rand_color()

    def gen_rand_color(self):
        self.r = random.randint(0,255)
        self.g = random.randint(0,255)
        self.b = random.randint(0,255)
        return (self.r, self.g, self.b)
 
 
def make_ball():
    """
    Function to make a new, random ball.
    """
    ball = Ball()
    # Starting position of the ball.
    # Take into account the ball size so we don't spawn on the edge.
    ball.x = random.randrange(BALL_SIZE, SCREEN_WIDTH - BALL_SIZE)
    ball.y = random.randrange(BALL_SIZE, SCREEN_HEIGHT - BALL_SIZE)
 
    # Speed and direction of rectangle
    ball.change_x = random.randrange(-2, 3)
    ball.change_y = random.randrange(-2, 3)
 
    return ball
 
 
def main():
    """
    This is our main program.
    """
    pygame.init()
 
    # Set the height and width of the screen
    size = [SCREEN_WIDTH, SCREEN_HEIGHT]
    screen = pygame.display.set_mode(size)
 
    pygame.display.set_caption("Bouncing Balls")
 
    # Loop until the user clicks the close button.
    done = False
 
    # Used to manage how fast the screen updates
    clock = pygame.time.Clock()
 
    ball_list = []
    ball_x_y_list = []
 
    ball = make_ball()

    ball_x_y_list.append((ball.change_x, ball.change_y))

    #max_x = list(map(itemgetter(0), ball_x_y_list)).count(max(list(map(itemgetter(0), ball_x_y_list))))
    #max_y = list(map(itemgetter(1), ball_x_y_list)).count(max(list(map(itemgetter(1), ball_x_y_list))))
    max_x = list(map(itemgetter(0), ball_x_y_list)).count(0)
    max_y = list(map(itemgetter(1), ball_x_y_list)).count(0)

    print("\nProbablity of highest change in x: ", max_x/len(ball_x_y_list))
    print("Probablity of highest change in y: ", max_y/len(ball_x_y_list))

    ball_list.append(ball)
 
    # -------- Main Program Loop -----------
    while not done:
        # --- Event Processing
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            elif event.type == pygame.KEYDOWN:
                # Space bar! Spawn a new ball.
                if event.key == pygame.K_SPACE:
                    ball = make_ball()
                    ball_x_y_list.append((ball.change_x, ball.change_y))

                    #max_x = list(map(itemgetter(0), ball_x_y_list)).count(max(list(map(itemgetter(0), ball_x_y_list))))
                    #max_y = list(map(itemgetter(1), ball_x_y_list)).count(max(list(map(itemgetter(1), ball_x_y_list))))
                    max_x = list(map(itemgetter(0), ball_x_y_list)).count(0)
                    max_y = list(map(itemgetter(1), ball_x_y_list)).count(0)

                    print("\nProbablity of highest change in x: ", max_x/len(ball_x_y_list))
                    print("Probablity of highest change in y: ", max_y/len(ball_x_y_list))

                    ball_list.append(ball)
 
        # --- Logic
        for ball in ball_list:
            # Move the ball's center
            ball.x += ball.change_x
            ball.y += ball.change_y
 
            # Bounce the ball if needed
            if ball.y > SCREEN_HEIGHT - BALL_SIZE or ball.y <= 0:
                ball.change_y *= -1
            if ball.x > SCREEN_WIDTH - BALL_SIZE or ball.x <= 0:
                ball.change_x *= -1
 
        # --- Drawing
        # Set the screen background
        screen.fill(BLACK)

        # Draw the balls
        for ball in ball_list:
            pygame.draw.rect(screen, ball.color, (ball.x, ball.y, BALL_SIZE, BALL_SIZE))
 
        # --- Wrap-up
        # Limit to 60 frames per second
        clock.tick(240)
 
        # Go ahead and update the screen with what we've drawn.
        pygame.display.flip()
 
    # Close everything down
    pygame.quit()
 
if __name__ == "__main__":
    main()