def get_negative_number_query(schema_name, table_name, col_name):
    """
    --------------------
    Description
    --------------------
    -> get_negative_number_query (method): Function that returns the query used for computing the number of times a column from a Postgres table has negative values 

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
    negative_number_query = f"SELECT COUNT(*) FROM {schema_name}.{table_name} WHERE {col_name} < 0;"

    return negative_number_query

def get_std_query(schema_name, table_name, col_name):
    """
    --------------------
    Description
    --------------------
    -> get_std_query (method): Function that returns the query used for computing the standard deviation value of a column from a Postgres table

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
    std_query = f"SELECT {col_name}, stddev_pop{col_name} as standard_deviation FROM {schema_name}.{table_name} GROUP By {col_name};"

    return std_query

#https://stackoverflow.com/questions/62660802/postgres-computing-the-standard-deviation-value-for-each-trip

def get_unique_query(schema_name, table_name, col_name):
    """
    --------------------
    Description
    --------------------
    -> get_unique_query (method): Function that returns the query used for computing the number of unique values of a column from a Postgres table

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
    unique_query = f"SELECT count(distinct{col_name}) FROM {schema_name}.{table_name};"

    return unique_query

#https://stackoverflow.com/questions/20165673/postgres-find-number-of-distinct-values-for-each-column
