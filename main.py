# Codigo que executa a ação do programa em si
import subprocess
from pathlib import Path
import pyautogui
import time
from threading import Thread
from funcs.whiteloadconfig import Configs
import logging
logging.raiseExceptions = False
# Carrega as configurações
configs = Configs.load_configs()
dir_exe_path = configs['dir_exe_path']
dir_exe_obj = Path(configs['dir_exe_path'])
dir_path_videos = configs['dir_path_videos']
repetir = configs['repetir']

def abrir_videos():
    subprocess.run([dir_exe_path, dir_path_videos, "/fullscreen"])
    
def repetir_playlist():
    time.sleep(1)
    if repetir == "True":
        time.sleep(2)
        pyautogui.click(pyautogui.size()[0] / 2, pyautogui.size()[1] / 2, button="right")
        time.sleep(0.2)
        for _ in range(4):
            time.sleep(0.1)
            pyautogui.press("down") 
        pyautogui.press("enter")
        time.sleep(0.2)
        pyautogui.press("enter")

def play():
    if dir_exe_obj.exists():
        Thread(target=abrir_videos).start()
        Thread(target=repetir_playlist).start()
    else:
        print("mpc-hc64.exe not found")
        
if __name__ == "__main__":    
    play()