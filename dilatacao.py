from time import sleep

class Aparente:

    def gama_ap(self):        
        self.v0 = float(input('\nInforme o valor de v0: '))
        self.Dap = float(input('\nInforme o valor de Δap: '))
        self.Dt = float(input('\nInforme o valor de Δt: '))
    
        self.gama_aparente = self.Dap / (self.v0 * self.Dt)
        return self.gama_aparente

    def gama_r(self):
        print('\nDigite abaixo considerando que as notações estejam igualadas.')
        
        self.gama_recipiente = input('\nInforme o coeficiente do recipiente: ')
        self.gama_aparente = input('\nInforme o coeficiente do aparente: ')
        
        decimal = float(self.gama_recipiente[:3])
        decimal1 = float(self.gama_aparente[:3])
        notation = self.gama_aparente[3:]
        
        self.game_real = decimal + decimal1

        return f'{self.game_real}{notation}'

obj = Aparente()

while True:
    print('''
Olá user, bem vindo ao mundo da Física!

1 - Coeficiente de dilatação volumétrico aparente.
2 - Coeficiente de dilatação volumétrico real.
3 - Sair do programa.''')

    opcao = int(input('\nInforme sua opção: '))

    if opcao == 1:
        print('\nCerto!, mas pra eu te responder antes preciso de alguns dados...')
        print(f'\nCoeficiente volumétrico aparente é igual a: {obj.gama_ap():.1e}')
        sleep(4)

    elif opcao == 2:
        print(f'\nCoeficiente volumétrico real é igual a: {obj.gama_r()}')
        sleep(4)
    
    elif opcao == 3:
        break
    
    else:
        print('\nOpção inválida!!!')
        continue