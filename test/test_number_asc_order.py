import pytest
from src.custom_stack_class import CustomStack, StackEmptyException
from src.number_asc_order import NumberAscOrder

# Testa se a ordenação funciona corretamente com 6 números aleatórios
def test_sort_with_six_numbers():
    stack = CustomStack(6)
    numbers = [23, 4, 55, 12, 38, 7]
    
    # Empilha os números (na ordem do sorteio)
    for num in numbers:
        stack.push(num)

    sorter = NumberAscOrder()
    sorted_result = sorter.sort(stack)

    assert sorted_result == sorted(numbers)  # Compara com a lista ordenada
    assert stack.is_empty()  # deve estar vazia após ordenar

# Testa se uma exceção é lançada ao tentar ordenar uma pilha vazia
def test_sort_with_empty_stack_raises_exception():
    stack = CustomStack(6)

    sorter = NumberAscOrder()

    with pytest.raises(StackEmptyException):
        sorter.sort(stack)
