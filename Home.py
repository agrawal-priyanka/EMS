import streamlit as st
import mysql.connector
import pandas as pd
import datetime
import csv
st.set_page_config(page_title="Employee Management System",layout = "centered")
st.markdown('<p style="font-family:Cartwheel; color:#05445E;font-size:50px;text-align:center;"><b>Employee Management System</b></p>',unsafe_allow_html=True)
st.markdown('<p style="font-family:Cartwheel; color:#05445E;font-size:30px;text-align:center;text-decoration: underline;"><b>Home Page</b></p>',unsafe_allow_html=True)
st.image('17564.jpg',width = 600)
