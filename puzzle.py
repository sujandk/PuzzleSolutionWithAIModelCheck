from logic import *

AKnight = Symbol("A is a Knight")
AKnave = Symbol("A is a Knave")

BKnight = Symbol("B is a Knight")
BKnave = Symbol("B is a Knave")

CKnight = Symbol("C is a Knight")
CKnave = Symbol("C is a Knave")

# Puzzle 0
# A says "I am both a knight and a knave."
knowledge0 = And(
 # A is either a Knight or a Knave, but not both
    Or(AKnight, AKnave),
    Not(And(AKnight, AKnave)),

    # If A is a Knight, then A's statement must be true: A is both a Knight and a Knave (contradiction)
    Implication(AKnight, And(AKnight, AKnave)),

    # If A is a Knave, then A's statement must be false: A is not both a Knight and a Knave
    Implication(AKnave, Not(And(AKnight, AKnave)))
)

# Puzzle 1
# A says "We are both knaves."
# B says nothing.
knowledge1 = And(
      # A is either a Knight or a Knave, but not both
    Or(AKnight, AKnave),
    Not(And(AKnight, AKnave)),

    # B is either a Knight or a Knave, but not both
    Or(BKnight, BKnave),
    Not(And(BKnight, BKnave)),

    # If A is a Knight, then A's statement is true: both A and B are Knaves
    Implication(AKnight, And(AKnave, BKnave)),

    # If A is a Knave, then A's statement is false: it is not true that both A and B are Knaves
    Implication(AKnave, Not(And(AKnave, BKnave)))
)

# Puzzle 2
# A says "We are the same kind."
# B says "We are of different kinds."
knowledge2 = And(
      # A is either a Knight or a Knave, but not both
    Or(AKnight, AKnave),
    Not(And(AKnight, AKnave)),

    # B is either a Knight or a Knave, but not both
    Or(BKnight, BKnave),
    Not(And(BKnight, BKnave)),

    # If A is a Knight, A's statement is true: A and B are the same kind
    Implication(AKnight, Biconditional(AKnight, BKnight)),

    # If A is a Knave, A's statement is false: A and B are of different kinds
    Implication(AKnave, Not(Biconditional(AKnight, BKnight))),

    # If B is a Knight, B's statement is true: A and B are of different kinds
    Implication(BKnight, Not(Biconditional(AKnight, BKnight))),

    # If B is a Knave, B's statement is false: A and B are the same kind
    Implication(BKnave, Biconditional(AKnight, BKnight))
)

# Puzzle 3
# A says either "I am a knight." or "I am a knave.", but you don't know which.
# B says "A said 'I am a knave'."
# B says "C is a knave."
# C says "A is a knight."
knowledge3 = And(
     Or(AKnight, AKnave),
    Not(And(AKnight, AKnave)),

    # B is either a Knight or a Knave, but not both
    Or(BKnight, BKnave),
    Not(And(BKnight, BKnave)),

    # C is either a Knight or a Knave, but not both
    Or(CKnight, CKnave),
    Not(And(CKnight, CKnave)),

    # If B is a Knight, then A said "I am a Knave"
    Implication(BKnight, Biconditional(AKnave, AKnave)),

    # If B is a Knave, then B's statement is false, meaning A did not say "I am a Knave"
    Implication(BKnave, Not(Biconditional(AKnave, AKnave))),

    # B says C is a Knave
    Implication(BKnight, CKnave),
    Implication(BKnave, CKnight),

    # C says A is a Knight
    Implication(CKnight, AKnight),
    Implication(CKnave, AKnave)
)


def main():
    symbols = [AKnight, AKnave, BKnight, BKnave, CKnight, CKnave]
    puzzles = [
        ("Puzzle 0", knowledge0),
        ("Puzzle 1", knowledge1),
        ("Puzzle 2", knowledge2),
        ("Puzzle 3", knowledge3)
    ]
    for puzzle, knowledge in puzzles:
        print(puzzle)
        if len(knowledge.conjuncts) == 0:
            print("    Not yet implemented.")
        else:
            for symbol in symbols:
                if model_check(knowledge, symbol):
                    print(f"    {symbol}")


if __name__ == "__main__":
    main()
