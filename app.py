import streamlit as st
import numpy as np
import pandas as pd
import plotly.express as px
from streamlit_option_menu import option_menu
st.set_page_config(layout='wide')
from PIL import Image

def main():
    st.title('How work environments affect employees')
    @st.cache
    def data_reader():
        hr_data = pd.read_excel('HR_DATA.xlsx')
        return hr_data
    hr_data = data_reader()
    
    with st.sidebar:

        selected = option_menu("Main Menu", ["Home", 'Data', 'EDA'], 
            icons=['house', 'calculator-fill', 'eyeglasses'], menu_icon="cast", default_index=0)

    if selected == 'Home':
        st.subheader('Impact of company environment on employees')
        st.write('It should be known that factors such as salary of an employee affects their satisfaction levels which may lead to either positive or negative growth of a company.')
        work_image = Image.open('salary.jpg')
        st.image(work_image, caption='An employee receiving their salary')


    elif selected == 'Data':
        st.subheader('HR dataset')
        st.write(hr_data)

    elif selected == 'EDA':
        st.subheader('Visualisations for deeper understanding using sample data from company XYZ')
        
        container = st.container()
        
        with container:
            st.subheader('A boxplot showing how salary affects satisfaction levels based on example departments')
            fig = px.box(data_frame = hr_data, x = 'Department', y = 'satisfaction_level', color = 'salary', color_discrete_sequence=['blue', 'orange', 'green'])
            st.plotly_chart(fig)

        with container:
            st.subheader('A bar chart showing how salary affects satisfaction levels in general')
            df1 = hr_data.groupby('salary')[['satisfaction_level']].mean().round(2)
            fig = px.bar(df1, x = df1.index, y = 'satisfaction_level', text = 'satisfaction_level', height = 500, width = 400, color_discrete_sequence=['darkblue'], title = 'How salary is related to employee satisfaction levels')
            fig.update_traces(textposition = 'outside')
            st.plotly_chart(fig)

        with container:
            st.subheader('Pie chart showing how satisfaction levels affect employee work time')
            fig = px.pie(hr_data, names = 'salary', values = 'satisfaction_level', width = 500, height = 400, title=('Pie chart showing how salary affects employee work time'))
            st.plotly_chart(fig)


if __name__ == '__main__':
    main()