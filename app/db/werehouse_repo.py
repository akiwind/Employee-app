from app.db.connection import get_conn

def add_item(item_name, item_quantity, item_value, item_category):
    conn = get_conn()
    cur = conn.cursor()
    cur.execute(
        "SELECT COUNT(*) FROM werehouse WHERE item_name = %s",(item_name,)        
    )
    count = cur.fetchone()[0]
    
    if count > 0:
        cur.execute(
        "SELECT item_quantity, item_id FROM werehouse WHERE item_name = %s",(item_name,)        
        )
        quant_data =  cur.fetchone()
        item_id =  quant_data[1]
        quant = quant_data[0]
        cur.execute(
            "UPDATE werehouse SET "
            "item_quantity = %s + %s "
            "WHERE item_id = %s",
            ( item_quantity, quant, item_id)
        )
        conn.commit()
        cur.close()
        conn.close()

    else:
        cur.execute(
            "INSERT INTO werehouse(item_name, item_quantity, item_value, item_category)" \
            "VALUES (%s, %s, %s, %s)" \
            "RETURNING item_id",
            (item_name, item_quantity, item_value, item_category)
        )    
        new_id = cur.fetchone()[0]
        conn.commit()
        cur.close()
        conn.close()
        return new_id

def get_all_items():
    conn = get_conn()
    cur = conn.cursor()
    cur.execute(
        "SELECT * FROM werehouse"        
    )
    all_data = cur.fetchall()
    cur.close()
    conn.close()
    return all_data

def get_item_by_id(item_id):
    conn = get_conn()
    cur = conn.cursor()
    cur.execute(
        "SELECT * FROM werehouse WHERE item_id = %s",(item_id,)        
    )
    item_data = cur.fetchone()
    cur.close()
    conn.close()
    return item_data

def update_item(item_name, item_quantity, item_value, item_category, item_id):
    conn = get_conn()
    cur = conn.cursor()
    cur.execute(
        (
        "UPDATE werehouse SET "
        "item_name = %s, "
        "item_quantity = %s, "
        "item_value = %s, "
        "item_category =%s "
        "WHERE item_id = %s"
        ),
        (item_name, item_quantity, item_value, item_category, item_id)  
    )
    conn.commit()
    cur.close()
    conn.close()
    return

def delete_item(item_id):
    conn = get_conn()
    cur = conn.cursor()
    cur.execute(
        "DELETE FROM werehouse WHERE item_id = %s",(item_id,)        
    )
    conn.commit()
    cur.close()
    conn.close()
    return

def item_name_exists(item_name):
    conn = get_conn()
    cur = conn.cursor()
    cur.execute(
        "SELECT COUNT(*) FROM werehouse WHERE item_name = %s",(item_name,)        
    )
    count = cur.fetchone()[0]
    conn.commit()
    cur.close()
    conn.close()
    return count > 0