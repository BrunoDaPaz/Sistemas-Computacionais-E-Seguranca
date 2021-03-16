from random import random


class Calculadora:

    def __init__(self, numero, numero2):
        self._Numero = numero
        self._Numero2 = numero2

    @property
    def numero(self):
        return self._Numero
    @numero.setter
    def numero(self, numero):
        self._Numero = numero

    @property
    def numero2(self):
        return self._Numero2
    @numero2.setter
    def numero2(self, numero2):
        self._Numero2 = numero2

    def converteBinario(self, numero):
        binario = ""
        while numero != 0:
            binario = binario + str(numero % 2)
            numero = int(numero / 2)
        print('Resultado em BINÁRIO: {}'.format(binario[::-1]))

    def converteOctal(self, numero):
        octal = ""
        while numero != 0:
            octal = octal + str(numero % 8)
            numero = int(numero / 8)
        print('\nResultado em OCTAL: {}'.format(octal[::-1]))

    def converteHexa(self, numero):
        hexadecimal = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, "A", "B", "C", "D", "E", "F"]
        resultado = []
        while numero > 0:
            resultado.append(hexadecimal[(numero % 16)])
            numero = numero // 16
        print('\nResultado em HEXADECIMAL: ', end='')
        print(''.join(map(str, resultado[::-1])))

    def somaBinario(self, numero, numero2):
        resultadoSoma = numero + numero2
        self.converteBinario(resultadoSoma)

    def somaHexa(self, numero, numero2):
        resultadoSoma = numero + numero2
        self.converteHexa(resultadoSoma)

    def somaOctal(self, numero, numero2):
        resultadoSoma = numero + numero2
        self.converteOctal(resultadoSoma)

    def subtrairBinario(self, numero, numero2):
        resultadoSubtracao = numero - numero2
        if  (resultadoSubtracao == 0):
            print('O resultado é ZERO!')
        else:
            self.converteBinario(resultadoSubtracao)

    def subtrairHexa(self, numero, numero2):
        resultadoSubtracao = numero - numero2
        if  (resultadoSubtracao == 0):
            print('O resultado é ZERO!')
        else:
            self.converteHexa(resultadoSubtracao)

    def subtrairOctal(self, numero, numero2):
        resultadoSubtracao = numero - numero2
        if  (resultadoSubtracao == 0):
            print('O resultado é ZERO!')
        else:
            self.converteOctal(resultadoSubtracao)

    def multiplicarBinario(self, numero, numero2):
        resultadoMultipliacao = numero * numero2
        self.converteBinario(resultadoMultipliacao)

    def multiplicarHexa(self, numero, numero2):
        resultadoMultipliacao = numero * numero2
        self.converteHexa(resultadoMultipliacao)

    def multiplicarOctal(self, numero, numero2):
        resultadoMultipliacao = numero * numero2
        self.converteOctal(resultadoMultipliacao)

    def converteBinDec(self, numero):

        import random
        vet = [0] * 8
        for i in range(8):
            vet[i] = random.randint(0, 1)
        print('O valor em binário gerado foi: ' + str(vet))

        soma = 0
        pot = 7
        for i in range(8):
            soma = soma + (vet[i] * (2 ** pot))
            pot = pot - 1
        print('O valor convertido para decimal é: ' + str(soma))

    def converteHexBin(self, numero):
        print('\nResultado em Binário: {}'.format(octal[::-1]))