import streamlit as st


def homepage():
    # title
    st.markdown(
    "<h1 style='text-align: center;'>PRICE RULE LOADER</h1>",
    unsafe_allow_html=True
    )

    # about
    st.markdown(
        """
        <div style="background-color: #E7F3FF; padding: 10px; border-radius: 10px;">
            <h4>Overview</h4>
        </div>
        """, 
        unsafe_allow_html=True
    )
    st.write("")

    st.write("This program generates new pricing rule with associated effective time frame for several customers. Main users are Pricing Team members.")

    st.write("")
    st.write("")

    # instruction
    st.markdown(
        """
        <div style="background-color: #E7F3FF; padding: 10px; border-radius: 10px;">
            <h4>Quickstart</h4>
        </div>
        """, 
        unsafe_allow_html=True
    )
    st.write("")
    st.write(
        """
        **What you need**
        - A **Customer Address** Excel file contains a column named "Customers #" or "SLSHAN"
        - A **Price Rule** Excel file contains 10 columns with neccessary information (see Price Rule Loader page)

        **Instruction**
        - Go to *📂 Price Rule Loader* from Navigation
        - Either use *Browse files* button or *drag-and-drop* your files to the Upload file drop box
        - Download and review results 
        """
    )