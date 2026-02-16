# Idéia da solução
def gambi(banco=None, user=None, tabela=None, valor=None):
    try:
        # Aqui seria a conexão com o banco de dados, usando as variáveis banco e user
        # E depois a consulta na tabela usando a variável tabela e valor
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

        return(True)
    except Exception as e:
        print(f"Ocorreu um erro: {e}")


print (gambi(banco="mongodb", user="root", tabela="clientes", valor=10))


