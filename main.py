import cv2
import time
from utils import estacionar
from model.model import model_tf


def camera():
    # Capturar video da webcam
    while True:
        vid = cv2.VideoCapture(0)

        # Capturar video frame by frame
        ret, frame = vid.read()

        # Mostrar o video numa janela
        cv2.imshow('input', frame)

        # Com o algoritmo de classificação prever se é uma matricula
        prediction = model_tf(frame)

        # Se prediction > .95 ler a matricula
        if prediction > .4:
            estacionar(frame=frame)
            time.sleep(2)

        vid = None

        # Clicar 'q' para sair do programa/janela
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Fechar tudo
    cv2.destroyAllWindows()


camera()
# img = cv2.imread('matricula.jpg')
# predict_matricula(threshold=.95, prediction=.99, frame=img)
# saida_carro('25-33-XQ')