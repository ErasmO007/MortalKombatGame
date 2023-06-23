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