# import de lib do oracle para que possamos fazer uso das suas funções
import cx_Oracle

# Informações de conexão para que possamos gerar o login
user = "usr88"
password = "usr88"
host = "200.132.53.144"
port = "1521"

# Construir o DSN (Data Source Name)
# o DSN é usado para especificar os detalhes necessários para
# estabelecer uma conexão com o banco de dados Oracle

dsn = cx_Oracle.makedsn(host, port, service_name='XEpdb1')

# Estabelecer a conexão
connection = cx_Oracle.connect(user, password, dsn)

cursor = connection.cursor()
# essa function após que tu insira
# o id do filme ela informa quantos atores ele tem

cursor.execute("SELECT quantos(50) FROM dual")
result1 = cursor.fetchall()

# passa o id do stremaing e informa quantos filmte naquele streaming
cursor.execute("Select total_filmes (60) from dual")
result2 = cursor.fetchall()

# Chamar a procedure com os parâmetros necessários
output_variable = cursor.var(cx_Oracle.STRING)
cursor.callproc("aonde", ["Clube da luta", output_variable])

# Obter o valor retornado pela procedure
result3 = output_variable.getvalue()

# Exibir os resultados da primeira function

print("Function, que informa quantos atores tem no filme:")
for row in result1:
    print(row)

# Exibir os resultados da segunda function

print("Function, que informa quantos filmes tem no streaming:")
for row in result2:
    print(row)

# Exibir o resultado retornado da procedure
print("Procedure, que informa em streaming o filme está:", result3)

# Fechar a conexão
connection.close()
