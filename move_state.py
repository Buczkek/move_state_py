# The ultimate player move function I will ever need (probably)
# Author: Buczkek (GitHub)


# Direction Definitions
RIGHT = 1
LEFT = 2
FORWARD = 3
BACKWARD = 4
UP = 5
DOWN = 6

# Movement Definitions
STILL = 0
POSITIVE = 1
NEGATIVE = 2

class Player:
    def __init__(self):
        self.was_left = False
        self.was_right = False
        self.was_forward = False
        self.was_backward = False
        self.was_up = False
        self.was_down = False

    def move_state(self, direction, activate) -> None:
        """Set the position move state.

        Args:
            direction: What direction to update
            activate: Start or stop moving in the direction
        """
        if direction == RIGHT:
            if activate and not self.was_left:
                self.was_left = self._xdir == NEGATIVE
            # self.was_left = not activate and self._xdir == NEGATIVE
            self._xdir = POSITIVE if activate else (NEGATIVE if self.was_left or self._xdir == NEGATIVE else STILL)
            if not activate:
                self.was_right = False
        elif direction == LEFT:
            if activate and not self.was_right:
                self.was_right = self._xdir == POSITIVE
            # self.was_right = not activate and self._xdir == POSITIVE
            self._xdir = NEGATIVE if activate else (POSITIVE if self.was_right or self._xdir == POSITIVE else STILL)
            if not activate:
                self.was_left = False
        elif direction == FORWARD:
            if activate and not self.was_backward:
                self.was_backward = self._zdir == POSITIVE
            # self.was_backward = not activate and self._zdir == POSITIVE
            self._zdir = NEGATIVE if activate else (POSITIVE if self.was_backward or self._zdir == POSITIVE else STILL)
            if not activate:
                self.was_forward = False
        elif direction == BACKWARD:
            if activate and not self.was_forward:
                self.was_forward = self._zdir == NEGATIVE
            # self.was_forward = not activate and self._zdir == NEGATIVE
            self._zdir = POSITIVE if activate else (NEGATIVE if self.was_forward or self._zdir == NEGATIVE else STILL)
            if not activate:
                self.was_backward = False
        elif direction == UP:
            if activate and not self.was_down:
                self.was_down = self._ydir == NEGATIVE
            # self.was_down = not activate and self._ydir == NEGATIVE
            self._ydir = POSITIVE if activate else (NEGATIVE if self.was_down or self._ydir == NEGATIVE else STILL)
            if not activate:
                self.was_up = False
        elif direction == DOWN:
            if activate and not self.was_up:
                self.was_up = self._ydir == POSITIVE
            # self.was_down = not activate and self._ydir == POSITIVE
            self._ydir = NEGATIVE if activate else (POSITIVE if self.was_up or self._ydir == POSITIVE else STILL)
            if not activate:
                self.was_down = False
