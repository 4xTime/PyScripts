

# Audio Converter from YouTube Video

This is a Python program that can download YouTube videos and convert them into audio files. The program can be run from the command line with the following command:

```python
python audio_converter.py --URL <youtube-video-url> --Format <audio-format>
```

This will download the video from the specified YouTube URL, convert it to the specified audio format, and save the resulting audio file in the same directory as the program. 

Alternatively, the program can also convert an existing video file on your local machine to an audio file with the following command:

```python
python audio_converter.py --ConvertFile <video-file> --Format <audio-format>
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
* `--DEL`: (Optional) If specified, the program will delete the downloaded video or the converted audio file after the conversion is complete.

## Example Usage

To download and convert a YouTube video to an mp3 audio file:

```
python audio_converter.py --URL https://www.youtube.com/watch?v=dQw4w9WgXcQ --Format mp3
```

To convert an existing video file to an ogg audio file:

```
python audio_converter.py --ConvertFile /path/to/video.mp4 --Format ogg
```

To download and convert a YouTube video to a wav audio file, and then delete the downloaded video:

```
python audio_converter.py --URL https://www.youtube.com/watch?v=dQw4w9WgXcQ --Format wav --DEL
```