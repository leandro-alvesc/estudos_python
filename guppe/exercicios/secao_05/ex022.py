# Ler idade e tempo de serviço de um trabalhador e escrever se ele pode ou não se aposentar
idade = int(input('Digite a idade: '))
tempo_servico = int(input('Digite o tempo de serviço: '))

if idade >= 65 or tempo_servico >= 30 or (idade >= 60 and tempo_servico >= 25):
    print('Pode aposentar.')
else:
    print('Não pode aposentar.')
