import streamlit as st
import pandas as pd
import json
from main import MarketResearchAssistant

def display_comparison_table(data):
    # Convert the comparison list to a DataFrame
    df = pd.DataFrame(data['comparison'])
    
    # Set the category as the index
    df.set_index('category', inplace=True)
    
    # Add some styling
    st.title("Product Comparison Analysis")
    
    # Create three columns for filters
    col1, col2, col3 = st.columns(3)
    
    with col1:
        show_narsi = st.checkbox('Show Narsi', value=True)
    with col2:
        show_copilot = st.checkbox('Show GitHub Copilot', value=True)
    with col3:
        show_cursor = st.checkbox('Show Cursor', value=True)
    
    # Filter columns based on checkboxes
    columns_to_show = []
    if show_narsi:
        columns_to_show.append('Narsi')
    if show_copilot:
        columns_to_show.append('GitHub Copilot')
    if show_cursor:
        columns_to_show.append('Cursor')
    
    # Display the filtered DataFrame
    st.dataframe(
        df[columns_to_show],
        use_container_width=True,
        height=400,
    )
    
    # Add a download button
    csv = df.to_csv()
    st.download_button(
        label="Download comparison as CSV",
        data=csv,
        file_name="product_comparison.csv",
        mime="text/csv",
    )

    # Display individual category details
    st.subheader("Category Details")
    for category in df.index:
        with st.expander(category):
            category_data = df.loc[category]
            for product, value in category_data.items():
                if product in columns_to_show:
                    st.write(f"**{product}:** {value}")

# Usage
if __name__ == "__main__":
    flow = MarketResearchAssistant()
    comparison_data = flow.kickoff()  

    data = json.loads(comparison_data)
    
    display_comparison_table(data) 