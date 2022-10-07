conj1={1,2,3,4,5,6,7}
conj2={5,6,7,8,9,10}

print(f"Conjunto 1:{conj1}")
print(f"Conjunto 2:{conj2}")

#Intersection: &
intersecao=conj1.intersection(conj2)
print(f"Intersecção: {intersecao}")

#Union: |
uniao=conj1.union(conj2)
print(f"União: {uniao}")

#Difference: -
diferenca=conj2.difference(conj1)
print(f"Diferença conjunto 2 em relação ao 1: {diferenca}")

#isdisjoint checa se os conjuntos são disjuntos (Não têm união), issubset checa se um conjunto é subconjunto do outro
