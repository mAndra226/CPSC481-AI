# Stephnaie Becerra
# Marco Andrade
# Brandon Evans
# Jack Loague

from logic import *

colors = ["red", "blue", "green", "purple"]
positions = [0, 1, 2, 3]
symbols = []
for i in range(4):
    for color in colors:
        symbols.append(Symbol(f"{color}{i}"))

knowledge = And()

# Each color has a position.
for color in colors:
    knowledge.add(Or(
        Symbol(f"{color}0"),
        Symbol(f"{color}1"),
        Symbol(f"{color}2"),
        Symbol(f"{color}3")
    ))

# Only one position per color.
for color in colors:
    for p1 in positions:
        for p2 in positions:
            if p1 != p2:
                knowledge.add(
                    Implication(Symbol(f"{color}{p1}"), Not(Symbol(f"{color}{p2}")))
                )

# Only one color per position.
for position in positions:
    for c1 in colors:
        for c2 in colors:
            if c1 != c2:
                knowledge.add(
                    Implication(Symbol(f"{c1}{position}"), Not(Symbol(f"{c2}{position}")))
                )

# First Guess
knowledge.add(
    And(
        (Symbol("red0")), (Symbol("blue1")), Not(Symbol("green2")), Not(Symbol("purple3"))
    )
)

# Second Guess
knowledge.add(
    And(
        Not(Symbol("blue0")), Not(Symbol("red1")), Not(Symbol("green2")), Not(Symbol("purple3"))
    )
)

for symbol in symbols:
    if model_check(knowledge, symbol):
        print(symbol)

"""
red0
blue1
purple2
green3
"""