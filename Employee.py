import streamlit as st
import mysql.connector
import pandas as pd
import csv
import streamlit_book as stb
import datetime
from datetime import date

mydb = mysql.connector.connect(host="localhost",user = "root",password = "msdmsdmsd",database="ems")
c=mydb.cursor()

st.markdown('<p style="font-family:serif; color:#05445E;font-size:40px;text-align:center;"><b>Employees</b></p>',unsafe_allow_html=True)
st.caption("This page is accessible by Employees only. Employees can view their personal details, leave details, final salaries ,apply for leave/WFH ,check leave/WFH Status and give feedback. Employees must enter their credentials in the sidebar to access all the features")
if 'login' not in st.session_state:
    st.session_state['login']=False
    
st.sidebar.text("Enter Employee Credentials below")
uid = st.sidebar.text_input("Enter User ID: ")
pwd = st.sidebar.text_input("Enter Password: ",type="password")
btn=st.sidebar.button("Login")
if btn:
    c.execute("select * from emp_login")
    for row in c:
        if (row[1]==uid and row[2]==pwd):
            st.session_state['login']=True
            break
    if(not st.session_state['login']):
        st.sidebar.text("Incorrect ID or Password")
if st.session_state['login']:
    btn3 = st.sidebar.button("Logout")
    if btn3:
        st.session_state['login']=False
        st.experimental_rerun()
    st.sidebar.text("Login Successful")
    choice2 = st.selectbox("Employee Features",("None","Final Salary", "Employee Details","View Leaves","Apply for Leave/WFH", "Check Leave/WFH Status","Feedback Form"))
    if(choice2=="Final Salary"):
        st.markdown('<p style="font-family:serif; color:#05445E;font-size:31px;text-align:center;border-style: solid;"><b>Final Salary Details</b></p>',unsafe_allow_html=True)
        eid = st.text_input("Enter Employee ID: ").title()
        btn = st.button("Enter")
        if btn:
            c.execute("select * from salary")
            m=[]
            for row in c:
                if(row[0]==eid):
                    m.append(row)
                    break
            df1 = pd.DataFrame(m,columns=["Employee ID","Monthly Salary","LOPS Leaves","Deduction","Bonus","Final Salary"])
            st.dataframe(df1)
    if (choice2 == "Employee Details"):
        st.markdown('<p style="font-family:serif; color:#05445E;font-size:31px;text-align:center;border-style: solid;"><b>Employee Details</b></p>',unsafe_allow_html=True)
        eid = st.text_input("Enter Employee ID: ").title()
        btn = st.button("Enter")
        if btn:
            c.execute("select * from employee")
            s = []
            for row in c:
                if(row[0]==eid):
                    s.append(row)
                    df2 = pd.DataFrame(s, columns=["Employee ID", "Name", "Gender", "DOB", "Mobile No.","Department Id","Role Name", "Monthly Salary"])
                    st.dataframe(df2)
    if(choice2=="View Leaves"):
        st.markdown('<p style="font-family:serif; color:#05445E;font-size:31px;text-align:center;border-style: solid;"><b>Leave Details</b></p>',unsafe_allow_html=True)
        eid = st.text_input("Enter Employee ID: ").title()
        btn = st.button("Enter")
        if btn:
            c.execute("select * from leaves")
            k=[]
            for row in c:
                if(row[1]==eid):
                    k.append(row)
            df3 = pd.DataFrame(k, columns=["Leave ID", "Employee ID", "Leave Date", "Leave Type", "Deduction","Amount Deducted"])
            st.dataframe(df3)
    if(choice2=="Feedback Form"):
        st.markdown('<p style="font-family:serif; color:#05445E;font-size:31px;text-align:center;padding-top:25px;"><b>Feedback Form</b></p>',unsafe_allow_html=True)
        myform = st.form(key = 'form1')
        col1, col2 = st.columns(2)
        with col1:
            name = myform.text_input("Enter your name").title()
        with col2:
            emp_id = myform.text_input("Enter your Employee ID").title()
        message = myform.subheader("How satisfied are you with the following aspects")
        work_env = myform.select_slider(label = "WORK ENVIRONMENT",options = ("Very Unsatisfied","Unsatisfied","Neutral","Satisfied","Very Satisfied"),value = "Neutral")
        sen_lead = myform.select_slider(label = "RELATIONSHIP WITH MANAGEMENT",options = ("Very Unsatisfied","Unsatisfied","Neutral","Satisfied","Very Satisfied"),value = "Neutral")
        sal = myform.select_slider(label = "SALARY",options = ("Very Unsatisfied","Unsatisfied","Neutral","Satisfied","Very Satisfied"),value = "Neutral")
        inc = myform.select_slider(label = "INCENTIVES",options = ("Very Unsatisfied","Unsatisfied","Neutral","Satisfied","Very Satisfied"),value = "Neutral")
        grow = myform.select_slider(label = "GROWTH OPPORTUNITIES",options = ("Very Unsatisfied","Unsatisfied","Neutral","Satisfied","Very Satisfied"),value = "Neutral")
        work = myform.select_slider(label = "WORK LIFE BALANCE",options = ("Very Unsatisfied","Unsatisfied","Neutral","Satisfied","Very Satisfied"),value = "Neutral")
        over = myform.select_slider(label = "OVERALL SATISFACTION",options = ("Very Unsatisfied","Unsatisfied","Neutral","Satisfied","Very Satisfied"),value = "Neutral")
        sugg = myform.text_area(label = "Any more suggestions: ",max_chars = 200 )   
        submit = myform.form_submit_button()
        if submit:
            inputs = [name,emp_id,work_env,sen_lead,sal,inc,grow,work,over,sugg]
            f = open("C:/myproject/lms/Scripts/feedback.csv", 'a')
            writer = csv.writer(f)
            writer.writerow(inputs)
            f.close()
            st.markdown('<p style="font-family:serif; color:#05445E;font-size:25px;text-align:center;"><b>Feedback Form Submitted Succesfully</b></p>',unsafe_allow_html=True)
            


    if choice2=="Apply for Leave/WFH":
        st.markdown('<p style="font-family:serif; color:#05445E;font-size:31px;text-align:center;border-style: solid;"><b>Apply for Leave or WFH</b></p>',unsafe_allow_html=True)
        col1, col2,col3 = st.columns(3)
        with col1:
            name = st.text_input("Name: ").title()
        with col2:
            eid = st.text_input("Employee ID: ").title()
        with col3:
            dept = st.text_input("Department name: ").title()
        choice10 = st.selectbox("Apply for Leave or WFH",("Leave","Work From Home"))
        if choice10=="Leave":           
            col1, col2,col3 = st.columns(3)
            with col1:
                type = st.text_input("Leave Type").title()
            with col2:
                leave_from= st.date_input("Leave From ",min_value = datetime.datetime.now())
            with col3:
                to = st.date_input("Leave Till",min_value = datetime.datetime.now())
            reason = st.text_area("State the Reason for leave")
            status = "TBD"
            btn = st.button("Submit Application")
            if btn:
                iid = str(datetime.datetime.now())
                did = date.today()
                mydb = mysql.connector.connect(host="localhost",user = "root",password = "msdmsdmsd",database="ems")
                c=mydb.cursor()
                c.execute("insert into leave_app values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(iid,did,eid,name,dept,type,leave_from,to,reason,status))
                mydb.commit()
                st.markdown('<p style="font-family:serif; color:#05445E;font-size:18px;text-align:center;"><b>Applied for leave succesfully. We request you to wait for approval from higher authorities</b></p>',unsafe_allow_html=True)

        if choice10=="Work From Home":
            col3,col4 = st.columns(2)
            with col3:
                wfh_from= st.date_input("WFH From: ",min_value = datetime.datetime.now())
            with col4:
                wfh_till= st.date_input("WFH Till: ",min_value = datetime.datetime.now())
            reason1 = st.text_area("Reason for WFH")
            status = "TBD"
            btn1 = st.button("Submit Application")
            if btn1:
                iid1 = str(datetime.datetime.now())
                did1 = date.today()
                c.execute("insert into wfh_app values(%s,%s,%s,%s,%s,%s,%s,%s,%s)",(iid1,did1,eid,name,dept,wfh_from,wfh_till,reason1,status))
                mydb.commit()
                st.markdown('<p style="font-family:serif; color:#05445E;font-size:18px;text-align:center;"><b>Applied for WFH succesfully. We request you to wait for approval from higher authorities</b></p>',unsafe_allow_html=True)



            

    if choice2=="Check Leave/WFH Status":
        st.markdown('<p style="font-family:Cartwheel; color:#05445E;font-size:18px;text-align:center;border-style: solid;border-width: 2px;"><b>Check Leave/WFH Status</b></p>',unsafe_allow_html=True)
        col3,col4=st.columns(2)
        m1 = col3.checkbox("Leave Status")      
        m2 = col4.checkbox("WFH Status")
        if m1:
            st.markdown('<p style="font-family:Cartwheel; color:#05445E;font-size:18px;text-align:center;border-style: solid;border-width: 2px;"><b>Check Leave Status</b></p>',unsafe_allow_html=True)
            col1, col2 = st.columns(2)
            with col1:
                name = st.text_input("Enter Name").title()
            with col2:
                date = st.date_input("Select Date on which you applied for leave",datetime.date(2023,1,1))
            btn = st.button("Check")
            if btn:
                c.execute("select * from leave_app where emp_name=%s and app_date=%s;", (name, date,))
                l=[]
                for row in c:
                    l.append(row)
                df9 = pd.DataFrame(l, columns=["Application Time", "Application Date", "Employee ID", "Employee Name","Department name","Leave Type","Leave from","Leave till","Reason","Leave Status"])
                if len(l)==0:
                    st.subheader("Incorrect Name or Application Date")
                else:
                    st.dataframe(df9)
                txt=df9["Leave Status"].values
                if txt == "Approved":
                    st.markdown('<p style="font-family:serif; color:#05445E;font-size:40px;text-align:center;"><b>Leave Status : Approved</b></p>',unsafe_allow_html=True)
                    st.balloons()
                elif txt == "Disapproved":
                    st.markdown('<p style="font-family:serif; color:#05445E;font-size:40px;text-align:center;"><b>Leave Status : Disapproved</b></p>',unsafe_allow_html=True)
                elif txt == "TBD":
                    st.markdown('<p style="font-family:serif; color:#05445E;font-size:40px;text-align:center;"><b>Leave Status : TBD</b></p>',unsafe_allow_html=True)
        
        if m2:
            st.markdown('<p style="font-family:Cartwheel; color:#05445E;font-size:18px;text-align:center;border-style: solid;border-width: 2px;"><b>Check WFH Status</b></p>',unsafe_allow_html=True)
            col1, col2 = st.columns(2)
            with col1:
                name = st.text_input("Enter Name").title()
            with col2:
                date = st.date_input("Select Date on which you applied for WFH",datetime.date(2023,1,1))
            btn = st.button("Check")
            if btn:
                c.execute("select * from wfh_app where emp_name=%s and app_date=%s;", (name, date,))
                l=[]
                for row in c:
                    l.append(row)
                df9 = pd.DataFrame(l, columns=["Application Time", "Application Date", "Employee ID", "Employee Name","Department name","Leave from","Leave till","Reason","WFH Status"])
                if len(l)==0:
                    st.subheader("Incorrect Name or Application Date")
                else:
                    st.dataframe(df9)
                txt=df9["WFH Status"].values
                if txt == "Approved":
                    st.markdown('<p style="font-family:serif; color:#05445E;font-size:40px;text-align:center;"><b>WFH Status : Approved</b></p>',unsafe_allow_html=True)
                    st.balloons()
                elif txt == "Disapproved":
                    st.markdown('<p style="font-family:serif; color:#05445E;font-size:40px;text-align:center;"><b>WFH Status : Disapproved</b></p>',unsafe_allow_html=True)
                elif txt == "TBD":
                    st.markdown('<p style="font-family:serif; color:#05445E;font-size:40px;text-align:center;"><b>WFH Status : TBD</b></p>',unsafe_allow_html=True)               










