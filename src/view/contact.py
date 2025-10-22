import streamlit as st


def contact():
    st.markdown(
    "<h1 style='text-align: center;'>📩 Contact</h2>",
    unsafe_allow_html=True
    )

    # bug report
    # st.markdown(
    # """
    # <div style="background-color: #FFF3CD; padding: 10px; border-radius: 10px;">
    #     <h4>🐞 Report an Issue</h4>
    #     <p>Please submit an <a href='https://app.smartsheet.com/b/form/ef9a89f1a3ec44fa89c98176c1924401'>Analytics Request</a>.</p>
    # </div>
    # """, 
    # unsafe_allow_html=True
    # )

    # st.write("")
    # st.write("")

    # feedback
    st.markdown(
        """
        <div style="background-color: #E7F3FF; padding: 10px; border-radius: 10px;">
            <h4>💬 For Feedback and Questions</h4>
            <p>Get in touch with Mia Pham at <a href='mailto:nguyen.pham@cornerstone.com'>nguyen.pham@cornerstone.com</a></p>
        </div>
        """, 
        unsafe_allow_html=True
    )
