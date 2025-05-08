import pytest
from src.custom_stack_class import *

# Testa se um único elemento pode ser empilhado corretamente
def test_push_one_elementinstack():
    element_value = 5.0  # Valor 

    cut = CustomStack(5)  # Cria uma pilha com limite 5 
    cut.push(element_value)  

    assert cut.is_empty() == False 
    assert element_value == cut.top()  
    assert 1 == cut.size()  

# Testa se pop() retorna o último elemento inserido
def test_pop_returns_last_element():
    stack = CustomStack(3)  # Cria uma pilha com capacidade 3
    stack.push(10)  # Empilha 10
    stack.push(20)  # Empilha 20

    popped = stack.pop()  # Remove o topo da pilha 
    assert popped == 20  # Verifica se o elemento removido é 20
    assert stack.size() == 1 

# Testa se top() retorna o último elemento sem removê-lo
def test_top_returns_last_element_without_removing():
    stack = CustomStack(3)
    stack.push(10)

    top = stack.top()  # Consulta o topo sem remover
    assert top == 10  # O topo deve ser o último elemento inserido
    assert stack.size() == 1  # O tamanho da pilha deve permanecer o mesmo

# Testa se pop() em uma pilha vazia lança a exceção StackEmptyException
def test_pop_empty_stack_raises_exception():
    stack = CustomStack(2)

    with pytest.raises(StackEmptyException):  
        stack.pop()

# Testa se top() em uma pilha vazia lança a exceção StackEmptyException
def test_top_empty_stack_raises_exception():
    stack = CustomStack(2)

    with pytest.raises(StackEmptyException): 
        stack.top()

# Testa se push() em uma pilha cheia lança a exceção StackFullException
def test_push_full_stack_raises_exception():
    stack = CustomStack(2)
    stack.push(1)
    stack.push(2)

    with pytest.raises(StackFullException): 
        stack.push(3)

# Testa se uma nova pilha está vazia
def test_is_empty_on_new_stack():
    stack = CustomStack(2)
    assert stack.is_empty()  # Uma pilha nova deve estar vazia

# Testa se o tamanho inicial de uma nova pilha é zero
def test_size_on_new_stack_is_zero():
    stack = CustomStack(2)
    assert stack.size() == 0  # O tamanho inicial deve ser zero
