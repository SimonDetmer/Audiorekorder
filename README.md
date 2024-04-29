# Audio Recorder
An audio recorder for capturing MP3 streams from the internet.

The following settings should be customizable:

- URL of the stream
- Recording duration
- File name for the saved stream
- Block size for read/write operations
- Optional: Display of all saved streams
- Optional: Display of help/usage information

Create a CLI audio recorder (you should use common packages, such as Argparse, Click, Docopt, Invoke, ..).

Invocation:

```bash
cli_audiorecorder.py <url> [--filename=<name>] [--duration=<time>] [--blocksize=<size>]
```

Example of CLI usage:

```bash
Usage:
  cli_audiorecorder.py <url> [--filename=<name>] [--duration=<time>] [--blocksize=<size>]
  cli_audiorecorder.py -h | --help

Options:
  -h --help             Show this screen.
  --filename=<name>     Name of recording [default: myRadio].
  --duration=<time>     Duration of recording in seconds [default: 30].
  --blocksize=<size>    Block size for read/write in bytes [default: 64].
```
