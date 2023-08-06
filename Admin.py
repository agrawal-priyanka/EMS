import streamlit as st
import mysql.connector
import pandas as pd
import csv
import datetime
st.markdown('<p style="font-family:Cartwheel; color:#05445E;font-size:40px;text-align:center;"><b>Admin</b></p>',unsafe_allow_html=True)
st.caption("This page is accessible by admins only. Admins can update, add, delete employee's details, leave details, salary details, job roles and departments. Admins must need to enter their credentials in the sidebar.")

mydb = mysql.connector.connect(host="localhost",user = "root",password = "msdmsdmsd",database="ems")
c=mydb.cursor()
if 'alogin' not in st.session_state:
        st.session_state['alogin']=False
st.sidebar.text("Enter Admin Credentials below")
uid1 = st.sidebar.text_input("Enter User ID: ")
pwd1 = st.sidebar.text_input("Enter Password: ",type="password")
btn=st.sidebar.button("Login")
if btn:
    c.execute("select * from adm_login")
    for row in c:
        if (row[0]==uid1 and row[1]==pwd1):
            st.session_state['alogin']=True
            break
    if(not st.session_state['alogin']):
        st.sidebar.text("Incorrect ID or Password")
if st.session_state['alogin']:
    btn3 = st.sidebar.button("Logout")
    if btn3:
        st.session_state['alogin']=False
        st.experimental_rerun()
    st.sidebar.text("Login Successful")
    choice3 = st.selectbox("Admin Features", ("None", "Employee Details","Final Salaries","Leaves","Work from Home Applications","Job Roles" ,"Departments"))
    if(choice3=="Final Salaries"):
        col1,col2,col3,col4=st.columns(4)
        m1 = col1.checkbox("View")      
        m2 = col2.checkbox("Add")    
        m3= col3.checkbox("Update")
        m4 = col4.checkbox("Delete")

        #choice4 = st.selectbox("Features",("None","View Salaries","Add Salary","Update Salary","Delete Salary"))
        if m1:
            st.markdown('<p style="font-family:Cartwheel; color:#05445E;font-size:18px;text-align:center;border-style: solid;border-width: 2px;"><b>View Salary Records</b></p>',unsafe_allow_html=True)
            c.execute("select * from salary")
            z = []
            for row in c:
                z.append(row)
            df4 = pd.DataFrame(z, columns=["Employee ID","Monthly Salary","LOPS Leaves","Deduction","Bonus","Final Salary"])
            st.dataframe(df4)
        if m2:
            st.markdown('<p style="font-family:Cartwheel; color:#05445E;font-size:18px;text-align:center;border-style: solid;border-width: 2px;"><b>Add Salary Record</b></p>',unsafe_allow_html=True)
            col1,col2=st.columns(2)
            with col1:
                eid1 = st.text_input("Enter Employee ID:").title()
            with col2:
                ms = st.text_input("Enter Monthly Salary:")
            col1,col2=st.columns(2)
            with col1:
                lop = st.text_input("Enter no. of LOPS Leaves:")
            with col2:
                d1 = st.text_input("Enter Deduction Amount (if any):")
            col1,col2=st.columns(2)
            with col1:
                b1 = st.text_input("Enter Bonus (if given):")
            with col2:
                fs = st.text_input("Enter Final salary:")
            btn = st.button("Add Salary")
            if btn:
                c.execute("insert into salary values(%s,%s,%s,%s,%s,%s",(eid1,ms,lop,d1,b1,fs,))
                mydb.commit()
                st.subheader("Salary Details Added Succesfully")
        if m3:
            st.markdown('<p style="font-family:Cartwheel; color:#05445E;font-size:18px;text-align:center;border-style: solid;border-width: 2px;"><b>Update Salary Record</b></p>',unsafe_allow_html=True)
            choice5=st.selectbox("Update",("None","Monthly Salary","LOPS Leaves","Deduction","Bonus","Final Salary"))
            if choice5=="Monthly Salary":
                eid=st.text_input("Enter Employee ID")
                ms=st.text_input("Enter Updated Salary")
                btn=st.button("Update Salary")
                if btn:
                    c.execute("update salary set month_sal=%s where emp_id=%s",(ms,eid,))
                    mydb.commit()
                    st.header("Salary Updated Succesfully")
            if choice5=="LOPS Leaves":
                eid=st.text_input("Enter Employee ID")
                ls=st.text_input("Enter Updated LOPS leaves")
                btn=st.button("Update LOPS Leaves")
                if btn:
                    c.execute("update salary set lops=%s where emp_id=%s",(ls,eid,))
                    mydb.commit()
                    st.header("LOPS Leaves Updated")
            if choice5=="Deduction":
                eid=st.text_input("Enter Employee ID")
                ded=st.text_input("Enter Updated Deduction")
                btn=st.button("Update Deductions")
                if btn:
                    c.execute("update salary set deduction=%s where emp_id=%s",(ded,eid,))
                    mydb.commit()
                    st.header("Deduction Updated Succesfully")
            if choice5=="Bonus":
                eid=st.text_input("Enter Employee's ID:")
                bs=st.text_input("Enter Updated Salary")
                btn=st.button("Update Bonus")
                if btn:
                    c.execute("update salary set bonus=%s where emp_id=%s",(bs,eid,))
                    mydb.commit()
                    st.header("Bonus Updated")
            if choice5=="Final Salary":
                eid=st.text_input("Enter Employee ID")
                fs=st.text_input("Enter Updated Final Salary")
                btn=st.button("Update Final Salary")
                if btn:
                    c.execute("update salary set final_sal=%s where emp_id=%s",(fs,eid,))
                    mydb.commit()
                    st.header("Fianl Salary Updated")
        if m4:
            st.markdown('<p style="font-family:Cartwheel; color:#05445E;font-size:18px;text-align:center;border-style: solid;border-width: 2px;"><b>Delete Salary Record</b></p>',unsafe_allow_html=True)
            eid1=st.text_input("Enter Employee's ID:")
            btn=st.button("Delete Salary")
            if btn:
                c.execute("delete from salary where emp_id=%s",(eid1,))
                mydb.commit()
                st.subheader("Salary Deleted")
    if (choice3 == "Employee Details"):
        st.write("You can View, Add, Update and Delete Employee Records")

        col1,col2,col3,col4=st.columns(4)
        m1 = col1.checkbox("View")      
        m2 = col2.checkbox("Add")    
        m3= col3.checkbox("Update")
        m4 = col4.checkbox("Delete")

        if m1 : # View
               
            st.markdown('<p style="font-family:Cartwheel; color:#05445E;font-size:18px;text-align:center;border-style: solid;border-width: 2px;"><b>View Employee Records</b></p>',unsafe_allow_html=True)
            c.execute("select * from employee")
            x = []
            for row in c:
                x.append(row)
            df5 = pd.DataFrame(x, columns=["Employee ID", "Name", "Gender", "DOB", "Mobile No.","Department Id","Role Name", "Monthly Salary"])
            st.dataframe(df5)
        if m2:
            st.markdown('<p style="font-family:Cartwheel; color:#05445E;font-size:18px;text-align:center;border-style: solid;border-width: 2px;"><b>Add Employee Record</b></p>',unsafe_allow_html=True)
            col3,col4 = st.columns(2)
            with col3:
                eid2 = st.text_input("Employee ID: ")
            with col4:
                ename = st.text_input("Employee Name: ").title()
            col1,col2 = st.columns(2)
            with col1:
                egen = st.text_input("Gender:")
            with col2:
                dob = st.date_input("Date of Birth: ",datetime.date(1990,1,1))
            col1,col2 = st.columns(2)
            with col1:
                mno = st.text_input("Contact details: ")
            with col2:
                dep = st.text_input("Department Id: ")
            col1,col2 = st.columns(2)
            with col1:
                role = st.text_input("Job role:").title()
            with col2:
                msal = st.text_input("Monthly Salary:")
            btn4= st.button("Add Employee Details:")
            if btn4:
                c.execute("insert into employee values(%s,%s,%s,%s,%s,%s,%s,%s)",(eid2,ename,egen,dob,mno,dep,role,msal))
                mydb.commit()
                st.subheader("Employee Details added succesfully")
        if (m4):
            st.markdown('<p style="font-family:Cartwheel; color:#05445E;font-size:18px;text-align:center;border-style: solid;border-width: 2px;"><b>Delete Employee Record</b></p>',unsafe_allow_html=True)
            eid3 = st.text_input("Enter Employee ID").title()
            btn5 = st.button("Delete Record")
            if btn5:
                c.execute("delete from employee where emp_id = %s",(eid3,))
                mydb.commit()
                st.subheader("Employee Details deleted successfully")
        if m3:
            st.markdown('<p style="font-family:Cartwheel; color:#05445E;font-size:18px;text-align:center;border-style: solid;border-width: 2px;"><b>Update Employee Record</b></p>',unsafe_allow_html=True)
            choice7= st.selectbox("Select one to Update",("Employee Name","Gender","Date of Birth","Contact Details","Department ID","Job Role","Monthly Salary"))
            if choice7=="Employee Name":
                eid4 = st.text_input("Enter Employee ID:").title()
                ename1 = st.text_input("Enter Employee's name:").title()
                btn6 = st.button("Update Name")
                if btn6:
                    c.execute("update employee set name=%s where emp_id = %s", (ename1,eid4,))
                    mydb.commit()
                    st.subheader("Employee name updated successfully")
            if choice7=="Gender":
                eid4 = st.text_input("Enter Employee ID:").title()
                gen = st.text_input("Enter Gender:").title()
                btn6 = st.button("Update Gender")
                if btn6:
                    c.execute("update employee set gender=%s where emp_id = %s", (gen, eid4,))
                    mydb.commit()
                    st.subheader("Employee gender Updated")
            if choice7 == "Date of Birth":
                eid4 = st.text_input("Enter Employee ID: ").title()
                dob1 = st.date_input("Enter Date of Birth ",datetime.date(1995,1,1))
                btn6 = st.button("Update")
                if btn6:
                    c.execute("update employee set dob=%s where emp_id = %s", (dob1, eid4,))
                    mydb.commit()
                    st.subheader("Employee's DOB Updated")
            if choice7 == "Contact Details":
                eid4 = st.text_input("Enter Employee ID:").title()
                con = st.text_input("Enter Contact Number")
                btn6 = st.button("Update")
                if btn6:
                    c.execute("update employee set Mob_no=%s where emp_id = %s", (con, eid4,))
                    mydb.commit()
                    st.subheader("Employee's contact number Updated")
            if choice7 == "Department ID":
                eid4 = st.text_input("Enter Employee ID: ").title()
                did = st.text_input("Enter Department ID:").title()
                btn6 = st.button("Update")
                if btn6:
                    c.execute("update employee set dept_id=%s where emp_id = %s", (did, eid4,))
                    mydb.commit()
                    st.subheader("Employee's dept. id Updated")
            if choice7 == "Job Role":
                eid4 = st.text_input("Enter Employee ID:").title()
                jb = st.text_input("Enter Job Role:").title()
                btn6 = st.button("Update")
                if btn6:
                    c.execute("update employee set role_name=%s where emp_id = %s", (jb, eid4,))
                    mydb.commit()
                    st.subheader("Employee's Job Role Updated")
            if choice7 == "Monthly Salary":
                eid4 = st.text_input("Enter Employee Id ").title()
                ms1 = st.text_input("Enter Enter Monthly Salary")
                btn6 = st.button("Update")
                if btn6:
                    c.execute("update employee set month_sal=%s where emp_id = %s", (ms1, eid4,))
                    mydb.commit()
                    st.subheader("Employee's Salary Updated")


    if (choice3 == "Leaves"):
        choice8=st.selectbox("Features",("None","Alter Leave Records", "Leave Applications"))
        if choice8=="Alter Leave Records":
            col1,col2,col3,col4=st.columns(4)
            m1 = col1.checkbox("View")      
            m2 = col2.checkbox("Add")    
            m3= col3.checkbox("Update")
            m4 = col4.checkbox("Delete")
            if m1:
                st.markdown('<p style="font-family:Cartwheel; color:#05445E;font-size:18px;text-align:center;border-style: solid;border-width: 2px;"><b>View Leave Records</b></p>',unsafe_allow_html=True)
                c.execute("select * from leaves")
                l = []
                for row in c:
                    l.append(row)
                df7 = pd.DataFrame(l, columns=["Leave ID", "Employee ID", "Leave Date", "Leave Type", "Deduction","Amount Deducted"])
                st.dataframe(df7)
            if m2:
                st.markdown('<p style="font-family:Cartwheel; color:#05445E;font-size:18px;text-align:center;border-style: solid;border-width: 2px;"><b>Add Leave Record</b></p>',unsafe_allow_html=True)
                col1,col2 = st.columns(2)
                with col1:
                    lid = st.text_input("Enter Leave ID ").title()
                with col2:
                    eid = st.text_input("Enter Employee ID ").title()
                col1,col2 = st.columns(2)
                with col1:
                    ldate = st.date_input("Enter Leave Date ",datetime.date(2023,1,1))
                with col2:
                    ltype = st.text_input("Enter Leave Type ").title()
                col1,col2 = st.columns(2)
                with col1:
                    ded = st.text_input("Enter Deduction (Y/N)").title()
                with col2:
                    ad = st.text_input("Enter Deduction Amount ")
                btn = st.button("Add Leave")
                if btn:
                    mydb = mysql.connector.connect(host="localhost", user="root", password="msdmsdmsd", database="ems")
                    c = mydb.cursor()
                    c.execute("insert into leaves values( %s,%s,%s,%s,%s,%s)",(lid,eid,ldate,ltype,ded,ad,))
                    mydb.commit()
                    st.subheader("Leave Added Succesfully")
            if m3:
                st.markdown('<p style="font-family:Cartwheel; color:#05445E;font-size:18px;text-align:center;border-style: solid;border-width: 2px;"><b>Update Leave Records</b></p>',unsafe_allow_html=True)
                choice9=st.selectbox("Update",("Employee ID","Leave Date","Leave Type","Deduction (Y/N)","Amount Deducted"))
                if choice9 == "Employee ID":
                    lid= st.text_input("Enter Leave ID").title()
                    eid = st.text_input("Enter Employee ID").title()
                    btn=st.button("Update")
                    if btn:
                        c.execute("update leaves set emp_id=%s where leave_id=%s",(eid,lid,))
                        mydb.commit()
                        st.subheader("Employee ID Updated")
                if choice9 == "Leave Date":
                    lid = st.text_input("Enter Leave ID").title()
                    date = st.date_input("Enter Leave Date",datetime.date(2023,1,1))
                    btn = st.button("Update")
                    if btn:
                        c.execute("update leaves set leave_date=%s where leave_id=%s", (date, lid,))
                        mydb.commit()
                        st.subheader("Leave Date Updated")
                if choice9 == "Leave Type":
                    lid = st.text_input("Enter Leave ID").title()
                    lt = st.text_input("Enter Leave Type").title()
                    btn = st.button("Update")
                    if btn:
                        c.execute("update leaves set leave_type=%s where leave_id=%s", (lt, lid,))
                        mydb.commit()
                        st.subheader("Leave Type Updated")
                if choice9 == "Deduction (Y/N)":
                    lid = st.text_input("Enter Leave ID").title()
                    ded = st.text_input("Enter Deduction(Y/N)").title()
                    btn = st.button("Update")
                    if btn:
                        c.execute("update leaves set deduction=%s where leave_id=%s", (ded, lid,))
                        mydb.commit()
                        st.subheader("Deduction Updated")
                if choice9 == "Amount Deducted":
                    lid = st.text_input("Enter Leave ID").title()
                    amt = st.text_input("Enter Amount to be deducted")
                    btn = st.button("Update")
                    if btn:
                        c.execute("update leaves set amount=%s where leave_id=%s", (amt, lid,))
                        mydb.commit()
                        st.subheader("Amount Updated")
            if m4:
                st.markdown('<p style="font-family:Cartwheel; color:#05445E;font-size:18px;text-align:center;border-style: solid;border-width: 2px;"><b>Delete Leave Record</b></p>',unsafe_allow_html=True)
                lid=st.text_input("Enter Leave ID").title()
                btn = st.button("Delete")
                if btn:
                    c.execute("delete from leaves where leave_id=%s",(lid,))
                    mydb.commit()
                    st.subheader("Leave Deleted")

        if choice8=="Leave Applications":
            col1,col2=st.columns(2)
            m1 = col1.checkbox("View Leave Applications")      
            m2 = col2.checkbox("Grant Leaves")
            
            if m1:
                st.markdown('<p style="font-family:Cartwheel; color:#05445E;font-size:18px;text-align:center;border-style: solid;border-width: 2px;"><b>View Leave Applications</b></p>',unsafe_allow_html=True)
                c.execute("select * from leave_app")
                l = []
                for row in c:
                    l.append(row)
                df7 = pd.DataFrame(l, columns=["Application Time", "Application Date", "Employee ID", "Employee Name","Department name","Leave Type","Leave from","Leave till","Reason","Leave Status"])
                st.dataframe(df7)
            if m2:
                st.markdown('<p style="font-family:Cartwheel; color:#05445E;font-size:18px;text-align:center;border-style: solid;border-width: 2px;"><b>Grant Leave</b></p>',unsafe_allow_html=True)
                lid = st.text_input("Enter Application Time Here")
                ded = st.text_input("Enter Leave Status (Approved/Disapproved/TBD)").title()
                btn = st.button("Update")
                if btn:
                    c.execute("update leave_app set leave_status=%s where app_time=%s", (ded, lid,))
                    mydb.commit()
                    st.subheader("Leave Status Updated")
                    
    if choice3=="Work from Home Applications":
        col1,col2=st.columns(2)
        m1 = col1.checkbox("View WFH Applications")      
        m2 = col2.checkbox("Grant WFH")
        if m1:
            st.markdown('<p style="font-family:Cartwheel; color:#05445E;font-size:18px;text-align:center;border-style: solid;border-width: 2px;"><b>View WFH Applications</b></p>',unsafe_allow_html=True)
            c.execute("select * from wfh_app")
            l = []
            for row in c:
                l.append(row)
            df8 = pd.DataFrame(l, columns=["Application Time", "Application Date", "Employee ID", "Employee Name","Department name","WFH from","WFH till","Reason","WFH Status"])
            st.dataframe(df8)
        if m2:
            st.markdown('<p style="font-family:Cartwheel; color:#05445E;font-size:18px;text-align:center;border-style: solid;border-width: 2px;"><b>Grant WFH</b></p>',unsafe_allow_html=True)
            lid = st.text_input("Enter Application Time Here")
            ded = st.text_input("Enter WFH Status (Approved/Disapproved/TBD)").title()
            btn = st.button("Update")
            if btn:
                c.execute("update wfh_app set wfh_status=%s where app_time=%s", (ded, lid,))
                mydb.commit()
                st.subheader("WFH Status Updated")
        
            


    if (choice3 == "Job Roles"):
        choice10=st.selectbox("Features",("None","View all Job Roles","Add New Job Role"))
        if choice10=="View all Job Roles":
            c.execute("select * from role")
            m = []
            for row in c:
                m.append(row)
            df8 = pd.DataFrame(m, columns=["Role ID", "Department ID", "Role Name", "Filled/Vacant", "Employee ID"])
            st.dataframe(df8)
        if (choice10 == "Add New Job Role"):
            rid = st.text_input("Enter Role ID ").title()
            did = st.text_input("Enter Department ID ").title()
            rname = st.text_input("Enter Role Name").title()
            fv = st.text_input("Enter if the Job role is Filled(fi) or Vacant(V)").title()
            ed = st.text_input("Enter Employee ID").title()
            btn = st.button("Add Job Role")
            if btn:
                c.execute("insert into role values( %s,%s,%s,%s,%s)",(rid,did,rname,fv,ed,))
                mydb.commit()
                st.subheader("Job Role Added Succesfully")

    if (choice3 == "Departments"):
        c.execute("select * from dept")
        d = []
        for row in c:
            d.append(row)
        df9 = pd.DataFrame(d, columns=["Department ID","Department Name"])
        st.dataframe(df9)
