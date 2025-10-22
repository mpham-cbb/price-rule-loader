import pandas as pd
import numpy as np
import streamlit as st
import time


def upload_dataset(key: str) -> pd.DataFrame():
    """"
    
    """
    file = st.file_uploader("Upload file", type=["xlsx", "xls"], accept_multiple_files=False, key=key)

    if not file:
        st.warning("Please upload a file.")
        return pd.DataFrame()

    data = pd.read_excel(file)
    file.close()

    return data


def progress_bar():
    progress_text = "Processing files. Please wait."
    my_bar = st.progress(0, text=progress_text)

    for percent_complete in range(100):
        time.sleep(0.01)
        my_bar.progress(percent_complete +1, text=progress_text)

    my_bar.empty()
    st.success("Files processed successfully.")


def trim_spaces(df):
    """
    This function trims trailing spaces in column names and values
    """

    df.columns = df.columns.str.strip()
    df = df.applymap(lambda x: x.strip() if isinstance(x, str) else x)

    return df


def fill_customers_with_pricing_rule(customer_df, pricing_rule_df):
    # clean dataset
    customer_df = trim_spaces(customer_df)
    pricing_rule_df = trim_spaces(pricing_rule_df)

    # Get the list of customers from the customer_df
    if "Customers #" in customer_df.columns:
        customers = customer_df["Customers #"].tolist()
    elif "SLSHAN" in customer_df.columns:
        customers = customer_df["SLSHAN"].tolist()
    else:
        raise ValueError("Customer DataFrame must contain either 'Customers #' or 'SLSHAN' column")

    # Determine the number of pricing_rules per customer
    rules_per_customer = len(pricing_rule_df)
    
    # Repeat each customer for all pricing_rules (for rules_per_customer times per customer)
    customers_repeated = sum([[customer] * rules_per_customer for customer in customers], [])
    
    # Create a new DataFrame by repeating the pricing_rule_df for each customer
    full_df = pd.concat([pricing_rule_df] * len(customers), ignore_index=True)
    
    # Add the repeated customers to the DataFrame
    full_df['Address'] = customers_repeated
    
    # Reorder columns 
    full_df = full_df[
        ['Pric  UM', 'Deviation Number', 'Address', 'Cust  Price Rule', 
         'Type', 'Pricing  Rule', 'Color  Code', 'Unit  Price',
         'Effective  Date', 'Expired  Date']
    ]
    # Convert the date columns back to mm/dd/yyyy format
    full_df['Effective  Date'] = pd.to_datetime(full_df['Effective  Date']).dt.strftime('%m/%d/%Y')
    full_df['Expired  Date'] = pd.to_datetime(full_df['Expired  Date']).dt.strftime('%m/%d/%Y')

    return full_df