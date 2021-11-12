

class Settings:
    """A class to store all settings for Aliens"""

    def __init__(self):
        """Initialize the game's stettings"""

        self.screenWidth = 1200
        self.screenHeight = 800
        self.bgColor = (230, 230, 230)

        #ship settings
        self.ship_speed = 1.5

        #Bullet settings
        self.bullet_speed = 1.0
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 3




