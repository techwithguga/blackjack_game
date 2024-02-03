import random

def deal_card():
  """Returns a random card from the deck."""
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  card = random.choice(cards)
  return card

random_card = deal_card()
print(random_card)

user_cards = [deal_card(),deal_card()]
computer_cards = [deal_card(),deal_card()]
sum_of_user_cards = user_cards[0] + user_cards[1]
sum_of_computer_cards = computer_cards[0] + computer_cards[1]

has_blackjack = True
ace=11

def check_blackjack(cards):
    if ace in cards and cards[0]+cards[1] == 21:
        return has_blackjack
    else:
        return has_blackjack == False

blackjack_user = check_blackjack(user_cards)
blackjack_computer = check_blackjack(computer_cards)


print(user_cards)
print(computer_cards)
print(sum_of_user_cards)
print(sum_of_computer_cards)

print(blackjack_user)
print(blackjack_computer)
    