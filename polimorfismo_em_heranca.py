class Passaro():
    def voar(self):
        print("Voar")

class Pardal(Passaro):
    def voar(self):
        return super().voar()

class Avestrus(Passaro):
    def voar(self):
        print("Esta Ave nao pode voar")


def plano_de_voo(obj):
    obj.voar()

teste1 = Pardal()
teste2 = Avestrus()

plano_de_voo(teste1)
plano_de_voo(teste2)