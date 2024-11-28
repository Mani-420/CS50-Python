# Random Library


import random

# 1_ random.choice()
# 2_ random.choices()
# 2_ random.sample()

cards = ["Ace", "Jack", "Queen", "King"]

# print(random.choice(cards))
# print(random.choices(cards, k=2))
# print(random.sample(cards, k=2))
print(random.choices(cards,weights=[43, 25, 25, 7], k=2))
