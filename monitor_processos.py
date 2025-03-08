import psutil
import time

def linha():
    print('-' * 80)

def processos_hierarquias():
    i_pid = 0
    i_ppid = 0
    i_zumbi = 0
    
    hierarquia = {}

    for proc in psutil.process_iter(['pid', 'name', 'ppid', 'status']):
        try:
            info = proc.info
            pid = info['pid']
            ppid = info['ppid']
            nome = info['name']
            status = info['status']

            if ppid not in hierarquia:
                hierarquia[ppid] = []
            hierarquia[ppid].append((pid, nome, status))

            if status == psutil.STATUS_ZOMBIE:
                print(f'Processo Zumbi encontrado: PID={pid}, Nome={nome}, PPID={ppid}')
                i_zumbi += 1

        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            continue

    linha()
    print('\n','\033[33mHIERAEQUIA DE PROCESSOS:\033[m'.center(80),'\n')
    linha()
    for ppid, processos in hierarquia.items():
        print(f'Processo Pai (PPID={ppid}):')
        for pid, nome, status in processos:
            print(f'  -> PID={pid}, Nome={nome}, Status={status}')
            i_pid += 1
        linha()
        i_ppid += 1
    return i_ppid, i_pid, i_zumbi

inicio = time.time()
ppid, pid, zumbi = processos_hierarquias()
fim = time.time()
tempo_execucao = fim - inicio

print('\n','\033[33mRELATÓRIO:\033[m'.center(80),'\n')
linha()
print(f'TEMPO DE EXECUÇÃO: {tempo_execucao:.2f} segundos')
print(f'TOTAL DE PROCESSOS PAI: {ppid}')
print(f'TOTAL DE PROCESSOS FILHO: {pid}')
print(f'TOTAL DE PROCESSOS ZUMBI: {zumbi}')
linha()
while True:
    comando = input("\nDigite 'EXIT' para fechar o prompt: ").strip().lower()
    if comando == 'exit':
        print("Fechando o prompt...")
        time.sleep(2)
        break
    else:
        print("Comando inválido. Digite 'EXIT' para sair.")