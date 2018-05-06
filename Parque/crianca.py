"""
CENTRO UNIVERSITÁRIO METODISTA IZABELA HENDRIX
PROGRAMAÇÃO FUNCIONAL ORIENTADA A OBJETOS - PYTHON
Projeto Integrador - Exercício 08 - DESAFIO
por Layla Comparin
"""

class Crianca:
  def __init__(self, n, d):  
      self.nome = n
      self.idade = d
      self.pegador = False
      self.correndo = False
      self.paralisado = False

  def correr(self):
        if self.paralisado:
            print('Não posso correr! Alguém me salva!')
        else:
            self.correndo = True
            print('Estou correndo. Ninguém me pega!!')

  def salvar(self, otherchildren):
        if self.correndo:
            if otherchildren.paralisado and not self.pegador:
                otherchildren.paralisado = False
                print(f'Te salvei! Começa a correr {otherchildren.nome}!!')

            elif self.pegador:
                print('Tenho que pegá-los!')

            else:
                print('Estou livre!')
        else:
            print('Preciso correr para salvar alguém!')

class Pegador(Crianca):
    def __init__(self, nome, datanasc):
        Crianca.__init__(self, nome, datanasc)
        self.pegador = True

    def pegar(self, otherchildren):
        if self.correndo:
            if otherchildren.paralisado:
                print('Já estou paralisado!')
            else:
                otherchildren.paralisado = True
                print(f'Te peguei!! Agora você está paralisado {otherchildren.nome}!')
        else:
            print('Não estou correndo, não posso pegar ninguém parado!')
