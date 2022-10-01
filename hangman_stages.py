def get_hangman_stages(remaining_attempts):
    """
    This function draws the character that will be used for the visual aspect of the game,
    while also setting the amount of attempts a player will have at the game.
    """
    max_attempts = 8
    stages = ["""
        ------
        |    |
        |
        |
        |
        |
        |
    ------------
    """, """
        ------
        |    |
        |    O
        |
        |
        |
        |
    ------------
    """, """
        ------
        |    |
        |    O
        |    |
        |    |
        |
        |
    ------------
    """, """
        ------
        |    |
        |    O
        |    |
        |    |
        |   /
        |
    ------------
    """, """
        ------
        |    |
        |    O
        |    |
        |    |
        |   / \\
        |
    ------------
    """, """
        ------
        |    |
        |    O
        |  --|
        |    |
        |   / \\
        |
    ------------
    """, """
        ------
        |    |
        |    O
        |  --|--
        |    |
        |   / \\
        |
    ------------
    """, """
        ------
        |    |
        |    O
        |  --|--o
        |    |
        |   / \\
        |
    ------------
    """, """
        ------
        |    |
        |    O
        | o--|--o
        |    |
        |   / \\
        |
    ------------
    """]
    return stages[max_attempts - remaining_attempts]