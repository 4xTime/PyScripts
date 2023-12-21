import pytube
import sys
from pydub import AudioSegment
import os
import time
import string
pytube.innertube._default_clients['ANDROID']=pytube.innertube._default_clients['WEB']

special_chars = ('$', '%', '^', '&', '*','_', '=', '+', '[', ']', '{', '}', ';', ':', '|', '\\','<', '>', '/', '?', '`', '~','"')

def remove_first_dot(str):
    if str[0] == '.':
        return str[1:]
    else:
        return str

def check_sys_argv(string):
    if string in sys.argv:
        return sys.argv.index(string)
    else:
        return -1

def search_special_chars_in_filename_and_remove(Filename):
    #special_chars = string.punctuation  
    for char in Filename:
        if char in special_chars:
            Filename = Filename.replace(char, '')
    return Filename

def ConvertToAudio(I_Filename,I_Format,FromURL):
    if FromURL == False:
        if I_Filename == -1:
            raise ValueError("You miss a flag for --URL or --ConvertFile")
        Filename = sys.argv[I_Filename+1]
    else:
        Filename = I_Filename
    
    if I_Format == -1:
        raise ValueError("You miss a flag for --Format")
    
    Format = remove_first_dot(str(sys.argv[I_Format+1].replace(" ","")))
    #Format = sys.argv[I_Format+1]

    input_file = os.path.abspath(Filename)

    output_file = Filename[:-4] +"."+Format
    try:
        audio = AudioSegment.from_file(input_file)

        audio.export(output_file, format=Format)
    except:
        print("An error has occurred")

    print("{} is converted to {}".format(Filename,Format))

def Download(I_link):
    if I_link == -1:
         raise ValueError("You miss a flag for --URL or --ConvertFile")
    link = sys.argv[I_link+1]
    youtubeObject = pytube.YouTube(link)

    Filename = youtubeObject.title + ".mp4"
    Filename = Filename.replace(" ","")

    Filename = search_special_chars_in_filename_and_remove(Filename)

    youtubeObject = youtubeObject.streams.get_highest_resolution()
    try:
        youtubeObject.download(filename=Filename)
    except:
        print("An error has occurred")
    print("Video Download is completed successfully")
    return Filename

def DownloadOnlyAudio(I_link,I_format):
    if I_link == -1:
        raise ValueError("You miss a flag for --URL")
    if I_format == -1:
        raise ValueError("You miss a flag for --Format")
    

    link = sys.argv[I_link+1]
    format = remove_first_dot(str(sys.argv[I_format+1].replace(" ","")))

    youtubeObject = pytube.YouTube(link)

    Filename = youtubeObject.title +"."+format
    Filename = Filename.replace(" ", "")

    # You may add a function to handle special characters in the filename here

    audioStream = youtubeObject.streams.filter(only_audio=True).first()
    try:
        audioStream.download(filename=Filename)
    except:
        print("An error has occurred during download.")
        return None
    
    print("Audio download completed successfully")


if check_sys_argv("--VIDEO") == -1 and check_sys_argv("--ConvertFile")==-1:
    try:
        DownloadOnlyAudio(check_sys_argv("--URL"),check_sys_argv("--Format"))
    except:
        print("An error has occurred during TRY_AUDIO.")
else:
    if check_sys_argv("--ConvertFile") != -1:
        ConvertToAudio(check_sys_argv("--ConvertFile"),check_sys_argv("--Format"),False)
        
    if check_sys_argv("--URL") != -1:
        Filename = Download(check_sys_argv("--URL"))
        ConvertToAudio(Filename,check_sys_argv("--Format"),True)
