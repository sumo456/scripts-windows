import subprocess
import time
import sys
from tqdm import tqdm

def install_tqdm():
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "tqdm"])
    except subprocess.CalledProcessError as e:
        print("Error al instalar tqdm:", e)

def run_command(command):
    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, bufsize=1, universal_newlines=True)
    total_steps = 100  # Estimación del número de pasos para la barra de progreso
    with tqdm(total=total_steps, desc=command, ncols=100) as pbar:
        while True:
            output = process.stdout.readline()
            if process.poll() is not None and output == '':
                break
            if output:
                tqdm.write(output.strip())
                pbar.update(1)
            time.sleep(0.1)  # Para hacer que la barra de progreso avance gradualmente
        # Completa la barra de progreso si es necesario
        pbar.update(total_steps - pbar.n)
    return process.returncode

commands = [
    "sfc /scannow",
    "DISM /Online /Cleanup-Image /CheckHealth",
    "DISM /Online /Cleanup-Image /ScanHealth",
    "DISM /Online /Cleanup-Image /RestoreHealth"
]

if __name__ == "__main__":
    install_tqdm()
    
    for command in commands:
        print(f"Running: {command}")
        return_code = run_command(command)
        if return_code != 0:
            print(f"Command failed with return code {return_code}: {command}")
        else:
            print(f"Command completed successfully: {command}")
