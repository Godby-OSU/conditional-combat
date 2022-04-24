from screens import Screens
from units import create_enemy
import time

class Battle():
    """Tracks data from battle and updates the screen with new info."""
    def __init__(self, screen: Screens):
        self._screen = screen
        self._friendly_units = []
        self._active_enemies = []
        self._inactive_enemies = []
        self._combat = False
        self._round = 1

    def add_friendly(self, unit):
        self._friendly_units.append(unit)

    def add_enemy(self, unit):
        self._inactive_enemies.append(unit)

    def generate_enemies(self):
        """Creates enemy units"""
        print("Generating Enemies")
        remaining_points = self._round
        while remaining_points > 0:
            self._inactive_enemies.append(create_enemy("slime"))
            remaining_points -= 1
        print("Generation completed.")

    def update_screen(self):
        print("Updating sprites list")
        unit_x = 200
        unit_y = 200
        pos_x = 0
        pos_y = 0

        for unit in self._active_enemies:
            self._screen.add_unit_battle(unit, (unit_x,unit_y), (pos_x,pos_y))
            pos_x += unit_x

        for unit in self._friendly_units:
            self._screen.add_unit_battle(unit, (unit_x, unit_y), (500,300))

        print("Completed: adding sprites to battle screen.")

    def start_combat(self):
        print("Starting Combat")
        self.generate_enemies()  # Create enemies in inactive list
        num_enemies = 0
        while num_enemies != 4 and len(self._inactive_enemies) != 0:  # Move up to 4 of those enemies into active

            self._active_enemies.append(self._inactive_enemies[0])
            del self._inactive_enemies[0]
            num_enemies += 1
        self.update_screen()
        self._screen.load_battle()
        self._combat = True
    
    def set_round(self, round):
        self._round = round

    def update(self):
        if self._combat:
            self._inactive_enemies = [] # Clear this out because we have max of 4 at the moment
            wait = 1.5
            print("There are", len(self._active_enemies), "here,")
            print("and", len(self._inactive_enemies), "waiting.")
            for unit in self._friendly_units:
                aoe = unit.get_aoe()
                damage = unit.get_damage()
                if aoe is True:
                    damage = int(damage/2)
                    print("Attacking multi targets.")
                    for enemy in self._active_enemies:
                        enemy.take_damage(int(damage))
                        print(enemy.get_name(), "takes", damage, "damage.")
                        time.sleep(wait)

                    dead_units = []
                    for enemy in self._active_enemies:
                        if enemy.check_pulse() is False:
                            print(enemy.get_name(), "goes down.")
                            dead_units.append(enemy)
                            time.sleep(wait)
                    for enemy in dead_units:
                        self._active_enemies.remove(enemy)
                        self._screen.remove_battle(enemy)
                else:
                    print("Attacking single target.")
                    enemy = self._active_enemies[0]
                    enemy.take_damage(damage)
                    print(enemy.get_name(), "takes", damage, "damage.")
                    time.sleep(wait)
                    if enemy.check_pulse() == False:
                        print(enemy.get_name(), "goes down.")
                        time.sleep(wait)
                        self._active_enemies.remove(enemy)
                        self._screen.remove_battle(enemy)

                if len(self._active_enemies) == 0 and len(self._inactive_enemies) == 0:
                    print("Round Over")
                    time.sleep(wait)
                    self._combat = False
                    self._round += 1
                    self._screen.load_selection()

            for enemy in self._active_enemies:
                damage = enemy.get_damage()
                print(enemy.get_name(), "attacking", self._friendly_units[0].get_name())
                time.sleep(wait)
                self._friendly_units[0].take_damage(damage)
                print(self._friendly_units[0].get_name(), "takes", damage, "damage.")
                time.sleep(wait)
            
            print(self._friendly_units[0].get_health(), "health remaining")
            time.sleep(wait)
            
            if self._friendly_units[0].check_pulse() == False:
                print("Game Over")
                self._combat = False
                self._screen.load_menu()





            
