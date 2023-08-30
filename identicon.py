from pgl import GWindow, GRect, GOval, GPolygon
import hashlib


class Parser:
    def __init__(self, string):
        self.pattern = bin(int(hashlib.sha256(string).hexdigest(), 16))[2:]
        self.pos = 0
        self.color1 = None
        self.color2 = None
        self.assign_colors()

    def next(self, amount):
        bits = self.pattern[self.pos : self.pos + amount]
        while len(bits) < amount:
            bits += "0"
        self.pos += amount
        return bits

    def assign_colors(self):
        self.color1 = int(self.next(8))
        self.pos += 8
        self.color2 = int(self.next(8))

    def process(self):
        while self.pos < len(self.pattern):
            n = self.next(1)
            code = ""
            if n == "0":
                yield "Empty"
            else:
                color_opt = self.next(1)
                code += color_opt
                shape = int(self.next(2), 2)
                if shape == 0:
                    code += "C"
                elif shape == 1:
                    code += "T"
                elif shape == 2:
                    code += "t"
                elif shape == 3:
                    code += "S"
                code += self.next(1)
                yield code


test = Parser(b"jed rembold")
print(list(test.process()))
