import functools
import operator
from typing import List, Callable, Dict, Any


def spell_reducer(spells: List[int], operation: str) -> int:
    operations = {
        "add": operator.add,
        "multiply": operator.mul,
        "max": max,
        "min": min
    }
    
    op_func = operations.get(operation)
    if not op_func:
        raise ValueError("Invalid operation")
        
    return functools.reduce(op_func, spells)


def partial_enchanter(base_enchantment: Callable) -> Dict[str, Callable]:
    return {
        "fire_enchant": functools.partial(
            base_enchantment, power=50, element="fire"
        ),
        "ice_enchant": functools.partial(
            base_enchantment, power=50, element="ice"
        ),
        "lightning_enchant": functools.partial(
            base_enchantment, power=50, element="lightning"
        )
    }


@functools.lru_cache(maxsize=None)
def memoized_fibonacci(n: int) -> int:
    if n <= 1:
        return n
    return memoized_fibonacci(n - 1) + memoized_fibonacci(n - 2)


def spell_dispatcher() -> Callable:
    @functools.singledispatch
    def dispatch(arg: Any) -> str:
        return "Unknown magic type"

    @dispatch.register(int)
    def _(arg: int) -> str:
        return f"Casting damage spell with {arg} power"

    @dispatch.register(str)
    def _(arg: str) -> str:
        return f"Applying {arg} enchantment"

    @dispatch.register(list)
    def _(arg: list) -> str:
        return f"Multi-casting {len(arg)} spells"

    return dispatch


def main() -> None:
    print("Testing spell reducer...")
    spells = [10, 20, 30, 40]
    print(f"Sum: {spell_reducer(spells, 'add')}")
    print(f"Product: {spell_reducer([10, 20, 30, 40], 'multiply')}")
    print(f"Max: {spell_reducer(spells, 'max')}")

    print("\nTesting memoized fibonacci...")
    print(f"Fib(10): {memoized_fibonacci(10)}")
    print(f"Fib(15): {memoized_fibonacci(15)}")

    print("\nTesting partial enchanter...")
    
    def base_ench(target: str, power: int, element: str) -> str:
        return f"Enchanting {target} with {element} (Power: {power})"
    
    enchants = partial_enchanter(base_ench)
    print(enchants["fire_enchant"](target="Sword"))
    print(enchants["lightning_enchant"](target="Shield"))

    print("\nTesting spell dispatcher...")
    dispatcher = spell_dispatcher()
    print(dispatcher(50))
    print(dispatcher("Invisibility"))
    print(dispatcher(["fireball", "heal"]))


if __name__ == "__main__":
    main()
