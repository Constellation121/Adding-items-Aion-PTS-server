# Code created by Constellation121

import pyodbc
from datetime import datetime


def adicionar_item(conexao, char_id, name_id, amount=0, slot=0, warehouse=0):
    cursor = conexao.cursor()
    
    if slot is None:
        slot = 0  
    if warehouse is None:
        warehouse = 0 
    
    current_time = datetime.now()
    
    print(f"char_id: {char_id}, name_id: {name_id}, amount: {amount}, slot: {slot}, warehouse: {warehouse}")
    
    sql = '''
    INSERT INTO dbo.user_item (char_id, name_id, amount, slot, warehouse, create_date, update_date)
    VALUES (?, ?, ?, ?, ?, ?, ?)
    '''
    
    parametros = (
        char_id,
        name_id,
        amount,          
        slot,             
        warehouse,        
        current_time,    
        current_time      
    )
    
    try:
        cursor.execute(sql, parametros)
        conexao.commit()
        print("Item inserido com sucesso.")
    except pyodbc.IntegrityError as e:
        print(f"Erro de integridade: {e}")
        conexao.rollback()


def conectar_bd():
    conn = pyodbc.connect(
        'DRIVER={ODBC Driver 17 for SQL Server};'
        'SERVER=*****;'
        'DATABASE=*****;'
        'UID=*****;'
        'PWD=*****;'
    )
    return conn


if __name__ == "__main__":
    conn = conectar_bd()
    
    adicionar_item(
        conn,
        char_id=1018,
        name_id=188501091,
        amount=1,  #  'amount'
        slot=1,     # 'slot'
        warehouse=0 # 'warehouse'
    )
    
    conn.close()
