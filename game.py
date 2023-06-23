class MKCharacterType:
    def __init__(self, name, strengths=None, weaknesses=None):
        """
        Represents a Mortal Kombat character type and its strengths/weaknesses.

        Parameters:
        - name (str): The name of the character type.
        - strengths (list): A list of types that this type is strong against.
        - weaknesses (list): A list of types that this type is weak against.
        """
        self.name = name
        self.strengths = [] if strengths is None else strengths
        self.weaknesses = [] if weaknesses is None else weaknesses

    def is_strong_against(self, other):
        """
        Checks if this type is strong against another type.

        Parameters:
        - other (MKCharacterType): The other character type to check against.

        Returns:
        - bool: True if this type is strong against the other type, False otherwise.
        """
        return other.name in self.weaknesses

    def is_weak_against(self, other):
        """
        Checks if this type is weak against another type.

        Parameters:
        - other (MKCharacterType): The other character type to check against.

        Returns:
        - bool: True if this type is weak against the other type, False otherwise.
        """
        return other.name in self.strengths

    class MKCharacter:
        def __init__(self, name, types):
            """
            Represents a Mortal Kombat character with a name and types.

             Parameters:
             - name (str): The name of the character.
             - types (list): A list of MKCharacterType objects representing the types of the character.
            """
            self.name = name
            self.types = types
            self.max_health = len(types) * 50
            self.current_health = self.max_health
            self.is_fainted = False

        def __repr__(self):
            """
            Returns a string representation of the character.

            Returns:
            - str: The string representation of the character.
            """
            type_names = "/".join([t.name for t in self.types])
            return f"{self.name} ({type_names})"

        def lose_health(self, damage):
            """
              Decreases the character's current health by the specified damage.

              Parameters:
              - damage (int): The amount of damage to subtract from the current health.
            """
            self.current_health = max(0, self.current_health - damage)
            if self.current_health == 0:
                self.faint()

        def faint(self):
         """
            Sets the character's is_fainted attribute to True, indicating it has fainted.
         """
         self.is_fainted = True


        def get_effectiveness(self, other_type):
          """
          Calculates the effectiveness of this character's types against another type.

           Parameters:
            - other_type (MKCharacterType): The other character type to check effectiveness against.

           Returns:
            - float: The effectiveness value as a floating-point number.
         """
          effectiveness = 1.0
          for character_type in self.types:
              for strength in character_type.strengths:
                if strength == other_type.name:
                    effectiveness *= 2.0
              for weakness in character_type.weaknesses:
                if weakness == other_type.name:
                    effectiveness *= 0.5
          return effectiveness

        def attack(self, other):
          """
          Attacks another character and reduces its health based on the attack's effectiveness.

          Parameters:
          - other (MKCharacter): The character to be attacked.
          """
          print(f"{self} is attacking {other}!")
          print("Select an attack:")
          print("1. front")
          print("2. back punch")
          print("3. back kick")
          print("4. Uppercut")

          while True:
            choice = input("Enter the number corresponding to the attack: ")
            if choice == "1":
                attack_name = "Attack 1"
                break
            elif choice == "2":
                attack_name = "Attack 2"
                break
            elif choice == "3":
                attack_name = "Attack 3"
                break
            elif choice == "4":
                attack_name = "Attack 4"
                break
            else:
                print("Invalid choice. Please enter a number between 1 and 4.")


          effectiveness = 1.0
          for character_type in other.types:
            effectiveness *= self.get_effectiveness(character_type)

          damage = int(((2 * len(self.types) / 5 + 2) * 40) / (len(other.types) + 1) * effectiveness)
          print(f"{self} uses {attack_name} and deals {damage} damage!")
          other.lose_health(damage)


def select_character_type():
    """
    Allows the user to select a Mortal Kombat character type.

    Returns:
    - MKCharacterType: The selected character type.
    """
    print("Select a character type:")
    print("1. Scorpion")
    print("2. Sub-Zero")
    print("3. Raiden")
    print("4. Sonya")

    while True:
        choice = input("Enter the number corresponding to the character type: ")
        if choice == "1":
            return scorpion_type
        elif choice == "2":
            return sub_zero_type
        elif choice == "3":
            return raiden_type
        elif choice == "4":
            return sonya_type
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

            def battle(character1, character2):
               """
               Simulates a battle between two Mortal Kombat characters.

                 Parameters:
    - character1 (MKCharacter): The first character.
    - character2 (MKCharacter): The second character.
    """
    print(f"{character1} vs. {character2}! Let the battle begin!")
    current_turn = 1
    while not character1.is_fainted and not character2.is_fainted:
        print(f"Round {current_turn}!")
        attacker = character1 if current_turn % 2 == 1 else character2
        defender = character2 if current_turn % 2 == 1 else character1
        attacker.attack(defender)
        print("Player 1      Player 2\n", character1.current_health, "HP          ",  character2.current_health, "HP")
        current_turn += 1
        if character1.is_fainted:
            winner = character2
        elif character2.is_fainted:
            winner = character1
    # winner = character1 if not character2.is_fainted else character2
    print(f"{winner} wins!")


# Define the Mortal Kombat character types
scorpion_type = MKCharacterType("Scorpion", strengths=["Sub-Zero"],
                               weaknesses=["Raiden", "Sonya"])
sub_zero_type = MKCharacterType("Sub-Zero", strengths=["Raiden"],
                               weaknesses=["Scorpion", "Sonya"])
raiden_type = MKCharacterType("Raiden", strengths=["Sonya"],
                             weaknesses=["Sub-Zero", "Scorpion"])
sonya_type = MKCharacterType("Sonya", strengths=["Scorpion"],
                            weaknesses=["Sub-Zero", "Raiden"])

# Create two Mortal Kombat characters with multiple types
print("Select characters for the battle:")
character1_type = select_character_type()
character2_type = select_character_type()
character1 = MKCharacter("Character 1", [character1_type])
character2 = MKCharacter("Character 2", [character2_type])

# Simulate the battle between the Mortal Kombat characters
battle(character1, character2)
