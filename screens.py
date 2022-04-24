#################
# Screens 
################
"""
Includes information required to manage visuals active on the current screen.
"""
import sys_info as sys
import screen_sprites as ss  

class Screens:
    """This class should do NOTHING except hold info for what is on each screen and load that info."""
    def __init__(self, sprite_group):
        self._sprite_group = sprite_group
        self._selection_sprites = [
           ss.Button(("battle_on", "battle_off"), (400,150), (int(sys.screen_x-400),int(sys.screen_y-150))),
           ss.Toggle_Button(("aoe_on", "aoe_off"), (200,75), (250,100))

        ]
        self._menu_sprites = [
            #ss.Text("Version 0", 30, sys.white, (900,470)),
            ss.Screen_Sprite("title", (sys.screen_x,200),(0,0)),
            ss.Button(("start_on", "start_off"), (400,150),(int(sys.screen_x/2-200),200),  self.load_selection),            
            ss.Button(("guide_on", "guide_off"), (400,150), (int(sys.screen_x/2-200),350), self.load_guide)  
        ]          

        self._battle_sprites = []  

        self._guide_sprites = [
            ss.Screen_Sprite(("guide_info"), (sys.screen_x, sys.screen_y), (0,0)),
            ss.Button(("close", "close"), (100,100), (sys.screen_x-100,0), self.load_menu)
        ]

        self._update = False

    def load_screen(self, screen_sprites):
        """Input the screen that you're adding the sprites to.
        Returns sprite list with all those sprites added."""
        self._sprite_group.empty()
        for sprite in screen_sprites:
            self._sprite_group.add(sprite)
        return self._sprite_group

    def load_menu(self):
        print("LOADING MENU")
        self.load_screen(self._menu_sprites)

    def load_selection(self):
        print("LOADING SELECTION")
        self.load_screen(self._selection_sprites)
        self._update = False

    def load_battle(self):
        print("LOADING BATTLE")
        self.load_screen(self._battle_sprites)

    def load_guide(self):
        print("LOADING GUIDE")
        self.load_screen(self._guide_sprites)

    def set_function(self, name, function):
        for sprite in self._selection_sprites:
            if sprite.get_name() == name:
                sprite.set_function(function)


    def add_unit_battle(self, unit, size, coords):
        """Takes unit info and generates a visual sprite from it."""
        unit.set_sprite(ss.Screen_Sprite(unit.get_name(), size, coords))
        self._battle_sprites.append(unit.get_sprite())
        print("Unit added to battle screen.")

    def add_unit_selection(self, unit, size, coords):
        unit.set_sprite(ss.Screen_Sprite(unit.get_name(), size, coords))
        self._selection_sprites.append(unit.get_sprite())
        
    def remove_battle(self, deleted_sprite):
        """Removes a sprite from the battle sprite list"""
        print("Removing from battle...")
        self._battle_sprites.remove(deleted_sprite.get_sprite())
        self.load_battle()

    def update(self):
        """Change this so that battle is not explicitly hardcoded."""
        if self._update is True:
            self._update is False
            self.load_battle()


# TO:DO Have a variable to track which screen is active.  The update function will use that variable to
# decide which background is changing instead of hardcoding it.  This will remove some extra load functions.