import openai
import random
from config import openai_api_key
from textPrevention import sanitize_input, validate_choice_input

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
    return response.choices[0].message.content

# Function to handle "leave" scenarios
def handle_leave_scenario(ai_generate=False):
    leave_messages = [
        "The adventure ends as you lose focus. In a weird fit of rage, you throw your coffee cup at the seagulls... GAME OVER!\n",
        "The adventure ends as the wobbly wooden cart handler loses control. The wooden cart slowly...\n Painstakingly wobbles towards you and your simple table...\n You stop the cart with you foot, allowing the handler to gain control of their wooden cart... \n Your coffee cup is whisked away by a seagull... GAME OVER!\n",
        "You finish your coffee, rising from the simple chair, gathering your things off the simple table...\n Simply walking from the harbor, heading home...\n You did not even bother to look back at the beach, the market, or the seagulls...\n Did you not notice the cat... GAME OVER!\n",
        "Oh, really.?. Your done? You're done with the market, and the beach, I get it the seagulls squawking can be annoying...\n... Did you not hear about the cat? Or notice the mythological creature!\n Just sayin' it was really cool...\n...GAME OVER...\n"
    ]
    # Testing out: AI-generated whimsical exit responses
    if ai_generate:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are an intelligent and whimsical storyteller who writes humorous and whimsical reasons for a character to leave a scene."},
                {"role": "user", "content": "Create an intelligent and whimsical reason why the player decides to leave the harbor and head home."}
            ]
        )
        return response.choices[0].message.content
    else:
        # Randomly select a leave message
        return random.choice(leave_messages)

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

    # Name Selection
    player_name = input("Enter your character's name: ")
    player_name = sanitize_input(player_name)  # Sanitize the input
    context += f"\nWelcome to the Harbor, {player_name}!\nTake in the view, enjoy your visit.\n"
    print(context)

    # Opening Story Scenario
    opening = input(
        'You’re seated at a simple table with a simple chair. Staring out at your surroundings, you found the insatiable urge to write. '
        'The longer you listen to the harbor, the waves crash against the shore, it became rhythmic. '
        'You began to worry if the seagulls would spoil your writing as they circled and cried overhead. \n'
        'As you sat there you write a poem on top of a poem, a poem for the seagulls that threatened you with spoil, '
        'begging for morsels from the nearby fishmongers. Poems for the procurer of the morning catch,'
        'along with poems for the pimps and paupers nearby watching with envious eyes, their stomachs growling with hunger...\n'
        'As time passed from one poem, to the next, your wrote a sonnet, and later a limerick for fun.'
        'You refrained from elegy and chose to write an acrostic poem for a challenge.\n'
        'As the words spilled, you took the last sip from your coffee... You felt the earge to go explore...\n'
        'Do you go "left" towards the lively market, "right" towards the beach, or "leave" to head home?\n'
    ).lower()

    # Handle the options at the first choice
    if opening == "leave":
        print(handle_leave_scenario(ai_generate=True))
        return
    elif opening == "left":
        context += f"\n{player_name} felt drawn to the sounds of the market on the left, where vendors called out their daily specials, and seagulls fought for scraps above."
        description = generate_description("left", context)
        print(description)
    elif opening == "right":
        context += f"\n{player_name} turned towards the calm and inviting beach. The sand shimmered under the morning sun, and the gentle lapping of waves filled the air."
        description = generate_description("right", context)
        print(description)
    else:
        print("Invalid choice. The adventure ends as you lose focus. GAME OVER!")
        return
    
    # Validate the opening choice
    allowed_choices = ["left", "right", "leave"]
    opening = validate_choice_input(opening, allowed_choices)

    # Second set of choices
    choice2 = input(
        'You notice a small wooden cart wobbly moving by, its wheels worn. '
        'You can smell the sweet scent of freshly picked flowers wafting in the air. '
        'Do you wander over to the wooden "cart" with its trinkets, approach the curious "fowl" by the handrail, or "leave" to head home?\n'
    ).lower()

    # Handle the "leave" option at the second choice
    if choice2 == "leave":
        print(handle_leave_scenario(ai_generate=True))
        return
    elif choice2 == "cart":
        context += f"\n{player_name} approached the wooden cart filled with trinkets and fresh flowers. The scent of wild roses filled the air as {player_name} leaned in to inspect the curious items."
        description = generate_description("cart", context)
        print(description)
    elif choice2 == "fowl":
        context += f"\n{player_name} noticed a small fowl perched on a handrail. The wild capon alternated each leg after a long stretch, extending its neck as the sun greeted all in its presence. \n"
        "The hen's feathers raise and with a fierce shake,a single feather drops...\n"
        "Jumping off the the handrail, wildly flapping and running soaring to the ground in glee. You think, these capons are crazy...\n"
        "They are curious about you, and they approach. Clucking and searching for food, wandering closer.\n"
        description = generate_description("fowl", context)
        print(description)
    else:
        print("Invalid choice. The adventure ends as you lose focus. GAME OVER!")
        return
    
    # Validate choice2
    allowed_choices = ["cart", "fowl", "leave"]
    opening = validate_choice_input(opening, allowed_choices)

    # Third set of choices
    choice3 = input(
        'As you listen to the sunrise over the harbor, something catches your eye down at the beach in the water. '
        'A large pool toy floats content and sure, with a mane and tail of rainbows and stars. '
        'Do you go closer "mythological creatures", notice the wily old "tom cat", or "leave" to head home?\n'
    ).lower()

    # Handle the "leave" option at the third choice
    if choice3 == "leave":
        print(handle_leave_scenario(ai_generate=True))
        return
    elif choice3 == "mythological creatures":
        context += f"\n{player_name} was drawn to the mythical pool toy on the beach. The toy was white as snow, with a mane and tail of rainbows and stars, and a tall golden horn."
        description = generate_description("mythological creatures", context)
        print(description)
    elif choice3 == "tom cat":
        context += f"\n{player_name} noticed the old tom cat approaching. The beach tom cat, with its raspy meow, had a mysterious presence."
        description = generate_description("tom cat", context)
        print(description)
    else:
        print("Invalid choice. The adventure ends as you lose focus. GAME OVER!")

    # Validate choice3a
        allowed_choices = ["mythological creatures", "tom cat", "leave"]
        opening = validate_choice_input(opening, allowed_choices)

if __name__ == "__main__":
    main()
