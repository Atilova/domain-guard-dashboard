def deco(function):
  


  def inner(*args, **kwargs):
    return function(*args, **kwargs)

  return inner


