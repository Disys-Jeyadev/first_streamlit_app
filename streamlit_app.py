import pandas
import streamlit 
import requests
import snowflake.connector
import URLError

streamlit.title("My MOM's New Healthy Dinner") 
streamlit.header('Breakfast Favorites')
streamlit.text('🥣 Omega 3 & Blueberry Oatmeal')
streamlit.text('🥗 Kale, Spinach & Rocket Smoothie')
streamlit.text('🐔 Hard-Boiled Free-Range Egg')
streamlit.text('🥑🍞 Avcoda Toast')
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')
# Let's put a pick list here so they can pick the fruit they want to include 
fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index))
fruits_to_show = my_fruit_list.loc[fruits_selected]
streamlit.dataframe(fruits_to_show)
streamlit.header("Fruityvice Fruit Advice!")
try:
  fruit_choice = streamlit.text_input('What fruit would you like information about?')
  if not fruit_choice:
      streamlit.error("Please select a fruit to get information.")
  else:
      streamlit.write('The user entered ', fruit_choice)
      fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" +fruit_choice)
      fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
      streamlit.dataframe(fruityvice_normalized)
 expect URLError as e:
  streamlit.error()
# my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
# my_cur = my_cnx.cursor()
# my_cur.execute('select * from "PC_RIVERY_DB"."PUBLIC"."FRUIT_LOAD_LIST";')
# my_data_row = my_cur.fetchall()
# streamlit.text("THE FRUIT LOAD LIST CONTAINS: ")
# streamlit.dataframe(my_data_row)
# add_my_fruit = streamlit.text_input('What fruit would you like to add ?')
# streamlit.write('Thanks for adding ', add_my_fruit)
# my_cur.execute('insert into "PC_RIVERY_DB"."PUBLIC"."FRUIT_LOAD_LIST" values("from strealit")';
