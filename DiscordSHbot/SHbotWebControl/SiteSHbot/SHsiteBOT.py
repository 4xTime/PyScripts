from flask import Flask, render_template, request
import os

app = Flask(__name__)

def save_event_data(nazwa, opis, time_to_expire,file_path):
    with open(file_path, "w") as file:
        file.write(f"Nazwa: {nazwa}\n")
        file.write(f"Opis: {opis}\n")
        file.write(f"Czas do wygaśnięcia: {time_to_expire}\n")

def dir_exist_ifnot_create(path)->bool:
    if os.path.exists(path):
        return True
    else:
        os.mkdir(path)
        print("directory events created now")
        return False

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/create_event', methods=['POST'])
def create_event():
    nazwa_eventu = request.form['nazwa-eventu']
    opis_eventu = request.form['opis-eventu']
    czas_do_wygasniecia = request.form['czas-do-wygasniecia']
    if dir_exist_ifnot_create("SHbotWebControl/SiteSHbot/events")==True or False:
        save_event_data(nazwa=nazwa_eventu,opis=opis_eventu,time_to_expire=czas_do_wygasniecia,file_path='SHbotWebControl/SiteSHbot/events/CE.txt')
    return 'Event created'

dir_exist_ifnot_create('SHbotWebControl/SiteSHbot/events')
app.run()

