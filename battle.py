from sprite_groups import battle_sprites, friendly_sprites, enemy_sprites, reserve_sprites
from sprite_classes.units import EnemyUnit
from stat_blocks import enemy_info
from display import display
import json
import time

class Battle():
    def __init__(self):
        self._round = 1
        self._enemy_size = (200, 200)
        # There can be a max of 4 specified enemies, each at a specified coordinate. 
        self._active_enemies = [None, None, None, None]                        
        self._pos_coords = {0: (0,0), 1: (200, 0), 2: (400, 0), 3: (600, 0)} 

    ####################
    # Spawning Enemies 
    ####################
    def create_enemy(self, enemy_type: str):
        """Creates an enemy sprite.  Stored in reserve group."""
        new_sprite = EnemyUnit(enemy_type, self._enemy_size, (0,0), enemy_info[enemy_type])
        reserve_sprites.add(new_sprite)

    def generate_encounter(self):
        """Creates a list of all enemies used for this combat."""
        print("Generating Enemies")
        remaining_points = self._round
        while remaining_points > 0:
            enemy_type = "slime" # If using more than one enemy type this could vary
            self.create_enemy(enemy_type)
            remaining_points -= 1
        print(reserve_sprites)
        print("====Generation completed.====")

    def transfer_sprite(self):
        """Transfers a single enemy sprite from reserve to active sprite group.
        Groups are unordered and have no specific name, thus a for loop is used to grab any sprite."""
        for sprite in reserve_sprites:
            reserve_sprites.remove(sprite)
            enemy_sprites.add(sprite)
            battle_sprites.add(sprite)                          # Battle sprites is what is being rendered
            return sprite

    def spawn_enemy(self):
        """Moves a sprite from reserve to the active enemy list."""
        position = 0
        for space in self._active_enemies:                      # Active enemy list has 4 spots                      
            if space is None:                                   # Empty slots indicated by None
                sprite = self.transfer_sprite()                 # Move that sprite to the active group
                sprite.set_pos(self._pos_coords[position])      # Sprite's coords depends on position in list
                self._active_enemies[position] = sprite         # Put a reference to the sprite the enemy list
                break
            else:
                position += 1

    def spawn_ally(self):
        """Moves ally units to the rendered list"""
        for ally in friendly_sprites:
            battle_sprites.add(ally)

    def start_combat(self):
        """Prepares the initial combat state"""
        self.generate_encounter()       # Create all enemy sprites
        # If there are empty spaces and enemies remaining in reserve
        print(self._active_enemies)
        print(reserve_sprites)
        while None in self._active_enemies and reserve_sprites:
            self.spawn_enemy()
            print("==========================================================SPAWNED")
        self.spawn_ally()
        display.change_window("battle")
        print(display.window)

    ####################
    # Processing Knockouts
    ####################
    def null_index(self, target):
        """Removes target from index and replaces it with None."""
        index = 0
        for enemy in self._active_enemies:
            if enemy == target:
                break
            else: index += 1
        self._active_enemies[index] = None

    def enemy_knockout(self):
        """Check if enemy is knocked out and process results."""
        for target in self._active_enemies:
            if target is not None:
                print(target)
                if not target.check_pulse():
                    print(target.get_name(), "goes down.")
                    target.kill()
                    self.null_index(target)

    def create_json(self):
        """Create highscores JSON entry for microservice to access"""
        print("Please enter name")
        name = input()
        data = {
        'name': name,
        'round': self._round }
        with open('gameover.json', 'w') as test:
            json.dump(data, test)

    def ally_knockout(self, target):
        """Check if ally is knocked out and process results"""
        print("CHECK")
        if not target.check_pulse():
            print("Game Over")
            self.create_json()
            display.change_window("title")

    ####################
    # Processing Attacks
    ####################   
    def process_damage(self, attacker, target):
        """Applies damage from attacker to target."""
        damage = attacker.get_damage()
        target.take_damage(damage)
        print(target.get_name(), "takes", damage, "damage.")


    def ally_attack(self, attacker):
        """Conducts an attack made by an ally unit"""
        aoe = attacker.get_aoe()
        # Start by targeting all active enemies
        for target in self._active_enemies:
            self.process_damage(attacker, target)
            # If it's not an aoe, stop after the first attack
            if not aoe:
                break

    def enemy_attack(self, attacker):
        """Conducts an attack made by an enemy."""
        # Groups are unsorted.  Since there is only one ally, a for loop still works.
        for ally in friendly_sprites:
            self.process_damage(attacker, ally)


    def execute_attack(self, attacker):
        """Executes an attack based on unit's faction."""
        faction = attacker.get_faction()
        if faction == "ally":
            self.ally_attack(attacker)
            self.enemy_knockout()
        else:
            self.enemy_attack(attacker)
            self.ally_knockout()

    ####################
    # Processing Combat
    ####################
    def next_wave(self):
        """Spawns more enemies if there are enemies in reserve and empty spots available.""" 
        while None in self._active_enemies:
            if reserve_sprites:
                self.spawn_enemy()
            else:
                return

    def round_end(self):
        """Checks if round is over and returns to selection if yes."""
        if not enemy_sprites:
            print("Round Over")
            self._round += 1
            display.change_window("selection")

    def battle_update(self):
        """Provides update on battle stats in console."""
        for sprite in friendly_sprites:
            hitpoints = sprite.get_health()
        print("=======================")
        print("There are", len(enemy_sprites), "here,")
        print("and", len(reserve_sprites), "in reserve.")
        print(hitpoints, "health remaining")
        print(self._active_enemies)
        print("=======================")


    def execute_battle(self):
        """Command that starts the battle sequence when a button is pressed."""
        self.start_combat()
        display.render_screen()
        time.sleep(1)
        while display.window == "battle":
            self.battle_update()

            for unit in friendly_sprites:
                self.execute_attack(unit)
            time.sleep(.5)
            for unit in self._active_enemies:
                if unit is not None:
                    self.execute_attack(unit)
            time.sleep(.5)

            self.next_wave()    # Spawns new enemies
            self.round_end()    # Ends round if all enemies exhausted.

battle = Battle()