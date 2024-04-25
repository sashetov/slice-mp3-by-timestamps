import sys

def parse_time(time_str):
    """Converts time string to total seconds."""
    parts = list(map(int, time_str.split(':')))
    seconds = sum(x * 60 ** i for i, x in enumerate(reversed(parts)))
    return seconds

def format_time(seconds):
    """Converts total seconds back to hh:mm:ss format."""
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    seconds = seconds % 60
    return f'{hours:02}:{minutes:02}:{seconds:02}'

def process_times(times):
    """Processes list of times and prints each accumulated time."""
    current_time = 0
    print('00:00:00')
    for time_str in times:
        current_time += parse_time(time_str)
        print(format_time(current_time))

def main(filename):
    try:
        with open(filename, 'r') as file:
            times = file.read().strip().split()
        process_times(times)
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(f"Usage: python {sys.argv[0]} <filename>")
        sys.exit(1)
    filename = sys.argv[1]
    main(filename)
