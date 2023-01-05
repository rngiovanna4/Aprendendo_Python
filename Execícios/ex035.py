'''Leia três retas e vê se formam um triângulo'''
print('='*40)
print('Digite três segmentos de reta e descubra se eles formam um triângulo')
print('='*40)

r1 = float(input('1º segmento '))
r2 = float(input('2º segmento '))
r3 = float(input('3º segmento '))

if r1 < (r2 + r3) and r2 < r1 + r3 and r3 < (r2 + r1):
    print('Os segmentos formam um triângulo')
else:
    print('Os segmentos não formam um triângulo')
    