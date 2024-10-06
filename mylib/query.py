import sqlite3
import logging

logging.basicConfig(
    level=logging.INFO,
    format='**%(asctime)s** - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("db_operations.md"),
        logging.StreamHandler()
    ]
)

def insert_row():
    """Insert a row into the DrugUse table."""
    conn = sqlite3.connect("DrugUseDB.db")
    cursor = conn.cursor()
    
    query = """
        INSERT INTO DrugUse (
            age, n, alcohol_use, alcohol_frequency, marijuana_use, 
            marijuana_frequency, cocaine_use, cocaine_frequency, 
            crack_use, crack_frequency, heroin_use, heroin_frequency,
            hallucinogen_use, hallucinogen_frequency, inhalant_use, 
            inhalant_frequency, pain_releiver_use, pain_releiver_frequency, 
            oxycontin_use, oxycontin_frequency, tranquilizer_use, 
            tranquilizer_frequency, stimulant_use, stimulant_frequency, 
            meth_use, meth_frequency, sedative_use, sedative_frequency) 
        VALUES ('75+', 1000, 50.0, 40.0, 30.0, 20.0, 5.0, 1.0, 0.0, 
            0.0, 0.0, 0.0, 10.0, 5.0, 3.0, 2.0, 5.0, 3.0, 0.5, 
            0.5, 1.0, 1.0, 2.0, 1.0, 0.0, 0.0, 0.5, 0.3)
    """
    cursor.execute(query)
    conn.commit()
    
    # 记录日志
    logging.info("Executed INSERT query:\n```sql\n%s\n```", query)
    logging.info("Inserted a new row into the DrugUse table.")
    
    conn.close()
    return "Success"

def select_rows():
    """Select and print all rows from the DrugUse table."""
    conn = sqlite3.connect("DrugUseDB.db")
    cursor = conn.cursor()
    
    query = "SELECT * FROM DrugUse"
    cursor.execute(query)
    rows = cursor.fetchall()
    
    logging.info("Executed SELECT query:\n```sql\n%s\n```", query)
    logging.info("Selected rows:\n%s", rows)
    
    for row in rows:
        print(row)
    
    conn.close()
    return "Success"

def update_row():
    """Update a specific row in the DrugUse table."""
    conn = sqlite3.connect("DrugUseDB.db")
    cursor = conn.cursor()
    
    query = """
        UPDATE DrugUse 
        SET alcohol_use = 60.0, marijuana_use = 35.0
        WHERE age = '30-34' AND n = 1000
    """
    cursor.execute(query)
    conn.commit()
    
    logging.info("Executed UPDATE query:\n```sql\n%s\n```", query)
    logging.info("Updated the row with age '30-34' and n=1000.")
    
    conn.close()
    return "Success"

def delete_row():
    """Delete a specific row from the DrugUse table."""
    conn = sqlite3.connect("DrugUseDB.db")
    cursor = conn.cursor()
    
    query = """
        DELETE FROM DrugUse 
        WHERE age = '30-34' AND n = 1000
    """
    cursor.execute(query)
    conn.commit()
    
    logging.info("Executed DELETE query:\n```sql\n%s\n```", query)
    logging.info("Deleted the row with age '30-34' and n=1000.")
    
    conn.close()
    return "Success"