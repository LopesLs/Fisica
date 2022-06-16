# // WorkSpace Class Liquida

class Liquida:

    def coeficiente_dilatacao_aparente(self):        
        print('\nA fórmula que será usada para saber o coeficiente aparente será ->  Δap = Yap * v0 * Δt')
        
        self.v0 = float(input('\nInforme o valor de v0: '))
        self.Dap = float(input('\nInforme o valor de Δap: '))
        self.Dt = float(input('\nInforme o valor de Δt: '))
        self.gama_aparente = self.Dap / (self.v0 * self.Dt)

        return (f'Coeficiente volumétrico aparente é igual a: {self.gama_aparente:.1e}')

    def coeficiente_dilatacao_real(self):
        print('\nA fórmula que será usada para saber o coeficiente real será -> Yr = Yrec + Yap')
        print('\nPor hora estamos apenas aceitando valores no formato com o "e", ex: 1.5x10^-4 = 1.5e-4 ')
        print('\nDigite abaixo considerando que as notações estejam igualadas.')
        
        self.gama_recipiente = input('\nInforme o coeficiente do recipiente (Yrec): ')
        self.gama_aparente = input('\nInforme o coeficiente do aparente (Yap): ')

        # // Pegando os valores dos Indices das notações científicas com .find()
        first_index_notation = int(self.gama_recipiente.find('e'))
        second_index_notation = int(self.gama_aparente.find('e'))
        notation = self.gama_recipiente[first_index_notation:]
        
        if notation != self.gama_aparente[second_index_notation:]:
            return ('\nNotamos que o expoente não está igualado, considere rever isso')
        
        elif first_index_notation == -1 or second_index_notation == -1:
            return ('Não conseguimos entender nessa forma que você apresentou, reveja os formatos que está valendo!')
        
        else:
            pass

        valor_primeira_expressao = float(self.gama_recipiente[:first_index_notation])
        valor_segunda_expressao = float(self.gama_aparente[:second_index_notation])

        self.gama_real = valor_primeira_expressao + valor_segunda_expressao

        return f'Coeficiente volumétrico real é igual a: {self.gama_real}{notation}'

    def variacao_aparente(self):
        
        # // Decidindo a partir de dados do usuário como o programa irá se comportar.
        formula = int(input('''
Existe duas fórmulas para saber a variação aparente, veja os seus dados e perceba qual se encaixam melhor ^^

1 - ΔVap = yap * v0 * Δt
2 - ΔVr = ΔVap + ΔVrec

Qual você escolheu? '''))
        
        if formula == 1:
        
            print('\nA fórmula escolhida: (Δvap = yap * v0 * Δt)')
            print('\nQuando estiver falando de notações siga a estrutura no formato com o "e", ex: 1.5x10-³ = 1.5e-3')
            
            self.coeficiente_volumetrico_aparente = input('\nInforme o valor coeficiente volumétrico aparente: ')
            self.volume_inicial = float(input('\nInforme v0: '))
            self.variacao_tempo = float(input('\nInforme a Δt considere (Δt = t - t0): '))

            index_notation = self.coeficiente_volumetrico_aparente.find('e')
            operation = self.coeficiente_volumetrico_aparente[index_notation + 1: index_notation + 1]

            if index_notation == -1:
                return ('Formato errado, reveja a estrutura que estamos aceitando pls!!!')

            else:
                notation = self.coeficiente_volumetrico_aparente[index_notation:]

            valor_coeficiente = float(self.coeficiente_volumetrico_aparente[:index_notation])

            self.variacao_full = valor_coeficiente * self.volume_inicial * self.variacao_tempo

            if operation == '-':
                variacao_base_10 = self.variacao_full * 10 ** int(notation[1:] * -1)

            else:
                variacao_base_10 = self.variacao_full * 10 ** int(notation[1:])

            return (f'Notação Científica: {self.variacao_full}{notation} ou Formato valor real: {variacao_base_10}')
        
        elif formula == 2:
            print('\nA fórmula escolhida: ΔVr = ΔVap + ΔVrec')
            
            self.variacao_real = float(input("\nInforme a varição volumétrica real (Δvr): "))
            self.variacao_recipiente = float(input('\nInforme a variação volumétrica do recipiente (Δvrec): '))
            self.variacao__aparente = self.variacao_real - self.variacao_recipiente

            return f'A variação aparente (ΔVap): {self.variacao__aparente}'
            
        else:
            return ('Reveja as opcões na tabela e tente novamente :/')

# // Qualquer dúvidas em relação ao code, se direcionar ao Dev do repositório.