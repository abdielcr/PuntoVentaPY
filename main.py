
clients = 'Maritza,Alejandro,Abdiel,Andrea,Carolina,June,'

def createClients(clientName):
    global clients
    
#Validacion de clientes existentes
    if clientName not in clients:
        clients += clientName

        _add_comma()
    else:
        print('CLient already is in the client\'s list')


#Listar Clientes
def listClients():
    global clients
    print(clients)


#Actualizar Clientes
def updateClient(clientName, updateClientName):
    global clients
    if clientName in clients:
        clients = clients.replace(clientName + ',',updateClientName+',')
    else:
        print('CLient is not in clients List')


#Eliminar Clientes
def deleteClient(clientName):
    global clients
    if clientName in clients:
        clients = clients.replace(clientName + ',', '')
    else:
        print('Client is not in clients List')

#Buscar Clientes
def searchCliente(clientName):
   global clients 
   clientList = clients.split(',')
   for client in clientList:
       if client != clientName:
           continue
       else:
           return True


#Añadir coma a los nombres
def _add_comma():
    global clients
    clients += ','


#Imprimir comandos
def _print_welcome():
    print('*' * 85)
    print('Welcome to Abdiels Sales')
    print('*' * 85)
    print('What would you like to do today?')
    print('[C]create client')
    print('[D]delete client')
    print('[U]Update CLient')
    print('[S]Search CLient')  
    print('[L]List Clients')
def _getClientName():
    return input('What is the client Name?')


#Logica de accion
if __name__== '__main__':
   _print_welcome()
   command = input()
   command = command.upper()

   if command == 'C':
       clientName = _getClientName()
       createClients(clientName)
       listClients()
    
   elif command == 'D':
       clientName = _getClientName()
       deleteClient(clientName)
       listClients()
   elif command == 'U':
       clientName = _getClientName()
       updateClientName = input('What is the updated client name?')
       updateClient(clientName)
       listClients()
   elif command == 'S':
       clientName = _getClientName()
       found = searchCliente(clientName)
       if found:
           print('The client is in the client\'s List')
       else:
           print('The cliente: {} is not our client'.format(clientName))
   elif command == 'L':
       listClients()
   else:
       print('Invalid OPTION')

