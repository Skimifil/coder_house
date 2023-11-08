class Retangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def area(self):
        print(f"{self.base * self.altura} é a area")

    def perimetro(self):
        print(f"{2*(self.base * self.altura)} é o perimetro")
