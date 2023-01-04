class NodoArbol(object):
    def __init__(self, izq=None, der=None):
        self.izq = izq
        self.der = der

    def children(self):
        return self.izq, self.der

    def __str__(self):
        return self.izq, self.der


def huffman_arbol_code(nodo, binString=''):
    '''
    Función para encontrar el codigo huffman
    '''
    if type(nodo) is str:
        return {nodo: binString}
    
    (l, r) = nodo.children()
    d = dict()
    d.update(huffman_arbol_code(l, binString + '0'))
    d.update(huffman_arbol_code(r, binString + '1'))
    return d

def huffman_arbol_decode(msg, nodo_raiz, nodo, msgd=''):
    '''
    Función para decodificar un mensaje huffman
    '''
    
    if len(msg) == 0:
        print('Mensaje decodificado: {}'.format(msgd))
        return msgd


     #print(len(msg), msgd)
    if type(nodo) is str:
        msgd = msgd + nodo
        nodo = nodo_raiz

    (l, r) = nodo.children()
    caracter = msg[0]

    if len(msg) == 1:
        msg = ''
    else:
        msg = msg[1:]

    if caracter == '1':
        huffman_arbol_decode(msg, nodo_raiz, r, msgd=msgd)
    else:
        huffman_arbol_decode(msg, nodo_raiz, l, msgd=msgd)

def crear_arbol(nodos):
    '''
    Función que crea el arbol
    :param nodos: Nodos
    :return: Nodo raíz del árbol
    '''
    print(nodos)
    print('\n')
    while len(nodos) > 1:
        (key1, c1) = nodos[0]
        (key2, c2) = nodos[1]
        nodos = nodos[2:]
        nodo = NodoArbol(key1, key2)
        nodos.append((nodo, c1 + c2))
        nodos = sorted(nodos, key=lambda x: x[1], reverse=False)
        print(nodos)
        print('\n')
    return nodos[0]

# crear la tabla de conteo como un diccionario
tabla_conteo = {
    'A':11,
    'B':2,
    'C':4,
    'D':3,
    'E':14,
    'G':3,
    'I':6,
    'L':6,
    'M':3,
    'N':6,
    'O':7,
    'P':4,
    'Q':1,
    'R':10,
    'S':4,
    'T':3,
    'U':4,
    'V':2,
    ' ':17,
    ',':2
    }
# obtener las frecuencias apartir de la tabla de conteo
total_conteo = sum(tabla_conteo.values())
tabla_frecuencia = {k:v/total_conteo for k,v in tabla_conteo.items()}
tabla_frecuencia

# ordenar la tabla por las frecuencias de menor a mayor y orden alfabético
lista_nodos_ordenados = sorted(tabla_frecuencia.items(), key=lambda x: x[1], reverse=False)
lista_nodos_ordenados

nodo = crear_arbol(lista_nodos_ordenados)

# nodo raíz y su sumatoria de pesos
nodo

nodo[0]

nodo[0].children()

codificacion = huffman_arbol_code(nodo[0])
for i in codificacion:
    print(f'{i} : {codificacion[i]}')

# ahora decodificacion de los mensajes
msg1 = "10001011101011000010111010001110000011011000000111100111101001011000011010011100110100010111010111111101000011110011111100111101000110001100000010110101111011111110111010110110111001110110111100111111100101001010010100000101101011000101100110100011100100101100001100100011010110101011111111111011011101110010000100101011000111111100010001110110011001011010001101111101011010001101110000000111001001010100011111100001100101101011100110011110100011000110000001011010111110011100"

msg2 = '0110101011011100101000111101011100110111010110110100001000111010100101111010011111110111001010001111010111001101110101100001100010011010001110010010001100010110011001110010010000111101111010'

huffman_arbol_decode(msg=msg1, nodo_raiz=nodo[0] , nodo=nodo[0], msgd='')

huffman_arbol_decode(msg=msg2, nodo_raiz=nodo[0] , nodo=nodo[0], msgd='')

msg_prueba = '10110'

huffman_arbol_decode(msg=msg_prueba, nodo_raiz=nodo[0] , nodo=nodo[0], msgd='')


# A Huffman Tree Node
import heapq

class node:
	def __init__(self, freq, symbol, left=None, right=None):
		# frequency of symbol
		self.freq = freq

		# symbol name (character)
		self.symbol = symbol

		# node left of current node
		self.left = left

		# node right of current node
		self.right = right

		# tree direction (0/1)
		self.huff = ''
		
	def __lt__(self, nxt):
		return self.freq < nxt.freq
		

# utility function to print huffman
# codes for all symbols in the newly
# created Huffman tree
def printNodes(node, val=''):
	
	# huffman code for current node
	newVal = val + str(node.huff)

	# if node is not an edge node
	# then traverse inside it
	if(node.left):
		printNodes(node.left, newVal)
	if(node.right):
		printNodes(node.right, newVal)

		# if node is edge node then
		# display its huffman code
	if(not node.left and not node.right):
		print(f"{node.symbol} -> {newVal}")


# characters for huffman tree
chars = ['a', 'b', 'c', 'd', 'e', 'f']

# frequency of characters
freq = [ 5, 9, 12, 13, 16, 45]

# list containing unused nodes
nodes = []

# converting characters and frequencies
# into huffman tree nodes
for x in range(len(chars)):
	heapq.heappush(nodes, node(freq[x], chars[x]))

while len(nodes) > 1:
	
	# sort all the nodes in ascending order
	# based on their frequency
	left = heapq.heappop(nodes)
	right = heapq.heappop(nodes)

	# assign directional value to these nodes
	left.huff = 0
	right.huff = 1

	# combine the 2 smallest nodes to create
	# new node as their parent
	newNode = node(left.freq+right.freq, left.symbol+right.symbol, left, right)

	heapq.heappush(nodes, newNode)

# Huffman Tree is ready!
printNodes(nodes[0])