def binary_search(array, item):
    low = 0 
    high = len(array) - 1 

    while low <= high:
        mid = (low + high) // 2 
        guess = array[mid]
        if guess == item: 
            return mid 
        if guess > item: 
            high = mid - 1 
        else:
            low = mid + 1 
    return None 


my_array = [1, 3, 5, 7, 9]
print(binary_search(my_array, 3))

"""
Passo a Passo do Código

Inicialização:
low é inicializado com 0, representando o índice inicial do array.
high é inicializado com len(array) - 1, que é o índice do último elemento do array.
Loop While:
O loop continua enquanto low for menor ou igual a high. Isso significa que ainda há elementos a serem verificados.
Cálculo do Meio:
mid é calculado como a média de low e high, usando divisão inteira (//). Isso determina o índice do elemento do meio.
Verificação do Elemento do Meio:
guess é o valor no índice mid do array.
Se guess for igual a item, o índice mid é retornado, pois o item foi encontrado.
Se guess for maior que item, significa que o item procurado está na metade inferior do array. Portanto, high é ajustado para mid - 1 para restringir a próxima busca à metade inferior.
Se guess for menor que item, o item está na metade superior do array. Assim, low é ajustado para mid + 1 para restringir a próxima busca à metade superior.
Conclusão:
Se o loop terminar sem retornar um índice, significa que o item não está no array. Portanto, a função retorna None.

Exemplo de Execução

Quando você executa print(binary_search(my_array, 3)) com my_array sendo [1, 3, 5, 7, 9]:

Na primeira iteração, mid é 2 (índice do valor 5). Como 5 é maior que 3, ajusta-se high para 1.
Na segunda iteração, mid é recalculado para 0 (índice do valor 1). Como 1 é menor que 3, ajusta-se low para 1.
Na terceira iteração, mid é novamente recalculado para 1 (índice do valor 3). Como 3 é igual a 3, a função retorna 1, que é o índice de 3 no array.

Esse método é muito eficiente para listas grandes, pois reduz o número de comparações necessárias de forma significativa em comparação com uma busca linear


"""
