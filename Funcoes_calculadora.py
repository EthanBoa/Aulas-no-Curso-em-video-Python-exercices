#Modulo de funcoes da calculadora

import math


#CINEMATICA
# Equação da Velocidade
def equacao_velocidade(v0=1, a=1, t=1):
    return v0 + a * t

# Equação do Deslocamento
def equacao_deslocamento(v0=1, a=1, t=1):
    return v0 * t + 0.5 * a * t**2

# Equação de Torricelli
def equacao_torricelli(v0=1, a=1, s=1, s0=0):
    return (v0**2 + 2 * a * (s - s0))**0.5

# Velocidade Média
def velocidade_media(s0=0, s1=1,t0=0, t1=1):
    return (s1-s0) / (t1-t0)

# Aceleração Média
def aceleracao_media(v0=0, v1=1,t0=0, t1=1):
    return (v1-v0) / (t1-t0)



#ELECTRODINAMICA
# Lei de Ohm
def lei_ohm(V=1, R=1):
    return V / R  # Corrente (I = V / R)

# Potência Elétrica
def potencia_eletrica(V=1, I=1):
    return V * I

# Resistência Elétrica
def resistencia_eletrica(V=1, I=1):
    return V / I

# Tensão Elétrica (ou Diferença de Potencial)
def tensao_eletrica(I=1, R=1):
    return I * R

# Intensidade da Corrente
def intensidade_corrente(V=1, R=1):
    return V / R



#ELETROESTATICA
# Lei de Coulomb
def lei_coulomb(q1=1, q2=1, r=1):
    k = 9*10**9  # Constante de Coulomb (N m²/C²)
    return k * q1 * q2 / r**2

# Campo Elétrico
def campo_eletrico(q=1, r=1):
    k = 9*10**9   # Constante de Coulomb
    return k * q / r**2

# Potencial Elétrico
def potencial_eletrico(q=1, r=1):
    k = 9*10**9  # Constante de Coulomb
    return k * q / r



#TRABALHO E ENERGIA
# Energia Cinética
def energia_cinetica(m=1, v=1):
    return 0.5 * m * v**2

# Energia Potencial Gravitacional
def energia_potencial(m=1, h=1, g=9.8):
    return m * g * h

# Energia Mecânica Total
def energia_mecanica_total(energia_cinetica, energia_potencial):
    return energia_cinetica + energia_potencial

# Trabalho
def trabalho(F=1, d=1, theta=0):
    return F * d * math.cos(math.radians(theta))

# Potência
def potencia(trabalho=1, tempo=1):
    return trabalho / tempo



#DINAMICA
# Segunda Lei de Newton
def segunda_lei_newton(m=1, a=1):
    return m * a  # Força (F = ma)

# Força Peso
def forca_peso(m=1, g=9.8):
    return m * g  # Peso (P = mg)

# Força Centrípeta
def forca_centripeta(m=1, v=1, r=1):
    return m * v**2 / r

# Quantidade de Movimento (Momento Linear)
def quantidade_de_movimento(m=1, v=1):
    return m * v

