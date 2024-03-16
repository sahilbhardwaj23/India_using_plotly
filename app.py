import streamlit as st
import numpy as np
import pandas as pd
import plotly.express as px

st.set_page_config(layout='wide')

df = pd.read_csv('india.csv')

list_of_states = list(df['State'].unique())
list_of_states.insert(0, 'Overall India')

st.title("Interactive Data Visualization of Socio-Economic Indicators in India")

st.write(
    "Our project aims to provide an interactive platform for exploring key socio-economic indicators across different states of India."
    " Leveraging the power of Plotly, a Python library for interactive data visualization, users can dynamically select specific states"
    " or the entire country and compare various socio-economic parameters such as population, household with internet access, literacy rate, and sex ratio."
    "The interface begins with a user-friendly selection menu allowing users to choose between individual states or the aggregated data for the entire country."
    "Upon selection, users can then pick any two out of the three parameters: population, household with internet access, literacy rate, and sex ratio."
    "Once the inputs are chosen, Plotly generates an interactive graph that dynamically visualizes the relationship between the selected parameters."
    "Users can hover over data points to view detailed information and explore the trends and patterns across different states or regions."
    "This project serves as a valuable tool for policymakers, researchers, and anyone interested in understanding the socio-economic landscape of India."
    "By providing an intuitive interface and dynamic visualization capabilities, it facilitates deeper insights and informed decision-making regarding socio-economic "
    "development initiatives."
)

visualization_placeholder = st.empty()

if st.sidebar.button('Go to Visualization'):
    selected_state = st.sidebar.selectbox('Select a state', list_of_states)
    primary = st.sidebar.selectbox('Select Primary Parameter', sorted(df.columns[5:]))
    secondary = st.sidebar.selectbox('Select Secondary Parameter', sorted(df.columns[5:]))

    plot = st.sidebar.button('Plot Graph')

    if plot:
        st.text('Size represent primary parameter')
        st.text('Color represents secondary parameter')
        if selected_state == 'Overall India':
            # plot for india
            fig = px.scatter_mapbox(df, lat="Latitude", lon="Longitude", size=primary, color=secondary, zoom=4,
                                    size_max=35,
                                    mapbox_style="carto-positron", width=1200, height=700, hover_name='District')

            visualization_placeholder.plotly_chart(fig, use_container_width=True)
        else:
            # plot for state
            state_df = df[df['State'] == selected_state]

            fig = px.scatter_mapbox(state_df, lat="Latitude", lon="Longitude", size=primary, color=secondary, zoom=6,
                                    size_max=35,
                                    mapbox_style="carto-positron", width=1200, height=700, hover_name='District')

            visualization_placeholder.plotly_chart(fig, use_container_width=True)
