class Televisao:
    def __init__(self):
        self.ligada = False
        self.canal = 5

    def power(self):
        if self.ligada:
            self.ligada = False
        else:
            self.ligada = True

    def aumenta_canal(self):
        self.canal += 1

    def diminui_canal(self):
        self.canal -= 1


if __name__ == '__main__':
    televisao = Televisao()
    print(televisao.ligada)

# televisao.power()
# print(televisao.ligada)
# televisao.power()
# print(televisao.ligada)
#
# print(televisao.canal)
# televisao.aumenta_canal()
# print(televisao.canal)
# televisao.aumenta_canal()
# print(televisao.canal)
#
# televisao.diminui_canal()
# print(televisao.canal)
