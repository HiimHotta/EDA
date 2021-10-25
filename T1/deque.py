

class Node:
	def __init__ (self, value, parent, depth):
		self.value = value
		self.parent = parent
		self.depth = depth
		self.jump  = None

		AddLeaf (self)

	# pai de u
	def parent (u):
		if u is None:
			return None
		return u.parent

	# Distancia ateh a raiz
	def D (u):
		if u is None:
			return 0
		return u.depth

	# k-esimo ancestral de u
	def LevelAncestor (k, u):
		y = D(u) - k

		while D(u) != y:
			if D(u.jump) >= y:
				u = u.jump

			else:
				u = parent (u)

		return u

	def AddLeaf (u):
		##caso u seja raiz
		if parent (u) is None:
		    return

		v = parent (u)

		if v.jump != r & D(v) - D(v.jump) == D(v.jump) - D(v.jump.jump):
			u.jump = v.jump.jump

		else:
			u.jump = v

	def LowestCommomAncestor (u, v):
		# garante que D(u) <= D(v)
		if D(u) > D(v):
			u, v = v, u

		#Sobe o mais profundo
		v = LevelAncestor (D(v) - D(u), v)

		if u == v:
			return u

		#Subimos simultaneamente
		while (parent (u) != parent (v)):
			if u.jump != v.jump:
				u = u.jump
				v = v.jump
			else:
				u = parent (u)
				v = parent (v)

		return parent (u)

class Deque:
	def __init__ (self):
		self.first = None
		self.last = None

	#Deque(): cria e devolve uma deque vazia
	def Deque ():
	    return Node (None, None, 0)
    	
    #Front(d): devolve o elemento no extremo front de d
	def Front (d):
		return d.first.value

	#Back(d): devolve o elemento no extremo back de d
	def Back (d):
		return d.last.value

	#PushFront(d,x): insere 'x' no extremo front de 'd' e devolve deque resultante
	def PushFront (d, x):
		deque = Deque ()
		node = Node (x, d.first, D(d.first) + 1)

		# Se for None, atualiza o first tambem
		if d.first is None:
			deque.last  = node

		deque.first = node

		return deque

	def Swap (d):
		deque = Deque ()
		deque.first = d.last
		deque.last = d.first

		return deque

	#PushBack(d,x): insere 'x' no extremo back de 'd' e devolve deque resultante
	def PushBack (d, x):
		return Swap (PushFront (Swap (d), x))

	#PopFront(d): remove o elemento no extremo front de 'd'
	def PopFront (d):
		# tratamento de erro
		if d.first is None:
		    return None

		mid = LowestCommomAncestor (d.first, d.last)

		deque = Deque ()
		deque.last = d.last

		if (mid != d.first):
			deque.first = parent (d.first)

		else:
			deque.first = LevelAncestor (d.first.depth + 1, d.last)

		return deque

	#PopBack(d): remove o elemento no extremo back de d
	def PopBack (d):
		return Swap (PopFront (Swap (d), x))

	#Kth(d,k): k-ésimo elemento de d, onde o front é o primeiro elemento de d
	def Kth (d, k):
		if d.first is None:
			return None

		# Commom 
		lca = LowestCommomAncestor (d.first, d.last)

		L1 = D (lca) - D (d.first)



		# k-esimo a partir de first
		if k - 1 <= D(L1):
			target = LevelAncestor (k - 1, d.first)

		# (k - L1)-esimo no caminho do LCA ateh o last
		else:
			L2 = D (d.last) - D (lca)
			target = LevelAncestor (L2 - (k - 1 - L1), d.last)

		return target.value


	#Print(d): imprime todos os elementos da deque d
	def Print (d):
		if d.first is None & d.last is None:
			print ("Deque vazia")

		# A partir de first

		i = parent (d.first)

		while i is not None:
			print (i.value)
			i = parent (i)

		# A partir de last

		i = parent (d.last)

		while i is not None:
			print (i.value)
			i = parent (i)

def test ():
	print ("Heloo") 
        
test()
