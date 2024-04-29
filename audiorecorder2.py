import urllib.request
import datetime
import click
import os


@click.command()
@click.argument('url', default='http://st01.dlf.de/dlf/01/128/mp3/stream.mp3', required=False)
@click.option('--duration', '-d', default=30, help='Duration of the recording in seconds')
@click.option('--filename', '-f', default='myRadio.mp3', help='Filename of the saved stream')
@click.option('--blocksize', '-b', default=64, help='Block size for reading/writing')
@click.option('--list-streams', '-l', is_flag=True, help='Display all saved streams')

def record_stream(url, duration, filename, blocksize, list_streams):
    if list_streams:
        click.echo('List of saved streams:')
        for file in os.listdir('.'):
            if file.endswith('.mp3'):
                click.echo(file)
    elif url:
        # Record the stream
        start_time = datetime.datetime.now()
        with urllib.request.urlopen(url) as stream:
            with open(filename, 'wb') as outfile:
                while (datetime.datetime.now() - start_time).seconds < duration:
                    outfile.write(stream.read(blocksize))
        click.echo('Recording completed.')

if __name__ == '__main__':
    record_stream()


#Beispielaufruf
#python audiorecorder2.py --duration 20 --filename recording.mp3 --blocksize 256 http://example.com/stream

#Anzeige der gespeicherten Streams
# python audiorecorder2.py --list-streams

# Anzeige der Hilfe- und Verwendungsinformationen
# python audiorecorder2.py --help
