from ex3.FantasyCardFactory import FantasyCardFactory
from ex3.AggressiveStrategy import AggressiveStrategy
from ex3.GameEngine import GameEngine


def main() -> None:
    print("=== DataDeck Game Engine ===")
    print("Configuring Fantasy Card Game...")

    factory = FantasyCardFactory()
    strategy = AggressiveStrategy()
    engine = GameEngine()

    engine.configure_engine(factory, strategy)

    print("Factory: FantasyCardFactory")
    print("Strategy: AggressiveStrategy")
    print(f"Available types: {factory.get_supported_types()}")

    print("\nSimulating aggressive turn...")

    turn_result = engine.simulate_turn()
    hand_str = ", ".join(
        f"{c.name} ({c.cost})" for c in turn_result["hand"]
    )

    print(f"Hand: [{hand_str}]")
    print("Turn execution:")
    print(f"Strategy: {turn_result['turn_execution']['Strategy']}")
    print(f"Actions: {turn_result['turn_execution']['Actions']}")

    print("\nGame Report:")
    print(engine.get_engine_status())

    print(
        "\nAbstract Factory + Strategy Pattern: "
        "Maximum flexibility achieved!"
    )


if __name__ == "__main__":
    main()
