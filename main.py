import sqlite3
import pandas as pd

db_path = 'Staff.db'
table_instructor = 'Instructor'
attribute_list_Instructor = ['ID', 'FNAME', 'LNAME', 'CITY', 'CCODE']
table_departments = 'Departments'
attribute_list_departments = ['DEPT_ID', 'DEP_NAME', 'MANAGER_ID', 'LOC_ID']

def csv_to_sqlite(csv_file, table_name, attribute_list):
    df = pd.read_csv(csv_file, names=attribute_list)
    with sqlite3.connect(db_path) as conn:
        df.to_sql(table_name, conn, if_exists='replace', index=False)

def append_to_instructor(tablename, id_no, fname, lname, city, ccode):
    data_dict = {'ID': [id_no], 'FNAME': [fname], 'LNAME': [lname], 'CITY': [city], 'CCODE': [ccode]}
    data_append = pd.DataFrame(data_dict)
    with sqlite3.connect(db_path) as conn:
        data_append.to_sql(tablename, conn, if_exists='append', index=False)

def append_to_departments(tablename, dept_id, dep_name, manager_id, loc_id):
    data_dict = {'DEPT_ID': [dept_id], 'DEP_NAME': [dep_name], 'MANAGER_ID': [manager_id], 'LOC_ID': [loc_id]}
    data_append = pd.DataFrame(data_dict)
    with sqlite3.connect(db_path) as conn:
        data_append.to_sql(tablename, conn, if_exists='append', index=False)

def custom_query(query_statement, TABLE_NAME=None):
    with sqlite3.connect(db_path) as conn:
        query_output = pd.read_sql(query_statement + f" FROM {TABLE_NAME}", conn)
    print(f"Query: {query_statement + f' FROM {TABLE_NAME}'}")
    print(f"{query_output}")
    print("-" * 50)

def print_table(table_name):
    query_statement = f"SELECT * FROM {table_name}"
    with sqlite3.connect(db_path) as conn:
        query_output = pd.read_sql(query_statement, conn)
    print(f"Table: {table_name}")
    print(f"{query_output}")
    print("-" * 50)
    

if __name__ == "__main__":
    csv_to_sqlite('Instructor.csv', table_instructor, attribute_list_Instructor)
    csv_to_sqlite('Departments.csv', table_departments, attribute_list_departments)

    append_to_instructor(table_instructor, 12345, 'John', 'Doe', 'New York', 'CS')
    append_to_departments(table_departments, 9, 'Quality Assurance', 30010, 'L0010')

    custom_query("SELECT count(*)", table_departments)