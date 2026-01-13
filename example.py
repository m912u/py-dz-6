# Безымянная функция, меняющая местами
# параметры, если второе больше первого
check_and_swap = lambda a,b: [a,b] if a<b else [b,a]

def sum_distance(a=int,b=int):
  """
  Функция складывает последовательноть чисел от a до b,
  незавсимо от порядка ввода
  """
  int_first,int_second=check_and_swap(a,b)
  return sum(range(int_first,int_second+1))

x=int(input("Введите число 1: "))
y=int(input("Введите число 2: "))
print("Сумма последовательности: ",sum_distance(x,y))
