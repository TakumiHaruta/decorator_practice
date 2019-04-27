print('--- L1: Define decorator()')
def decorator(var_i):
   print('--- L3: In decorator() -> var_i = {}'.format(var_i))
   var_i = "decorator"
   print('--- L5: In decorator() -> var_i = {}'.format(var_i))

   def _decorator(f):
       nonlocal var_i
       print('--- L9: In _decorator() -> var_i = {}'.format(var_i))
       var_i = "_decorator"
       print('--- L11: In _decorator() -> var_i = {}'.format(var_i))

       def wrapper(var_i):
           print("--- L14: Before decorate")
           print('--- L15: In wrapper() -> var_i = {}'.format(var_i))
           var_i = "wrapper"
           f(var_i)
           print("--- L18: After decorate")
       return wrapper
   return _decorator


print('--- L23: Define outer()')
def outer():
   print("--- L25: Into outer()")
   var_i = "var_i"
   print('--- L27: In outer() -> var_i = {}'.format(var_i))

   @decorator(var_i)
   def inner(var_i):
       # innerからどの変数を参照・変更できるかを調べます
       print("--- L32: Into inner()")
       print('[Ref] L33: inner() -> var_i = {}'.format(var_i))
       var_i = "CHANGED"
       print('[Chg] L35: inner() -> var_i = {}'.format(var_i))

   print('--- L37: Execute inner()')
   inner(var_i)
   print('--- L39: In outer()  -> var_i = {}'.format(var_i))


print('--- L42: Execute outer()')
outer()
print('--- Finish')
