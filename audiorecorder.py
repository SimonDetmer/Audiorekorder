import requests
from pydub import AudioSegment


def download_mp3_stream(url, output_file):
    try:
        # Den MP3-Stream von der URL herunterladen
        response = requests.get(url, stream=True)
        response.raise_for_status()

        # Bytes des Streams speichern
        stream_bytes = bytearray()
        for chunk in response.iter_content(chunk_size=1024):
            if chunk:
                stream_bytes.extend(chunk)

        # Bytes in AudioSegment umwandeln
        audio = AudioSegment.from_file(io.BytesIO(stream_bytes))

        # AudioSegment als MP3-Datei speichern
        audio.export(output_file, format="mp3")

        print("Die Aufnahme wurde erfolgreich gespeichert als:", output_file)

    except Exception as e:
        print("Ein Fehler ist aufgetreten:", str(e))


# Beispielaufruf
url = "URL_DES_MP3_STREAMS"
output_file = "aufnahme.mp3"
download_mp3_stream(url, output_file)
