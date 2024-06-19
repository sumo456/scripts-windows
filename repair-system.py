import subprocess
import time
from tqdm import tqdm

def install_tqdm():
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "tqdm"])
    except subprocess.CalledProcessError as e:
        print("Error al instalar tqdm:", e)

def run_command(command):
    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    total_steps = 100  # Estimación del número de pasos para la barra de progreso
    with tqdm(total=total_steps, desc=command, ncols=100) as pbar:
        while True:
            output = process.stdout.readline()
            if process.poll() is not None:
                break
            if output:
                tqdm.write(output.strip().decode())
            pbar.update(1)
            time.sleep(0.1)  # Para hacer que la barra de progreso avance gradualmente
        pbar.update(total_steps - pbar.n)  # Completa la barra de progreso
    return process.returncode

commands = [
    "sfc /scannow",
    "DISM /Online /Cleanup-Image /CheckHealth",
    "DISM /Online /Cleanup-Image /ScanHealth",
    "DISM /Online /Cleanup-Image /RestoreHealth"
]

if __name__ == "__main__":
    import sys
    install_tqdm()
    
    for command in commands:
        print(f"Running: {command}")
        return_code = run_command(command)
        if return_code != 0:
            print(f"Command failed with return code {return_code}: {command}")
        else:
            print(f"Command completed successfully: {command}")
