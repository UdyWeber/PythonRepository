# from typing import List

# new_list = [1, 2, 3]

# def return_list_of_values(lista: List[int, []]) -> int:
#     return lista[0, -1]

# print(return_list_of_values(new_list))

# from typing import List
# def func(a: int = 1, lista: List[int, [int, [str]]] = [1, [2, 3, ['a', 'b']]]):
#   return lista[a]

# print(func)

# from typing import List

# def func(lista: List[int]) -> int:
#     return lista[-1]

# print(func([1, 2, 3]))

from typing import List, Optional
def soma(a: int, b: Optional[float] = None) -> int: 
  if not b:
    return a
  return a + b

print(soma(1))