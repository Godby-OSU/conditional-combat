################
# Battle Window 
################
from windows.window import Window
from sys_info import screen_x, screen_y
import sprites.sprite_classes as spc
import time
import json
import sprites.stat_blocks as sb
import sprites.unit_classes as Unit
import sprites.stat_blocks as Stats


class BattleWindow(Window):
    """Updates the visuals involved in combat."""
    def __init__(self, display, tag: str, friendly_unit_class):
        super().__init__(display, tag)
        self.friendly_units = friendly_unit_class.get_list()  # Friendly unit list is imported b/c used in multiple places
        self._bulk_add_sprites(self.friendly_units)           # Adds friendly units from list to this window's sprite group

    def activate_window(self):
        logic = BattleLogic(self, self.friendly_units) 
        logic.run_logic()


class BattleLogic():
    """Runs the combat"""
    def __init__(self, battle_window: BattleWindow, friendly_units: list):
        self.battle_window = battle_window
        self._friendly_units = friendly_units   # Active friendly sprites
        self._active_enemies = []               # Active enemy sprites
        self._inactive_enemies = []             # List of strings naming type of units to be generated
        self.round = 1
        self._combat = False
        self._round = 1
        self._wait = 1
        self._num_enemies = 0 

    def generate_encounter(self):
        """Creates a list of all enemies used for this engagement"""
        print("Generating Enemies")
        remaining_points = self._round
        while remaining_points > 0:
            enemy_type = "slime" # If using more than one enemy type this could vary
            self._inactive_enemies.append(enemy_type)
            remaining_points -= sb.enemy_info[enemy_type]["value"]           
        print("Generation completed.")

    def spawn_enemy_sprites(self):
        """Creates enemy sprites and adds units to the display."""
        print("Spawning Enemies")
        pos_x = 0
        pos_y = 0

        while self._num_enemies != 4 and len(self._inactive_enemies) != 0:  # When less than 4 active and inactive enemies remain
            for unit in self._inactive_enemies:
                stats = Stats.enemy_info[unit]
                image_dir = self.battle_window.images
                new_enemy = Unit.EnemyUnit(image_dir, unit, (200,200), (pos_x,pos_y), stats)    # Generates a new enemy sprite
                print("NEW ENEMY")
                self._active_enemies.append(new_enemy)                                          # Adds new enemes
                print("ACTIVE ADDED")
                del self._inactive_enemies[0]                                                   # Deletes added unit from inactive list
                pos_x += 200
                self._num_enemies += 1
                print("Unit Added")
        print("Enemies Spawned.")

    def start_combat(self):
        print("Starting Combat")
        self.generate_encounter()  # Creates a list of al enemies to be used
        self.spawn_enemy_sprites() # Creates the currently active enemy sprites.
        print(self._active_enemies)
        print(self._friendly_units)
        self.battle_window._bulk_add_sprites(self._active_enemies)
        self.battle_window._render_screen()
        self._combat = True
    
    def create_json(self):
        """Create highscores JSON entry for microservice to access"""
        print("Please enter name")
        name = input()
        data = {
        'name': name,
        'round': self._round }
        with open('gameover.json', 'w') as test:
            json.dump(data, test)

    def process_damage(self, attacker, target):
        """Applies damage from attacker to the target."""
        print("Attacking", target.get_name())
        time.sleep(self._wait)
        damage = attacker.get_damage()
        target.take_damage(damage)
        print(target.get_name(), "takes", damage, "damage.")
        time.sleep(self._wait)

    def process_death(self, target, enemy: bool):
        """ Checks if unit has been defeated.  
        Removes defeated enemy unit.  Game Over if ally defeated."""
        if not target.check_pulse():
            print(target.get_name(), "goes down.")
            time.sleep(self._wait)
            if enemy:
                target.kill()
                self._active_enemies.remove(target)
            else:
                print("Game Over")
                self.create_json()
                self._combat = False
                self.battle_window._change_window("menu")

    def process_attack(self, attacker):
        """Processing the attack phase for a single unit regardless of faction."""
        # Determine if friendly or enemy unit attacking.
        targets = self._friendly_units
        aoe = False
        enemy_bool = False
        if attacker.get_faction() == "ally":
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
        """Process a round of combat"""
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
                self.round += 1
                self._combat = False
                self.battle_window._change_window("selection")

            if self._combat:
                time.sleep(self._wait)

    def run_logic(self):
        self.start_combat()
        self.run_round()
