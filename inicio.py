# Idéia da solução
nm_banco = "mariahdb"

def gambi(banco: str=None, user: str=None, tabela: str=None, valor: int=None, *args):
# Faz com que a variável nm_banco seja acessível dentro da função gambi, permitindo que ela seja manipulada.
    global nm_banco
    nm_banco = "mongodb"
    
    try:
        # Aqui seria a conexão com o banco de dados, usando as variáveis banco e user
        # E depois a consulta na tabela usando a variável tabela e valor
        banco = nm_banco
        print (f'Banco= {banco} Usuario= {user} Tabela= {tabela} Valor={valor}')
        
        if banco is None:
            raise ValueError("O parâmetro 'banco' é obrigatório.")
        
        if user is None:
            raise ValueError("O parâmetro 'user' é obrigatório.")
        
        if tabela is None:
            raise ValueError("O parâmetro 'tabela' é obrigatório.")
        
        if valor is None:
            raise ValueError("O parâmetro 'valor' é obrigatório.")

        ...
        gambi2("parametro extra", "outro parametro extra", 1, "comentario")

        return(True)
    except Exception as e:
        print(f"Ocorreu um erro: {e}")

def gambi2(*args):
# "*args" é um argumento que pode passar qualquer qtd de qualquer, pois ele vai transformar em uma tupla, e o nome args é apenas uma convenção
# pode transformar a atupla em list pois a list pode ser modificada, diferente da tupla que é imutável
    print(args)
    for arg in args:
        print(arg)

print (gambi(banco=nm_banco, user="root", tabela="clientes", valor=10))
   
