import random
import time
from db_conn import query
from datetime import datetime
from ocr import *
import cv2


def escolher_lugar():
    # Verifica na base de dados os lugares livres e escolhe
    # um lugar aleatorio
    lugares_livres = [i[0] for i in query('lugares_livres', [])]
    if lugares_livres == []:
        return 0
    else:
        return random.choice(lugares_livres)


def verificar_saida(matricula=None):
    # Verifica se o carro encontra-se estacionado
    verificar = query('verificar_saida', [matricula])
    try:
        return verificar[0][0]
    except:
        return 0


def entrada_carro(matricula=None, lugar=None):
    # Query ocupar o lugar escolhido
    query('ocupar_lugar', [matricula, lugar])

    # Registar a hora de entrada, registar na tabela entradas e sair do loop
    hr_entrada = datetime.now()
    query('registo_entrada', [matricula, hr_entrada])

    print(f"{matricula} - Entrada às {hr_entrada}")


def saida_carro(matricula=None):
    # Obter a hora de saida
    hr_saida = datetime.now()

    # Obter hora de entrada
    hr_entrada = query('hora_entrada', [matricula])

    # Registar saída do veículo
    query('registo_saida', [matricula, hr_saida])

    # Desocupar o lugar
    query('desocupar_lugar', [matricula])

    # Calcular o custo total e registar na tabela registos
    tempo_total = hr_saida - hr_entrada[0][0]
    tempo_total_minutos = int(tempo_total.total_seconds() / 60)
    custo_total = round(float(0.4 * tempo_total_minutos), 2)

    values_registo = [matricula, tempo_total_minutos, custo_total]
    query('registo', values_registo)

    print(f'{matricula} - Saída às {hr_saida}\n'
          f'Tempo Total: {tempo_total_minutos}\n'
          f'Custo Total: {custo_total}\n'
          f'Boa viagem!')


def estacionar(frame=None):
    # grava a imagem e obtem a matricula usado o easyocr
    cv2.imwrite('matricula.jpg', frame)
    matricula = matricula_ocr('matricula.jpg')

    # verificar se o carro encontra-se estacionado consultado a nossa base de dados
    # se sim, damos saida do carro, caso contrario, damos entrada

    if matricula is not None:
        if verificar_saida(matricula=matricula) == 1:
            saida_carro(matricula=matricula)

            time.sleep(10)  # dar o tempo suficiente para o carro sair
        else:
            if escolher_lugar() == 0:

                print('Está tudo ocupado')
                time.sleep(5)
            else:
                entrada_carro(matricula=matricula, lugar=escolher_lugar())
                time.sleep(10)  # dar o tempo suficiente para o carro entrar
    else:
        pass