#!/usr/bin/env python3

import os

def monitor_system():

    cpu_load = os.popen("top -bn1 | grep 'Cpu(s)'").read().strip()

    memory_usage = os.popen("free -h").read().strip()

    uptime = os.popen("uptime -p").read().strip()

    print("Мониторинг системы:")
    print("\nЗагрузка CPU:")
    print(cpu_load)
    print("\nИспользование памяти:")
    print(memory_usage)
    print("\nВремя работы системы:")
    print(uptime)

if __name__ == "__main__":
    monitor_system()
