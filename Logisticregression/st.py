##streamlit app
#python library
# no req of html and css
#webpages for ml and data science projects
# import libraries


import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import altair as alt

st.set_page_config(page_title="Streamlit function demo",
                   page_icon="😎"
                   , layout="centered")

#title and text elements

st.title("Hello world") #title of the page
st.header("1.Text elements")  #text elements
st.subheader("markdown,code,latex") #text elements
st.write("**bold text**","italic text",'code text') #markdown text
st.code("print('hello world')", language='python') #hello world code
st.latex("E=mc^2")  #formula displaying
st.divider()  #horizontal line

#metrices and messages
st.header("2.metrices and messages")
st.metric(label="Revanue", value=1234, delta="+10%", delta_color="inverse")  #metric
st.error("This is an error message")  #error message
st.warning("This is a warning message")  #warning message   
st.info("This is an info message")  #info message
st.success("This is a success message")  #success message
#st.exception("This is an exception message")  #exception message
st.divider()  #horizontal line

#data display
st.header("3.Data display")
df=pd.DataFrame(np.random.randn(10, 3), columns=["a","b","c"])  #dataframe
st.dataframe(df) # data frame
st.table(df.head(3)) #
st.json(df.to_dict())  #


st.divider()


#chart and graphs

st.header("4.charts")
st.line_chart(df)
st.bar_chart(df)
st.area_chart(df)
chart=alt.chart(df.reset_index()).mark_line().encode(x="index",y="a")
st.altair_chart(chart,use_container_width=True)
fig , ax =plt.subplots()
ax.plot(df.index,df.a)
st.pyplot(fig)
st.divider()
