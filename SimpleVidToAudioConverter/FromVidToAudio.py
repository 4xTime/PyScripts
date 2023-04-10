from pytube import YouTube
import sys
from pydub import AudioSegment
import os
import time
import string

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

    youtubeObject = YouTube(link)

    Filename = youtubeObject.title + ".mp4"
    Filename = Filename.replace(" ","")

    Filename = search_special_chars_in_filename_and_remove(Filename)

    youtubeObject = youtubeObject.streams.get_highest_resolution()
    try:
        youtubeObject.download(filename=Filename)
    except:
        print("An error has occurred")
    print("Download is completed successfully")
    return Filename


if check_sys_argv("--ConvertFile") != -1:
    ConvertToAudio(check_sys_argv("--ConvertFile"),check_sys_argv("--Format"),False)
    
if check_sys_argv("--URL") != -1:
    Filename = Download(check_sys_argv("--URL"))
    ConvertToAudio(Filename,check_sys_argv("--Format"),True)

if check_sys_argv("--DEL") != -1:
    try:
        os.remove(Filename)
    except:
        print("Cannot delete a file")
    print("File successfully deleted")

