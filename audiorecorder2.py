#!/usr/bin/env python

"""
Installierte Module:
- urllib.request: Zur Verwendung von URLs
- datetime: Zur Verwendung von Datums- und Zeitobjekten
- click: Zur Erstellung der Befehlzeilenanweisung
- os: Zur Interaktion mit dem Betriebssystem
"""
import urllib.request
import datetime
import click
import os

"""
Dekoratorfunktionen:
- @click.command(): Wandelt die folgende Funktion in eine Befehlzeilenanwendung um
- @click.argument(): Deklariert ein Argument namens 'url', greift auf default-url zurück, wenn nichts angegeben wird
- @click.option(): Deklariert Optionen für die Befehlszeilenanwendung, in diesem Falle Dauer, Dateiname, Größe und gespeicherte Daten 
"""
@click.command()
@click.argument('url', default='http://st01.dlf.de/dlf/01/128/mp3/stream.mp3', required=False)
@click.option('--duration', '-d', default=30, help='Duration of the recording in seconds')
@click.option('--filename', '-f', default='myRadio.mp3', help='Filename of the saved stream')
@click.option('--blocksize', '-b', default=64, help='Block size for reading/writing')
@click.option('--list-streams', '-l', is_flag=True, help='Display all saved streams')


# Die Hauptfunktion, die den Befehlszeilenbefehl definiert und das Verhalten der Anwendung
# festlegt. Sie nimmt die Argumente und Optionen entgegen, die vom Benutzer
# auf der Befehlszeile angegeben werden.

def record_stream(url, duration, filename, blocksize, list_streams):
    #Überprüft, ob die Option --list-streams angegeben wurde.
    if list_streams:
        # Gibt Liste gespeicherter mp3s aus.
        click.echo('List of saved streams:')
        # Durchläuft alle Dateien im aktuellen Verzeichnis.
        for file in os.listdir('.'):
            # Überprüft, ob die Datei mit ".mp3" endet.
            if file.endswith('.mp3'):
                click.echo(file)
    # Wenn keine Option --list-streams angegeben wurde, wird dieser Block ausgeführt.
    elif url:
        # Speichert die aktuelle Zeit als Startzeit für die Aufnahme.
        start_time = datetime.datetime.now()
        # Öffnet die URL und liest den Stream.
        with urllib.request.urlopen(url) as stream:
            # Öffnet eine Datei im Binärmodus zum Schreiben.
            with open(filename, 'wb') as outfile:
                # Während die Aufnahmedauer nicht erreicht ist, liest der Code Blöcke von Daten vom Stream und schreibt sie in die Datei.
                while (datetime.datetime.now() - start_time).seconds < duration:
                    outfile.write(stream.read(blocksize))
        # Gibt eine Nachricht auf der Befehlszeile aus, wenn die Aufnahme abgeschlossen ist.
        click.echo('Recording completed.')

#     Überprüft, ob das Skript direkt ausgeführt wird.
#     record_stream(): Wenn ja, wird die Funktion record_stream() aufgerufen, um die Befehlszeilenanwendung auszuführen.
if __name__ == '__main__':
    record_stream()


#Beispielaufruf
#python audiorecorder2.py --duration 20 --filename recording.mp3 --blocksize 256 http://example.com/stream

#Anzeige der gespeicherten Streams
# python audiorecorder2.py --list-streams

# Anzeige der Hilfe- und Verwendungsinformationen
# python audiorecorder2.py --help
