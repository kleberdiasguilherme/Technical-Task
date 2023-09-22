import os
import shutil
import schedule
import time
import logging

logging.basicConfig(filename='log.txt', level=logging.INFO, format='%(asctime)s - %(message)s')

def copiar():
    caminho_original = r"C:\Tarefa de teste\input"
    caminho_copia    = r"C:\Tarefa de teste\input_copia"

    try:
        os.mkdir(caminho_copia)
    except FileExistsError as e:
        print(f'Pasta {caminho_copia} já existe.')


    for root, _, files in os.walk(caminho_copia):
        for file in files:
            arquivo_copia   = os.path.join(root, file)
            arquivo_orginal = os.path.join(caminho_original, os.path.relpath(arquivo_copia, caminho_copia))
            
            if not os.path.exists(arquivo_orginal):
                os.remove(arquivo_copia)
                print(f'Removido: {arquivo_copia}')
                logging.info(f'Arquivo removido : {file}')

    for root, _, files in os.walk(caminho_original):
        for file in files:
            old_file_path = os.path.join(root, file)
            new_file_path = os.path.join(caminho_copia, file)
            
            shutil.copy(old_file_path, new_file_path)
            print(f'Arquivo {file} copiado com sucesso!')
            logging.info(f'Arquivo copiado com sucesso!: {file}')

        
def tarefa_programada():
    print('Tarefa proframada iniciada')
    logging.info('Tarefa programada iniciada')
    copiar()
    print('Tarefa concluida')
    logging.info('Tarefa concluída')

schedule.every(10).seconds.do(tarefa_programada)

if __name__ == "__main__":
    while True:
        schedule.run_pending()
        time.sleep(10)


