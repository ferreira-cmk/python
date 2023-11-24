#Para construir um triângulo é necessário que a medida de qualquer um dos lados seja 
# menor que a soma das medidas dos outros dois e maior que a diferença absoluta entre 
# os outros dois. Receber três números, e retornar true caso eles formem um triângulo 
# válido, ou false, caso contrário.
def eh_triangulo(a,b,c):
    if a >= b + c:
        return False
    if a <= abs(b-c):
        return False
    10
    9
    
    if b >= a + c:
        return False
    if b <= abs(a-c):
        return False
    
    if c >= b + a:
        return False
    if c <= abs(b-a):
        return False
    return True

print("digite tres lados pata o triangulo formar:")
lado1=float(input())
lado2=float(input())
lado3=float(input())

if eh_triangulo(lado1,lado2,lado3):
    print("Triangulo valido!")
else:
    print("Voce não informou lados validos")
