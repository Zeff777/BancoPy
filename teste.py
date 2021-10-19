from models.cliente import Cliente
from models.conta import Conta


daniel: Cliente = Cliente('Daniel Silva', 'daniel@gmail.com', '123.456.789-99', '04/08/1997')
emma: Cliente = Cliente('Emma Silver', 'emma@hotmail.com', '987.654.321.00', '17/05/1997')
print(daniel)
print()
print(emma)
print('-------------------------------')
print()


contaA: Conta = Conta(daniel)
contaB: Conta = Conta(emma)

print(contaA)
print(contaB)


