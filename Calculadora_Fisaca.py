# Projeto Calculadora Física

from Funcoes_calculadora import *  # Certifique-se de que o módulo se chama Funcoes_calculadora.py

def menu_principal():
    print("\033[1;41m ATENCAO: CASO DIGITE UM COMANDO INVALIDO O PROGRAMA PODE FALHAR! TENHA CUIDADO COM O QUE DIGITA.\033[m")
    opcao = 0
    while opcao != 6:
        print("\n                    MENU CALCULADORA:                    ")
        print("""
            [ 1 ] CINEMATICA 
            [ 2 ] ELECTRODINAMICA 
            [ 3 ] ELETROESTATICA 
            [ 4 ] TRABALHO E ENERGIA
            [ 5 ] DINAMICA
            [ 6 ] SAIR!
        """)
        try:
            opcao = int(input("Escolha uma das opções: "))
        except ValueError:
            print("Opção inválida! Por favor, digite um número.")
            continue
        
        if opcao == 1:
            menu_cinematica()
        elif opcao == 2:
            menu_eletrodinamica()
        elif opcao == 3:
            menu_eletroestatica()
        elif opcao == 4:
            menu_trabalho_energia()
        elif opcao == 5:
            menu_dinamica()
        elif opcao == 6:
            print("Saindo...")
        else:
            print("Opção inválida. Tente novamente.")

# Menu de Cinemática
def menu_cinematica():
    while True:
        print("\n                    MENU CINEMATICA:                    ")
        print("""
            [ 1 ] Equação da Velocidade
            [ 2 ] Equação do Deslocamento
            [ 3 ] Equação de Torricelli
            [ 4 ] Velocidade Média
            [ 5 ] Aceleração Média
            [ 6 ] Voltar ao Menu Principal
        """)
        
        try:
            calculo = int(input("O que você quer calcular: "))
        except ValueError:
            print("Entrada inválida! Por favor, digite um número.")
            continue
        
        if calculo == 1:
            v0 = float(input("Informe o valor da velocidade inicial (m/s): "))
            a = float(input("Informe o valor da aceleração (m/s²): "))
            t = float(input("Informe o valor do tempo (s): "))
            print(f"V = {equacao_velocidade(v0, a, t):.2f} m/s")
        
        elif calculo == 2:
            v0 = float(input("Informe o valor da velocidade inicial (m/s): "))
            a = float(input("Informe o valor da aceleração (m/s²): "))
            t = float(input("Informe o valor do tempo (s): "))
            print(f"S = {equacao_deslocamento(v0, a, t):.2f} m")
        
        elif calculo == 3:
            v0 = float(input("Informe o valor da velocidade inicial (m/s): "))
            a = float(input("Informe o valor da aceleração (m/s²): "))
            s0 = float(input("Informe a posição inicial (m): "))
            s = float(input("Informe a posição final (m): "))
            print(f"V² = {equacao_torricelli(v0, a, s, s0):.2f} m²/s²")
        
        elif calculo == 4:
            s0 = float(input("Informe o valor da posição inicial (m): "))
            s1 = float(input("Informe o valor da posição final (m): "))
            t0 = float(input("Informe o tempo inicial (s): "))
            t1 = float(input("Informe o tempo final (s): "))
            print(f"Velocidade Média = {velocidade_media(s0, s1, t0, t1):.2f} m/s")
        
        elif calculo == 5:
            v0 = float(input("Informe o valor da velocidade inicial (m/s): "))
            v1 = float(input("Informe o valor da velocidade final (m/s): "))
            t0 = float(input("Informe o tempo inicial (s): "))
            t1 = float(input("Informe o tempo final (s): "))
            print(f"Aceleração Média = {aceleracao_media(v0, v1, t0, t1):.2f} m/s²")
        
        elif calculo == 6:
            break
        
        else:
            print("Opção inválida! Tente novamente.")

# Menu de Eletrodinâmica
def menu_eletrodinamica():
    while True:
        print("\n                    MENU ELETRODINAMICA:                    ")
        print("""
            [ 1 ] Lei de Ohm
            [ 2 ] Potência Elétrica
            [ 3 ] Resistência Elétrica
            [ 4 ] Voltar ao Menu Principal
        """)
        
        try:
            calculo = int(input("O que você quer calcular: "))
        except ValueError:
            print("Entrada inválida! Por favor, digite um número.")
            continue
        
        if calculo == 1:
            V = float(input("Informe o valor da tensão (V): "))
            R = float(input("Informe o valor da resistência (Ω): "))
            print(f"I = {lei_ohm(V, R):.2f} A")
        
        elif calculo == 2:
            V = float(input("Informe o valor da tensão (V): "))
            I = float(input("Informe o valor da corrente (A): "))
            print(f"P = {potencia_eletrica(V, I):.2f} W")
        
        elif calculo == 3:
            V = float(input("Informe o valor da tensão (V): "))
            I = float(input("Informe o valor da corrente (A): "))
            print(f"R = {resistencia_eletrica(V, I):.2f} Ω")
        
        elif calculo == 4:
            break
        
        else:
            print("Opção inválida! Tente novamente.")

