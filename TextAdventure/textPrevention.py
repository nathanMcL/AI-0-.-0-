import re 

def sanitize_input(user_input):
    """ 
    Reminder to self, you want to sanitize the user input by removing potentially harrmful characters and limiting to alphanumric input.
    When there are places for user input.

    Args:
    - The user_input (str): The raw input provided by the user.

    Returns:
    - str: The sanitized version of the input.
    """
    if not isinstance(user_input, str):
        return "" # Return an empty string in input is not a string.
    # Remove potentially harmful characters that are not lettters, numbers, spaces, or basic punctuation
    cleaned_input = re.sub(r'[^a-zA-Z0-9\s\.,!?\'"-]', '', user_input)
    return cleaned_input.strip()

def validate_choice_input(user_input, allowed_choices):
    """
    You want to also make sure the user input is one of the valid or allowed choices (left, right, leave, etc...)

    Args:
    - user_input (str): This is the raw input provided by the user.
    - allowed_choices (list): Lists of valid key word choices.

    Returns:
    - str: The validated and sanitized choice "if" it matches one of the allowed choices.
    - None: If the input does not match any allowed choice.
    """
    sanitized_input = sanitize_input(user_input).strip().lower()
    while sanitized_input not in allowed_choices:
        print(f"Invalid choice. Pleae sleect one of the allowed options.")
        user_input = input(f"Choose from {allowed_choices}: ")
        sanitized_input = sanitize_input(user_input).strip().lower()
    return sanitized_input

