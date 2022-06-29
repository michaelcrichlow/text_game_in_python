# ------------------------------------------------------------------
# ----- EXERCISE - USING CLASSES TO BUILD A TEXT-BASED GAME --------
# ------------------------------------------------------------------
#
# __author__    = "Mike Crichlow"
# __date__      = 06.28.2022
#
# Notes:

from sys import exit


class RoomData(object):

    max_number_of_rooms = 3

    room_one_greeting = """
---------------------------------------------------
"ROOM 01 - MURKY CELL"
---------------------------------------------------
To your left is gray wall.
In front of you are iron bars.
To your right is a brown wall.
Behind you is an impressive stone wall.
"""

    room_two_greeting = """
---------------------------------------------------
"ROOM 02 - GOLD ROOM"
---------------------------------------------------
As the dust settles, you look around in absolute amazement.
The room seems to be made of solid gold!
'This is fantastic!' you say to yourself. 'When I find my
way out of this, I've got to come back to this room. It's 
worth a fortune!'

The room is a cube: 25 feet high, 25 feet wide and 25 feet
tall. In the center of the room a sunken pool sits - 10 ft
square - filled with still, clear water. It's very deep.
(You cannot see the bottom.)

Beside the pool is a broomstick and a rope.
"""

    room_greetings = {
        "room1_greeting": room_one_greeting,
        "room2_greeting": room_two_greeting
    }

    nouns = {
        "room1_nouns": ["gray wall", "iron bars", "brown wall", "stone wall"],
        "room2_nouns": ["gold walls", "pool", "broomstick", "rope"]
    }

    verbs = {
        "room1_verbs": ["examine", "hit"],
        "room2_verbs": ["examine", "use"]
    }

    vc_room1 = ["examine gray wall",
                "examine iron bars",
                "examine brown wall",
                "examine stone wall",
                "hit gray wall",
                "hit iron bars",
                "hit brown wall",
                "hit stone wall"]

    vc_room2 = ["examine gold walls",
                "examine pool",
                "examine broomstick",
                "examine rope",
                "use gold walls",
                "use pool",
                "use broomstick",
                "use rope"]

    valid_choices = {
        "room1": vc_room1,
        "room2": vc_room2
    }

    escape_room_one = """
The brown wall shatters into a million pieces and falls to the ground, 
stirring up dust. 
'Oh, boy,' you say to yourself, waving dust from your face. 
'Here goes nothing.' 
You shield your face from the dust and walk over the rubble into the next room.
"""

    escape_room_two = """
You approach the edge of the pool and cast the end
of your rope into the water. Suddenly, the floor starts
rumbling. You step backwards but still manage to stay on
your feet. Then, a magnificent fish -- gigantic in size 
-- leaps out of the water, swallows you whole and dives 
back into the water.

Your poor rope was left behind.

The fish swims for what feels like hours, but was actually
closer to ten minutes. Then, it abruptly emerges from a pool
in another room. It vomits you out, waves goodbye and dives
back into the water. As you wave goodbye a slab of concrete
slides over the pool you just emerged from -- blocking that
route. You look up and see a massive door leading outside.
You did it!! You escaped!!
"""

    interact = {
        # room one
        "examine gray wall": "The gray wall is rough to the touch and looks strong and sturdy.There's nothing else of note.",
        "examine iron bars": "The iron bars are a dull mixture of brown and gray. While old, they seem sturdy.",
        "examine brown wall": "The brown wall looks thin and weak. There's a faint crack in the bottom right corner.",
        "examine stone wall": "The stone wall is tall, strong and imposing. It's probably the outer wall of a structure of some kind.",

        "hit gray wall": "You hit the gray wall repeatedly with punches and kicks. This results in nothing more than scratched knuckles and sore legs. The wall however -- is fine.",
        "hit iron bars": "Hitting the iron bars does nothing. The disturbacne however, \ncreates tiny flakes of rust that swirl in the air and then \nsettle on the ground. It's like the worst party confetti -- ever.",
        "hit brown wall": escape_room_one,
        "hit stone wall": "You hit the stone wall with determined fists. This does absolutely nothing...and now your hands hurt.",

        # room two
        "examine gold walls": "The gold walls are beautiful, but ultimately unhelpful.",
        "examine pool": "The pool's water is crystal clear, but you can't see the bottom. Better stay clear.",
        "examine broomstick": "Yup...it's a broomstick.",
        "examine rope": "The rope is long, white and thin. May be useful.",

        "use gold walls": "You try to think of a way to use the gold walls, but can't.",
        "use pool": "The water looks too deep. Maybe later.",
        "use broomstick": "You twirl the stick around like Donatello from the Ninja Turtles. It's fun... but isn't very helpful.",
        "use rope": escape_room_two
    }

    escape_phrases = {
        "room1": "hit brown wall",
        "room2": "use rope"
    }


