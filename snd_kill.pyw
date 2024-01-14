import subprocess
from time import sleep
import psutil


def kill_snd():
    subprocess.call(["taskkill", "/f", "/im", "SndVol.exe"])


def get_running_processes():
    processes = list(psutil.process_iter())
    for process in processes:
        try:
            process_info = process.as_dict(attrs=['pid', 'name', 'username'])
            if process_info['name'].lower() == "sndvol.exe":
                kill_snd()
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass


while True:
    get_running_processes()
    sleep(0.3)


