from database import conectar

def cadastrar_cliente(nome, empresa, telefone, servico, valor_mensal, dia_vencimento, data_inicio, email='', status='EM DIA', observacoes=''):
    
    conect = None
    
    try:

        conect = conectar()
        cursor = conect.cursor()

        cursor.execute('''
                    INSERT INTO clientes (nome, empresa, telefone, email, servico, valor_mensal, dia_vencimento, data_inicio, status, observacoes)
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                        ''', (nome, empresa, telefone, email, servico, valor_mensal, dia_vencimento, data_inicio, status, observacoes))
       
        linhas_alteradas = cursor.rowcount

        conect.commit()

        if linhas_alteradas == 0:
            return False
        else: 
            return True

    except Exception as e:
        if conect is not None:
            conect.rollback()
            
        print(f'Erro ao cadastrar novo cliente [{e}]')
        return False
    
    finally:
        if conect is not None:
            conect.close()

    

def listar_clientes():

    conect = None

    try:

        conect = conectar()
        cursor = conect.cursor()

        cursor.execute('''
                    SELECT nome, empresa, telefone, email, servico, valor_mensal, dia_vencimento, data_inicio, status, observacoes
                    FROM clientes
                        ''')

        resposta = cursor.fetchall()

        print(resposta)
        return resposta
    
    except Exception as e:
        print(f'Erro ao listar clientes [{e}]')
        return False

    finally:
        if conect is not None:
            conect.close()


    

def buscar_cliente(cliente_id):

    conect = None

    try:
        conect = conectar()
        cursor = conect.cursor()

        cursor.execute('''
                    SELECT nome, empresa, telefone, email, servico, valor_mensal, dia_vencimento, data_inicio, status, observacoes
                    FROM clientes
                    WHERE id = ?
    ''', (cliente_id,))

        resposta = cursor.fetchone()
        return resposta

    except Exception as e:
        print(f'Erro ao buscar cliente [{e}]')
        return False

    finally:
        if conect is not None:
            conect.close()

    

def editar_cliente(cliente_id, nome, empresa, telefone, servico, valor_mensal, dia_vencimento, data_inicio, email, status, observacoes):
    
    conect = None
    
    try:
        conect = conectar()
        cursor = conect.cursor()

        cursor.execute('''
                    UPDATE clientes
                    SET nome = ?, empresa = ?, telefone = ?, email = ?, servico = ?, valor_mensal = ?, dia_vencimento = ?, data_inicio = ?, status = ?, observacoes = ?
                    WHERE id = ?

''', (nome, empresa, telefone, email, servico, valor_mensal, dia_vencimento, data_inicio, status, observacoes, cliente_id))

        
        linhas_alteradas = cursor.rowcount

        conect.commit()


        if linhas_alteradas == 0:
            return False
        else: 
            return True

    except Exception as e:
         if conect is not None:
            conect.rollback()

         print(f'Erro ao editar cliente [{e}]')
         return False

    finally:
        if conect is not None:
            conect.close()


def cancelar_cliente(cliente_id):

    conect = None

    try:
        conect = conectar()
        cursor = conect.cursor()

        cursor.execute('''
                    UPDATE clientes
                    SET status = 'CANCELADO'
                    WHERE id = ?
        ''', (cliente_id,))

        linhas_alteradas = cursor.rowcount

        conect.commit()


        if linhas_alteradas == 0:
            return False
        else:
            return True

    except Exception as e:
        if conect is not None:
            conect.rollback()
            
        print(f'Erro ao cancelar cliente [{e}]')
        return False

    finally:
        if conect is not None:
            conect.close()