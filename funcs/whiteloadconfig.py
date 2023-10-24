import json
from pathlib import Path

dir_exe_path = r"C:\Program Files (x86)\K-Lite Codec Pack\MPC-HC64\mpc-hc64.exe"
dir_path_videos = r"C:\Users\Universal\Downloads\TH"

padrao_config = {
    "nome" : "AutoPlayVideos",
    "version" : "1.0",
    "dir_exe_path" : "C:/Program Files (x86)/K-Lite Codec Pack/MPC-HC64/mpc-hc64.exe",
    "dir_path_videos" : "",
    "repetir" : "True"
}

# Dicionário com as configurções
dirconfigs = "configs.json"

# Caminho do arquivo JSON
class Configs:
    def create_configs(newconfig) -> None:
        with open(dirconfigs, "w") as file:
            json.dump(dirconfigs, file, indent=4)
            
    # Grava as configurações no arquivo JSON
    def save_configs(dataconfigs) -> None:
        with open(dirconfigs, "w") as file:
            json.dump(dataconfigs, file, indent=4)

    # Carrega as configurações
    def load_configs() -> any:
        if Path(dirconfigs).exists():
            with open(dirconfigs, "r") as file:
                dataconfigs = json.load(file)
                return dataconfigs
        else:
            Configs.save_configs(padrao_config)
            return padrao_config