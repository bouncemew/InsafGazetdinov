def get_name(func):
  def print_name():
      name = func()
      print("Привет, ", name)
  return print_name
@get_name
def n_name():
    name = input('Введите имя: ')
    return name
n_name()


