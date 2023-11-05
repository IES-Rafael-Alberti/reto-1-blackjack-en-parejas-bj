# DAM1_DAW1_Reto1_23_24
Juguemos al BlackJack

## Reto 1 (DAM1 y DAW1)

### Descripción:
```
* PROGRAMACIÓN:

Crear un programa en Python con funciones para jugar al Blackjack.

Al entrar debe preguntar el modo de juego:

    1. Dos jugadores.
    2. Un jugador contra la máquina.

* BASE DE DATOS:

Crear también un modelo lógico de datos, diseñando el Modelo Entidad/Relación con ERDplus, para una futura actualización del programa Blackjack con las siguientes características:

    1. El sistema diseñado debe almacenar los datos de los jugadores, correo, contraseña, apodo, nombre, apellidos y fecha de nacimiento.
    2. Hay dos tipos de jugadores, pueden ser profesionales o aficionados, de los profesionales guardaremos, además de la información anterior, su ficha de federado y su puesto en el ranking al principio del año. 
    3. Así mismo, la base de datos tendrá la información de las partidas, con el modo de juego (2 jugadores o jugador/máquina), fecha y hora de comienzo y fin de la partida, y el resultado final, guardando el ganador y el perdedor, o el empate.
    4. Igualmente se deben guardar los datos de las rondas o turnos que se juegan en cada partida: pide carta o se planta, cartas del jugador en cada turno y los puntos.
    5. También se quiere guardar datos del equipo o club que representa el jugador, si es que juega representando algún club, los datos que se quieren guardar del club son el nombre, fecha de creación, dirección de la sede, nombre del presidente y número telefono del presidente.
```

### Premisas generales:
```
1. El código debe estar escrito en Python.
2. Se considerará entregado el reto cuando se realice la entrega de la tarea en Moodle con el enlace de GitHub a vuestro repositorio.
3. NO SE PUEDE ENTREGAR hasta pasadas 48h de la presentación del reto. Aunque podéis realizar commit y push en el repositorio desde el inicio sin problemas.
4. Se considerará entregado el reto cuando se realice la entrega de la tarea en Moodle con el enlace de GitHub a vuestro repositorio.
5. No se pueden usar listas, tuplas o diccionarios. Evitar sentencias while True, break, continue y pass.
6. Código legible y buenas prácticas de programación, incluyendo el principio de responsabilidad única, nombres de métodos y variables correctas y descriptivas con nomenclatura camelCase o palabras separadas por "_".
7. Entregar el programa junto con pruebas unitarias de las funciones utilizadas.
8. Para corregirlo, el programa debe pasar los test que se hayan diseñado.
9. No es necesario realizar pruebas a funciones que contengan un input().
10. Se deben realizar todas las comprobaciones necesarias para que el programa no genere errores/excepciones.
11. El programa debe estar documentado/comentado con docstrings y comentarios internos (ver https://revilofe.github.io/section1/u02/teoria/PROG-U2.5.-Documentar/)
12. El trabajo se llevará a cabo en parejas, utilizando control de versiones (Git) y plataformas de colaboración como GitHub para coordinarse. Todas las aportaciones deben ser entre los dos miembros del equipo.
13. El último commit marcará el tiempo de entrega. Se corregirán los tres primeros que se hayan entregado dentro de la siguiente hora al último commit de la primera entrega.
14. Se tendrá un tiempo máximo de 2 semanas desde la fecha de apertura del reto para terminarlo.
15. Si se detecta copia entre retos o de cualquier otra fuente, la entrega quedará eliminada.
16. La aceptación de la solución al reto como solución válida, supondrá un beneficio en la nota final del módulo.
```

### Objetivo del juego:
	Conseguir 21 puntos o plantarse con más puntos que el otro jugador.

### Funcionamiento:
	1. Gana el jugador que tenga la puntuación más alta sin pasarse de 21 puntos.
	2. La baraja de cartas es la cadena de caracteres "A234567890JKQ". Las cartas tienen los siguientes puntos:
 
		A -> 1 o 10 (según le venga mejor al resto de cartas que tiene en su poder el jugador)
		2...9 -> el propio valor del número.
		0, J, Q, K -> 10
  
	3. Cada jugador irá solicitando cartas por turnos, después del primer turno obligatorio, un jugador puede plantarse cuando lo decida.
	4. Después de cada turno, se debe mostrar la información de la ronda o turno, las cartas y puntos de cada jugador:
 
		RONDA 3
		J1 - jugador1 - A3K (14)
		J2 - jugador2 - A44 (18)
  
	5. Cuando un jugador se pasa de 21, automáticamente pierde y gana el otro jugador.
	6. Las cartas de los jugadores y puntuaciones se revelan a la vez después de pasar el turno ambos jugadores, es decir, cada jugador decide pedir una carta más o plantarse y a continuación se muestra la información de cada jugador.
 
 		RONDA 3
		J1 - jugador1 - 63K (19)
		J2 - jugador2 - J4Q **se pasa**
  
	7. El programa debe solicitar el modo de juego y a continuación el nombre o apodo del o los jugadores.
	8. Cada jugador pide una carta por turno o se planta. Como mínimo un jugador debe solicitar una carta, es decir, la primera vez no se le da la opción a plantarse. Pero el resto de turnos si.
	9. El juego acaba cuando ambos jugadores se plantan. Mientras que un jugador no se pase de 21 puntos y no se plante se debe preguntar si quiere una carta más.
	10. Cuando finaliza el juego se debe mostrar lo siguiente (4 posibilidades):

		JUEGO TERMINADO - Ronda 3
		Game over ¡Los dos os habéis pasado!
		J1 - jugador1 - 4K9 (23)
		J2 - jugador2 - J70 (27)

		JUEGO TERMINADO - Ronda 3
		¡Empate!
		J1 - jugador1 - 4K5 (19)
		J2 - jugador2 - A9 (19)
    
		JUEGO TERMINADO - Ronda 3
		¡Gana J1 - jugador1!
		J1 - jugador1 - JQA (21)
		J2 - jugador2 - 491J (24)

		JUEGO TERMINADO - Ronda 3
		¡Gana J2 - jugador2!
		J1 - jugador1 - 3K5 (18)
		J2 - jugador2 - 28Q (20)

