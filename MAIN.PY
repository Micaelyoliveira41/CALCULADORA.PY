while True:
    # usuário informa os números.

    x = str(input('informe o primeiro número: ')).replace(',','.')
    y = str(input('informe o segundo número: ')).replace(',','.')

    #converte para números decimais

    x = float(x)
    y = float(x)

    print('informe a operação que deseja fazer:\n')
    print('"+" para somar.')
    print('"*" para multiplicar.')
    print('"/" para dividir.')
    print('"%" para encontrar o resto da divisão.')

    op = input('operação desejada: ')

    match op:
        case  '+':
            print(f'A soma é: {x+y}.')
        case  '-':
            print(f'A subtração é: {x-y}.')
        case  '*':
            print(f'A multiplicação é: {x*y}.')
        case  '/':
            print(f'A divisão é: {x/y}.')
        case  '%':
            print(f'O resto da divisão é: {x%y}.')
        case _:
            print('operação inválida')
            continue

# pergunta para o usuário se deseja continuar ou encerrar
    continuar = input('deseja continuar (s/n)? ')

#verifica a opção do usuário

    if continuar == 's':
        continue
    elif continuar == 'n':
        break
    else:
        print('opção inválida')
    continue