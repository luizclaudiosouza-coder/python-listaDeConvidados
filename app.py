convidados_da_festa = ['Maria','João','Ana','Carlos','Mariana']

status_presença = {}

print('--- Verificação da lista de convidados ---')

lista_de_chegadas = ['João','Ana','Pedro','Maria']

for pessoas in lista_de_chegadas:
    if pessoas in convidados_da_festa:
        print(f'OLÁ, {pessoa}! Bem vindo à festa. ')
        status_presenca[pessoa] = "confirmado"

    else:
        print(f'Desculpe,{pessoa}, Seu nome não está na lista')
        status_presenca[pessoa] = 'Não convidado'
        
