import requests
import io
from pydub import AudioSegment


@click.command()
def demo():
    print('demo')

if __name__ == '__main__':
    demo()



def download_mp3_stream(url, output_file, duration_seconds):
    try:
        # Den MP3-Stream von der URL herunterladen
        response = requests.get(url, stream=True)
        response.raise_for_status()

        # Bytes des Streams speichern
        stream_bytes = bytearray()

        # Aufnahmezeit in Millisekunden umrechnen
        duration_ms = duration_seconds * 1000

        # Datenchunks sammeln, bis die gewünschte Dauer erreicht ist
        total_duration = 0
        for chunk in response.iter_content(chunk_size=8):
            if chunk:
                stream_bytes.extend(chunk)
                total_duration += len(chunk) * 8 / 16000  # Annäherung der Dauer in Sekunden
                if total_duration >= duration_ms:
                    break

        # Bytes in AudioSegment umwandeln
        audio = AudioSegment.from_file(io.BytesIO(stream_bytes))

        # AudioSegment als MP3-Datei speichern
        audio.export(output_file, format="mp3")

        print("Die Aufnahme wurde erfolgreich gespeichert als:", output_file)

    except Exception as e:
        print("Ein Fehler ist aufgetreten:", str(e))


# Beispielaufruf mit einer beispielhaften MP3-URL und einer Aufnahmedauer von 10 Sekunden
url = "http://st01.dlf.de/dlf/01/128/mp3/stream.mp3"
output_file = "aufnahme.mp3"
duration_seconds = 10
download_mp3_stream(url, output_file, duration_seconds)

# Original-Code von Preuss
start_time = datetime.datetime.now()


with urllib.request.urlopen('http://st01.dlf.de/dlf/01/128/mp3/stream.mp3') as stream:
    with open('stream.mp3', 'wb') as outfile:
        while (datetime.datetime.now() - start_time).seconds < 10:
            outfile.write(stream.read(128))

