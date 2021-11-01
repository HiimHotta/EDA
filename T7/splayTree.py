#Referencia pra correção minha: 
#https://en.wikipedia.org/wiki/Splay_tree
#https://en.wikipedia.org/wiki/Splay_tree


class Node:
	def __init__ (self, parent, key):
		self.left = None
		self.right = None
		self.parent = parent
		self.key = key


class ST ():
	#ST(): cria e devolve uma splay tree vazia
	def __init__ (self):
		self.root = Node (None, None)

	# L_Rotate (x): rotaciona x para a esquerda
	def L_Rotate (x):
		y = x.right

		# Primeiro o lado direito
		if y:
			x.right = y.left

			if y.left:
				y.left.parent = x

			y.parent = x.parent

		# Caso x seja raiz
		if not x.parent:
			self.root = y;

		elif x == x.parent.left:
			x.parent.left = y

		else: 
			x.parent.right = y

		if y:
			y.left = x;

		x.parent = y

	def R_Rotate (x):
		y = x.left

		if y:
			x.left = y.right;

			if y.right:
				y.right.parent = x

			y.parent = x.parent

		if not x.parent:
			root = y

		elif x == x.parent.left:
			x.parent.left = y

		else:
			x.parent.right = y

		if y:
			y.right = x

		x.parent = y

	def RR_Splay (x):
		R_Rotate (x.parent.parent)

		R_Rotate (x.parent)

	def RL_Splay (x):
		R_Rotate (x.parent)

		L_Rotate (x.parent)

	def LL_Splay (x):
		L_Rotate (x.parent.parent)

		L_Rotate (x.parent)

	def LR_Splay (x):
		L_Rotate (x.parent)

		R_Rotate (x.parent)

	#Recebe Nó x e aplica a rotação enquanto for possível
	def Splay (x):
		while x.parent:
			# Não tem avô
			if not x.parent.parent:
				if x.parent.left == x:
					R_Rotate (x.parent)
				else:
					L_Rotate (x.parent)

			#Criado funcoes aux que nem na aula, nomes já sao bem simples
			elif x.parent.left == x and x.parent.parent.left == x.parent:
				self.RR_Splay (x)

			elif x.parent.left == x and x.parent.parent.right == x.parent:
				self.RL_Splay (x)

			elif x.parent.right == x and x.parent.parent.right == x.parent:
				self.LL_Splay (x)

			else:
				self.LR_Splay (x)


	#Insert(r, x): insere x na ST com raiz r
	def Insert (self, x):
		target = r
		while target:
			if target.key <= x:
				target = target.right
			else:
				target = target.left

		target = Node (target.parent, x)

		Splay (x)

	# Procura o nó com chave x e retorna ele
	def Search_Node (self, x):
		target = self.root
		prev = None
		while target:
			prev = target.parent	
			if target.key < x:
				target = target.right

			elif target > x:
				target = target.left

			else:
				Splay (target)
				return target

		Splay (target)
		return None

	#Search(r,x): true se x está na ST com raiz r e false caso contrário
	def Search (self, x):
		target = Search_Node (self.root, x)

		if not target:
			return False

		Splay (target)

		return True
	

	#Min(r): menor chave presente na ST com raiz r
	def Min (self):
		pass

	#Delete (r, x): remove x da ST com raiz r
	def Delete (self, x):
		target = self.Search_Node (x)

		#cria 2 sub-arvores que nao apontam para a raiz x mais

		target_L = ST ()

		target_L.root = target.left

		target_L.root.parent = None
		
		target_R = ST ()

		target_R.root = target.right

		target_R.root.parent = None

		# Caso tenha uma subarvore esquerda
		# Dá um Splay no Max do lado esquerdo e coloca o direito como o 'right'
		if target_L:
			target_L.Max ()

			target_L.right = target_R

			self.root = target_L

		# Nao tem subarvore esquerda, entao tenho que tomar o lado direito como root
		elif target_R:
			target_R.Min ()

			target_R.left = target_L

			self.root = target_R

		# Caso em que x era o último elemento
		else:
			self.root = None


	#Print(r): imprime todos os elementos na ST com raiz r
	def Print (self):
		pass

a = ST()
if not a.root.parent:
	print (a.root.parent)

