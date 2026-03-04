class Bird:
    color = ''
    size = ''


    def __init__(self, can_fly = True):
        self.can_fly = can_fly


dove_bob = Bird()
dove_bob.can_fly = False

penguin = Bird(can_fly=False)
