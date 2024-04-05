import pandas as pd
import ast

df = pd.read_csv("zd_MO_state_20240214.csv", index_col = 0)

import ast

def extract_custom_fields(customfielddata):
    custom_fields = ast.literal_eval(customfielddata)
    return {key.split('_')[1]: value for key, value in custom_fields.items()}

def customfield(df):
    if 'customfielddata' in df.columns:
        # Apply the function to each row in the DataFrame
        df['custom_fields'] = df['customfielddata'].apply(extract_custom_fields)

        # Mapping of field keys to column names
        field_to_column = {
            '56': 'Commercial',
            '57': 'Commercial - Min. Lot Size',
            '58': 'Commercial - Max. Lot Coverage - Buildings',
            '59': 'Commercial - MaxLotCov. - Building & Impervious',
            '60': 'Commercial - Max. Height',
            '61': 'Commercial - Max Stories',
            '62': 'Office',
            '63': 'Office - Min. Lot Size',
            '64': 'Office - Max. Lot Coverage - Buildings',
            '65': 'Office - MaxLotCov. - Building & Impervious',
            '66': 'Office - Max. Height',
            '67': 'Office - Max Stories',
            '68': 'Light Industrial',
            '69': 'Light Industrial - Min. Lot Size',
            '70': 'Light Industrial - Max. Lot Coverage - Buildings',
            '71': 'Light Industrial - MaxLotCov. - Building & Impervious',
            '72': 'Light Industrial - Max. Height',
            '73': 'Light Industrial - Max Stories',
            '74': 'Heavy Industrial',
            '75': 'Heavy Industrial - Min. Lot Size',
            '76': 'Heavy Industrial - Max. Lot Coverage - Buildings',
            '77': 'Heavy Industrial - MaxLotCov. - Building & Impervious',
            '78': 'Heavy Industrial - Max. Height',
            '79': 'Heavy Industrial - Max Stories',
            '80': 'Institutional Only',
            '81': 'Park/Green Space ONly'
        }

        # Create separate columns for each custom field
        for field in field_to_column:
            df[field_to_column[field]] = df['custom_fields'].apply(lambda x: x.get('27_' + field, ''))

        # Drop unnecessary columns
        df.drop(['customfielddata', 'custom_fields'], axis=1, inplace=True)

    return df

#filter data that has been completed ("status" == "done")
def filter_status(df, status_value='done'):
    return df[df['status'] == status_value]

def unit_float(df):
    # Iterate over the columns
    for unit_column_name in df.columns:
        if unit_column_name.endswith('_units'):
            # Extract the corresponding value column name
            value_column_name = unit_column_name.replace('_units', '')

            # Check if the value column exists in the DataFrame
            if value_column_name in df.columns:
                # Filter rows where the unit column is marked as "number"
                number_rows = df[unit_column_name] == 'number'

                # Convert the value column to float where the unit column is "number"
                df.loc[number_rows, value_column_name] = df.loc[number_rows, value_column_name].astype(float)
                
    return df

def group_type(df):
    unique_types = pd.unique(df['type'])
    grouped_df = df.groupby('type')
    type_groups = {}
    for type_val in unique_types:
        type_groups[f'df_{type_val.lower()}'] = grouped_df.get_group(type_val)
    return type_groups

def group_jurisdiction(df):
    unique_jurisdictions = pd.unique(df['jurisdiction'])
    grouped_df = df.groupby('jurisdiction')
    jurisdiction_groups = {}
    for jurisdiction_val in unique_jurisdictions:
        jurisdiction_groups[f'df_{jurisdiction_val.lower()}'] = grouped_df.get_group(jurisdiction_val)
    return jurisdiction_groups