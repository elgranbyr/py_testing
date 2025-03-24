# TDD
Libro "The Clean Coder" (2011)
[BlogThe Three Rules of TDD](http://butunclebob.com/ArticleS.UncleBob.TheThreeRulesOfTdd)

1. test que falle (rojo) -> Normalmente se falla porque no existe el componente a testear
2. test que pase (verde) -> Se escribe el código necesario para que el test pase
3. refactorizar (azul) -> Se refactoriza el código para que sea más limpio y eficiente

## Problema:
Se desea crear un componente que reciba como entrada un codigo de cliente y un arreglo de productos y su preciod y devuelva como salida la creaciòn de un pedido.

El Payload de entrada es el siguiente:
```
{
    "codigo_cliente": "1234567890",
    "productos": [{"codigo": "1234567890", "precio": 1000}]
}
```


El valor de retorno del componente es un diccionario con los siguientes campos:
- codigo_pedido
- fecha_pedido
- cliente
- total
