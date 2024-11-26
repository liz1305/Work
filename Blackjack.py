import random

# Start the game loop
while True:
    # Initial hands
    user_hand = [random.choice(['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']),
                 random.choice(['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A'])]
    computer_hand = [random.choice(['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']),
                     random.choice(['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A'])]


    # having 2 duplicate of the same value is becoz we need to take 2 cards for each person hands/ com
    def calculate_score(hand):
        score = 0
        for card in hand:
            score += card_value(card)

            # Function to convert card to value


    def card_value(card):
        if card in ['J', 'Q', 'K']:
            return 10
        elif card == 'A':
            return 11
        else:
            return int(card)

            # Calculate scores


    user_score = 0
    for card in user_hand:
        user_score += card_value(
            card)  # plus both card tgt even the card u added brand new after typing y for adding more cards
    computer_score = 0
    for card in computer_hand:
        computer_score += card_value(card)  # same thing as the above explanation
    # Check for blackjack
    user_blackjack = (user_score == 21)
    computer_blackjack = (computer_score == 21)

    # Show the player's and dealer's cards
    print("\nYour cards:", user_hand)
    print("Your score:", user_score)
    print("\nDealer's first card:", computer_hand[0])

    # Immediate win/loss on blackjack
    if computer_blackjack:
        print("\nDealer has blackjack! You lose.")
    elif user_blackjack:
        print("\nYou have blackjack! You win.")
    else:
        # Player's turn
        while True:
            choice = input("Type 'y' to get another card, 'n' to stop: ").lower()
            if choice == 'y':
                # Draw a new card for the player
                new_card = random.choice(['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A'])
                user_hand.append(new_card)
                user_score = sum(card_value(card) for card in user_hand)

                # Adjust for ace if over 21
                if user_score > 21:
                    for i in range(len(user_hand)):
                        if user_hand[i] == 'A' and user_score > 21:
                            user_hand[i] = '1'  # Change Ace to 1
                            user_score = 0
                            for card in user_hand:
                                user_score += card_value(card)  # plus the 2 card tgt that we got from the randomizer

                print("\nYour cards:", user_hand)
                print("Your score:", user_score)

                if user_score > 21:
                    print("Bust! You lose.")
                    break
            else:
                break

                # Computer's turn if player hasn't busted
        if user_score <= 21:
            while computer_score < 17:
                new_card = random.choice(['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A'])
                computer_hand.append(new_card)
                user_score = 0
                for card in user_hand:
                    user_score += card_value(card)

                    # Adjust for ace if over 21
                if computer_score > 21:
                    for i in range(len(computer_hand)):
                        if computer_hand[i] == 'A' and computer_score > 21:
                            computer_hand[i] = '1'  # Change Ace to 1
                            computer_score = 0
                            for card in computer_hand:
                                computer_score += card_value(card)
                 if user_score <= 21:
                    while computer_score < 17:
                        new_card = random.choice(['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A'])
                        computer_hand.append(new_card)
                        computer_score = calculate_score(computer_hand)
# Show final hands and scores
        if user_score <= 21:

         print("Your final hand:", user_hand)
         print("Your final score:", user_score)
         print("\nDealer's final hand:", computer_hand)
         print("Dealer's final score:", computer_score)
         print("\n=====================")
    # Determine winner
     if computer_score > 21:
        while:
             print("Dealer busts! You win.")
         elif user_score > computer_score:
            print("You win!")
         elif user_score < computer_score:
            print("You lose.")
         else:
            print("It's a draw.")

    # Ask if the player wants to play again
play_again = input("\nDo you want to play again? (y/n): " ).lower()
       # .lower mean it change the capital letters into small letter
if play_again != 'y':
    break