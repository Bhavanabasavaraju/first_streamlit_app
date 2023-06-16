import streamlit

streamlit.title('Hello')

streamlit.header('Breakfast Menu')
streamlit.text('Omega 3 and Bluberry Oatmeal')
streamlit.text('kale, spinach and Rocket Smoothie')
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')
import pandas

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)
streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index))
