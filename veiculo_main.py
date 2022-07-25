#Arthur Vinicius Gouvea Sandim
#21204602
from veiculo import Carro,Moto

listaVeiculos = []

while True:#abre o menu de opções de veículos
    print('------- Controle de Veículos -------')
    print()
    print('1 - Cadastrar veículo')
    print('2 - Consultar veículo por placa')
    print('3 - Consultar lista de veículos cadastrados')
    print('4 - Encerrar programa')
    print()
    opc2 = int(input('Digite a opção desejada: '))
    print()
    while not 0<opc2<5:#valida opções inválidas
        print('- Opção inválida -')
        print()
        opc2 = int(input('Digite a opção desejada novamente: '))
        print()  
    if opc2 == 4:#encerra a execução do programa
        print('*'*34)
        print('Fim da execução do programa.')
        break
    elif opc2 == 1:#cadastro de veículo
        print('------ Cadastro de Veículos ------')
        print()
        tipo = str(input('Tipo[Carro/Moto]: '))
        #valida o tipo do veículo pois é ele quem determina a criação do objeto por herança
        if tipo.lower() != 'carro' and tipo.lower() != 'moto':
            print()                                           
            print('- Tipo de veículo inválido -')
            print()                 
            continue
        dono = str(input('Proprietário: '))
        marca = str(input('Marca: '))
        modelo = str(input('Modelo: '))
        cor = str(input('Cor: '))
        placa = str(input('Placa: ').upper())
        if tipo.lower() == 'carro':
            veic = Carro(marca, modelo, cor, placa, dono)
            listaVeiculos.append(veic)
            print()
            print('- Veículo cadastrado -')
        elif tipo.lower() == 'moto':
            veic = Moto(marca, modelo, cor, placa, dono)
            listaVeiculos.append(veic)
            print()
            print('- Veículo cadastrado -')
        print()               
    elif opc2 == 2:#consulta, alteração e exclusão de veículos
        print('-- Consulta de Veículos por Placa --')
        print()                
        placa = str(input('Digite a placa do veículo: ').upper())
        print()   
        if listaVeiculos == []:#valida veiculo nao encontrado se lista vazia
            print('- Veículo não localizado -')                       
            print()
        else:
            cnt = 0
            for veiculo in listaVeiculos:
                if placa == veiculo.getPlaca():
                    cnt+=1
                    veiculo.mostra_dados()
                    #menu de alteração e exclusão de veículo
                    print('-- Escolha uma ação --')
                    print('1 - Alterar Veículo')
                    print('2 - Excluir Veículo')
                    print('3 - Voltar para o menu anterior')
                    print()
                    opc3 = int(input('Digite a opção desejada: '))
                    print()
                    while not 0<opc3<4:#valida opções inválidas
                        print('- Opção inválida -')
                        print()
                        opc3 = int(input('Digite a opção desejada novamente: '))  
                    if opc3 == 3:#sai do laço
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
                        
                        if not 0<opc4<7:#valida opções inválidas
                            print('- Opção inválida -')
                            print()
                            opc4 = int(input('Digite a opção desejada novamente: '))                            
                        elif opc4 == 6:#sai do laço
                            break                         
                        elif opc4 == 1:#alttera dono
                            novo_dono = str(input('Novo Proprietário: '))
                            veiculo.setDono(novo_dono)
                            print("- Veículo alterado -")
                            veiculo.mostra_dados()
                        elif opc4 == 2:#altera marca
                            nova_marca = str(input('Nova Marca: '))
                            veiculo.setMarca(nova_marca) 
                            print("- Veículo alterado -")
                            veiculo.mostra_dados()
                        elif opc4 == 3:#altera modelo
                            novo_modelo = str(input('Novo Modelo: '))
                            veiculo.setModelo(novo_modelo)
                            print("- Veículo alterado -")
                            veiculo.mostra_dados()                               
                        elif opc4 == 4:#altera cor
                            nova_cor = str(input('Nova Cor: '))
                            veiculo.setCor(nova_cor)
                            print("- Veículo alterado -")
                            veiculo.mostra_dados()
                        elif opc4 == 5:#altera placa
                            nova_placa = str(input('Nova Placa: '))
                            veiculo.setPlaca(nova_placa)
                            print("- Veículo alterado -")
                            veiculo.mostra_dados()
                    elif opc3 == 2:#exclusão de veículos
                        for veiculo in listaVeiculos:
                            if placa == veiculo.getPlaca():
                                listaVeiculos.remove(veiculo)
                                print('- Veículo removido -')
                                print()
                    else:
                        print('- Veículo não localizado -')                        
                        print()
                        break
            if (cnt==0) and listaVeiculos != []:
                print('- Veículo não localizado -')                        
                print()
    elif opc2 == 3:#lista de veiculos cadastrados
        print('-------- Veículos Cadastrados ------')
        print()
        veic_cadast = dict() #USO DO DICIONÁRIO            
        if listaVeiculos == []:
            print('- Não há veículos cadastrados -')                        
            print()
        else:
            for element in listaVeiculos:
                veic_cadast[element.getDono()] = f"{element.getMarca()} / {element.getModelo()} / {element.getPlaca()}"
            for p,v in veic_cadast.items():
                print("Proprietário: ", p)
                print("Veiculo:", v)
                print()
