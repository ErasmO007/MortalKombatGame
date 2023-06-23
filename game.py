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
