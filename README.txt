Autor:
José Spinelli

Monitor de Processos e Hierarquias

Este script Python utiliza a biblioteca 'psutil' para monitorar e exibir a hierarquia de processos em execução no sistema. Ele também identifica processos zumbis e fornece um relatório detalhado ao final da execução.

Funcionalidades:
- Listagem de Processos: Exibe a hierarquia de processos, mostrando a relação entre processos pais e filhos.
- Identificação de Zumbis: Detecta e lista processos zumbis (processos que terminaram, mas ainda possuem entradas na tabela de processos).
- Relatório de Execução: Gera um relatório com o tempo de execução, o número total de processos pais, processos filhos e processos zumbis encontrados.

Requisitos:
- Python 3.x instalado.
- Biblioteca 'psutil' instalada. Caso não tenha, instale usando o comando:
  pip install psutil

Como Executar:
1. Salve o script em um arquivo com extensão .py, por exemplo, monitor_processos.py.
2. Execute o script usando o Python:
   python [nome do arquivo].py
3. O script exibirá a hierarquia de processos e, ao final, um relatório com o tempo de execução e o número de processos encontrados.
4. Para sair do script, digite EXIT quando solicitado.

Observações:
- O script pode demorar um pouco para ser executado, dependendo do número de processos em execução no sistema.
- Processos zumbis são raros em sistemas bem gerenciados, mas podem aparecer em situações específicas.