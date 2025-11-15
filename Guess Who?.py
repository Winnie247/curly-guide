from random import randint
from ai import characters, get_ai_character

#introduces the game
print("Let's play!")
print("GUESS WHO!")
print("( ͡° ͜ʖ ͡°)")

#generates the player
randomizer = randint(1,20)
r = randomizer

player, ReHa, BlHa, BrHa, BloHa, GrE, BrE, BlE, G = characters[r]

#code to give the ai a character
ai_player, ai_ReHa, ai_BlHa, ai_BrHa, ai_BloHa, ai_GrE, ai_BrE, ai_BlE, ai_G = get_ai_character()

print(f"\n🎭 Your character is {player}!")
print(f"🎭 The AI has chosen a character... can you guess who? ( ͠° ͟ʖ ͡°)")
print("( ͠° ͟ʖ ͡°)")

# Display all characters
print("\n" + "="*50)
print("CHARACTER SHEET:")
print("="*50)
for idx, (name, reha, blha, brha, bloha, gre, bre, ble, g) in characters.items():
    gender = "👨" if g else "👩"
    hair = ""
    if reha:
        hair = "🔴 Red Hair"
    elif blha:
        hair = "💛 Blonde Hair"
    elif brha:
        hair = "🟤 Brown Hair"
    elif bloha:
        hair = "🖤 Black Hair"
    
    eyes = ""
    if gre:
        eyes = "💚 Green Eyes"
    elif bre:
        eyes = "🟤 Brown Eyes"
    elif ble:
        eyes = "💙 Blue Eyes"
    
    print(f"{idx:2d}. {name:15} {gender} {hair:20} {eyes}")

print("="*50)
print("\n¯\\_(ツ)_/¯ Start guessing!\n")

# Display characteristics legend
print("="*50)
print("CHARACTERISTICS LEGEND:")
print("="*50)
print("Hair Colors:")
print("  🔴 Red Hair")
print("  💛 Blonde Hair")
print("  🟤 Brown Hair")
print("  🖤 Black Hair")
print("\nEye Colors:")
print("  💚 Green Eyes")
print("  🟤 Brown Eyes")
print("  💙 Blue Eyes")
print("\nGender:")
print("  👨 Male")
print("  👩 Female")
print("="*50 + "\n")

# Game loop
def play_game():
    remaining = set(range(1, 21))  # All character IDs
    ai_remaining = set(range(1, 21))  # AI's remaining suspects
    guesses = 0
    flipped = set()  # Characters player has flipped
    your_char = player
    
    print("\n" + "="*50)
    print("🎮 LET'S PLAY GUESS WHO! 🎮")
    print("="*50)
    print(f"I'm thinking of a character...")
    print(f"Characters remaining: {len(remaining)}")
    print("\nYou can ask questions like:")
    print("  - Does your character have red hair?")
    print("  - Is your character male?")
    print("  - Does your character have blue eyes?")
    print("="*50 + "\n")
    
    print("📋 YOUR BOARD:")
    display_player_board(flipped)
    
    while len(remaining) > 1 and len(ai_remaining) > 1:
        # PLAYER'S TURN
        print(f"\n📊 AI characters remaining: {len(remaining)}")
        
        # Ask question
        question = input("\n❓ Your question: ").strip()
        
        # Determine answer based on AI character
        answer = evaluate_question(question, ai_player, ai_ReHa, ai_BlHa, ai_BrHa, ai_BloHa, ai_GrE, ai_BrE, ai_BlE, ai_G)
        guesses += 1
        
        print(f"🤖 AI says: {'YES ✓' if answer else 'NO ✗'}")
        
        # Eliminate characters based on answer
        new_remaining = set()
        for char_id in remaining:
            name, reha, blha, brha, bloha, gre, bre, ble, g = characters[char_id]
            char_matches = evaluate_question(question, name, reha, blha, brha, bloha, gre, bre, ble, g)
            
            # Keep characters that match the AI's answer
            if char_matches == answer:
                new_remaining.add(char_id)
        
        remaining = new_remaining
        
        if not remaining:
            print("\n(╯°□°)╯︵ ┻━┻ Hmm, something went wrong with the logic!")
            return
        
        # Show who's left
        if len(remaining) <= 6:
            print("\n👥 AI's remaining suspects:")
            for char_id in sorted(remaining):
                name, _, _, _, _, _, _, _, _ = characters[char_id]
                print(f"   • {name}")
        
        # Check if player wants to guess
        if len(remaining) <= 3:
            guess_input = input("\n🎯 Do you want to make a guess? (yes/no): ").strip().lower()
            if guess_input in ['yes', 'y']:
                if len(remaining) == 1:
                    guess_id = list(remaining)[0]
                    guess = characters[guess_id][0]
                    print(f"\n🎉 You guessed: {guess}")
                else:
                    guess = input("Who do you think it is? ").strip()
                    for char_id in remaining:
                        if characters[char_id][0].lower() == guess.lower():
                            guess_id = char_id
                            break
                    else:
                        print(f"\n❌ {guess} isn't even a suspect anymore!")
                        continue
                
                if guess.lower() == ai_player.lower():
                    print(f"\n🏆 CORRECT! It was {ai_player}! 🏆")
                    print(f"You got it in {guesses} questions! ୧༼ಠ益ಠ༽୨")
                    return
                else:
                    print(f"\n(╯°□°)╯︵ ┻━┻ Wrong! It was {ai_player}!")
                    return
        
        # AI'S TURN
        print(f"\n\n🤖 AI's turn...")
        print(f"📊 AI has {len(ai_remaining)} suspects remaining")
        
        if len(ai_remaining) <= 1:
            break
        
        ai_question = generate_ai_question(ai_remaining)
        print(f"\n🤖 AI asks: {ai_question}")
        
        # Get player's answer
        player_answer = input("Your answer (yes/no): ").strip().lower()
        player_answer = player_answer in ['yes', 'y']
        
        # Check if player is telling the truth
        correct_answer = evaluate_question(ai_question, your_char, ReHa, BlHa, BrHa, BloHa, GrE, BrE, BlE, G)
        
        if player_answer != correct_answer:
            print(f"\n😏 Wait a minute... that doesn't match! You're CHEATING! 🤖 CAUGHT YOU!")
            print(f"Your character is {your_char}, so the answer should be: {'YES ✓' if correct_answer else 'NO ✗'}")
            print(f"\n🏆 I WON because you CHEATED! 🏆")
            print(f"I knew your character was {your_char}! ( ͡° ͜ʖ ͡°)")
            return
        
        print(f"✓ OK!")
        
        # Eliminate characters based on answer
        new_ai_remaining = set()
        for char_id in ai_remaining:
            name, reha, blha, brha, bloha, gre, bre, ble, g = characters[char_id]
            char_matches = evaluate_question(ai_question, name, reha, blha, brha, bloha, gre, bre, ble, g)
            
            if char_matches == player_answer:
                new_ai_remaining.add(char_id)
        
        ai_remaining = new_ai_remaining
        
        if not ai_remaining:
            print("\n🤖 Hmm, something's not right...")
            return
        
        # Show what's left for AI
        if len(ai_remaining) <= 6:
            print(f"\n🤖 AI's remaining suspects: {len(ai_remaining)}")
            for char_id in sorted(ai_remaining):
                name, _, _, _, _, _, _, _, _ = characters[char_id]
                print(f"   • {name}")
        
        # AI makes a guess if narrowed down enough
        if len(ai_remaining) <= 2:
            if len(ai_remaining) == 1:
                ai_guess = characters[list(ai_remaining)[0]][0]
            else:
                ai_guess = characters[list(ai_remaining)[0]][0]
            
            print(f"\n🤖 I think you are... {ai_guess}!")
            
            if ai_guess.lower() == your_char.lower():
                print(f"\n🏆 I WON! You were {ai_guess}! 🏆")
                print(f"I got it in {guesses} questions! ୧༼ಠ益ಠ༽୨")
                return
            else:
                print(f"\n(╯°□°)╯︵ ┻━┻ I guessed wrong! You were {your_char}!")
                return

