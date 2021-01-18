import socket
import threading
import os

porta = os.getenv('PORT')

ServerSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

ServerSocket.bind(('0.0.0.0', porta))

ServerSocket.listen(50)

ClientsSocketsList = []
EnderecoList = []

Encode_mode = 'utf-8'

def transmitir(mensagem):

	

	for EveryClient in ClientsSocketsList:
	
		EveryClient.send(mensagem.encode(Encode_mode))
			
			



def receber_transmitir(ClientSocketParam):

	while True:

		try:
			msg = ClientSocketParam.recv(1024).decode(Encode_mode)
			transmitir(msg)

		except:

			index_do_end_correspondente_ao_socket_problematico = ClientsSocketsList.index(ClientSocketParam)

			ClientSocketParam.close()

			print(f'{EnderecoList[index_do_end_correspondente_ao_socket_problematico]} se desconectou do SERVER')
	 
			ClientsSocketsList.remove(ClientSocketParam)

			EnderecoList.pop(index_do_end_correspondente_ao_socket_problematico)





'''thread_de_transmissao = threading.Thread(target = transmitir, daemon = True)
thread_de_transmissao.start()'''



while True:
	
	
	ClientSocket, Endereco = ServerSocket.accept()
	
	EnderecoList.append(Endereco)
	ClientsSocketsList.append(ClientSocket)
	ClientSocket.send('Voce se conectou com sucesso ao servidor!'.encode(Encode_mode))
	print(f'{Endereco} se conectou ao SERVER')
	threadclient = threading.Thread(target = receber_transmitir, args = (ClientSocket,), daemon = True )
	threadclient.start()









	
	
	

	
