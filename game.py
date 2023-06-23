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