def generate_ai_question(remaining):
    """Generate a smart question based on remaining suspects"""
    # Count traits
    red_hair = sum(1 for char_id in remaining if characters[char_id][1])
    blonde_hair = sum(1 for char_id in remaining if characters[char_id][2])
    brown_hair = sum(1 for char_id in remaining if characters[char_id][3])
    black_hair = sum(1 for char_id in remaining if characters[char_id][4])
    green_eyes = sum(1 for char_id in remaining if characters[char_id][5])
    brown_eyes = sum(1 for char_id in remaining if characters[char_id][6])
    blue_eyes = sum(1 for char_id in remaining if characters[char_id][7])
    male = sum(1 for char_id in remaining if characters[char_id][8])
    
    total = len(remaining)
    traits = [
        (red_hair, "Does your character have red hair?"),
        (blonde_hair, "Does your character have blonde hair?"),
        (brown_hair, "Does your character have brown hair?"),
        (black_hair, "Does your character have black hair?"),
        (green_eyes, "Does your character have green eyes?"),
        (brown_eyes, "Does your character have brown eyes?"),
        (blue_eyes, "Does your character have blue eyes?"),
        (male, "Is your character male?"),
    ]
    
    # Pick trait that splits remaining characters roughly in half
    best_trait = min(traits, key=lambda x: abs(x[0] - total/2))
    return best_trait[1]

def display_player_board(flipped):
    """Display player's board of flipped characters"""
    print("\n" + "="*70)
    for row in range(0, 20, 5):
        for col in range(5):
            char_id = row + col + 1
            if char_id <= 20:
                name, _, _, _, _, _, _, _, _ = characters[char_id]
                if char_id in flipped:
                    print(f"✓ {name:15}", end=" ")
                else:
                    print(f"  {name:15}", end=" ")
        print()
    print("="*70)

def evaluate_question(question, name, reha, blha, brha, bloha, gre, bre, ble, g):
    """Evaluate if a question applies to a character"""
    q = question.lower()
    
    # Hair color questions
    if any(word in q for word in ['red hair', 'red', 'ginger']):
        return reha
    if any(word in q for word in ['blonde', 'blonde hair', 'blond', 'yellow']):
        return blha
    if any(word in q for word in ['brown hair', 'brown', 'brunette']):
        return brha
    if any(word in q for word in ['black hair', 'black', 'dark hair']):
        return bloha
    
    # Eye color questions
    if any(word in q for word in ['green eye', 'green']):
        return gre
    if any(word in q for word in ['brown eye', 'brown']):
        return bre
    if any(word in q for word in ['blue eye', 'blue']):
        return ble
    
    # Gender questions
    if any(word in q for word in ['male', 'man', 'boy', 'he', 'him', 'his']):
        return g
    if any(word in q for word in ['female', 'woman', 'girl', 'she', 'her']):
        return not g
    
    # Name-based questions
    if 'name' in q or 'called' in q or 'is' in q:
        name_keywords = name.lower().split()
        if any(keyword in q for keyword in name_keywords):
            return True
        return False
    
    # Default: can't determine
    print("🤔 I don't understand that question. Try asking about hair, eyes, or gender!")
    return True

# Start the game
play_game()



