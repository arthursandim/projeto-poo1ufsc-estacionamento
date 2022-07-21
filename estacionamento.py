from veiculo import Carro,Moto

while True:#abre o menu principal do sistema
    vagas = [['']*4]*5
    listaVeiculos = []
    print('--- Controle de estacionamento ---')
    print()
    print('1 - Consultar vagas')
    print('2 - Opções de veículos')
    print('3 - Cadastrar/Remover veículo na vaga')
    print('4 - Calcular preço final')
    print('5 - Sair')
    print()
    opc = int(input('Digite a opção desejada: '))
    print()
    if not 0<opc<6:#valida opções inválidas
        print('-- Opção inválida --')
        print()
        opc = int(input('Digite a opção desejada novamente: '))   
    elif opc == 5:#Encerra o programa
        print("-"*34)
        print('Fim da execução do programa.')
        break
        print()
    elif opc == 1:#consultar vagas
        print(f'-------------- Vagas -------------')
        print()
        cont = 1
        for i in range(0,5):
            for j in range(0,4):
                if cont < 10:
                        print(f'[0{cont} {vagas[i][j]:^5}]', end='')
                else:
                    print(f'[{cont} {vagas[i][j]:^5}]', end='') 
                cont+=1   
            print()
        print()       
    elif opc == 2:#opções de veículos
        
        while True:#abre o menu de opções de veículos
            print('------- Opções de Veículos -------')
            print()
            print('1 - Cadastrar veículo')
            print('2 - Consultar veículo por placa')
            print('3 - Consultar lista de veículos cadastrados')
            print('4 - Voltar para o menu anterior')
            print()
            opc2 = int(input('Digite a opção desejada: '))
            print()
            if not 0<opc<5:#valida opções inválidas
                print('-- Opção inválida --')
                print()
                opc2 = int(input('Digite a opção desejada novamente: '))  
            elif opc2 == 4:#sair do laço
                break
            elif opc2 == 1:#cadastro de veículo
                print('------ Cadastro de Veículos ------')
                print()
                tipo = str(input('Tipo[Carro/Moto]: '))
                #valida o tipo do veículo pois é ele quem determina a criação do objeto por herança
                while tipo.lower() != 'carro' and tipo.lower() != 'moto':
                    print()
                    print()                                               
                    print('-- Tipo de veículo inválido --')              
                    tipo = str(input('Tipo[Carro/Moto]: '))
                dono = str(input('Proprietário: '))
                marca = str(input('Marca: '))
                modelo = str(input('Modelo: '))
                cor = str(input('Cor: '))
                placa = str(input('Placa: ').upper())
                if tipo.lower() == 'carro':
                    veic = Carro(marca, modelo, cor, placa, dono)
                    listaVeiculos.append(veic)
                    print()
                    print('-- Veículo cadastrado --')
                elif tipo.lower() == 'moto':
                    veic = Moto(marca, modelo, cor, placa, dono)
                    listaVeiculos.append(veic)
                    print()
                    print('-- Veículo cadastrado --')
                print()               
            elif opc2 == 2:#consulta, alteração e exclusão de veículos
                print('-- Consulta de Veículos por Placa --')
                print()                
                placa = str(input('Digite a placa do veículo: ').upper())
                print()   
                if listaVeiculos == []:#valida veiculo nao encontrado se lista vazia
                    print('-- Veículo não localizado-- ')                        
                    print()
                for veiculo in listaVeiculos:
                    if placa == veiculo.getPlaca():
                        veiculo.mostra_dados()
                        #menu de alteração e exclusão de veículo
                        print('-- Escolha uma ação --')
                        print('1 - Alterar Veículo')
                        print('2 - Excluir Veículo')
                        print('3 - Voltar para o menu anterior')
                        print()
                        opc3 = int(input('Digite a opção desejada: '))
                        print()
                        if not 0<opc<4:#valida opções inválidas
                            print('-- Opção inválida --')
                            print()
                            opc3 = int(input('Digite a opção desejada novamente: '))  
                        elif opc3 == 3:#sai do laço
                            break
                        elif opc3 == 1:#alteração de veículos
                            print('-- Escolha uma ação --')
                            print("1 - Alterar Proprietário")
                            print("2 - Alterar Marca")
                            print("3 - Alterar Modelo")
                            print("4 - Alterar Cor")
                            print("5 - Alterar Placa")
                            print("6 - Voltar para o menu anterior")
                            print()
                            opc4 = int(input('Digite a opção desejada: '))
                            print()
                            
                            if not 0<opc<7:#valida opções inválidas
                                print('-- Opção inválida --')
                                print()
                                opc3 = int(input('Digite a opção desejada novamente: '))                            
                            elif opc4 == 6:#sai do laço
                                break                         
                            elif opc4 == 1:#alttera dono
                                novo_dono = str(input('Novo Proprietário: '))
                                veiculo.setDono(novo_dono)
                                print("-- Veículo editado --")
                                veiculo.mostra_dados()
                            elif opc4 == 2:#altera marca
                                nova_marca = str(input('Nova Marca: '))
                                veiculo.setMarca(nova_marca) 
                                print("-- Veículo editado --")
                                veiculo.mostra_dados()
                            elif opc4 == 3:#altera modelo
                                novo_modelo = str(input('Novo Modelo: '))
                                veiculo.setModelo(novo_modelo)
                                print("-- Veículo editado --")
                                veiculo.mostra_dados()                               
                            elif opc4 == 4:#altera cor
                                nova_cor = str(input('Nova Cor: '))
                                veiculo.setCor(nova_cor)
                                print("-- Veículo editado --")
                                veiculo.mostra_dados()
                            elif opc4 == 5:#altera placa
                                nova_placa = str(input('Nova Placa: '))
                                veiculo.setPlaca(nova_placa)
                                print("-- Veículo editado --")
                                veiculo.mostra_dados()
                        elif opc3 == 2:#exclusão de veículos
                            for veiculo in listaVeiculos:
                                if placa == veiculo.getPlaca():
                                    listaVeiculos.remove(veiculo)
                                    print('-- Veículo removido --')
                                    print()
                    else:
                        print('- Veículo não localizado -')                        
                        print()
            elif opc2 == 3:#lista de veiculos cadastrados
                print('--- Veículos  Cadastrados ---')
                print()
                veic_cadast = dict()             
                if listaVeiculos == []:
                    print('-- Não há veículos cadastrados --')                        
                    print()
                else:
                    for element in listaVeiculos:
                        veic_cadast[element.getDono()] = f"{element.getMarca()}/{element.getModelo()}/{element.getPlaca()}"
                    for p,v in veic_cadast.items():
                        print("Proprietário: ", p)
                        print("Veiculo:", v)
                        print()