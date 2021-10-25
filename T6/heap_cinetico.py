from heapq import heappop, heappush, heapify

####References
#https://stackoverflow.com/questions/10162679/python-delete-element-from-heap
####


#  Tentei implementar usando bibliotecas prontas de python para me acostumar com
#a linugagem, nao sei se era correto. Mas me pareceu bastante complicado tambem
#  Imaginei que por nao se tratar de ED1 ou ED2, nao precisaria reimplementar
#max-heap. Contudo, o desafio se provou muito mais complicado, jah que nao consegui
#usar funcionalidades que ficariam disponiveis em implementacao propria.


class Element:	
	# i -> posicao i e i + 1 do vetor
	# t -> instante em que o certificado vence
	def __init__ (self, id, x0, speed, xnow):
		self.id = id
		self.x0 = x0
		self.speed = speed
		self.xnow = xnow

	def __lt__(self, other):
		return self.xnow < other.xnow

	def Change (self, v, now):
		self.x0    = self.x0 - v * now
		self.speed = v

	def Update (self, xnow):
		self.xnow = xnow


class Certificate:

	# i -> posicao i e i + 1 do vetor
	# t -> instante em que o certificado vence
	def __init__ (self, i, t):
		self.i = i
		self.t = t

	def __lt__(self, other):
		return self.t < other.t

class KinHeap:
	#   KinHeap(id, x0, speed, n): cria um maxheap cinético com n elementos,
	# com identificador, valor inicial e velocidade nos vetores id, x0 e speed. 

	# H -> maxheap com os elementos (usa o valor corrente como chave)
	#(no caso, vou multiplicar tudo por -1 para aproveitar heapq)

	# Q -> minheap com os certificados 

	# id -> dicionario com 'id' como key e o indice do vetor como value

	# now -> momento atual
	def __init__ (self, id, x0, speed, n):		
		self.id = dict (zip (id, list(range (n))))

		self.H = []

		for i in range (n):
			heappush (H, Element (id[i], x0[i], speed[i], x0[i]))

		self.Q = []

		for i in range (n - 1):
			# calcula o tempo em que o certificado expira
			t = (x0[i] - x0[i + 1]) / (speed[i + 1] - speed[i])
			heappush (Q, Certificate (i, t))

		self.now = 0


	# Calcula o irmao do elemento na heap
	def Sibling (self, i):
		if i % 2:
			return i + 1
		return i - 1

	def Update (self, i):
		pass

	#Advance(t): avança o tempo para o instante t
	def Advance (self, t):
		while self.Q[0] <= t:
			self.now = self.Q[0]
			Event (heappop (self.Q))

		now = t

	def Event (self, i, t):
		#H.swap (i, i // 2)

		if i > 1:
			Update (i / 2)

		Update (i)

		if 2 * i <= self.n:
			Update (2 * i)

		if 2 * i + 1 <= self.n:
			Update (2 * i + 1)

		s = Sibling (i)

		if s > 0:
			Update (s)

	# Change(id, v): altera a velocidade do elemento id para v
	def Change (self, id, v):
		idx = self.id [id]
		
		H[idx].Change(v, self.now)

		if i > 1:
			Update (i)

		if 2 * i < self.n:
			Update (2 * i)

		if 2 * i + 1 < self.n:
			Update (2 * i + 1)


	#Insert(id, xnow, v): insere o elemento id na posição xnow com velocidade v
	def Insert (self, id, xnow, v):
		self.n += 1

		# calcula o x0 'original'
		x0 = xnow - v * self.now

		heappush (self.H, Element (id, x0, v, xnow))

		#self.id.update (zip ())


	#Max(): identificador do elemento com o maior valor no instante atual
	def Max ():
		# H[0] -> maximum element of Heapmax H
		return self.H[0].id

	#DeleteMax(): remove o elemento com o maior valor
	def DeleteMax ():
		max_idx = Max ()

		H[max_idx] = H[-1]

		H.pop()

		heapify (H)

	#Delete(id): remove o elemento id
	def Delete(id):
		idx = self.id[id]

	#Print(): imprime o heap no instante atual
	def Print ():
		pass