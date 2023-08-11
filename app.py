import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly as plo
from plotly import graph_objs as go
from plotly import offline as po
from sklearn.linear_model import LinearRegression
import numpy as np
import time

data=pd.read_csv("Salary_Data.csv")
st.title("SALARY PREDICTOR")
l=["HOME","PREDICTION","CONTRIBUTE"]
st.sidebar.header("NAVIGATION")
val=st.sidebar.radio("Go To",l)

lr=LinearRegression()
x=np.array(data["YearsExperience"]).reshape(-1,1)
y=np.array(data["Salary"]).reshape(-1,1)
lr.fit(x,y)

if(val=="HOME"):
    st.image("bgg1.jpg")
    if st.checkbox("showTable"):
        st.table(data)

    i=st.selectbox("GRAPH TYPE",["INTERACTIVE","NON INTERACTIVE"])
    ex=st.slider("filter the years of experience",0,20)
    data=data.loc[ex<=data["YearsExperience"]]

    if(i=="NON INTERACTIVE"):
        plt.figure(figsize=(10,5))
        plt.scatter(data["YearsExperience"],data["Salary"])
        plt.ylim(0)
        plt.xlabel("YearsExperience")
        plt.ylabel("Salary")
        plt.tight_layout()
        st.pyplot()
    if(i=="INTERACTIVE"):
        layout=go.Layout(
            xaxis=dict(range=[0,16]),
            yaxis=dict(range=[0,210000])
        )
        f=go.Figure(data=go.Scatter(x=data["YearsExperience"],y=data["Salary"],mode="markers"),
                    layout=layout)
        st.plotly_chart(f)

        
        
        


if(val=="PREDICTION"):
    st.image("money.png")
    st.title("PREDICT YOUR SALARY")
    value=st.number_input("ENTER YOUR EXPERIENCE",0,25)
    value=np.array(value).reshape(-1,1)
    p=lr.predict(value)
    
    if(st.button("PREDICT")):
        pro=st.progress(0)
        for i in range(100):
            time.sleep(0.01)
            pro.progress(i+1)
        time.sleep(0.05)
        
        st.success(f"YOUR PREDICTED SALARY IS {int(p)}")



if(val=="CONTRIBUTE"):
    st.header("CONTRIBUTE")
    exp=st.number_input("ENTER THE EXP",0,20)
    age=st.number_input("ENTER THE AGE",0,60)
    sal=st.number_input("ENTER YOUR SALARY",0,2000000,step=1000)
    if(st.button("submit")):
        add={"YearsExperience":[exp],"Age":[age],"Salary":[sal]}
        add=pd.DataFrame(add)
        add.to_csv("Salary_Data.csv",mode='a',header=False,index=False)
        st.success("Submitted")