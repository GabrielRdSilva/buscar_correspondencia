import time
import multiprocessing
inicial = time.time()
def process_task(item):
    print(item)
    # Faça algo com o item
    return item * 5
if __name__ == "__main__":
    items = [1, 2, 3, 4, 5]

    # Cria o objeto Pool com o número máximo de processos desejados
    pool = multiprocessing.Pool(processes=4)

    # Mapeia a função de tarefa para os itens usando o pool
    resultados = pool.map(process_task, items)

    # Fecha o pool de processos, indicando que não haverá mais tarefas
    pool.close()

    # Aguarda a conclusão de todos os processos do pool
    pool.join()
    print(resultados)
    print("Todas as tarefas concluídas")
final = time.time()    
print(final-inicial)