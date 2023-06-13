import numpy as np
import pickle

loaded_model = pickle.load(open("C:/Users\DELL/Desktop/Fake-News-Detection-using-Machine-Learning-master/trained_model.pkl","rb"))

X_new = ['dhaka reuters bangladesh myanmar agreed monday set joint working group repatriation rohingya muslim refugee fled bangladesh foreign minister abul hassan mahmood ali told reporters talks myanmar official looking forward peaceful solution crisis ali said talks myanmar government official kyaw tint swe half million rohingya refugees myanmar fled neighboring bangladesh late august escape united nations branded ethnic cleansing myanmar s military']
#X_news = [X_new]
prediction = loaded_model.predict(X_new)
print(prediction)

if(prediction[0]== 'true' ):
    print("The new is Real")
else:
    print("The new is Fake")