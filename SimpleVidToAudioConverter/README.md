

# Audio Converter from YouTube Video

This is a Python program that can download audio and videos files from YouTube video files will convert into audio files. The program can be run from the command line with the following command:

```python
python FromVidToAudio.py --URL <youtube-video-url> --Format <audio-format>
```

This will download the audio from the specified YouTube URL,save the resulting audio file in the same directory as the program. 

You can also download a video file that will be converted to audio (the video file will be saved in the same directory as the program, along with the audio).

```python
python FromVidToAudio.py --URL <youtube-video-url> --Format <audio-format> --VIDEO
````

Alternatively, the program can also convert an existing video file on your local machine to an audio file with the following command:

```python
python FromVidToAudio.py --ConvertFile <video-file> --Format <audio-format>
```

Note that the program currently only supports the following audio formats: mp3, wav, and ogg.

## Requirements

The following libraries are required to run the program:

* pytube
* pydub

These can be installed using pip:

```
pip install pytube
pip install pydub
```
or
```
pip3 install -r requirements.txt
```
## Usage

The program can be run from the command line using the following options:

* `--URL <youtube-video-url>`: The URL of the YouTube video to download and convert to audio.
* `--ConvertFile <video-file>`: The path to the video file on your local machine to convert to audio.
* `--Format <audio-format>`: The desired audio format to convert to. Currently supported formats are: mp3, wav, and ogg.
* `--VIDEO`: (Optional) If specified, the program will download also video from URL.

## Example Usage

To download and convert a YouTube video to an mp3 audio file:

```
python FromVidToAudio.py --URL https://www.youtube.com/watch?v=dQw4w9WgXcQ --Format mp3
```

To convert an existing video file to an ogg audio file:

```
python FromVidToAudio.py --ConvertFile /path/to/video.mp4 --Format ogg
```

To download a video file from a YouTube video and convert it to an audio file:

```
python FromVidToAudio.py --URL https://www.youtube.com/watch?v=dQw4w9WgXcQ --Format wav --VIDEO
```