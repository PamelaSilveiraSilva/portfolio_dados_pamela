# src/main.py
import time
import subprocess
import sys
import os

# intervalo em segundos (ex: 300 = 5 minutos)
INTERVAL = 300

def run_step(cmd):
    print(f"▶️ Executando: {cmd}")
    result = subprocess.run(cmd, shell=True)
    if result.returncode != 0:
        print(f"❌ Erro ao executar: {cmd}")
        return False
    return True

if __name__ == "__main__":
    print("Iniciando loop ETL. Ctrl+C para parar.")
    try:
        while True:
            # 1) extract
            if not run_step("python src\\extract.py"):
                time.sleep(10)
                continue
            # 2) transform
            if not run_step("python src\\transform.py"):
                time.sleep(10)
                continue
            # 3) load
            if not run_step("python src\\load.py"):
                time.sleep(10)
                continue
            print("✅ Ciclo ETL completo. Aguardando intervalo...")
            time.sleep(INTERVAL)
    except KeyboardInterrupt:
        print("Processo interrompido pelo usuário.")
