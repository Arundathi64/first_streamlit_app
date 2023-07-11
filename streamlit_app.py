import streamlit

streamlit.title("My Mom's New Healthy Diner")

streamlit.header('Breakfast Favorites')
streamlit.text('🥣Omega 3 and Blueberry oatmeal')
streamlit.text('🥗Kale and Spinach Smoothie')
streamlit.text('🐔Hard boiled freerange egg')
streamlit.text('🥑🍞Avacado toast')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

import pandas
my_fruit_list = pandas.read_csv(" https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')

#Let's put a pick list here so they can add the fruit they want to include
streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avacado','Strawberries'])

#Display the table on the page
streamlit.dataframe(my_fruit_list)
