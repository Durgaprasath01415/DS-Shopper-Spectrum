import streamlit as st
st.set_page_config(
    layout="wide",
    initial_sidebar_state="expanded"
)
pages = {
    "Menu" : [
        st.Page("pages/product_recommedation.py", title="Product Recommedation",icon =":material/filter_alt:"),
        st.Page("pages/customer_segmentation.py", title="Malnutrition Analysis",icon =":material/filter_alt:"),
    ]
}
pg = st.navigation(pages)
pg.run()