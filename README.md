Juego de Tres en Raya
Este es un juego de Tres en Raya implementado en Python. Puedes jugar contra la máquina que utiliza el algoritmo Minimax con poda alfa-beta para tomar decisiones.

## Reglas del juego:
El juego se juega en un tablero de 3x3.
Elige 'X' o 'O' para comenzar. 'X' siempre comienza.
Gana el jugador que forme una línea horizontal, vertical o diagonal de su símbolo ('X' u 'O') en el tablero.
Si todas las casillas se llenan y no hay un ganador, se declara un empate.

## Cómo jugar:
Ejecuta el programa y sigue las instrucciones para elegir 'X' o 'O'.

```bash
python TresEnRaya.py
```
Ingresa las coordenadas de tu movimiento en formato fila, columna (por ejemplo, "1,2").

Observa el tablero y disfruta del juego.
Si ganas o se produce un empate, se te preguntará si quieres jugar de nuevo.

Explicacion del algoritmo minimax con poda alfa-beta usado en el codigo:

La función minimax es como el cerebro de la computadora. Ayuda a la computadora a pensar en las mejores jugadas posibles. Ahora, vamos a usar la explicación del algoritmo para entender cómo funciona dentro de esta función.

is_maximizing es como un interruptor que dice si la computadora está tratando de maximizar sus posibilidades de ganar (cuando es su turno) o minimizar tus posibilidades de ganar (cuando es tu turno).

Cuando is_maximizing es True, significa que es el turno de la computadora, y está tratando de maximizar su puntuación. Cuando is_maximizing es False, significa que es tu turno, y la computadora está tratando de minimizar tu puntuación.

alpha y beta son dos números que ayudan a la computadora a entender si ya ha encontrado una jugada mejor que las que ha explorado. Si alpha es muy alto, significa que ha encontrado una jugada muy buena para la computadora. Si beta es muy bajo, significa que ha encontrado una jugada muy mala para la computadora.

Ahora, aquí viene el corazón del algoritmo. La computadora explora todas las posibles jugadas que puede hacer. Para cada jugada, asume que tú y ella juegan de la mejor manera posible. Luego, mira el resultado de esa jugada.

Si is_maximizing es True (el turno de la computadora), la computadora quiere maximizar su puntuación. Así que busca la jugada que le da la puntuación más alta (max_eval), y también actualiza alpha para asegurarse de que sea lo suficientemente alto para saber que ha encontrado una jugada buena. Si beta es menor o igual a alpha, significa que ya encontró una jugada mejor, por lo que detiene la exploración y regresa max_eval.

Si is_maximizing es False (tu turno), la computadora quiere minimizar tu puntuación. Así que busca la jugada que le da la puntuación más baja (min_eval), y también actualiza beta para asegurarse de que sea lo suficientemente bajo para saber que ha encontrado una jugada mala. Si beta es menor o igual a alpha, significa que ya encontró una jugada peor, por lo que detiene la exploración y regresa min_eval.

La función minimax continúa explorando todas las jugadas posibles, y al final, devuelve la puntuación más alta si es el turno de la computadora (cuando is_maximizing es True) o la puntuación más baja si es tu turno (cuando is_maximizing es False).

## Contactos:
Si te gusta mi trabajo o estás buscando consultoría para tus proyectos, Pentesting, servicios de RED TEAM - BLUE TEAM, implementación de normas de seguridad e ISOs, controles IDS - IPS, gestión de SIEM, implementación de topologías de red seguras, entrenamiento e implementación de modelos de IA, desarrollo de sistemas, Apps Móviles, Diseño Gráfico, Marketing Digital y todo lo relacionado con la tecnología, no dudes en contactarme al +591 75764248 y con gusto trabajare contigo.

