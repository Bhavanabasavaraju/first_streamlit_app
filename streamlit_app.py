import streamlit

streamlit.title('Hello')

streamlit.header('Breakfast Menu')
streamlit.text('Omega 3 and Bluberry Oatmeal')
streamlit.text('kale, spinach and Rocket Smoothie')
streamlit.text('Rice, spinach and Rocket Smoothie')
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')



import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')


fruits_selected = streamlit.multiselect("pick some fruits:", list(my_fruit_list.index),['avocado','strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]


streamlit.dataframe(fruits_to_show)
