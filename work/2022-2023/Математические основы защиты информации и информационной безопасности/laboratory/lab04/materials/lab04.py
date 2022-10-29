from prettytable import PrettyTable
import inspect

class GCD:
  def euclid(self, a: int, b: int) -> int:
    r0 = a
    r1 = b
    while r1!=0:
      r0 = r0%r1
      r0, r1 = r1, r0
    return r0

  def binary_euclid(self, a: int, b: int) -> int:
    even = lambda x: not x%2
    g = 1
    while even(a) and even(b):
      a //= 2
      b //= 2
      g *= 2
    u = a
    v = b
    while u!=0:
      while even(u):
        u //= 2
      while even(v):
        v //= 2     
      if u>=v:
        u -= v
      else:
        v -= u 
    return g*v

  def extend_euclid(self, a: int, b: int) -> int:
    r0 = a
    r1 = b
    x0 = 1
    x1 = 0
    y0 = 0
    y1 = 1
    i = 1

    while r1!=0:
      q = r0//r1
      r0 = r0%r1
      r0, r1 = r1, r0

      x0 -= q*x1
      x0, x1 = x1, x0 

      y0 -= q*y1
      y0, y1 = y1, y0

    return f'{a}*({x0}) + {b}*({y0}) = {r0}' 

  def extend_binary_euclid(self, a: int, b: int) -> int:
    even = lambda x: not x%2
    g = 1
    a_copy = a
    b_copy = b
    while even(a) and even(b):
      a //= 2
      b //= 2
      g *= 2
    u = a
    v = b
    A = 1
    B = 0
    C = 0
    D = 1
    while u!=0:
      while even(u):
        u //= 2
        if even(A) and even(B):
          A //= 2
          B //= 2
        else:
          A = (A+b) // 2
          B = (B-a) // 2

      while even(v):
        v //= 2  
        if even(C) and even(D):
          C //= 2
          D //= 2
        else:
          C = (C+b) // 2
          D = (D-a) // 2
      if u>=v:
        u-=v
        A-=C
        B-=D
      else:
        v-=u
        C-=A
        D-=B
    return f'{a_copy}*({C}) + {b_copy}*({D}) = {g*v}'       

def main():
  gcd = GCD()
  method_list = inspect.getmembers(gcd, predicate=inspect.ismethod)
  examples = [(12345, 24690), (12345, 54321), (12345, 12541), (140,96)]
  pt = PrettyTable()
  pt.field_names = ["method"] + [f"GCD({a},{b})" for a, b in examples]
  pt.add_rows([[name] + [method(a,b) for a,b in examples] for name, method in method_list])
  print(pt)

main()