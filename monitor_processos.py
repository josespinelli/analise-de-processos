import psutil
import time

def linha():
    print('-' * 80)

def processos_hierarquias():
    i_pid = 0
    i_ppid = 0
    i_zumbi = 0
    
    hierarquia = {}

    for proc in psutil.process_iter(['pid', 'name', 'ppid', 'status', 'cpu_percent', 'memory_info']):
        try:
            info = proc.info
            pid = info['pid']
            ppid = info['ppid']
            nome = info['name']
            status = info['status']
            cpu_percent = info['cpu_percent']
            memory_info = info['memory_info']

            if ppid not in hierarquia:
                hierarquia[ppid] = []
            hierarquia[ppid].append((pid, nome, status, cpu_percent, memory_info.rss))

            if status == psutil.STATUS_ZOMBIE:
                print(f'Processo Zumbi encontrado: PID={pid}, Nome={nome}, PPID={ppid}')
                i_zumbi += 1

        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            continue

    linha()
    print('\n','\033[33mHIERARQUIA DE PROCESSOS:\033[m'.center(80),'\n')
    linha()
    for ppid, processos in hierarquia.items():
        print(f'Processo Pai (PPID={ppid}):')
        for pid, nome, status, cpu_percent, memory_rss in processos:
            print(f'  -> PID={pid}, Nome={nome}, Status={status}, CPU%={cpu_percent}, Memória RSS={memory_rss / 1024 / 1024:.2f} MB')
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
input('Pressione "ENTER" para fechar o prompt: ')