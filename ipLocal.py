import sys
import socket
import argparse

def get_parser():
	parser = argparse.ArgumentParser(description="Retorna la ip local")
	parser.add_argument('--prefijo', help='Prefijo de la ip local')
	parser.add_argument('--sufijo', help='Sufijo de la ip local')
	return parser
	
def get_ip_de_hoy():
	return socket.gethostbyname(socket.gethostname())
	
if __name__ == '__main__':
	args = get_parser().parse_args()
	
	ip_de_hoy = get_ip_de_hoy()
	
	if args.prefijo is not None:
		ip_de_hoy = args.prefijo + ip_de_hoy
	
	if args.sufijo is not None:
		ip_de_hoy = ip_de_hoy + args.sufijo
	
	print(ip_de_hoy)
