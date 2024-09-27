# x = input()

# X = x.upper()  # tudo maiúsculo

# print("entrada: ", x)
# print("entrada em maiúsculo: ", X)


texto = "meu dado"  # string
inteiro = 10, 9, 8, 7, 6, 5, 4, 3, 2, 1
real = 3.14  # float
booleano_verdadeiro = True  # bool
booleano_falso = False  # bool

type(texto)  # verifica o tipo da variável

# string -> str
# inteiro -> int
# real -> float
# booleano -> bool

# casting
# str -> float
float("3.14")
# str -> int
int("10")

# float -> int
int(3.14)
# int -> float
float(10)  # 10.0

# int -> str
str(10)  # "10"
# float -> str
str(3.14)  # "3.14"

# str -> bool
bool("True")  # True
bool("False")  # True
bool("")  # False

# int -> bool
bool(0)  # False
bool(1)  # True
bool(-1)  # True

# float -> bool
bool(0.0)  # False
bool(0.1)  # True
bool(-0.1)  # True


# Operações aritméticas

# soma
10 + 5  # 15
# subtração
10 - 5  # 5
# multiplicação
10 * 5  # 50
# divisão
10 / 5  # 2. -> float
# divisão inteira
10 // 5  # 2
# resto da divisão ou módulo
10 % 5  # 0
# avaliando se é par ou ímpar
10 % 2  # 0 -> par
11 % 2  # 1 -> ímpar

# potência
10**5  # 100000

# raiz quadrada
100**0.5  # 10.0


# Operações de comparação
# igualdade
10 == 5  # False
10 == 10  # True
# diferença
10 != 5  # True
10 != 10  # False
# maior
10 > 5  # True
10 > 10  # False
# menor
10 < 5  # False
10 < 10  # False
10 < 11  # True
# maior ou igual
10 >= 5  # True
10 >= 10  # True
10 >= 11  # False

# menor ou igual
10 <= 5  # False
10 <= 10  # True
10 <= 11  # True
