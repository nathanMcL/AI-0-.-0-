# This script is  for Ideas for a Choose Your Own Adventure game

print("""
                 _
               _(_)_                          wWWWw   _
   @@@@       (_)@(_)   vVVVv     _     @@@@  (___) _(_)_
  @@()@@ wWWWw  (_)\    (___)   _(_)_  @@()@@   Y  (_)@(_)
   @@@@  (___)     `|/    Y    (_)@(_)  @@@@   \|/   (_)\
    /      Y       \|    \|/    /(_)    \|      |/      |
 \ |     \ |/       | / \ | /  \|/       |/    \|      \|/
\\\|//   \\|///  \\\|//\\\|/// \|///  \\\|//  \\|//  \\\|//
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

""")

print("Welcome to the Harbor.")
print("take in the view, enjoy your visit.")

# Choice 1
choice1 = input('You\'re sitting staring at the terrain, you found the insatiable urge to write.\n '
                'the longer you listen to the harbor, the waves crash against the shore, it became rhythmic.\n '
                'You began to worry if the seagulls would spoil your writing as they circled and cried overhead.\n'
                'As you sat there you write a poem on top of a poem, a poem for the seagulls that threatened you\n '
                'with spoil,\n'
                'begging for morsels from the nearby fishmongers. Poems for the procurer of the morning catch,\n'
                'along with poems for the pimps and paupers nearby watching with envious eyes, their stomachs\n '
                'growling with hunger'
                'As you wrote one poem, the next became a sonnet, and later a limerick for fun.\n'
                'You refrained from elegy and chose to write an acrostic poem for a challenge.\n'
                'As the words spilled, you took another sip from your coffee...\n'
                'You raise your head from writing and choose to look "left" or "right" \n').lower()

print('''
  )))
    (((
  +-----+
  |     |]
  `-----'    
___________
`---------'
''')

if choice1 == "a":
    choice2 = input('A wooden cart wobbles by, its wooden wheels worn. As the wooden cart approaches\n'
                    'you can smell the sweet scent of freshly picked flowers wafting in the air, you\n'
                    'greet with "How do you do?", They respond "Good morning!"\n'
                    'The sun at your back warms you as the seas misty breeze touches your arm.\n'
                    'You sit there listening to the harbor, you feel aloft among the clouds as the sun rises higher.\n'
                    'Do you change your view? or get up and leave?\n'
                    'Type "view" to stay and enjoy the harbor.\n'
                    'Type "leave" to get up and walk home. \n').lower()

    if choice2 == "w":
        choice3 = input("You look to your left and see a fowl perched on a handrail.\n "
                        "Alternating each leg after a long stretch. A neck extends as the sun greets\n"
                        "all in its presence. The hen's feathers raise and with a fierce shake,\n"
                        "a single feather drops. Jumping off the the handrail, wildly flapping and running pretending\n"
                        "to soar through the air with glee. You think, these crazy capons are curious about you,\n"
                        "and they approach. Clucking and searching for food, wandering closer.\n"
                        "you must choose:"
                        "You notices something on the 'beach'..."
                        "A 'Tom-cat' approaches..."
                        "or you choose to 'leave' and go home...\n").lower()

        if choice3 == "Beach":
            print("It was funny while you sat there listening to the sunrise over the harbor,\n"
                  "something caught your eye down at the beach in the water. A large pool toy.\n "
                  "There was a still soft breeze, and the water on the beach was still. A seagull screeched by.\n"
                  "Further up in the sky, an eagle circles overhead. Down on the beach, a toy, white\n"
                  "as snow floats content and sure. A mane and tail of rainbows and stars. Her horn was tall\n"
                  "and golden, a testament to the legendary status of mythological creatures.\n"
                  "You imagine climbing on its back and riding her into the sky. The warmth of the sun feels\n "
                  "so inviting, the breeze thought never to cease, and a little sparrow swooped by and chirped at\n "
                  "you.\n")

        elif choice3 == "Tom-cat":
            print("While sipping on your morning coffee down at the harbor. The beach's\n"
                  " tom-cat scares off the wild chicks. His meow was raspy, So you apologized for not having\n"
                  "any scraps of food to give the alley cat. The feline with a gaze unyielding,\n"
                  "never soft, you think what secrets twinkle in your eye? In shades of slate and tones of gray,\n"
                  "you catch raising light and stand guardian by day. Even in your stillness, you\n"
                  "embody grace, each twitch, each stir, you keenly see. No fleeting motion leaves a\n "
                  "trace that escapes your silent scrutiny. You are a beach cat, on your throne, we sit apart,\n"
                  "but not alone. For in your quiet, stoney gaze you capture all the sun's ablaze.\n")

        elif choice3 == "leave":
            print("You decide you've received all the inspiration from this writing experience,\n "
                  "you decide to leave and walk home.\n"
                  "Game Over.\n")
        else:
            print("You uncross your legs, accidentally bumping the small table spilling your coffee...\n Game Over.")
    else:
        # print("A seagull spoils your writing experience by swooping down and stealing your breakfast scone...\n
        # Game Over.")
        if choice1 != "right":
            print("The smell of fish is strong, distributing you, breaking your writing focus.\n "
                  "You decide to get up and leave the harbor...\n Game Over.")