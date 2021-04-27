class Cadastro:

    __slots__ = ["_lista_pessoas"]


    def __init__(self):
        self._lista_pessoas = []


    @property
    def lista_pessoas(self):
        return 


    def cadastra(self, pessoa):
        existe = self.busca(pessoa.cpf)
        if (existe):
            return False
        else:
            self._lista_pessoas.append(pessoa)
            return True

    
    def busca(self, cpf):
        for pessoa in self._lista_pessoas:
            if (cpf == pessoa.cpf):
                return pessoa
        return None
