from random import randint

characters = {
    1: ("Bob", False, True, False, False, True, False, False, True),
    2: ("Martha", False, False, False, True, False, False, True, False),
    3: ("John", True, False, False, False, False, True, False, True),
    4: ("Sarah", False, True, False, False, False, False, True, False),
    5: ("Michael", False, False, True, False, True, False, False, True),
    6: ("Jennifer", True, False, False, False, False, True, False, False),
    7: ("David", False, False, False, True, False, False, True, True),
    8: ("Lisa", False, True, False, False, False, False, True, False),
    9: ("James", True, False, False, False, True, False, False, True),
    10: ("Emily", False, False, True, False, False, True, False, False),
    11: ("William", False, True, False, False, True, False, False, True),
    12: ("Sophie", True, False, False, False, False, False, True, False),
    13: ("Christopher", False, False, False, True, False, True, False, True),
    14: ("Amanda", False, True, False, False, False, True, False, False),
    15: ("Daniel", True, False, False, False, True, False, False, True),
    16: ("Rachel", False, False, True, False, False, False, True, False),
    17: ("Kevin", False, True, False, False, False, False, True, True),
    18: ("Nicole", True, False, False, False, True, False, False, False),
    19: ("Ryan", False, False, True, False, True, False, False, True),
    20: ("Jessica", False, True, False, False, False, True, False, False),
}

def get_ai_character():
    """Assign a random character to the AI"""
    ai_r = randint(1, 20)
    ai_player, ai_ReHa, ai_BlHa, ai_BrHa, ai_BloHa, ai_GrE, ai_BrE, ai_BlE, ai_G = characters[ai_r]
    return ai_player, ai_ReHa, ai_BlHa, ai_BrHa, ai_BloHa, ai_GrE, ai_BrE, ai_BlE, ai_G
