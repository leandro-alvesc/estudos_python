def comer(comida, saudavel):
    if saudavel:
        final = 'quero manter a forma.'
    else:
        final = 'YOLO'

    return f'Estou comendo {comida} porque {final}'


def dormir(horas):
    if horas > 8:
        return f'Dormi {horas} horas! Estou atrasado...'
    elif horas <= 7:
        return f'Dormi por apenas {horas} horas. Tenho que melhorar meu sono!'
    else:
        return f'Dormi por {horas} horas, estou descansado!'


def engracada(pessoa):
    comediantes = ['Jim Carrey', 'Matheus Canella']
    if pessoa in comediantes:
        return True
    return False

