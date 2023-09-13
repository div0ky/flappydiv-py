# Colors
RED = (255, 0, 0)
GREEN = (0, 255, 0)
WHITE = (255, 255, 255)

# Window settings
WINDOW_WIDTH = 1500
WINDOW_HEIGHT = 800
FPS = 60
TITLE = "Flappy Bird Clone"

# Bird settings
BIRD_WIDTH = 50
BIRD_HEIGHT = 50
BIRD_START_X = WINDOW_WIDTH // 4
BIRD_START_Y = WINDOW_HEIGHT // 2
BIRD_JUMP_HEIGHT = -5

GRAVITY = 0.20

# Pipe settings
PIPE_WIDTH = 100
PIPE_GAP = 150
PIPE_MIN_Y = 100  # Minimum height of the top pipe
PIPE_MAX_Y = WINDOW_HEIGHT - 300  # Maximum height of the top pipe
PIPE_ADD_INTERVAL = 1.25  # Seconds between adding new pipes
PIPE_SPEED = 5

# Define the network dimensions
INPUT_DIM = 4
HIDDEN_DIM = 24
OUTPUT_DIM = 2

# Hyperparameters
GAMMA = 0.99  # discount factor
BATCH_SIZE = 64
EPS_START = 1.0
EPS_END = 0.1
EPS_DECAY = 1000
TARGET_UPDATE = 10  # Update target network every 10 episodes