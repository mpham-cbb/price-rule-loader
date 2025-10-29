import streamlit as st
import pandas as pd

from utils.general_utils import (
    upload_dataset, progress_bar,
    fill_customers_with_pricing_rule)


def price_loader():
    # Authentication is already handled in main app
    # title
    st.markdown(
    "<h1 style='text-align: center;'>PRICE RULE LOADER</h1>",
    unsafe_allow_html=True
    )


    ## Section A: Customer address (ship to) file
    st.header(':man-woman-girl-boy: A. Customers Address')
    
    # with st.expander("See File Format Example"):
    st.write("Make sure your file is in either following format:")

    # file format example
    cust_addr_example = pd.DataFrame(columns=['Customers #'])
    cust_addr_example_1 = pd.DataFrame(columns=['SLSHAN'])
    st.dataframe(cust_addr_example)    
    st.dataframe(cust_addr_example_1)    
    
    # pass in customer address df
    customer_df = upload_dataset(key="customer_upload")
    if len(customer_df) > 0:
        progress_bar()
        st.write(customer_df.shape)

    
    ## Section B: Pricing rule template
    st.header(':page_facing_up: B. New Pricing Rule Template')
    # with st.expander("See File Format Example"):
    st.write("Make sure your file is in the following format:")

    # file format example
    price_rule_cols = ['Pric  UM', 'Deviation Number', 'Address', 'Cust  Price Rule', 
                    'Type', 'Pricing  Rule', 'Color  Code', 'Unit  Price', 
                    'Effective  Date', 'Expired  Date']
    price_rul_example = pd.DataFrame(columns=price_rule_cols)
    st.dataframe(price_rul_example)

    # pass in pricing_rule template df
    pricing_rule_df = upload_dataset(key="pricing_rule_upload")
    if len(pricing_rule_df) > 0:
        progress_bar()
        st.write(pricing_rule_df.shape)


    ## Section C: dfs transformation and result
    # Prevent errors before processing
    if customer_df.empty and pricing_rule_df.empty:
        # st.info("Please upload both Customer and Pricing Rule files to proceed.")
        st.stop()  # Stop execution until files are uploaded

    elif customer_df.empty:
        # st.warning("Customer Address file is missing. Please upload it.")
        st.stop()

    elif pricing_rule_df.empty:
        # st.warning("Pricing Rule file is missing. Please upload it.")  
        st.stop()

    # If both files are uploaded, proceed with processing
    st.success("Files uploaded successfully! Processing data...")

    output_df = fill_customers_with_pricing_rule(customer_df, pricing_rule_df)
    st.success("Data processed successfully!")

    # Dowload file
    st.header("📎Exporting Results")

    st.markdown(
        """
            Check your **Downloads** folder.  
            The file's name is **`new_price_rule_file.csv`**.  
            Rename accordingly.
        """)

    if st.download_button(
        label = "Download Ready!",
        data = output_df.to_csv(index=False),
        file_name = "new_price_rule_file.csv",
        mime="text/csv"
    ):
        st.toast("Check Downloads folder! :ok_hand:")
    
