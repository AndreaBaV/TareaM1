import argparse, datetime, sys, piso, display
import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

def main():
	parser = argparse.ArgumentParser("Simulacion", description="Andrea Bahena")
	subparsers = parser.add_subparsers(dest='command')  
	
	subparser = subparsers.add_parser("M1", description="Primera Entrega")
	subparser.add_argument("--M", required=True, type=int, help="Cantidad de columnas")
	subparser.add_argument("--N", required=True, type=int, help="Cantidad de filas")
	subparser.add_argument("--Agentes", required=True, type=int, help="Cantidad de montacargas")
	subparser.add_argument("--Basuras", required=True, type=int, help="Cantidad de basuras")
	subparser.add_argument("--Tiempo", required=True, type=int, help="Tiempo maximo de ejecucion")
	subparser.add_argument("--CeldaInicial", required=True, type=int, help="Ubicacion del incinerador")
	subparser.add_argument("--TipoBusqueda", required=True, type=int, help="Tipo de busqueda - 1: aleatoria, 2: sistematica")
	subparser.add_argument("--CantidadNodos", required=True, type=int, help="Cantidad de nodos")
	
	Options = parser.parse_args()
	
	if Options.command == "M1":  # Verificar el subcomando
		max_cells = Options.M * Options.N
		display.main(Options)

		if Options.Agentes > max_cells or Options.Basuras > max_cells or Options.CeldaInicial > max_cells:
			print("Error: Los agentes, la basura o la celda inicial no puede ser mayor que el número de celdas")
			sys.exit(1)

	elif Options.command == "Nodos":
		print(f"Generando {Options.CantidadNodos} nodos para la simulación")

if __name__ == "__main__":
	print("\n" + "\033[0;32m" + "[start] " + str(datetime.datetime.now()) + "\033[0m" + "\n")
	main()
	print("\n" + "\033[0;32m" + "[end] " + str(datetime.datetime.now()) + "\033[0m" + "\n")
