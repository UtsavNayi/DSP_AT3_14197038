from logging import exception
import unittest

from src.serie_numeric.logics import NumericColumn

class TestNumericLogic(unittest.TestCase):
    #testcase 1: Test the logic of the db
    def test_case1(self):
        db='postgres1'
        schema_name=None 
        table_name=None, 
        col_name=None 
        serie=None

        with self.assertRaises(SystemExit) as e:
            NumericColumn(db, schema_name,table_name, col_name, serie)
        exception = e.exception
        self.assertEqual(exception.code, 1) 

    #testcase 2: Test the logic of the schema name
    def test_case2(self):
        db= 'postgres'
        schema_name='public1' 
        table_name=None 
        col_name=None 
        serie=None
        
        with self.assertRaises(SystemExit) as e:
            NumericColumn(db, schema_name,table_name, col_name, serie)
        exception = e.exception
        self.assertEqual(exception.code, 1)

    #testcase 3: Test the logic of the table name
    def test_case3(self):
        db= 'postgres'
        schema_name='public'
        table_name=''
        col_name=None 
        serie=None
        
        with self.assertRaises(SystemExit) as e:
            NumericColumn(db, schema_name,table_name, col_name, serie)
        exception = e.exception
        self.assertEqual(exception.code, 1) 

    #testcase 4: Test the logic of the col name
    def test_case4(self, table_name):
        db= 'postgres'
        schema_name='public'
        table_name= {table_name}
        col_name=''
        serie=None
        
        with self.assertRaises(SystemExit) as e:
            NumericColumn(db, schema_name,table_name, col_name, serie)
        exception = e.exception
        self.assertEqual(exception.code, 1)

    #testcase 5: Test the logic of the serie
    def test_case5(self, table_name, col_name):
        db= 'postgres'
        schema_name='public'
        table_name= {table_name}
        col_name={col_name}
        serie=''
        
        with self.assertRaises(SystemExit) as e:
            NumericColumn(db, schema_name,table_name, col_name, serie)
        exception = e.exception
        self.assertEqual(exception.code, 1)



if __name__ == '__main__':
    unittest.main(verbosity=2)