# aula09_bootcamp

## Decoradores

### Usando Log
Para debugar o código, a maioria usam *print* ou *debugar*. 
Aprenderemos a usar o log.
O Log consiste em monitorar o seu pipeline com os respectivos detalhes da execução, independentemente de estar na frente do computador ou não, pois não será algo semi-automático e sim autonomo.

Uma lib importante para esse tipo de finalidade é o loguro (https://github.com/Delgan/loguru)

Outra lib para log pode ser o sentry (https://sentry.io/)

### Decorador
Decorador nada mais é que empacotar função dentro de outra função.
```
def decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        ...
        try:
            result = func(*args, **kwargs)
            ...
            return result
        except Exception as e:
            ...
            raise # Re-lança a exceção para não alterar o comportamento da função
    return wrapper
```
E para adicionar no seu codigo basta iniciar a chamada do decorador iniciando com ```@```
