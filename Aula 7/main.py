import pandas as pd
import numpy as np

#                   Exercício 1                   #
# Criar um array com 10 elementos inteiros aleatórios no intervalo [0, 100]
array = np.random.randint(0, 101, 10)

# Exibir os valores do array
print("Valores do array:", array)

# Exibir o tipo de dado do array
print("Tipo de dado do array:", array.dtype)
print("#######################################################")

#                   Exercício 2                   #
# Criar uma matriz de 5x5 com valores aleatórios no intervalo [0, 1]
matriz = np.random.rand(5, 5)

# Exibir a matriz
print("Matriz:")
print(matriz)

# Encontrar o valor mínimo, máximo e média da matriz
valor_minimo = np.min(matriz)
valor_maximo = np.max(matriz)
media = np.mean(matriz)

# Exibir os resultados
print("\nValor Mínimo:", valor_minimo)
print("Valor Máximo:", valor_maximo)
print("Média:", media)
print("#######################################################")

#                   Exercício 3                   #
# Criar um array com 10 elementos aleatórios no intervalo [0, 1]
array_original = np.random.rand(10)

# Exibir o array original
print("Array Original:")
print(array_original)

# Multiplicar por 10 e converter para inteiro
array_modificado = (array_original * 10).astype(int)

# Exibir o novo array
print("\nNovo Array:")
print(array_modificado)
print("#######################################################")

#                   Exercício 4                   #
# Criar um array de duas dimensões com shape (3, 3) e valores aleatórios inteiros no intervalo [0, 9]
array = np.random.randint(0, 10, (3, 3))

# Exibir o array original
print("Array Original:")
print(array)

# Substituir todos os elementos da segunda linha por -1
array[1, :] = -1

# Exibir o array modificado
print("\nArray Modificado:")
print(array)
print("#######################################################")

#                   Exercício 5                   #
# Criar um DataFrame com as informações dadas
data = {
    'fruta': ['Banana', 'Maça', 'Pera'],
    'preco': [7.90, 10.20, 11.80],
    'quantidade': [12, 3, 4]
}

df = pd.DataFrame(data)

# Exibir o DataFrame
print(df)