class Room(object):

    def __init__(self, rd: RoomData) -> None:
        self.rd = rd
        self.roomNumber = 0

    def greeting(self) -> None:
        print(self.rd.room_greetings[f"room{self.roomNumber}_greeting"])


def print_silly_dots():
    """Useful for padding between sections of the game."""
    print(".")
    print(".")
    print(".")


class GameInfo(object):

    def welcome(self) -> None:
        print("---------------------------------------------------")
        print("Mike's Game 3.10.4 (version 0.0002) on win32")
        print("Type 'help' for more information or 'exit' to quit.")
        print("---------------------------------------------------")
        print_silly_dots()

    def my_help(self) -> None:
        print_silly_dots()
        print("---------------------------------------------------")
        print("HELP - HOW TO PLAY")
        print("---------------------------------------------------")
        print("This is a 'Choose your own Adventure' style game.")
        print("It basically uses nouns and verbs.")
        print("If ever unclear at what you can do, type 'nouns' or 'verbs'.")
        print("---------------------------------")
        print("For example: ")
        print("What do you want to do? >>> nouns")
        print("---------------------------------")
        print("'nouns' prints the objects that can be interacted with.")
        print("'verbs' prints how you can interact with them.")
        print("For example, if 'cat' is one of the nouns and 'pet' is one of the verbs, \nthen 'pet cat' would be a valid action you could take.")
        print("Put various combinations together and see what happens. Have fun!")
        print_silly_dots()

    def my_exit(self):
        print("Exiting game...")
        exit(0)

    def final_thanks(self) -> None:
        """Prints the credits thanking the player for playing the game."""
        print("---------------------------------------------------")
        print("Thanks for playing!")
        print("I hope you had fun.")
        print("See you next time. ^_^")
        print("---------------------------------------------------")


class TextAdventure1(object):

    def __init__(self) -> None:
        self.input = ""
        self.room_number = 1

        self.info = GameInfo()
        self.rd = RoomData()
        self.rm = Room(self.rd)
        self.nouns = []
        self.verbs = []
        self.choice = ""
        self.escaped_room = False

    # this is the main function called in order to run the program
    def run(self) -> None:

        # welcome and startup info
        self.info.welcome()

        # main gameplay loop
        while self.room_number < self.rd.max_number_of_rooms:

            # assign room number
            self.rm.roomNumber = self.room_number

            # print room greeting
            self.rm.greeting()

            # define nouns and verbs
            self.nouns = self.rd.nouns[f"room{self.room_number}_nouns"]
            self.verbs = self.rd.verbs[f"room{self.room_number}_verbs"]

            # establishment that self.escaped_room = False
            self.escaped_room = False

            while self.escaped_room == False:

                # give the input
                self.choice = input("What do you want to do? >>>   ")

                if self.choice == "help":
                    self.info.my_help()
                elif self.choice == "exit":
                    self.info.my_exit()
                elif self.choice == "nouns":
                    print(self.nouns)
                elif self.choice == "verbs":
                    print(self.verbs)
                elif self.choice in self.rd.valid_choices[f"room{self.room_number}"]:
                    print(self.rd.interact[self.choice])
                else:
                    print("...")
                    print("Instructions unclear. (Make sure you don't have any typos.)")
                    print("Type 'nouns' to see WHAT you can interact with.")
                    print("Type 'verbs' to see HOW you can interact with them.")
                    print("...")

                if self.choice == self.rd.escape_phrases[f"room{self.room_number}"]:
                    self.escaped_room = True
                    self.room_number += 1

        # print credits
        self.info.final_thanks()


def main() -> None:

    game = TextAdventure1()
    game.run()


if __name__ == '__main__':
    main()
