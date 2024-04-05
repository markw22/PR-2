import unittest
import pandas as pd
import ast


from PR2 import extract_custom_fields
from PR2 import customfield
def test_extract_custom_fields(self):
        customfielddata = '{"field_name_1": "value1", "field_name_2": "value2"}'
        expected_result = {"name": "value1", "2": "value2"}
        self.assertEqual(extract_custom_fields(customfielddata), expected_result)

def test_customfield(self):
        # Sample DataFrame with customfielddata column
        df = pd.DataFrame({'customfielddata': ['{"field_name_56": "Value1", "field_name_57": "Value2"}']})

        customfield(df)

        # Check if custom_fields column is added
        self.assertIn('custom_fields', df.columns)

def test_customfield(self):
        # Sample DataFrame with customfielddata column
        df = pd.DataFrame({
            'customfielddata': [
                '{"field_name_56": "Value1", "field_name_57": "Value2"}'
            ]
        })

        # Call the function
        result_df = customfield(df)

        # Check if custom_fields column is dropped
        self.assertNotIn('custom_fields', result_df.columns)

        # Check for the presence of some expected columns
        expected_columns = [
            'Commercial',
            'Commercial - Min. Lot Size',
            'Office',
            'Light Industrial',
            'Heavy Industrial',
            'Institutional Only',
            'Park/Green Space ONly'
        ]
        for column in expected_columns:
            self.assertIn(column, result_df.columns)

from PR2 import filter_status
def test_filter_status(self):
        # Sample DataFrame
        df = pd.DataFrame({
            'id': [1, 2, 3, 4],
            'status': ['done', 'pending', 'done', 'pending']
        })

        # Call the function
        result_df = filter_status(df)

        # Check if only rows with status 'done' are returned
        expected_ids = [1, 3]
        self.assertCountEqual(result_df['id'].tolist(), expected_ids)

from PR2 import unit_float
def test_unit_float(self):
        # Sample DataFrame
        df = pd.DataFrame({
            'value1': [1, 2, '3', 4],
            'value1_units': ['number', 'number', 'number', 'number'],
            'value2': [5, '6', '7', 8],
            'value2_units': ['number', 'number', 'text', 'number']
        })

        # Call the function
        result_df = unit_float(df)

        # Check if value1 column is converted to float where units are 'number'
        self.assertTrue(result_df['value1'].dtype == float)

        # Check if value2 column is not converted where units are not 'number'
        self.assertTrue(result_df['value2'].dtype != float)

from PR2 import group_type
def test_group_type(self):
        # Sample DataFrame
        df = pd.DataFrame({
            'type': ['A', 'B', 'A', 'C', 'B'],
            'value': [1, 2, 3, 4, 5]
        })

        # Call the function
        result = group_type(df)

        # Check if keys are formed correctly
        expected_keys = ['df_a', 'df_b', 'df_c']
        self.assertCountEqual(result.keys(), expected_keys)

        # Check if values are grouped correctly
        expected_lengths = [2, 2, 1]
        for key, length in zip(expected_keys, expected_lengths):
            self.assertEqual(len(result[key]), length)

from PR2 import group_jurisdiction
def test_group_jurisdiction(self):
        # Sample DataFrame
        df = pd.DataFrame({
            'jurisdiction': ['A', 'B', 'A', 'C', 'B'],
            'value': [1, 2, 3, 4, 5]
        })

        # Call the function
        result = group_jurisdiction(df)

        # Check if keys are formed correctly
        expected_keys = ['df_a', 'df_b', 'df_c']
        self.assertCountEqual(result.keys(), expected_keys)

        # Check if values are grouped correctly
        expected_lengths = [2, 2, 1]
        for key, length in zip(expected_keys, expected_lengths):
            self.assertEqual(len(result[key]), length)
