from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.core.window import Window
from pathlib import Path
from kivy.config import Config
from funcs.whiteloadconfig import Configs
import main
import subprocess
import pyautogui
import time
from threading import Thread
from funcs.whiteloadconfig import Configs
import logging
logging.raiseExceptions = False

Window.size = (601, 361)
Window.minimum_width, Window.minimum_height = 600, 360

class ConfigAPP(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.dir_exe_path = Configs.load_configs()['dir_exe_path']
        self.dir_path_videos = Configs.load_configs()['dir_path_videos']
        self.repetir = Configs.load_configs()['repetir']
        self.play = main.play
    def saveconfigs(self):
        self.repetir = str(self.root.ids.switchrepetir.active)
        self.dir_path_videos = str(self.root.ids.pathvideos.text)
        self.dir_exe_path = str(self.root.ids.pathampc.text)
        config = {
            "nome" : "AutoPlayVideos",
            "version" : "1.0",
            "dir_exe_path" : str(self.dir_exe_path),
            "dir_path_videos" : str(self.dir_path_videos),
            "repetir" : self.repetir
        }
        Configs.save_configs(config)
        
    def botaorepetir(self):
        if self.repetir == 'True':
            return True
        else:
            return False
    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.title = "AutoPlayVideos - Developed by JonesGP Studio"
        return Builder.load_file("config.kv")
    
if __name__ == "__main__":
    ConfigAPP().run()