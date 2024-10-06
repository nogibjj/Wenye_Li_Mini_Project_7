import sqlite3


def query():
    """Query the database and perform insert, update, and delete operations"""
    conn = sqlite3.connect("DrugUseDB.db")
    cursor = conn.cursor()

    # Perform SELECT
    cursor.execute("SELECT * FROM DrugUse LIMIT 5")
    rows = cursor.fetchall()
    print("Initial rows:")
    for row in rows:
        print(row)

    # Perform INSERT
    cursor.execute(
        """
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
    )
    print("Inserted a new row.")

    # Perform UPDATE
    cursor.execute(
        """
        UPDATE DrugUse 
        SET alcohol_use = 60.0, marijuana_use = 35.0
        WHERE age = '30-34' AND n = 1000
        """
    )
    print("Updated a row.")

    # Perform DELETE
    cursor.execute(
        """
        DELETE FROM DrugUse 
        WHERE age = '30-34' AND n = 1000
        """
    )
    print("Deleted a row.")

    conn.commit()
    conn.close()

    return "Success"

if __name__ == "__main__":
    query()