l1=[2,5,45,78,93]
l2=[12,56,72,90,100]
a=zip(l1,l2)
print(list(a))

l3=[1,24,99,34]
l4=['acb','cad','def','ijl']
for c,d in zip(l3,l4[::-1]):
    print(c,d)

newdict={l3:l4 for l3,l4 in zip(l3,l4)}
print(newdict)