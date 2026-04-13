from typing import Callable, Any, Tuple, List


def spell_combiner(spell1: Callable, spell2: Callable) -> Callable:
    def combined_spell(*args: Any, **kwargs: Any) -> Tuple[Any, Any]:
        return (spell1(*args, **kwargs), spell2(*args, **kwargs))
    return combined_spell


def power_amplifier(base_spell: Callable, multiplier: int) -> Callable:
    def amplified_spell(*args: Any, **kwargs: Any) -> Any:
        return base_spell(*args, **kwargs) * multiplier
    return amplified_spell


def conditional_caster(condition: Callable, spell: Callable) -> Callable:
    def cast_spell(*args: Any, **kwargs: Any) -> Any:
        if condition(*args, **kwargs):
            return spell(*args, **kwargs)
        return "Spell fizzled"
    return cast_spell


def spell_sequence(spells: List[Callable]) -> Callable:
    def cast_sequence(*args: Any, **kwargs: Any) -> List[Any]:
        return [spell(*args, **kwargs) for spell in spells]
    return cast_sequence


def main() -> None:
    def fireball(target: str) -> str:
        return f"Fireball hits {target}"

    def heal(target: str) -> str:
        return f"Heals {target}"

    def damage_spell(power: int) -> int:
        return power

    def is_enemy(target: str) -> bool:
        return target == "Enemy"

    print("Testing spell combiner...")
    combined = spell_combiner(fireball, heal)
    res1, res2 = combined("Dragon")
    print(f"Combined spell result: {res1}, {res2}")

    print("\nTesting power amplifier...")
    mega_fireball = power_amplifier(damage_spell, 3)
    print(f"Original: {damage_spell(10)}, Amplified: {mega_fireball(10)}")

    print("\nTesting conditional caster...")
    smart_attack = conditional_caster(is_enemy, fireball)
    print(smart_attack("Enemy"))
    print(smart_attack("Friend"))

    print("\nTesting spell sequence...")
    sequence = spell_sequence([fireball, heal, fireball])
    for result in sequence("Goblin"):
        print(result)


if __name__ == "__main__":
    main()