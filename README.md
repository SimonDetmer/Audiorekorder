# Audiorekorder
Audiorekorder um mp3-Streams aus dem Internet aufzunehmen

Dabei sollen folgende Einstellungen parametrisiert / eingestellt werden können:

    URL des Streams
    Dauer der Aufnahme
    Dateiname des gespeicherten Streams
    Blockgröße beim Lesen/Schreiben
    Optional: Anzeige aller gespeicherten Streams
    ggf. Anzeige von Hilfe-/ Usage-Infos

Erstellen Sie einen CLI-Audiorekorder (Sie sollten gängige Packages verwenden, z. B. Argparse, Click, Docopt, Invoke, ..)
Aufruf:

  cli_audiorecorder.py <url> [--filename=<name>] [--duration=<time>] [--blocksize=<size>]


Beispiel für CLI:

Usage:
  cli_audiorecorder.py <url> [--filename=<name>] [--duration=<time>] [--blocksize=<size>]
  cli_audiorecorder.py -h | --help

Options:
  -h --help             Show this screen.
  --filename=<name>     Name of recording [default: myRadio].
  --duration=<time>     Duration of recording in seconds [default: 30].
  --blocksize=<size>    Block size for read/write in bytes [default: 64].
