# mp3_slicer

## Use Value
- this tool is useful for cutting up mixtapes you downloaded off youtube or elsewhere into individual tracks based on a timestamped tracklist you provide in another file

## Prereqs
- working ffmpeg w/ codecs for mp3 installed

## Building and running
- building
    ```
    $ ./build.sh
    ```
    - builds cython binary that you can then put in your `PATH` at your discretion
- running
    ```
    $ python mp3_slicer.py
    Usage: mp3_slicer.py <timestamps_filename> <input_file>
    $ ./dist/mp3_slicer
    Usage: ./dist/mp3_slicer <timestamps_filename> <input_file>
    ```

## Usage
```
$ mp3_slicer
Usage: mp3_slicer <timestamps_filename> <input_file>
```

## Timestamps file format
- The timestamps file looks something like this:
    ```
    this is what the mp3 output file 1 will be called 00:00
    this is what the mp3 output file 2 will be called 01:23
    ...
    this is what the mp3 output file n will be called 02:14:23
    ```
- The last file gets sliced to the end of the original file's length.

## Input file
- The program has only been tested with mp3 input but since its using ffmpeg binary it should support any number of inputs, so YMMV
