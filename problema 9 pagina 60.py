A=set(input("Sa se introduca elementele multimii A(doar litere mari din alfabetul latin): "))
B=set(input("Sa se introduca elementele multimii B(doar litere mari din alfabetul latin): "))
print("Intersectia multimilor A si B: ",A.intersection(B))
print("Reuniunea multimilor A si B: ",A.union(B))
print("Diferenta multimilor A si B: ",A.difference(B))
print("diferenta multimilor B si A: ",B.difference(A))