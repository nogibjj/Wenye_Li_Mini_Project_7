from databricks import sql
import os
import logging
from dotenv import load_dotenv

logging.basicConfig(
    level=logging.INFO,
    format='**%(asctime)s** - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("db_operations.md"),
        logging.StreamHandler()
    ]
)

load_dotenv()
server_h = os.getenv("SERVER_HOSTNAME")
access_token = os.getenv("DATABRICKS_KEY")
http_path = os.getenv("HTTP_PATH")

def complex_query():
    """A complex SQL query involving joins, aggregation, and sorting."""
    with sql.connect(
        server_hostname=server_h,
        http_path=http_path,
        access_token=access_token,
    ) as connection:
        cursor = connection.cursor()

        query = """
            WITH AgeStats AS (
                SELECT age,
                       AVG(alcohol_use) AS avg_alcohol_use,
                       AVG(marijuana_use) AS avg_marijuana_use
                FROM DrugUseDB
                GROUP BY age
            )
            SELECT d.age, d.n, d.alcohol_use, a.avg_alcohol_use, 
            d.marijuana_use, a.avg_marijuana_use
            FROM DrugUseDB d
            JOIN AgeStats a
            ON d.age = a.age
            ORDER BY d.age ASC, d.n DESC
        """
        cursor.execute(query)
        rows = cursor.fetchall()

        logging.info("Executed query:\n```sql\n%s\n```", query)
        logging.info("Query results:\n%s", rows)
        
        for row in rows:
            print(row)

        cursor.close()
    return "Success"


if __name__ == "__main__":
    complex_query()