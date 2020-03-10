class Mascote(object):

    def __init__(self, name, age, race, sex):
        self.name = name
        self.age = age
        self.race = race
        self.sex = sex
        self.perdido = False

    def printando(self):
        print("Printando Dados do Mascote\nNome: {0}; \nIdade: {1};\nRaça: {2};\nSexo: {3};\nEstá Perdido: {4}\n\n".format(self.name, self.age, self.race, self.sex,self.perdido))



class MascotePerdido(object):

    def __init__(self, mascote, local, data, hora, condicao):
        print("O Mascote {0} foi perdido!".format(mascote.name))
        self.mascote = mascote
        self.local = local
        self.data = data
        self.hora = hora
        self.condicao = condicao
        self.mascote.perdido = True

    def printando(self):
        print("Dados do Mascote Perdido\nNome: {0}; \nIdade: {1};\nRaça: {2};\nSexo: {3};\n".format(self.mascote.name, self.mascote.age, self.mascote.race, self.mascote.sex))
        print("Local: {0}\nHora: {1}\nData: {2}\nCondição: {3}\n\n".format(self.local,self.hora,self.data,self.condicao))

class MascoteEncontrado(object):

    def __init__(self, mascote, local, data, hora, condicao):
        print("O Mascote {0} foi encontrado!".format(mascote.name))
        self.mascote = mascote
        self.local = local
        self.data = data
        self.hora = hora
        self.condicao = condicao
        self.mascote.perdido = False

    def printando(self):
        print("Dados do Mascote Encontrado\nNome: {0}; \nIdade: {1};\nRaça: {2};\nSexo: {3};\n".format(self.mascote.name, self.mascote.age, self.mascote.race, self.mascote.sex))
        print("Local: {0}\nHora: {1}\nData: {2}\nCondição: {3}\n\n".format(self.local,self.hora,self.data,self.condicao))





dog = Mascote("Jubileu",5,"Lião","Macholous")
dog.printando()
perdido = MascotePerdido(dog,"Av. Brasil","20/12/2009","10:30","Passeando")
perdido.printando()
dog.printando()
encontrado = MascoteEncontrado(dog,"Av. Paulista","12/02/2010","21:20","Dormindo")
encontrado.printando()
dog.printando()
