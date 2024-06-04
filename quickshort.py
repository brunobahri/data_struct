def quicksort(arr, low, high):
    if low < high:
        # Obtém o índice do pivô usando a mediana de três
        pi = partition_with_median_of_three(arr, low, high)

        # Chamadas recursivas para ordenar os elementos antes e depois da partição
        quicksort(arr, low, pi - 1)
        quicksort(arr, pi + 1, high)

def partition_with_median_of_three(arr, low, high):
    mid = (low + high) // 2
    # Encontra a mediana entre o primeiro, o meio e o último elemento
    pivot_index = median_of_three(arr, low, mid, high)
    # Troca a mediana para o final para usar como pivô
    arr[pivot_index], arr[high] = arr[high], arr[pivot_index]

    pivot = arr[high]
    i = low - 1

    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def median_of_three(arr, low, mid, high):
    # Compara os elementos nas posições low, mid e high para encontrar a mediana
    if (arr[low] > arr[mid]) != (arr[low] > arr[high]):
        return low
    elif (arr[mid] > arr[low]) != (arr[mid] > arr[high]):
        return mid
    else:
        return high

# Exemplo de uso:
array = [10, 7, 8, 9, 1, 5]
quicksort(array, 0, len(array) - 1)
print(array)

