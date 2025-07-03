Ist  = ['Apple', 'Guava', 'Mango','Banana', 'Kiwi']

print("Length of list:",len(Ist))
print("First Element:",Ist[0])
print("Last Element:",Ist[-1])

Ist.append('Papaya')
print("Updated List:",Ist)

Ist.remove('Guava')
print("Updated List:", Ist)

Ist.sort()
print("Sorted List:", Ist)

Ist.pop(1)
print("Updated List:",Ist)

Ist.reverse()
print("Reversed List:",Ist)

print("Multiplication on List:", Ist*2)

Ist = Ist[:4]
print("Sliced List:",Ist)

Ist.clear()
print("Updated List:", Ist)
