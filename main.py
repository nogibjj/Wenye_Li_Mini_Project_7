"""
ETL-Query script
"""

from mylib.extract import extract
from mylib.transform_load import load
from mylib.query import insert_row, update_row, delete_row, select_rows

# Extract
print("Extracting data...")
extract()

# Transform and load
print("Transforming data...")
load()

"""Query: Perform CRUD operations"""

print("Inserting data...")
insert_row()

print("Updating data...")
update_row()

print("Deleting data...")
delete_row()

print("Selecting and displaying data...")
select_rows()
