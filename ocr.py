import re
from paddleocr import PaddleOCR

# regex para matriculas portuguesas
matriculas_regex = "[0-9]{2}[\s-]{0,1}[0-9]{2}[\s-]{0,1}[A-Z]{2}|" \
                   "[0-9]{2}[\s-]{0,1}[A-Z]{2}[\s-]{0,1}[0-9]{2}|" \
                   "[A-Z]{2}[\s-]{0,1}[0-9]{2}[\s-]{0,1}[A-Z]{2}"


def matricula_ocr(imagem=None):
    paddle_ocr = PaddleOCR(use_angle_cls=True, lang='en')
    reader = paddle_ocr.ocr(imagem)

    results = [i[1][0] for i in reader]  # iterar todos os resultados

    for result in results:
        matched = bool(re.match(matriculas_regex, result))
        if matched is True:
            return formatar_matricula(result)


def formatar_matricula(matricula=None):
    # remove todos os espaços vazios e hifens
    matricula = matricula.replace(' ', '')
    matricula = matricula.replace('-', '')

    # formata a matricula no seguinte formato XX-XX-XX
    final = matricula[:2] + '-' + matricula[2:4] + '-' + matricula[4:]

    return final
