import pygame
import requests

def main():
	cep_input = input('Digite o CEP para a consulta: ')
	if len(cep_input) !=8:
		print('CEP NÃO ENCONTRADO')
		exit()

	request = requests.get('https://viacep.com.br/ws/{}/json/'.format(cep_input))

	andress_data = request.json()

	if 'erro' not in andress_data:
		print('CEP ENCONTRADO')

		print('CEP: {}'.format(andress_data['cep']))
		print('Estado: {}'.format(andress_data['uf']))
		print('Cidade: {}'.format(andress_data['localidade']))
		print('Bairro: {}'.format(andress_data['bairro']))
		print('Logradouro: {}'.format(andress_data['logradouro']))
		print('Complemento: {}'.format(andress_data['complemento']))

	else:
			print('{}: CEP inválido.'.format(cep_input))

if __name__ =='__main__':
	main()