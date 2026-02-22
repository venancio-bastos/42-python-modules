import sys
import math

def calculate_distance(point1: tuple[int, int, int], point2: tuple[int, int, int]) -> float:
    """
    Calculates the Euclidean distance between two 3D points[cite: 224].
    Uses tuple unpacking to extract x, y, z coordinates.
    """
    x1, y1, z1 = point1
    x2, y2, z2 = point2
    
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2 + (z2 - z1)**2)


def parse_coordinates(coord_str: str) -> tuple[int, int, int]:
    """
    Parses a string of format "x,y,z" into a tuple of integers[cite: 225].
    Can raise a ValueError if the string contains non-numeric characters[cite: 244].
    """
    parts = coord_str.split(',')
    
    return (int(parts[0]), int(parts[1]), int(parts[2]))


def main() -> None:
    """
    Demonstrates the creation, parsing, unpacking, and distance calculation
    of 3D coordinate tuples, while handling potential errors gracefully.
    """
    print("=== Game Coordinate System ===")
    
    origin = (0, 0, 0)
    
    pos1 = (10, 20, 5)
    print(f"Position created: {pos1}")
    
    dist1 = calculate_distance(origin, pos1)
    print(f"Distance between {origin} and {pos1}: {dist1:.2f}")
    
    valid_str = "3,4,0"
    print(f"\nParsing coordinates: \"{valid_str}\"")
    parsed_pos = parse_coordinates(valid_str)
    print(f"Parsed position: {parsed_pos}")
    
    dist2 = calculate_distance(origin, parsed_pos)
    print(f"Distance between {origin} and {parsed_pos}: {dist2:.1f}")
    
    invalid_str = "abc, def, ghi"
    print(f"\nParsing invalid coordinates: \"{invalid_str}\"")
    try:
        parse_coordinates(invalid_str)
    except ValueError as e:
        print(f"Error parsing coordinates: {e}")
        print(f"Error details Type: {type(e).__name__}, Args: {e.args}")
        
    print("\nUnpacking demonstration:")
    x, y, z = parsed_pos
    print(f"Player at X={x}, Y={y}, Z={z}")
    print(f"Coordinates: X={x} Y={y} Z={z}")


if __name__ == "__main__":
    main()