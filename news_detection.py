import numpy as np
import pickle
import streamlit as st
import time
import pywhatkit as kt


#Loding the saved model
loaded_model = pickle.load(open("C:/Users\DELL/Desktop/Fake-News-Detection-using-Machine-Learning-master/trained_model.pkl","rb"))

#Creating a function for Prediction

def news_prediction(input_data):

    prediction = loaded_model.predict(input_data)
    print(prediction)

    if(prediction[0]== 'true' ):
       return "The news is Real"
    else: 
       return "The news is Fake"


   
def google_search(query):
   import pandas as pd
   df=pd.read_csv("C:\\Users\\DELL\\Desktop\\Project\\News.csv")
   row=df.loc[df['text']==query]['title'].values[0]
   st.info("Please wait for few mininutes, You will be redirected to another page for information regarding to this news.")
   bar=st.progress(0)
   for i in range(1,100,20):
      bar.progress(i)
      time.sleep(2)
   kt.search(row)
      

def main(): 
   #Flag variable
   flag=False
   with st.sidebar:
      #giving a title 
      st.title('Check if News is real or fake!')

      #getting the input data from users
      Title=st.text_area('News Title',key="title") 
      
      if 'NewsTitle' not in st.session_state:   
         st.session_state.NewsTitle = ''

      def submit():   
         st.session_state.NewsTitle = st.session_state.title
         st.session_state.title = ''
         
      st.button("Clear",on_click=submit)
               
      #code for Predection
      detection = ''

      #creating a button for detection
      if st.button('Detect the News'):
         if (Title == ""):
            #st.write("Please Enter some text in text box")
            st.warning('Please Enter some text in text box', icon="⚠️")
         else:
            detection = news_prediction([Title]) 
            progress_text = "Operation in progress. Please wait."
            my_bar = st.progress(0, text=progress_text)
            for percent_complete in range(100):   
               time.sleep(0.1)
            my_bar.progress(percent_complete + 1, text=progress_text)
            flag=True
            
   if detection == 'The news is Fake':
      st.error(detection)
   elif detection == 'The news is Real':
      st.success(detection)
      
   if flag:
      print(google_search(Title))
   else:
      st.warning("Please click on detect the news")




if __name__ == '__main__':
   main()