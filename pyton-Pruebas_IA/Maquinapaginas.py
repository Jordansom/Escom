import os
import psutil
import keyboard  # Asegúrate de tener instalado el módulo 'keyboard'
from IPython.display import clear_output  # Importa la función clear_output si estás usando Jupyter Notebook o IPython

def get_server_stats():
    # Obtener uso de CPU
    cpu_usage = psutil.cpu_percent(interval=1)

    # Obtener uso de memoria
    mem_usage = psutil.virtual_memory().percent

    # Obtener uso de swap
    swap_usage = psutil.swap_memory().percent

    # Obtener número de procesos
    num_processes = len(psutil.pids())

    # Obtener número de interrupciones
    num_interrupts = psutil.cpu_stats().interrupts

    # Obtener cambios de contexto
    context_switches = psutil.cpu_stats().ctx_switches

    # Obtener uso de CPU por núcleo
    cpu_usage_per_core = psutil.cpu_percent(interval=1, percpu=True)

    # Crear un diccionario para almacenar las estadísticas
    stats = {
        'cpu_usage': cpu_usage,
        'mem_usage': mem_usage,
        'swap_usage': swap_usage,
        'num_processes': num_processes,
        'num_interrupts': num_interrupts,
        'context_switches': context_switches,
        'cpu_usage_per_core': cpu_usage_per_core
    }

    return stats

def print_server_stats(stats):
    clear_output(wait=True)  # Borra la salida anterior
    print("Press 'x' to exit")
    print("Uso de CPU: {:.2f}%".format(stats['cpu_usage']))
    print("Uso de Memoria: {:.2f}%".format(stats['mem_usage']))
    print("Uso de Swap: {:.2f}%".format(stats['swap_usage']))
    print("Número de Procesos: {}".format(stats['num_processes']))
    print("Número de Interrupciones: {}".format(stats['num_interrupts']))
    print("Cambios de Contexto: {}".format(stats['context_switches']))
    print("Uso de CPU por núcleo:")
    for i, usage in enumerate(stats['cpu_usage_per_core']):
        print("Núcleo {}: {:.2f}%".format(i, usage))

if __name__ == '__main__':
    stats = get_server_stats()
    print_server_stats(stats)