import subprocess
import sys
import os
from tkinter import filedialog
from tkinter import messagebox
from tkinter import *
import ctypes
import time

def run():
    msg=messagebox.showinfo('Message', 'Select where to install it')
    current_directory = filedialog.askdirectory()

    check = os.path.isfile(current_directory+"\ReadMe.txt")
    if check == True:
        msg=messagebox.showinfo('Message', 'Stormworks Editor is already installed there')


    subprocess.check_call([sys.executable, "-m", "pip", "install", "googledrivedownloader"])
    from google_drive_downloader import GoogleDriveDownloader as gdd


    gdd.download_file_from_google_drive(file_id='1ql2JHWTIByaufX4ry6vH6XwHslTLkkdT',
                                        dest_path= current_directory+"\lol.zip",
                                        unzip=True)
    time.sleep(1)
    os.remove(current_directory+"\lol.zip")

    msg=messagebox.showinfo('Message', 'Done Installing')
    
    msg=messagebox.showinfo('Message', 'Where is the location of stormworks?')
    StormworksDir = filedialog.askdirectory()
    with open(current_directory+"\StormworksDir.txt", 'w') as f:
        f.write(StormworksDir)
    msg=messagebox.showinfo('Message', 'Set up Complete :D')
    os.startfile(current_directory)
    quit()



def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

if is_admin():
    run()
else:
    # Re-run the program with admin rights
    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)

