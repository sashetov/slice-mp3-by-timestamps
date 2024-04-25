import sys
import subprocess
from multiprocessing import Pool

def convert_time_to_seconds(time_str):
    """
    Converts a time string in HH:MM:SS, MM:SS, or SS format to seconds.
    Raises ValueError if seconds or minutes are not between 0 and 59.
    """
    parts = time_str.split(':')
    seconds = 0
    parts = list(map(int, parts[::-1]))
    if any(p > 59 for p in parts[:-1]):
        raise ValueError('Seconds and minutes must be between 0 and 59')
    for i, part in enumerate(parts):
        if i == 0:  # Seconds
            seconds += part
        elif i == 1:  # Minutes
            seconds += part * 60
        elif i == 2:  # Hours
            seconds += part * 3600
    return seconds

def process_tracks(filename):
    """
    Reads a file containing tracks with their end times, converts time to
    seconds, and returns a list of [track_name, timestamp] pairs.
    """
    with open(filename, 'r') as file:
        lines = file.readlines()
    timestamps = {}
    tracks=[]
    for line in lines:
        *name_parts, time_str = line.strip().split()
        key = ' '.join(name_parts)
        timestamp = convert_time_to_seconds(time_str)
        timestamps[key] = timestamp
        tracks.append([key, timestamp])
    return tracks

def process_track(args):
    """
    Processes a single track by creating an ffmpeg command to extract it from
    the input file.
    Accepts a tuple containing the input file name, current track, and start
    time of next track.
    """
    input_file, track, next_start = args
    track_name, start = track
    if next_start is not None:
        duration = next_start - start
        cmd = f"ffmpeg -i '{input_file}' -ss {start} -t {duration} -acodec copy '{track_name}.mp3'"
    else:
        cmd = f"ffmpeg -i '{input_file}' -ss {start} -acodec copy '{track_name}.mp3'"
    print(cmd)
    subprocess.run(cmd, shell=True)

def run_ffmpeg_commands(input_file, tracks):
    """
    Schedules ffmpeg commands for a list of tracks using multiprocessing to
    execute them concurrently.
    """
    with Pool() as pool:
        tasks = [(input_file, tracks[i], tracks[i + 1][1] if i + 1 < len(tracks) else None) for i in range(len(tracks))]
        pool.map(process_track, tasks)

def main():
    """
    Main function to process the input MP3 file using timestamps from a
    provided file, extracts tracks using ffmpeg.
    Exits with usage message on missing arguments.
    """
    if len(sys.argv) != 3:
        print(f"Usage: {sys.argv[0]} <timestamps_filename> <input_file>")
        sys.exit(1)
    ts_file_name = sys.argv[1]
    input_file = sys.argv[2]
    print(f"Processing input file: {input_file} with timestamps file: {ts_file_name}")
    tracks = process_tracks(ts_file_name)
    run_ffmpeg_commands(input_file, tracks)

if __name__ == "__main__":
    main()
