import streamlit as st
import pandas as pd

from src.serie_numeric.logics import NumericColumn
from src.database.logics import PostgresConnector

def display_numerics(table_schema, table_name):
    """
    --------------------
    Description
    --------------------
    -> display_numerics (function): Function that displays all the relevant information for every numerical column of a table

    --------------------
    Parameters
    --------------------
    => To be filled by student
    -> name (type): description

    --------------------
    Pseudo-Code
    --------------------
    => To be filled by student
    -> pseudo-code

    --------------------
    Returns
    --------------------
    => To be filled by student
    -> (type): description

    """

    print(table_schema)
    print(table_name)
    lt = st.session_state.db.load_table(table_schema, table_name)
    data1 = pd.DataFrame(lt)
    data1 = data1.convert_dtypes().dtypes
    data1 = data1.to_frame().reset_index()
    data1 = data1.rename(columns= {'index':'Column', 0: 'Datatype'})
    data1 = data1.loc[data1['Datatype']=='int']
    col_list = list(data1['Column'])
    count = 1

    for name in col_list:
        with st.expander(f"{count}. Column: {str(name)}", expanded=False):
            col_serie = st.session_state.db.run_query(f"SELECT {name} FROM {table_schema}.{table_name};")
            display_numeric(table_schema, table_name, name, col_serie)
            count = count+1

def display_numeric(table_name, table_schema, col_name, i):

    """
    --------------------
    Description
    --------------------
    -> display_numeric (function): Function that instantiates a NumericColumn class from a dataframe column and displays all the relevant information for a single numerical column of a table

    --------------------
    Parameters
    --------------------
    => To be filled by student
    -> name (type): description

    --------------------
    Pseudo-Code
    --------------------
    => To be filled by student
    -> pseudo-code

    --------------------
    Returns
    --------------------
    => To be filled by student
    -> (type): description
    """

    numeric = NumericColumn(schema_name=table_schema, table_name=table_name, col_name=col_name, db=st.session_state.db, serie = pd.Series(i))
    numeric.set_data()
    
   # = col_name(column=('col &d' % i for i in range(2)))
   # st.table(df)
