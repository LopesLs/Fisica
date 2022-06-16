# // Testando as classes criadas :)

from solidos import Solida
from liquidos import Liquida
from time import sleep

while True:

    try:
        entrada = int(input(('''
* * * * * * * * * * * * * * * * * * * *
*                                     *
*  Welcome!, os conteúdos atuais são  *
*                                     * 
* * * * * * * * * * * * * * * * * * * *
*                                     *
*      1 - Física dos Líquidos        *
*      2 - Física dos Sólidos         *
*      3 - Sair do progama            *
*                                     *
* * * * * * * * * * * * * * * * * * * *

Digite aqui sua escolha: ''')))
    
    except Exception:
        print('\nLOG: SÓ ACEITAMOS VALORES INTEIROS COMO RESPOSTA')
        sleep(4)
        continue
    
    else:
        pass

    if entrada == 1:

        while True:
            liquido = Liquida()
            
            print('''
* * * * * * * * * * * * * * * * * * * * * * *
*                                           *
*  Olá user, bem vindo ao mundo da Física!  *
*                                           *
*           [Dilatação Líquida]             *
*                                           *
* * * * * * * * * * * * * * * * * * * * * * *
*                                           *
* 1 - Coeficiente de dilatação volumétrico. *
* 2 - Coeficiente de dilatação Real.        *
* 3 - Variação dilatação volumétrica.       *
* 4 - Voltar para o menu principal.         *
*                                           *
* * * * * * * * * * * * * * * * * * * * * * *''')

            try:
                opcao = int(input('\nDigite aqui a sua escolha : '))
            
            except Exception:
                print('\nLOG: INFORME APENAS NÚMEROS PARA ESCOLHER AS OPÇÕES!!!')
                sleep(4)
                continue
            
            if opcao == 1:
                print(f'\n{liquido.coeficiente_dilatacao_aparente()}')
                sleep(2)

            elif opcao == 2:
                print(f'\n{liquido.coeficiente_dilatacao_real()}')
                sleep(2)
            
            elif opcao == 3:
                print(f'\n{liquido.variacao_aparente()}')
                sleep(2)
            
            elif opcao == 4:
                break
            
            else:
                print('\nOpção inválida!!!')
                continue
            
    elif entrada == 2:
        # // Desenvolvendo
        print('\nAinda estamos em desenvolvimento, mas sairá em breve ;)')
        sleep(3)

    elif entrada == 3:
        print('\nValeu mesmo por utilizar meu programa!, [ Dev: Lopez √ ]')
        break
    else:
        print('\nCalma aí, só temos duas opções até agora :/')
        sleep(3)

# // Qualquer dúvida em relação ao code se dirigir ao Dev do repositório.