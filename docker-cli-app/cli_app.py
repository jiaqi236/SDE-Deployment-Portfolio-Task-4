import sys

def convert_minutes_to_time(total_minutes):
    """
    Convert a total number of minutes into hours, minutes, and seconds.
    Example: 125.5 minutes -> 2 hours, 5 minutes, 30 seconds
    """
    # Work in seconds to handle decimals cleanly
    total_seconds = round(total_minutes * 60)

    hours = total_seconds // 3600
    remaining = total_seconds % 3600
    minutes = remaining // 60
    seconds = remaining % 60

    return hours, minutes, seconds

def print_result(total_minutes, hours, minutes, seconds):
    print("=" * 50)
    print(f"  Total input: {total_minutes} minutes")
    print("=" * 50)
    print(f"  {hours} hour(s), {minutes} minute(s), {seconds} second(s)")
    print("=" * 50)

    # Human-readable summary
    parts = []
    if hours > 0:
        parts.append(f"{hours} hour{'s' if hours != 1 else ''}")
    if minutes > 0:
        parts.append(f"{minutes} minute{'s' if minutes != 1 else ''}")
    if seconds > 0:
        parts.append(f"{seconds} second{'s' if seconds != 1 else ''}")

    if not parts:
        print("  That's zero time!")
    else:
        print("  In words: " + ", ".join(parts))

def main():
    print()
    print("#############################################")
    print("#   Time Converter CLI (running in Docker)  #")
    print("#   Converts minutes to H : M : S           #")
    print("#############################################")
    print()

    # Mode 1: command-line argument (e.g., "docker run my-app 125")
    if len(sys.argv) == 2:
        try:
            total_minutes = float(sys.argv[1])
            if total_minutes < 0:
                print("Error: Minutes cannot be negative.")
                return
            h, m, s = convert_minutes_to_time(total_minutes)
            print_result(total_minutes, h, m, s)
        except ValueError:
            print(f"Error: '{sys.argv[1]}' is not a valid number.")
        return

    # Mode 2: interactive mode
    print("Enter a number of minutes to convert, or 'quit' to exit.")
    print("Examples: 90, 125.5, 10000")
    print("-" * 50)

    while True:
        user_input = input("\nMinutes > ").strip()
        if user_input.lower() in ("quit", "exit", "q"):
            print("Goodbye!")
            break

        try:
            total_minutes = float(user_input)
            if total_minutes < 0:
                print("Error: Minutes cannot be negative.")
                continue
            h, m, s = convert_minutes_to_time(total_minutes)
            print_result(total_minutes, h, m, s)
        except ValueError:
            print("Error: Please enter a valid number (e.g., 90 or 125.5).")

if __name__ == "__main__":
    main()