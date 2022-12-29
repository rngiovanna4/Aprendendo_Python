#Um conversor de metros para centimetros e milimetros
from tkinter.tix import Meter


metrer = float(input('Digite o valor em metros: '))
centimeter = (metrer*100)
millimeter = (metrer*1000)

print('{}m equivale a {:.2f}cm\n{}m equivale a {:.2f}mm'.format(metrer,centimeter,metrer,millimeter))


