from ex0.factories import CreatureFactory, FlameFactory, AquaFactory
from ex1.factories import HealingCreatureFactory, TransformCreatureFactory
from ex2.strategies import (
    BattleStrategy,
    NormalStrategy,
    AggressiveStrategy,
    DefensiveStrategy,
    InvalidStrategyError
)


def battle(opponents: list[tuple[CreatureFactory, BattleStrategy]]) -> None:
    print("*** Tournament ***")
    print(f"{len(opponents)} opponents involved")

    for i in range(len(opponents)):
        for j in range(i + 1, len(opponents)):
            print("* Battle *")
            f1, s1 = opponents[i]
            f2, s2 = opponents[j]

            c1 = f1.create_base()
            c2 = f2.create_base()

            print(c1.describe())
            print("VS.")
            print(c2.describe())
            print("now fight!")

            try:
                s1.act(c1)
                s2.act(c2)
            except InvalidStrategyError as e:
                print(f"Battle error, aborting tournament: {e}")
                return


def main() -> None:
    flame = FlameFactory()
    aqua = AquaFactory()
    heal = HealingCreatureFactory()
    transform = TransformCreatureFactory()

    normal = NormalStrategy()
    defensive = DefensiveStrategy()
    aggressive = AggressiveStrategy()

    print("Tournament 0 (basic)")
    print("[(Flameling+Normal), (Healing+Defensive)]")
    battle([(flame, normal), (heal, defensive)])

    print("\nTournament 1 (error)")
    print("[(Flameling+Aggressive), (Healing+Defensive)]")
    battle([(flame, aggressive), (heal, defensive)])

    print("\nTournament 2 (multiple)")
    print("[(Aquabub+Normal), (Healing+Defensive), (Transform+Aggressive)]")
    battle([(aqua, normal), (heal, defensive), (transform, aggressive)])


if __name__ == "__main__":
    main()