# Menu de Eletrostática
def menu_eletroestatica():
    while True:
        print("\n                    MENU ELETROESTATICA:                    ")
        print("""
            [ 1 ] Lei de Coulomb
            [ 2 ] Campo Elétrico
            [ 3 ] Potencial Elétrico
            [ 4 ] Voltar ao Menu Principal
        """)
        
        try:
            calculo = int(input("O que você quer calcular: "))
        except ValueError:
            print("Entrada inválida! Por favor, digite um número.")
            continue
        
        if calculo == 1:
            q1 = float(input("Informe a carga q1 (C): "))
            q2 = float(input("Informe a carga q2 (C): "))
            r = float(input("Informe a distância entre as cargas (m): "))
            print(f"F = {lei_coulomb(q1, q2, r):.2f} N")
        
        elif calculo == 2:
            q = float(input("Informe a carga (C): "))
            r = float(input("Informe a distância (m): "))
            print(f"E = {campo_eletrico(q, r):.2f} N/C")
        
        elif calculo == 3:
            q = float(input("Informe a carga (C): "))
            r = float(input("Informe a distância (m): "))
            print(f"V = {potencial_eletrico(q, r):.2f} V")
        
        elif calculo == 4:
            break
        
        else:
            print("Opção inválida! Tente novamente.")

# Menu de Trabalho e Energia
def menu_trabalho_energia():
    while True:
        print("\n                    MENU TRABALHO E ENERGIA:                    ")
        print("""
            [ 1 ] Energia Cinética
            [ 2 ] Energia Potencial Gravitacional
            [ 3 ] Trabalho
            [ 4 ] Potência
            [ 5 ] Voltar ao Menu Principal
        """)
        
        try:
            calculo = int(input("O que você quer calcular: "))
        except ValueError:
            print("Entrada inválida! Por favor, digite um número.")
            continue
        
        if calculo == 1:
            m = float(input("Informe a massa (kg): "))
            v = float(input("Informe a velocidade (m/s): "))
            print(f"Energia Cinética = {energia_cinetica(m, v):.2f} J")
        
        elif calculo == 2:
            m = float(input("Informe a massa (kg): "))
            h = float(input("Informe a altura (m): "))
            g = float(input("Informe a aceleração da gravidade (m/s²): "))
            print(f"Energia Potencial = {energia_potencial(m, h, g):.2f} J")
        
        elif calculo == 3:
            F = float(input("Informe a força (N): "))
            d = float(input("Informe a distância (m): "))
            theta = float(input("Informe o ângulo (graus): "))
            print(f"Trabalho = {trabalho(F, d, theta):.2f} J")
        
        elif calculo == 4:
            trabalho = float(input("Informe o trabalho realizado (J): "))
            tempo = float(input("Informe o tempo (s): "))
            print(f"Potência = {potencia(trabalho, tempo):.2f} W")
        
        elif calculo == 5:
            break
        
        else:
            print("Opção inválida! Tente novamente.")

# Menu de Dinâmica
def menu_dinamica():
    while True:
        print("\n                    MENU DINAMICA:                    ")
        print("""
            [ 1 ] Segunda Lei de Newton
            [ 2 ] Força Peso
            [ 3 ] Força Centrípeta
            [ 4 ] Quantidade de Movimento
            [ 5 ] Voltar ao Menu Principal
        """)
        
        try:
            calculo = int(input("O que você quer calcular: "))
        except ValueError:
            print("Entrada inválida! Por favor, digite um número.")
            continue
        
        if calculo == 1:
            m = float(input("Informe a massa (kg): "))
            a = float(input("Informe a aceleração (m/s²): "))
            print(f"F = {segunda_lei_newton(m, a):.2f} N")
        
        elif calculo == 2:
            m = float(input("Informe a massa (kg): "))
            g = float(input("Informe a aceleração da gravidade (m/s²): "))
            print(f"Peso = {forca_peso(m, g):.2f} N")
        
        elif calculo == 3:
            m = float(input("Informe a massa (kg): "))
            v = float(input("Informe a velocidade (m/s): "))
            r = float(input("Informe o raio (m): "))
            print(f"Força Centrípeta = {forca_centripeta(m, v, r):.2f} N")
        
        elif calculo == 4:
            m = float(input("Informe a massa (kg): "))
            v = float(input("Informe a velocidade (m/s): "))
            print(f"Quantidade de Movimento = {quantidade_de_movimento(m, v):.2f} kg.m/s")
        
        elif calculo == 5:
            break
        
        else:
            print("Opção inválida! Tente novamente.")

# Execução do Programa
if __name__ == "__main__":
    menu_principal()
