class Mongo:
    def __init__(self, banco: str=None, user: str=None, tabela: str=None, valor: list=None):
        self.banco = banco
        self.user = user
        self.tabela = tabela
        self.valor = list(valor) if valor is not None else []
        self.__statusmongo = self.__vrf_mongo()
        self.__statusbanco = self.__vrf_banco()
        self.__statususer = self.__vrf_user()
        self.__statustabela = self.__vrf_tabela()
        self.__statusvalor = self.__vrf_valor()
        self.__prm = self.__vld_prm()
    
    def __vld_prm(self):
        # Lógica para verificar se o Banco de Dados existe
        if self.banco is None:
            retorno = "O parâmetro 'banco' é obrigatório."
            # raise ValueError("O parâmetro 'banco' é obrigatório.")
        elif self.user is None:
            retorno = "O parâmetro 'user' é obrigatório."
            # raise ValueError("O parâmetro 'user' é obrigatório.")
        elif self.tabela is None:
            retorno = "O parâmetro 'tabela' é obrigatório."
            # raise ValueError("O parâmetro 'tabela' é obrigatório.")
        else: 
            retorno = False
        ...
        return (retorno)

    def __vrf_mongo(self):
        ... # Lógica para verificar se a instância do MongoDB ta ativa
        return (True)

    def __vrf_banco(self):
        # Lógica para verificar se o Banco de Dados existe
        ...
        return (True)

    def __vrf_user(self):
        # Lógica para verificar se o usuário tem permissão para acessar o banco
        ...
        return (True)

    def __vrf_tabela(self):
        # Lógica para verificar se a tabela existe no banco
        ...
        return (True)

    def __vrf_valor(self):
        ... # Lógica para validar os data types enviados da tabela
        return (True)

    def insert(self):
        if not self.__prm:
            print(f'Inserindo valor {self.valor} na tabela {self.tabela} do banco {self.banco} com o usuário {self.user}')
        else:
            print(self.__prm)

        return (True)

db = "DB_SABESP"
usu = "admin"
tab = "TB_CLIENTES"
val = 1, "Ze da Silva", "PF", "Ativo", "2024-06-01"

sabesp = Mongo(db, usu, tab, val)
sabesp.insert()


# # Idéia da solução
# nm_banco = "mariahdb"

# def gambi(banco: str=None, user: str=None, tabela: str=None, valor: int=None, *args):
# # Faz com que a variável nm_banco seja acessível dentro da função gambi, permitindo que ela seja manipulada.
#     global nm_banco
#     nm_banco = "mongodb"
    
#     try:
#         # Aqui seria a conexão com o banco de dados, usando as variáveis banco e user
#         # E depois a consulta na tabela usando a variável tabela e valor
#         banco = nm_banco
#         print (f'Banco= {banco} Usuario= {user} Tabela= {tabela} Valor={valor}')
        
#         ...
#         gambi2("parametro extra", "outro parametro extra", 1, "comentario")

#         return(True)
#     except Exception as e:
#         print(f"Ocorreu um erro: {e}")

# def gambi2(*args):
# # "*args" é um argumento que pode passar qualquer qtd de qualquer, pois ele vai transformar em uma tupla, e o nome args é apenas uma convenção
# # pode transformar a atupla em list pois a list pode ser modificada, diferente da tupla que é imutável
#     print(args)
#     for arg in args:
#         print(arg)

# print (gambi(banco=nm_banco, user="root", tabela="clientes", valor=10))
   
