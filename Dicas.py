"""
Dicas PowerShell

PowerShell
Get-ExecutionPolicy -> Verifica qual a situação da liberdade de execução de códigos na maquina (Restricted, Unrestricted, AllSigned)
Set-ExecutionPolicy -> Altera a situação da liberdade de execução de códigos na maquina
Set-ExecutionPolicy Restricted -Force (Não executa nada)
Set-ExecutionPolicy Unrestricted -Force (Executa tudo)
Set-ExecutionPolicy AllSigned -Force (Quando for executar pergunta autorização)

Utilize o curlcomando para baixar o arquivo do repositório GitHub do winutils para a pasta recém-criada:

curl --ssl-no-revoke -L -o C:\hadoop\bin\winutils.exe https://github.com/cdarlint/winutils/raw/master/hadoop-3.3.6/bin/winutils.exe

Passos VS Code
1 - Criar projeto (folder)
2 - criar venv (py -m venv venv)
3 - ativar venv (.\venv\Scripts\activate)


Dicas PYTHON
Docstring é uma nota que pode ser em várias linhas
É feito colocando 3 aspas (simples ou duplas) iniciais e 3 aspas finais

Comentário é somente a utilização de um # 

a utilização de reticências (...) é para indicar que o código continua e talvez seja colocado posteriormente, 
ou seja, não é necessário colocar o código completo para mostrar um exemplo

"""

print(1, 2, 3)
# É possível definir o separador e o caracter final da linha
print(1, 2, 3, sep='-')
print(4, 5, 6, sep='-', end='\r\n')
print(7, 8, 9, sep='-', end='$$')
print()

# Caracter de Escape é quando precisa se colocar um caracter como aspas por exemplo dentro de uma string aberta com aspas
print("\"Alex\"")

# Caracter de Expressões Regulares é quando precisa se mostrar tudo inclusive os Escapes
print(r"\"Alex\"")

#Tipos Str, Int, Float e Boleano
print(type('ABC'), type(123), type(456.786), type(True))

for ... in range(10):
    print("Olá Mundo")