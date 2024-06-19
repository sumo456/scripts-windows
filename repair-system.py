import subprocess
import time
from tqdm import tqdm
import sys

def install_tqdm():
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "tqdm"])
    except subprocess.CalledProcessError as e:
        print("Error al instalar tqdm:", e)

def run_command(command):
    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    total_steps = 100  # Estimación del número de pasos para la barra de progreso
    progress_step = 0  # Contador para la barra de progreso

    with tqdm(total=total_steps, desc=command, ncols=100) as pbar:
        while True:
            output = process.stdout.readline()
            if process.poll() is not None and not output:
                break
            if output:
                tqdm.write(output.strip().decode())
            if progress_step < total_steps:
                pbar.update(1)
                progress_step += 1
            time.sleep(0.1)  # Para hacer que la barra de progreso avance gradualmente
        pbar.update(total_steps - progress_step)  # Completa la barra de progreso si es necesario

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
