from statistics import mean, median
import streamlit as st
import pandas as pd
import altair as alt
import psycopg2
from psycopg2 import OperationalError

from src.database.logics import PostgresConnector
from src.serie_numeric.queries import get_negative_number_query, get_std_query, get_unique_query

class NumericColumn:
    """
    --------------------
    Description
    --------------------
    -> NumericColumn (class): Class that manages a column loaded from Postgres

    --------------------
    Attributes
    --------------------
    -> schema_name (str): Name of the dataset schema (mandatory)
    -> table_name (str): Name of the dataset table (mandatory)
    -> col_name (str): Name of the column (mandatory)
    -> db (PostgresConnector): Instantation of PostgresConnector class for handling Postgres connection (mandatory)
    -> serie (pd.Series): Pandas serie where the content of a column has been loaded (mandatory)
    -> n_unique (int): Number of unique value of a serie (optional)
    -> n_missing (int): Number of missing values of a serie (optional)
    -> col_mean (int): Average value of a serie (optional)
    -> col_std (int): Standard deviation value of a serie (optional)
    -> col_min (int): Minimum value of a serie (optional)
    -> col_max (int): Maximum value of a serie (optional)
    -> col_median (int): Median value of a serie (optional)
    -> n_zeros (int): Number of times a serie has values equal to 0 (optional)
    -> n_negatives (int): Number of times a serie has negative values (optional)
    -> histogram (int): Altair histogram displaying the count for each bin value of a serie (optional)
    -> frequent (int): Datframe containing the most frequest value of a serie (optional)

    """
    def __init__(self, db, schema_name=None, table_name=None, col_name=None, serie=None):

        self.schema_name = schema_name
        self.table_name = table_name
        self.col_name = col_name
        self.db = db
        self.serie = serie
        self.n_missing = 0
        self.col_mean = 0
        self.col_min = 0
        self.col_max = 0
        self.col_median = 0
        self.n_zeros = 0
        self.histogram = 0
        self.frequent = 0




    def set_data(self):
        """
        --------------------
        Description
        --------------------
        -> set_data (method): Class method that computes all requested information from self.serie to be displayed in the Numeric section of Streamlit app 

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
        data = { 'Description' : ['Number of Unique Values','Number of Rows with Missing Values','Number of Rows with 0','Number of Rows with Negative Values','Average Value','Standard Deviation Value','Minimum Value','Maximum Value','Median Value'],
        'Value' : [self.set_unique(), self.set_missing(), self.set_zeros(), self.set_negatives(), self.set_mean(), self.set_std(), self.set_min(), self.set_max(), self.set_median(), self.set_median()]}
        print(pd.DataFrame(data))
        st.table(data)

    def is_serie_none(self):
        """
        --------------------
        Description
        --------------------
        -> is_serie_none (method): Class method that checks if self.serie is empty or none 

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
        if(self.serie.notna().sum() == 0):
            print("Column has the missing values")
        return

    def set_unique(self):
        """
        --------------------
        Description
        --------------------
        -> set_unique (method): Class method that computes the number of unique value of a column using a SQL query (get_unique_query())

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
        unique = get_unique_query(self.schema_name, self.table_name, self.col_name)
        q = self.db.run_query(unique)
        return q

    def set_missing(self):
        """
        --------------------
        Description
        --------------------
        -> set_missing (method): Class method that computes the number of missing value of a serie

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
        self.n_missing = self.serie[self.col_name].isna().sum()
        return self.n_missing

    def set_zeros(self):
        """
        --------------------
        Description
        --------------------
        -> set_zeros (method): Class method that computes the number of times a serie has values equal to 0

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
        self.n_zeros = self.serie[self.col_name].loc[self.serie[self.col_name] == 0 ].count()
        return self.n_zeros

    def set_negatives(self):
        """
        --------------------
        Description
        --------------------
        -> set_negatives (method): Class method that computes the number of times a serie has negative values using a SQL query (get_negative_number_query())

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
        negative = get_negative_number_query(self.schema_name, self.table_name, self.col_name)
        q = self.db.run_query(negative)
        return q

    def set_mean(self):
        """
        --------------------
        Description
        --------------------
        -> set_mean (method): Class method that computes the average value of a serie

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
        self.col_mean = self.serie[self.col_name].mean().round(2)
        return self.col_mean

    def set_std(self):
        """
        --------------------
        Description
        --------------------
        -> set_std (method): Class method that computes the standard deviation value of a serie using a SQL query (get_std_query)

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
        std = get_std_query(self.schema_name, self.table_name, self.col_name)
        q = self.db.run_query(std)
        return q
        
    def set_min(self):
        """
        --------------------
        Description
        --------------------
        -> set_min (method): Class method that computes the minimum value of a serie

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
        min = self.serie.min()
        return min

    def set_max(self):
        """
        --------------------
        Description
        --------------------
        -> set_max (method): Class method that computes the maximum value of a serie

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
        max = self.serie.max()
        return max

    def set_median(self):
        """
        --------------------
        Description
        --------------------
        -> set_median (method): Class method that computes the median value of a serie

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
        median = self.serie.median()
        return median

    def set_histogram(self):
        """
        --------------------
        Description
        --------------------
        -> set_histogram (method): Class method that computes the Altair histogram displaying the count for each bin value of a serie

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
        df = self.serie.to_frame().reset_index()
        df = df.rename(columns = {'index': 'value', 0: 'Count of Records'})
        h = alt.Chart(df).mark_bar().encode(x = 'Count of Records', y = 'value')
        st.altair_chart(h, use_container_width=True)

    def set_frequent(self, end=20):
        """
        --------------------
        Description
        --------------------
        -> set_frequent (method): Class method that computes the Dataframe containing the most frequest value of a serie

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
        s_freq = self.serie.value_counts()
        s_freq = s_freq.to_frame().reset_index()
        s_freq = s_freq.rename(columns = {'index': 'Value', 0: 'Occurence'})
        s_freq['Percentage'] = ''
        sum = len(self.serie)
        s_freq['Percentage'] = s_freq['Occurence'] / sum
        st.dataframe(s_freq.head(15))
        return s_freq.head(15)


    def get_summary_df(self,):
        """
        --------------------
        Description
        --------------------
        -> get_summary_df (method): Class method that formats all requested information from self.serie to be displayed in the Overall section of Streamlit app as a Pandas dataframe with 2 columns: Description and Value

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
        
    '''
    if __name__ == "__main__": 
          connection_object = PostgresConnector()
          conn = connection_object.open_connection()
          curr = connection_object.open_cursor()
          col_list = connection_object.run_query("SELECT company_name FROM public.customers;")
          text_obj = NumericColumn(schema_name="public", table_name="customers", col_name="company_name", db=connection_object, serie = pd.Series(col_list))
          text_obj.get_summary_df()
          '''
    