from time import sleep

class Liquida:

    def coeficiente_volumetrico_aparente(self):        
        print('\nA fórmula que será usada para saber o coeficiente aparente será -> Yap = Δap / (v0 * Δt)')
        
        self.v0 = float(input('\nInforme o valor de v0: '))
        self.Dap = float(input('\nInforme o valor de Δap: '))
        self.Dt = float(input('\nInforme o valor de Δt: '))
    
        self.gama_aparente = self.Dap / (self.v0 * self.Dt)
        return self.gama_aparente

    def coeficiente_volumetrico_real(self):
        print('\nA fórmula que será usada para saber o coeficiente real será -> Yr = Yrec + Yap')
        print('\nPor hora estamos apenas aceitando valores no formato com o "e", ex: 1.5x10^-4 = 1.5e-4 ')
        print('\nDigite abaixo considerando que as notações estejam igualadas.')
        
        self.gama_recipiente = input('\nInforme o coeficiente do recipiente (Yrec): ')
        self.gama_aparente = input('\nInforme o coeficiente do aparente (Yap): ')

        # // Pegando os valores dos Indices das notações científicas com .find()
        first_index_notation = int(self.gama_recipiente.find('e'))
        second_index_notation = int(self.gama_aparente.find('e'))
        notation = self.gama_aparente[first_index_notation:]
        
        if notation != self.gama_recipiente[second_index_notation:]:
            return ('\nNotamos que o expoente não está igualado, considere rever isso')
        
        elif first_index_notation == -1 or second_index_notation == -1:
            return ('Não conseguimos entender nessa forma que você apresentou, reveja os formatos que está valendo!')
        
        else:
            pass

        valor_primeira_expressao = float(self.gama_recipiente[:first_index_notation])
        valor_segunda_expressao = float(self.gama_aparente[:second_index_notation])

        self.gama_real = valor_primeira_expressao + valor_segunda_expressao

        return f'Coeficiente volumétrico real é igual a: {self.gama_real}{notation}'

    def variacao_volumetrica_aparente(self):
        print('\nA fórmula que será usada para saber a dilatação volumétrica aparente será -> ΔVap = v0 x Δt')
        print('\nQuando estiver falando de notações siga a estrutura no formato com o "e", ex: 1.5x10-³ = 1.5e-3')
        
        self.coeficiente_volumetrico_aparente = input('\nInforme o valor coeficiente volumétrico aparente: ')
        self.volume_inicial = float(input('\nInforme v0: '))
        self.variacao_tempo = float(input('\nInforme a Δt considere (Δt = t - t0): '))

        index_notation = self.coeficiente_volumetrico_aparente.find('e')
        operation = self.coeficiente_volumetrico_aparente[index_notation + 1: index_notation + 1]
        print(operation)

        if index_notation == -1:
            return 'Formato errado, reveja a estrutura que estamos aceitando pls!!!'

        else:
            notation = self.coeficiente_volumetrico_aparente[index_notation:]

        valor_expressao = float(self.coeficiente_volumetrico_aparente[:index_notation])

        self.variacao = valor_expressao * self.volume_inicial * self.variacao_tempo

        if operation == '-':
            real_number = self.variacao * 10 ** int(notation[1:] * -1)

        else:
            real_number = self.variacao * 10 ** int(notation[1:])

        return f'{self.variacao:.0f}{notation} ou o valor real {real_number:.2f}'




obj = Liquida()

while True:
    print('''
Olá user, bem vindo ao mundo da Física!

1 - Coeficiente de dilatação volumétrico aparente.
2 - Coeficiente de dilatação volumétrico real.
3 - Variação volumétrica aparente
4 - Sair do programa.''')

    opcao = int(input('\nInforme sua opção: '))

    if opcao == 1:
        print('\nCerto!, mas pra eu te responder antes preciso de alguns dados...')
        print(f'\nCoeficiente volumétrico aparente é igual a: {obj.coeficiente_volumetrico_aparente():.1e}')
        sleep(4)

    elif opcao == 2:
        print(f'\n{obj.coeficiente_volumetrico_real()}')
        sleep(4)
    
    elif opcao == 3:
        print(f'\n{obj.variacao_volumetrica_aparente()}')
    
    elif opcao == 4:
        break
    
    else:
        print('\nOpção inválida!!!')
        continue