#!/usr/bin/env python3

""" Rock Paper Scissors Lizard Spock Game
Game logic for a RPSLS class, gets input from the user, generates a random choice for the CPU, and compares the choices to determine a winner

Rules:
Scissors cuts Paper

Paper covers Rock

Rock crushes Lizard

Lizard poisons Spock

Spock smashes Scissors

Scissors decapitates Lizard

Lizard eats Paper

Paper disproves Spock

Spock vaporizes Rock

(and as it always has) Rock crushes Scissors
"""

from random import choice


class RPSLS:
    """
    Represents a Rock-Paper-Scissors-Lizard-Spock (RPSLS) game.
    """

    def __init__(self) -> None:
        """Initialize the RPS game."""
        self.__choices: dict[str:str, ...] = {
            "R": "rock",
            "P": "paper",
            "S": "scissors",
            "L": "lizard",
            "K": "Spock",
        }

        self.__scenarios: dict[tuple[str, str] : str, ...] = {
            ("rock", "scissors"): "Rock crushes Scissors!",
            ("rock", "lizard"): "Rock crushes Lizard",
            ("paper", "rock"): "Paper covers Rock",
            ("paper", "Spock"): "Paper disproves Spock",
            ("scissors", "paper"): "Scissors cuts Paper",
            ("scissors", "lizard"): "Scissors decapitates Lizard",
            ("Spock", "rock"): "Spock vaporizes Rock",
            ("Spock", "scissors"): "Spock smashes scissors",
            ("lizard", "Spock"): "Lizard poisons Spock",
            ("lizard", "paper"): "Lizard eats Paper",
        }

    # Class methods

    def get_user_choice(self) -> str:
        """
        Get the user's choice and return it.

        Returns:
            str: The user's choice.
        """
        while True:
            try:
                user_choice: str = input(
                    "Enter your choice: (R)ock / (P)aper / (S)cissors / (L)izard / Spoc(k): "
                ).upper()
                if user_choice in self.__choices.keys():
                    print(f"You chose: {self.__choices[user_choice]}")
                    return self.__choices[user_choice]
                else:
                    raise ValueError
            except ValueError:
                print(
                    f"Choose between: (R)ock / (P)aper / (S)cissors / (L)izard / Spoc(k)"
                )

    def get_cpu_choice(self) -> str:
        """
        Get the CPU's random choice and return it.

        Returns:
            str: The CPU's choice.
        """
        cpu_choice: str = choice(tuple(self.__choices.values()))
        print(f"CPU chose: {cpu_choice}")
        return cpu_choice

    def check_winner(self, user_choice: str, cpu_choice: str) -> None:
        """
        Check who wins the RPSLS game based on user and CPU choices.

        Args:
            user_choice (str): The user's choice.
            cpu_choice (str): The CPU's choice.
        """
        if user_choice == cpu_choice:
            print("It's a tie!")

        # player wins
        elif (user_choice, cpu_choice) in self.__scenarios.keys():
            print(f"{self.__scenarios[(user_choice, cpu_choice)]}\nYou win!")

        # CPU wins
        elif (cpu_choice, user_choice) in self.__scenarios.keys():
            print(f"{self.__scenarios[(cpu_choice, user_choice)]}\nYou lose!")


# not part of the class
def play():
    """
    Play the Rock-Paper-Scissors-Lizard-Spock game.
    """
    rpsls = RPSLS()  # Create object instance of RPSLS class
    user = rpsls.get_user_choice()
    comp = rpsls.get_cpu_choice()
    rpsls.check_winner(user, comp)


#  Run as a standalone program if __name__ is __main__
if __name__ == "__main__":
    play()
