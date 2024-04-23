import urllib.request
import datetime

start_time = datetime.datetime.now()


with urllib.request.urlopen('http://st01.dlf.de/dlf/01/128/mp3/stream.mp3') as stream:
    with open('stream.mp3', 'wb') as outfile:
        while (datetime.datetime.now() - start_time).seconds < 10:
            outfile.write(stream.read(128))
