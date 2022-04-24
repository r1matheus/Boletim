# -*- coding: UTF-8 -*-
# Introdução do código
nome = str(input('Digite seu nome: '))
ra = int(input('Digite seu R.A: '))
maiusculo = nome.title()
print("Perfeito {}, estamos validando seu R.A" .format(maiusculo))
print("****************************************************")

# nome das materias
py_nome = "Python"
eng_nome = "Engenharia de SW"
arq_nome = "Arquitetura de Computadores"
so_nome = "Sistemas Operacionais"
prj_nome = "Projetos"


# Notas e Calculo das notas
py = int(input('Qual foi nota na P1 de Python: '))
py2 = int(input('Qual foi nota na P2 de Python: '))
media_py = py + py2 / 2
print("****************************************************")

eng = int(input('Qual foi nota na P1 de Engenharia de SW: '))
eng2 = int(input('Qual foi nota na P2 de Engenharia de SW: '))
media_en = eng + eng2 / 2
print("****************************************************")

arq = int(input('Qual foi nota na P1 de Arquitetura de Computadores: '))
arq2 = int(input('Qual foi nota na P2 de Arquitetura de Computadores: '))
media_arq = arq + arq2 / 2
print("****************************************************")

so = int(input('Qual foi nota na P1 de Sistemas Operacionais: '))
so2 = int(input('Qual foi nota na P2 de Sistemas Operacionais: '))
media_so = so + so2 / 2
print("****************************************************")

prj = int(input('Qual foi nota na P1 de Projetos: '))
prj2 = int(input('Qual foi nota na P2 de Projetos: '))
media_prj = prj + prj2 / 2
print("****************************************************")
print("****************************************************")


# Aprovado ou Reprovados

# Python
if media_py > 7:
    print("{}, Você foi Aprovado em {}" .format(maiusculo, py_nome))
else:
    print("{}, Você foi REPROVADO Reprovado em {}" .format(maiusculo, py_nome))

# Engenharia
if media_en > 7:
    print("{}, Você foi Aprovado em {}" .format(maiusculo, eng_nome))
else:
    print("{}, Você foi REPROVADO Reprovado {}" .format(maiusculo, eng_nome))

# Arquitetura
if media_arq > 7:
    print("{}, Você foi Aprovado em {}" .format(maiusculo, arq_nome))
else:
    print("{}, Você foi REPROVADO em {}" .format(maiusculo, arq_nome))

# Sistemas Operacionais
if media_so > 7:
    print("{}, Você foi Aprovado em {}" .format(maiusculo, so_nome))
else:
    print("{}, Você foi REPROVADO em {}" .format(maiusculo, so_nome))

# Projetos
if media_prj > 7:
    print("{}, Você foi Aprovado em {}" .format(maiusculo, prj_nome))
else:
    print("{}, Você foi REPROVADO em {}" .format(maiusculo, prj_nome))
