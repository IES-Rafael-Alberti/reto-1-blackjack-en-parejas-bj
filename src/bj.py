"""
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
"""
import random, time

def eleccionModoJuego() -> int:

    opc = None
    
    while opc is None:
        try:
            opc = int(input("Elija modo de juego: \n1. Dos jugadores. \n2. Un jugador contra la maquina\n"))
            if opc != 1 and opc != 2:
                opc = None
                print("\nERROR - Debe elejir un modo de juego valido.")
            else:
                return int(opc)
        except:
            print("\nERROR - Debe elejir un modo de juego valido.")



def pedirNombreJugadores(modoJuego):

    jug1 = ''
    jug2 = 'Maquina'

    if modoJuego == 1:
        jug1 = input("introduce nombre jugador 1: \n")
        jug2 = input("introduce nombre jugador 2: \n")
    else:
        jug1 = input("introduce nombre jugador 1: \n")

    return jug1,jug2



def solicitarCarta():

    baraja = "A234567890JQK"

    carta = random.choice(baraja)

    return carta



def valorCarta(carta, total):

    valor = 0

    if carta == "J" or carta == "Q" or carta == "K":
        valor = 10

    elif carta == "A":
        if total >= 12:
            valor = 1
        else:
            valor = 10

    else:
        if int(carta) >= 2 and int(carta) <= 9:
            valor = int(carta)
        else:
            valor = 10
    
    return valor



def main():
    
    fin = False
    continuaj1 = True
    continuaj2 = True

     # Elejir modo 1 o 2 jugadores
    eleccionModo = eleccionModoJuego()

    # Pide nombre de 1 o de los 2 jugadores (en caso de pedir 1, el jug2 sera "Maquina")
    j1,j2 = pedirNombreJugadores(eleccionModo)

    puntosj1 = 0
    puntosj2 = 0

    cartasj1 = ""
    cartasj2 = ""
    ronda = 1

    while not fin: 
      

        print("Repartiendo cartas...")
        #time.sleep(2)

        if continuaj1:
            carta = solicitarCarta()
            cartasj1 += carta
            numeroj1 = valorCarta(carta,puntosj1)
            puntosj1 += int(numeroj1)
            
        if continuaj2:
            carta = solicitarCarta()
            cartasj2 += carta
            numeroj2 = valorCarta(carta,puntosj2)
            puntosj2 += int(numeroj2)

        
        if puntosj1 > 21:
            msj1 = "**se pasa**"
            continuaj1 = False
        else:
            msj1 = puntosj1


        if puntosj2 > 21:
            msj2 = "**se pasa**"
            continuaj2 = False
        else:
            msj2 = puntosj2
        
        
        print(f"RONDA {ronda} \nJ1 - {j1} - {cartasj1} ({msj1}) \nJ2 - {j2} - {cartasj2} ({msj2})")
        ronda += 1
        

        if continuaj1:   
            finj1 = input(("J1, ¿te plantas? (si/no): "))
            if finj1 == "si":
                continuaj1 = False
            
        
        if continuaj2:   
            finj2 = input(("J2, ¿te plantas? (si/no): "))
            if finj2 == "si":
                continuaj2 = False


        if continuaj1 == False and continuaj2 == False:
            fin = True
        


    #print(valorCarta(cartaSolicitada,11))

if __name__ == "__main__":
    main()