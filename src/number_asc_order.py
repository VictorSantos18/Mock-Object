from src.custom_stack_class import CustomStack, StackEmptyException

class NumberAscOrder:

  def sort(self, stack: CustomStack) -> list:
    if stack.is_empty():
        raise StackEmptyException("A pilha está vazia.")

    result = []

    # Desempilha todos os elementos e armazena em uma lista
    while not stack.is_empty():
        result.append(stack.pop())

    # Ordena os números em ordem crescente
    result.sort()
    return result
