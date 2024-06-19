import subprocess
import time
import sys

def install_tqdm():
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "tqdm"])
    except subprocess.CalledProcessError as e:
        print("Error al instalar tqdm:", e)

def run_command(command):
    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    total_steps = 100  # Estimación del número de pasos para la barra de progreso
    step_duration = 3  # Duración de cada paso en segundos (ajústala según tus necesidades)

    for step in range(total_steps):
        output = process.stdout.readline()
        if output:
            print(output.strip().decode('utf-8', errors='ignore'))
        time.sleep(step_duration / total_steps)
        if process.poll() is not None:
            break
    
    # Leer el resto de la salida del proceso si no se ha terminado
    while True:
        output = process.stdout.readline()
        if not output:
            break
        print(output.strip().decode('utf-8', errors='ignore'))

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
