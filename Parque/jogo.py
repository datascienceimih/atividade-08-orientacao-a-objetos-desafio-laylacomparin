"""
CENTRO UNIVERSITÁRIO METODISTA IZABELA HENDRIX
PROGRAMAÇÃO FUNCIONAL ORIENTADA A OBJETOS - PYTHON
Projeto Integrador - Exercício 08 - DESAFIO
por Layla Comparin
"""

from crianca import Crianca
from crianca import Pegador

crianca1 = Crianca('Layla', 10)
crianca2 = Crianca('Ana Clara', 8)
crianca3 = Pegador('Fernando', 9)

# Qual o nome e idade de vocês?
print('Meu nome é ' + crianca1.nome + ' e eu tenho ' + str(crianca1.idade) + ' anos.')
print('Meu nome é ' + crianca2.nome + ' e eu tenho ' + str(crianca2.idade) + ' anos.')
print('Meu nome é ' + crianca3.nome + ' e eu tenho ' + str(crianca3.idade) + ' anos.')

# Qual de vocês é o pegador?
print(crianca1.pegador)
print(crianca2.pegador)
print(crianca3.pegador)

## É hora do play:
crianca2.correr()
crianca3.correr()

crianca3.pegar(crianca2)
crianca2.correr()
crianca3.pegar(crianca2)
crianca1.salvar(crianca2)
crianca1.correr()
crianca1.salvar(crianca2)
crianca1.salvar(crianca2)
crianca3.salvar(crianca1)
