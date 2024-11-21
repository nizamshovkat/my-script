#!/usr/bin/env python3
import os

def check_disk_space():

    disk_info = os.popen('df -h').read()
    print("Информация о дисковом пространстве:")
    print(disk_info)

if __name__ == "__main__":
    check_disk_space()
