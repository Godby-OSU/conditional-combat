from screens import Screens
from units import create_enemy, Unit, Friendly_Unit
import time
import json

class Battle():
    """Tracks data from battle and updates the screen with new info."""
    def __init__(self, screen: Screens):
        self._screen = screen
        self._friendly_units = []
        self._active_enemies = []
        self._inactive_enemies = []
        self._combat = False
        self._round = 1
        self._wait = 1

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
            self._screen.create_and_add_sprite(unit, (unit_x,unit_y), (pos_x,pos_y))
            pos_x += unit_x

        for unit in self._friendly_units:
            self._screen.create_and_add_sprite(unit, (unit_x, unit_y), (500,300))

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
        self._screen.load_screen("battle")
        self._combat = True
    
    def set_round(self, round):
        self._round = round

    def create_json(self):
        print("Please enter name")
        name = input()
        data = {
        'name': name,
        'round': self._round }
        with open('gameover.json', 'w') as test:
            json.dump(data, test)



    def process_damage(self, attacker: Unit, target: Unit):
        """Applies damage from attacker to the target."""
        print("Attacking", target.get_name())
        time.sleep(self._wait)
        damage = attacker.get_damage()
        target.take_damage(damage)
        print(target.get_name(), "takes", damage, "damage.")
        time.sleep(self._wait)

    def process_death(self, target: Unit, enemy: bool):
        """ Checks if unit has been defeated.  
        Removes defeated enemy unit.  Game Over if ally defeated."""
        if not target.check_pulse():
            print(target.get_name(), "goes down.")
            time.sleep(self._wait)
            if enemy:
                self._active_enemies.remove(target)
                self._screen.remove_sprite(target)
            else:
                print("Game Over")
                self.create_json()
                self._combat = False
                self._screen.load_screen("menu")

    def process_attack(self, attacker: Unit):
        """Processing the attack phase for a single unit regardless of faction."""
        # Determine if friendly or enemy unit attacking.
        targets = self._friendly_units
        aoe = False
        enemy_bool = False
        if isinstance(attacker, Friendly_Unit):
            aoe = attacker.get_aoe()  # Only friendly units have aoe currently. 
            targets = self._active_enemies
            enemy_bool = True

        # Process the damage and check if target still alive
        if aoe:
            print("Attacking multiple targets...")
            for target in targets:
                self.process_damage(attacker, target)
                self.process_death(target, enemy_bool)       
        else:
            target = targets[0]
            self.process_damage(attacker, target)
            self.process_death(target, enemy_bool)    

    def run_round(self):
        """Processes an entire round of combat."""
        if self._combat:
            print("=======================")
            print("There are", len(self._active_enemies), "here,")
            print("and", len(self._inactive_enemies), "in reserve.")
            print(self._friendly_units[0].get_health(), "health remaining")
            print("=======================")


            for unit in self._friendly_units:
                self.process_attack(unit)
                print("")
            for unit in self._active_enemies:
                self.process_attack(unit)
                print("")

            if len(self._active_enemies) == 0 and len(self._inactive_enemies) == 0:
                print("Round Over")
                time.sleep(self._wait)
                self._round += 1
                self._combat = False
                self._screen.load_screen("selection")

            if self._combat:
                time.sleep(self._wait)