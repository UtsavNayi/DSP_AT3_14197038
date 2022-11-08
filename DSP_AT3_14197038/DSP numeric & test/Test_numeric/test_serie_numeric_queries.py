from ast import Try
from logging import exception
import unittest

from src.serie_numeric.queries import get_negative_number_query, get_std_query, get_unique_query

class TestGetNegativeNumber(unittest.TestCase):

    #testcase 1: Test if the column values are negative or not.
     def test_case1(self):
         schema_name = {schema_name} 
         table_name = f'{schema_name}.{table_name}'
         col_name= f"SELECT COUNT(*) FROM {schema_name}.{table_name} WHERE {col_name} > 0;"

         with self.assertRaises(SystemExit) as e:
             get_negative_number_query(schema_name, table_name, col_name)
         exception = e.exception
         self.assertEqual(exception.code, 1)

    #testcase 2: Test if the column values are negative and true.
     def test_case1(self):
         raised= False
         schema_name = {schema_name}
         table_name =f'{schema_name}.{table_name}'
         col_name = f"SELECT COUNT(*) FROM {schema_name}.{table_name} WHERE {col_name} < 0;"
         
         try:
             with self.assertRaises(SystemExit) as e:
                 get_negative_number_query(schema_name, table_name, col_name)
         except:
             raised = True
             self.assertTrue(raised, 'Exception raised') 
         
         exception = e.exception
         self.assertEqual(exception.code, 1)

class TestStdQuery(unittest.TestCase):

    #testcase 3: Test the standard deviation of column values.
     def test_case3(self):
         schema_name = {schema_name} 
         table_name = f'{schema_name}.{table_name}'
         col_name= f"SELECT {col_name}, {col_name} as standard_deviation FROM {schema_name}.{table_name} GROUP By {col_name};"

         with self.assertRaises(SystemExit) as e:
             get_std_query(schema_name, table_name, col_name)
         exception = e.exception
         self.assertEqual(exception.code, 1)

    #testcase 4: Test if the column values are returning the standard deviation.
     def test_case4(self):
         raised= False
         schema_name = {schema_name}
         table_name =f'{schema_name}.{table_name}'
         col_name = f"SELECT {col_name}, stddev_pop{col_name} as standard_deviation FROM {schema_name}.{table_name} GROUP By {col_name};"
         
         try:
             with self.assertRaises(SystemExit) as e:
                 get_std_query(schema_name, table_name, col_name)
         except:
             raised = True
             self.assertTrue(raised, 'Exception raised') 
         
         exception = e.exception
         self.assertEqual(exception.code, 1)

class TestUniqueQuery(unittest.TestCase):

    #testcase 5: Test the unique number of columns.
     def test_case3(self):
         schema_name = {schema_name} 
         table_name = f'{schema_name}.{table_name}'
         col_name= f"SELECT count({col_name}) FROM {schema_name}.{table_name};"

         with self.assertRaises(SystemExit) as e:
             get_unique_query(schema_name, table_name, col_name)
         exception = e.exception
         self.assertEqual(exception.code, 1)

    #testcase 6: Test if the functions shows the unique number of columns in the table.
     def test_case4(self):
         raised= False
         schema_name = {schema_name}
         table_name =f'{schema_name}.{table_name}'
         col_name = f"SELECT count(distinct{col_name}) FROM {schema_name}.{table_name};"
         
         try:
             with self.assertRaises(SystemExit) as e:
                 get_unique_query(schema_name, table_name, col_name)
         except:
             raised = True
             self.assertTrue(raised, 'Exception raised') 
         
         exception = e.exception
         self.assertEqual(exception.code, 1)



if __name__ == '__main__':
    unittest.main(verbosity=2)