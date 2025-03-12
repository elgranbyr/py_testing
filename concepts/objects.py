import ducktype

pcall=ducktype.ProtoCallable()
arreglo=[1
, "2"
, {'key':'value'}
, lambda x: x*2
, True
, ducktype.Humano()
, pcall
, pcall()
]



print(f"\nArreglo: {arreglo}")

for item in arreglo:
    if callable(item):
        print(f"\n Item: {item} callable: {type(item)}")
    else:
        print(f"\n Item: {item} type: {type(item)}")