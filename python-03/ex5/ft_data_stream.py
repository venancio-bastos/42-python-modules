
from typing import Generator

def generate_game_events(total: int) -> Generator[str, None, None]:
    """
    Generates game events on-demand using the yield keyword.
    Produces a continuous stream of data without storing it in memory [cite: 341-342].
    """
    players = ["alice", "bob", "charlie", "diana"]
    actions = ["killed monster", "found treasure", "leveled up", "explored cave"]
    
    for i in range(total):

        player = players[i % len(players)]
        level = (i % 15) + 1
        action = actions[(i * 3) % len(actions)]
        

        yield f"Player {player} (level {level}) {action}"


def fibonacci_generator(limit: int) -> Generator[int, None, None]:
    """Generates the Fibonacci sequence on-demand up to a given limit."""
    a = 0
    b = 1
    for _ in range(limit):
        yield a
        c = a + b
        a = b
        b = c


def prime_generator(limit: int) -> Generator[int, None, None]:
    """Generates a sequence of prime numbers on-demand up to a given limit."""
    count = 0
    n = 2
    while count < limit:
        is_prime = True
        for i in range(2, n):
            if n % i == 0:
                is_prime = False
                break
        if is_prime:
            yield n
            count += 1
        n += 1


def main() -> None:
    """
    Processes the data streams and calculates statistics on the fly.
    Demonstrates the memory efficiency of generator functions [cite: 351-352].
    """
    print("=== Game Data Stream Processor ===")
    
    total_to_process = 1000
    print(f"Processing {total_to_process} game events...\n")
    

    event_stream = generate_game_events(total_to_process)
    

    total_events = 0
    high_level_players = 0
    treasure_events = 0
    level_up_events = 0
    

    for event in event_stream:
        total_events += 1
        

        if total_events <= 3:
            print(f"Event {total_events}: {event}")
            

        if "treasure" in event:
            treasure_events += 1
        if "leveled up" in event:
            level_up_events += 1
            

        for high_lvl in range(10, 16):
            if f"(level {high_lvl})" in event:
                high_level_players += 1
                break

    print("\n=== Stream Analytics ===")
    print(f"Total events processed: {total_events}")
    print(f"High-level players (10+): {high_level_players}")
    print(f"Treasure events: {treasure_events}")
    print(f"Level-up events: {level_up_events}")
    
    print("\nMemory usage: Constant (streaming)")
    print("Processing time: Lightning fast!")
    
    print("\n=== Generator Demonstration ===")
    

    fib_gen = fibonacci_generator(10)

    fib_list = []
    for num in fib_gen:
        fib_list.append(str(num))
    print(f"Fibonacci sequence (first 10): {', '.join(fib_list)}")
    
    prime_gen = prime_generator(5)
    prime_list = []
    for num in prime_gen:
        prime_list.append(str(num))
    print(f"Prime numbers (first 5): {', '.join(prime_list)}")


if __name__ == "__main__":
    main()