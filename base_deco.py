var_a = "var_a"

print('--- L3: Define decorator()')
def decorator(var_h):
   var_c = "var_c"
   print('--- L6: In decorator() -> VAR_X = {}'.format(VAR_X))

   def _decorator(f):
       var_d = "var_d"
       print('--- L10: In _decorator() -> VAR_X = {}'.format(VAR_X))

       def wrapper(var_g):
           print("--- L13: Before decorate")
           print('--- L14: In wrapper() -> VAR_X = {}'.format(VAR_X))
           var_e = "var_e"
           f(var_g)
           print("--- L17: After decorate")
       return wrapper
   return _decorator


print('--- L22: Define outer()')
def outer(var_f):
   print("--- L24: Into outer()")
   var_b = "var_b"
   print('--- L26: In outer() -> VAR_X = {}'.format(VAR_X))

   @decorator("var_h")
   def inner(var_g):
       # innerからどの変数を参照・変更できるかを調べます
       print("--- L31: Into inner()")
       print('[Ref] L32: inner() -> VAR_X = {}'.format(VAR_X))
       VAR_X = "CHANGED"
       print('[Chg] L34: inner() -> VAR_X = {}'.format(VAR_X))

   print('--- L36: Execute inner()')
   inner("var_g")
   print('--- L38: In outer()  -> VAR_X = {}'.format(VAR_X))


print('--- L41: Execute outer()')
outer("var_f")
print('--- Finish')
