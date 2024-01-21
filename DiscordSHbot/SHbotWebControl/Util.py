from urllib.request import urlopen
import os
import time
import datetime 
import asyncio
import discord
from discord.ext import commands

RESET = '\033[0m'
BLACK = '\033[30m'
RED = '\033[31m'#BAD
GREEN = '\033[32m'#GOOD
YELLOW = '\033[33m'#filepath
BLUE = '\033[34m'#var
MAGENTA = '\033[35m'#function
CYAN = '\033[36m'#USER
WHITE = '\033[37m'

def log_time():
    return time.ctime(time.time())

def color_text(text, color):
    return f"{color}{text}{RESET}"

def event_log(event):
    curr_date = datetime.date.today()
    file_name = str(curr_date) + ".txt"
    dir = os.path.join("SHbotWebControl/ServerLog", file_name)
    if not os.path.isfile(dir):
        with open(dir, 'w') as file:
            file.write(str(event))
    else:
        with open(dir, 'a') as file:
            file.write('\n'+str(event))
    file.close()
        

def get_format_from_file(path):    
    if os.path.isdir(path):
        for file_name in os.listdir(path):
            if os.path.isfile(os.path.join(path, file_name)) and file_name[-4:] == ".txt":
                return True
    else:
        return False


def search_for_user(user):
    if not os.path.isfile('SHbotWebControl/dataset.txt'):
        print(f"{log_time()}{color_text(' ERROR: ',RED)}Path does not exist for {color_text('search_for_user',MAGENTA)}")
        event_log(f"{log_time()} ERROR: Path does not exist for 'search_for_user'")
        return False, 0, None

    line_num = -1
    with open('SHbotWebControl/dataset.txt', 'r') as file:
        for line_num, line in enumerate(file):
            if str(user) in line:
                return True, line_num, line

    return False, line_num, None


def create_file_for_dataset_and_serverlog(file_path_dataset,file_path_serverlog):
    if not os.path.isfile(file_path_dataset):
        with open(file_path_dataset, 'w') as f:
            print(f"{log_time()}{color_text(' SUCCES: ',GREEN)}File {color_text(file_path_dataset,YELLOW)} created!")
            event_log(f"{log_time()} SUCCES: File {file_path_dataset} created!")
    if not os.path.exists(file_path_serverlog):
        try:
            os.makedirs(file_path_serverlog)
            print(f"{log_time()}{color_text(' SUCCES: ',GREEN)}Directory {color_text(file_path_serverlog,YELLOW)} created!")
            event_log(f"{log_time()} SUCCES: Directory {file_path_serverlog} created!")
        except OSError as e:
            print(f"{log_time()}{color_text(' ERROR: ',RED)}While creating directory: {e}")
            event_log(f"{log_time()} ERROR: While creating directory: {e}")


def delete_file_after_event_create(directory):
    for filename in os.listdir(directory):
        if os.path.isfile(os.path.join(directory, filename)):
            os.remove(directory+"/"+filename)

def extract_data(directory):
    time.sleep(1)
    for filename in os.listdir(directory):
        if os.path.isfile(os.path.join(directory, filename)):
            filename = directory+'/'+filename
    with open(filename, 'r') as file:
        data = file.read()
        name = data[data.index("Nazwa:") + len("Nazwa:"):data.index("\nOpis:")].strip()
        description = data[data.index("Opis:") + len("Opis:"):data.index("\nCzas do wygaśnięcia:")].strip()
        expiration = int(data[data.index("Czas do wygaśnięcia:") + len("Czas do wygaśnięcia:"):].strip())

    return name, description, expiration

def read_credentials_from_file(file_path):
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()
            if len(lines) < 3:
                event_log(f"{log_time()} ERROR: File should contain 'channel_id' 'token' and 'server_id'.")
                raise ValueError(f"{log_time()}{color_text(' ERROR:',RED)}File should contain {color_text('channel_id',BLUE)} {color_text('token',BLUE)} and {color_text('server_id',BLUE)}.")

            token = lines[0].split('=')[-1].strip()                
            channel_id = lines[1].split('=')[-1].strip()
            server_id = lines[2].split('=')[-1].strip()

        return int(channel_id), int(server_id), token
    except FileNotFoundError:
        print(f"{log_time()}{color_text(' ERROR:',RED)} File '{color_text(file_path,YELLOW)}'not found.")
        event_log(f"{log_time()} ERROR: File '{file_path}' not found.")
        return None, None
    except ValueError as ve:
        print(f"{log_time()}{ color_text(' ERROR:',RED)} {ve}")
        event_log(f"{log_time()} ERROR: {ve}")
        return None, None
    except Exception as e:
        print(f"{log_time()} An {color_text(' ERROR',RED)} occurred: {e}")
        event_log(f"{log_time()} An  ERROR  occurred: {e}")
        return None, None
    
def SetBotChannel(ctx,ID):
    channel = ctx.get_channel(ID)
    return channel
