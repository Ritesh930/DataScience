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
import time

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
chart = alt.Chart(df.reset_index()).mark_line().encode(x="index", y="a")

#chart=alt.chart(df.reset_index()).mark_line().encode(x="index",y="a")
st.altair_chart(chart,use_container_width=True)
fig , ax =plt.subplots()
ax.plot(df.index,df.a)
st.pyplot(fig)
st.divider()

#widgets
st.header("5.widgets")
with st.form("Input form: "):
    name=st.text_input("Enter your name:",type="password")
    age=st.number_input("Enter your age:")
    mood=st.radio("Select your mood",("happy","sad","neutral"))
    languages = st.multiselect("Select your language:", ["hindi", "english", "spanish", "french"])

    #languages=st.multiselect("select your language:","hindi","english","spanish","french")
    submit=st.form_submit_button("submit")
    if submit:
        st.success(f"Name:{name},Age:{age},Mood:{mood},Language:{languages}")

col1,col2,col3=st.columns([4,1,1])   #width to be managed
with col1:
    st.text_input("Enter your name:",type="password")
    st.number_input("Enter your age:")


with col2:
    st.radio("Select your mood",("happy","sad","neutral"))
    st.multiselect("Select your language:", ["hindi", "english", "spanish", "french"])


with col3:
    st.title("output")    
# submit=st.form_submit_button("submit")
# if submit:
#         st.success(f"Name:{name},Age:{age},Mood:{mood},Language:{languages}")    


col1,col2=st.columns(2)
with col1:
     number=st.slider("select a number",0,100)        
with col2:
     colour=st.color_picker("select the colour")

st.text_area("Enter your message")
st.date_input("Select a date")
st.time_input("select the time")
st.file_uploader("upload a file")     
st.divider()


st.header("6.media")
st.image("https://th.bing.com/th/id/OIP.nyLAzWYdvc-wb9ntq1cU7QHaHa?r=0&w=1080&h=1080&rs=1&pid=ImgDetMain",caption="Random image")


#slidebar and sidebar
st.sidebar.header("sidebar header")
st.sidebar.write("this is a sidebar text")
st.sidebar.button("click me")
option=st.sidebar.selectbox("select an option",("option 1","option 2","option 3"))


##
#tab1,tab2,tab3=st.tabs(["tab 1","tab 2","tab 3"])
with st.container():
    st.write("This is a container")

with st.expander("See explanation"):
    st.write("This is inside the expander")



with st.spinner("loading..."):
    time.sleep(10)
st.toast("toast message ",icon="👍")

st.page_link("https://marketplace.visualstudio.com/items?itemName=VisualStudioExptTeam.vscodeintellicode",label="streamlit website",icon="👍")

    


#file handeling
#generator and decortor
#multithreading and multiprocessing
#method overloading and overriding
#debug and unit testing

