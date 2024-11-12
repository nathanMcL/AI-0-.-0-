import openai
from config import openai_api_key

# OpenAI API key
client = openai.OpenAI(api_key=openai_api_key)

def generate_description(choice, context):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a detailed and immersive storyteller who uses vivid language to create a coherent narrative."},
            {"role": "assistant", "content": context},
            {"role": "user", "content": f"Continue the story. The player chose to go {choice}. What happens next? Focus on maintaining the established tone and setting."}
        ]
    )
    #return response['choices'][0]['message']['content']
    return response.choices[0].message.content

def main():
    context = r"""
        The Harbor
                                 _
                               _(_)_                              wWWWw      _
             @@@@             (_)@(_)   vVVVv    _        @@@@    (___)    _(_)_
            @@()@@   wWWWw      (_)\    (___)  _(_)_     @@()@@     Y     (_)@(_)
             @@@@    (___)      `|/       Y   (_)@(_)     @@@@    \\|/      (_)
              /        Y       \\|      \\|//   (_)      \\|        |/       |
          \\ |      \\ |/        |/     \\|/   \\|/        |/     \\|      \\|/
        \\\\\|//   \\\\|///  \\\\|//\\\\\\|/// \\|///  \\\\|//  \\\\|//  \\\\|//
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

    """

    player_name = input("Enter your character's name: ")
    context += f"\nWelcome to the Harbor, {player_name}!\nTake in the view, enjoy your visit.\n"

    print(context)

    # Opening Story Scenario
    opening = input(
        'You\'re seated at a simple table with a simple chair. Staring out at your surroundings, you found the insatiable urge to write. \n '
        'The longer you listen to the harbor, the waves crash against the shore, it became rhythmic.\n '
        'You began to worry if the seagulls would spoil your writing as they circled and cried overhead.\n'
        'As you sat there you write a poem on top of a poem, a poem for the seagulls that threatened you with spoil.\n '
        'Begging for morsels from the nearby fishmongers. Poems for the procurer of the morning catch,\n'
        'along with poems for the pimps and paupers nearby watching with envious eyes, their stomachs growling with hunger.\n '
        'As you wrote one poem, the next became a sonnet, and later a limerick for fun.\n'
        'You refrained from elegy and chose to write an acrostic poem for a challenge.\n'
        'As the words spilled, you took the last sip of your coffee... The sea breeze brushed your face.\n'
        'You feel inspired and restless, you stand from the simple chair and simple table.\n'
        'do you look "left" towards the lively market, "right" towards the beach, or "leave" to head home?\n'
    ).lower()

    # Add the `opening` choice to the {context}
    context += f"\nThe player chose: {opening}."
    
    # Choice 1: Left
    if opening == "left":

        # Context to guide the AI generation
        context += f"\n{player_name} felt drawn to the sounds of the market on his left, where vendors called out their daily specials, and seagulls fought for scraps above."

        description = generate_description("left", context)
        print(description)
        context += f"\n{description}"

        # Coffee Cup
        print('''
              )))
              (((
            +-----+
            |     |]
            `-----'    
           ___________
           `---------'
                ''')

        # Story Scenario 2
        choice2 = input(
            'You notice a small wooden cart. As the cart wobbles by, its wooden wheels are worn.\n'
            'you can smell the sweet scent of freshly picked flowers wafting in the air,\n'
            'you greet with "How do you do?", They respond "Good morning!"\n'
            'The sun at your back warms you as the sea misty breeze touches your arm.\n'
            'You pause a moment listening to the harbor, you feel aloft among the clouds as the sun rises higher.\n'
            'Do you wonder over to the wooden "cart" with its trickets and fresh blooms, or has the movement of a curious "fowl" by the handrail caught your attention?\n'
        ).lower()

        # Add the `choice2` choice to the {context}
        context += f"\nThe player chose: {choice2}."

        # The Wooden Cart
        if choice2 == "cart":

            # Context to guide the AI generation
            context += f"\n{player_name} approached the wooden cart filled with trinkets and fresh flowers. The scent of wild roses filled the air as {player_name} leaned in to inspect the curious items."

            description = generate_description("cart", context)
            print(description)
            context += f"\n{description}"

        # The Chickadee
        elif choice2 == "fowl":

            # Context to guide the AI generation
            context += f"\n{player_name} noticed a small fowl perched on a handrail. The bird alternated each leg after a long stretch, extending its neck as the sun greeted all in its presence.\n"
            "Then hen's feathers raise and with a fierce shake, a single feather drops."

            description = generate_description("fowl", context)
            print(description)
            context += f"\n{description}"

        else:
            print("The sound of a screeching seagull startles you as it snatches your coffee cup and flies away in a cackle...GAME OVER!")

    # Choice 2: Right
    elif opening == "right":

        # Context to guide the AI generation
        context += f"\n{player_name} turned towards the calm and inviting beach. The sand shimmered under the morning sun, and the gentle lapping of waves filled the air."

        description = generate_description("right", context)
        print(description)
        context += f"\n{description}"

        # Story Scenario 3a
        choice3a = input(
            'As you sat there listening to the sunrise over the harbor.\n'
            'Something caught your eye down at the beach in the water. A large pool toy.\n '
            'There was a still soft breeze, and the water on the beach was still. A seagull screeched by.\n'
            'Further up in the sky, an eagle circles overhead. Down on the beach, a toy, white \n'
            'as snow floats content and sure. A mane and tail of rainbows and stars. Her horn was tall\n'
            'and golden, a testament to the legendary status of "mythological creatures".\n'
            'You imagine climbing on its back and riding her into the sky. The warmth of the sun feels \n'
            'so inviting, the breeze thought never to cease, and a little sparrow swooped by and chirped at you. \n'
            'Do you write about "mythological creatures" or notice that whiley old "Tom cat"?\n'
        ).lower()
        
        # Story Scenario 3b
        choice3b = input(
            'An alley cat approaches. His meow was raspy. So you apologized for not having\n'
            'any scraps of food to give the alley cat. The feline with a gaze unyielding,\n'
            'never soft, you think what secrets twinkle in your eye? In shades of slate and tones of gray,\n'
            'you catch raising light and stand guardian by day. Even in your stillness, you\n'
            'embody grace, each twitch, each stir, you keenly see. No fleeting motion leaves a\n'
            'trace that escapes your silent scrutiny. You are a beach cat, on your throne, we sit apart,\n'
            'but not alone. For in your quiet, stoney gaze you capture all the suns ablaze. \n'
            'Do you write about "mythological creatures" or notice that whiley old "Tom cat"?\n'
        ).lower()

        if choice3a == "mythological creatures":

            # Context to guide the AI generation
            context += f"\n{player_name} was drawn to the mythical pool toy on the beach. The toy was white as snow, with a mane and tail of rainbows and stars, and a tall golden horn.\n"

            description = generate_description("mythological creatures", context)
            print(description)
            context += f"\n{description}"

        elif choice3b == "Tom Cat":

            # Context to guide the AI generation
            context += f"\n{player_name} noticed a tom cat approaching. The beach tom cat scared off the wild chicks, his meow was raspy.\n"

            description = generate_description("Tom Cat", context)
            print(description)
            context += f"\n{description}"  
          
        elif opening == "leave":
            print("The smell of fish is strong, distributing you, breaking your writing focus.\n "
                "You decide to get up and leave the harbor, and head home...\n GAME OVER!")
        else:
            print("Invalid choice. The adventure ends as you lose focus. GAME OVER!")

if __name__ == "__main__":
    main()
