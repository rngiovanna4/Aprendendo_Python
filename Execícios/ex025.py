'''Leia um nome completo e veja se possue  Silva'''
nome = input('Digite se nome completo').strip().upper()

if 'SILVA' in nome:
    print('Tem Silva no nome')
else:
    print('Não tem Silva no nome')