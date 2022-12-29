#Leia o salário de um funcionário e mostre seu novo salário com 15% de aumento
salary = float(input('Digite o salário:\n R$ '))
newsalary = (salary*0.15)+salary

print('O novo salário, após o reajuste de 15% é R${:.2f}'.format(newsalary))