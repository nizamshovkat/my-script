#!/usr/bin/env python3

import os

def check_service_status(service_name):

    status = os.popen(f"systemctl is-active {service_name}").read().strip()
    if status == "active":
        print(f"Служба {service_name} запущена ✅")
    else:
        print(f"Служба {service_name} не работает ❌")

def restart_service(service_name):

    print(f"Перезапускаю службу {service_name}...")
    os.system(f"sudo systemctl restart {service_name}")
    print(f"Служба {service_name} успешно перезапущена!")

if __name__ == "__main__":
    print("=== Проверка статуса служб ===")
    services = ["nginx", "ssh", "mysql"]
    for service in services:
        check_service_status(service)


    service_to_restart = input("\nВведите имя службы для перезапуска (или нажмите Enter для выхода): ")
    if service_to_restart:
        restart_service(service_to_restart)
