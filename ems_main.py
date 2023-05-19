import mysql.connector
import streamlit as st
import pandas as pd
st.set_page_config(page_title="Employee Management System")
st.title("Employee Management System")
choice = st.sidebar.selectbox("Menu",("Home", "Employee","Admin"))
st.header(choice)
if(choice=="Home"):
    st.image('https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTO3ZZCmRTehEnxgQdoxpc4cPDdalg5hvvIGPLH1xTfTg&usqp=CAU&ec=48665701')
if(choice=="Employee"):
    if 'login' not in st.session_state:
        st.session_state['login']=False
    uid = st.text_input("Enter User ID: ")
    pwd = st.text_input("Enter Password: ")
    btn=st.button("Login")
    if btn:
        mydb = mysql.connector.connect(host="localhost",user = "root",password = "msdmsdmsd",database="ems")
        c=mydb.cursor()
        c.execute("select * from emp_login")
        for row in c:
            if (row[1]==uid and row[2]==pwd):
                st.session_state['login']=True
                break
        if(not st.session_state['login']):
            st.header("Incorrect ID or Password")
    if st.session_state['login']:
        btn3 = st.button("Logout")
        if btn3:
            st.session_state['login']=False
            st.experimental_rerun()
        st.header("Login Successful")
        choice2 = st.selectbox("Features", ("Final Salary", "Employee Details","Leaves"))
        if(choice2=="Final Salary"):
            eid = st.text_input("Enter Employee ID: ")
            btn = st.button("Enter")
            if btn:
                mydb = mysql.connector.connect(host="localhost", user="root", password="msdmsdmsd", database="ems")
                c= mydb.cursor()
                c.execute("select * from salary")
                m=[]
                for row in c:
                    if(row[0]==eid):
                        m.append(row)
                        break
                df1 = pd.DataFrame(m,columns=["Employee ID","Monthly Salary","LOPS Leaves","Deduction","Bonus","Final Salary"])
                st.dataframe(df1)
        if (choice2 == "Employee Details"):
            eid = st.text_input("Enter Employee ID: ")
            mydb = mysql.connector.connect(host="localhost", user="root", password="msdmsdmsd", database="ems")
            c = mydb.cursor()
            c.execute("select * from employee")
            s = []
            for row in c:
                if(row[0]==eid):
                    s.append(row)
            df2 = pd.DataFrame(s, columns=["Employee ID", "Name", "Gender", "DOB", "Mobile No.","Department Id","Role Name", "Monthly Salary"])
            st.dataframe(df2)
        if(choice2=="Leaves"):
            eid = st.text_input("Enter Employee ID: ")
            mydb = mysql.connector.connect(host="localhost", user="root", password="msdmsdmsd", database="ems")
            c = mydb.cursor()
            c.execute("select * from leaves")
            k=[]
            for row in c:
                if(row[1]==eid):
                    k.append(row)
            df3 = pd.DataFrame(k, columns=["Leave ID", "Employee ID", "Leave Date", "Leave Type", "Deduction","Amount Deducted"])
            st.dataframe(df3)
if(choice=="Admin"):
    if 'alogin' not in st.session_state:
        st.session_state['alogin']=False
    uid1 = st.text_input("Enter User ID: ")
    pwd1 = st.text_input("Enter Password: ")
    btn=st.button("Login")
    if btn:
        mydb = mysql.connector.connect(host="localhost",user = "root",password = "msdmsdmsd",database="ems")
        c=mydb.cursor()
        c.execute("select * from adm_login")
        for row in c:
            if (row[0]==uid1 and row[1]==pwd1):
                st.session_state['alogin']=True
                break
        if(not st.session_state['alogin']):
            st.header("Incorrect ID or Password")
    if st.session_state['alogin']:
        btn3 = st.button("Logout")
        if btn3:
            st.session_state['alogin']=False
            st.experimental_rerun()
        st.header("Login Successful")
        choice3 = st.selectbox("Features", ("None", "Employee Details","Final Salaries","Leaves","Job Roles" ,"Departments"))
        if(choice3=="Final Salaries"):
            choice4 = st.selectbox("Features",("None","View Salaries","Add Salary","Update Salary","Delete Salary"))
            if choice4 == "View Salaries":
                mydb = mysql.connector.connect(host="localhost", user="root", password="msdmsdmsd", database="ems")
                c = mydb.cursor()
                c.execute("select * from salary")
                z = []
                for row in c:
                    z.append(row)
                df4 = pd.DataFrame(z, columns=["Employee ID","Monthly Salary","LOPS Leaves","Deduction","Bonus","Final Salary"])
                st.dataframe(df4)
            if (choice4 == "Add Salary"):
                eid1 = st.text_input("Enter Employee ID ")
                ms = st.text_input("Enter Monthly Salary ")
                lop = st.text_input("Enter no. of LOPS Leaves ")
                d1 = st.text_input("Enter Deduction Amount (if any) ")
                b1 = st.text_input("Enter Bonus (if given) ")
                fs = st.text_input("Enter Final salary ")
                btn = st.button("Add Salary")
                if btn:
                    mydb = mysql.connector.connect(host="localhost", user="root", password="msdmsdmsd", database="ems")
                    c = mydb.cursor()
                    c.execute("insert into salary values(%s,%s,%s,%s,%s,%s",(eid1,ms,lop,d1,b1,fs,))
                    mydb.commit()
                    st.subheader("Salary Details Added Succesfully")
            if (choice4=="Update Salary"):
                choice5=st.selectbox("Update",("None","Monthly Salary","LOPS Leaves","Deduction","Bonus","Final Salary"))
                if choice5=="Monthly Salary":
                    eid=st.text_input("Enter Employee ID")
                    ms=st.text_input("Enter Updated Salary")
                    btn=st.button("Update Salary")
                    if btn:
                        mydb = mysql.connector.connect(host="localhost", user="root", password="msdmsdmsd", database="ems")
                        c = mydb.cursor()
                        c.execute("update salary set month_sal=%s where emp_id=%s",(ms,eid,))
                        mydb.commit()
                        st.header("Salary Updated Succesfully")
                if choice5=="LOPS Leaves":
                    eid=st.text_input("Enter Employee ID")
                    ls=st.text_input("Enter Updated LOPS leaves")
                    btn=st.button("Update LOPS Leaves")
                    if btn:
                        mydb = mysql.connector.connect(host="localhost", user="root", password="msdmsdmsd", database="ems")
                        c = mydb.cursor()
                        c.execute("update salary set lops=%s where emp_id=%s",(ls,eid,))
                        mydb.commit()
                        st.header("LOPS Leaves Updated")
                if choice5=="Deduction":
                    eid=st.text_input("Enter Employee ID")
                    ded=st.text_input("Enter Updated Deduction")
                    btn=st.button("Update Deductions")
                    if btn:
                        mydb = mysql.connector.connect(host="localhost", user="root", password="msdmsdmsd", database="ems")
                        c = mydb.cursor()
                        c.execute("update salary set deduction=%s where emp_id=%s",(ded,eid,))
                        mydb.commit()
                        st.header("Deduction Updated Succesfully")
                if choice5=="Bonus":
                    eid=st.text_input("Enter Employee ID")
                    bs=st.text_input("Enter Updated Salary")
                    btn=st.button("Update Bonus")
                    if btn:
                        mydb = mysql.connector.connect(host="localhost", user="root", password="msdmsdmsd", database="ems")
                        c = mydb.cursor()
                        c.execute("update salary set bonus=%s where emp_id=%s",(bs,eid,))
                        mydb.commit()
                        st.header("Bonus Updated")
                if choice5=="Final Salary":
                    eid=st.text_input("Enter Employee ID")
                    fs=st.text_input("Enter Updated Final Salary")
                    btn=st.button("Update Final Salary")
                    if btn:
                        mydb = mysql.connector.connect(host="localhost", user="root", password="msdmsdmsd", database="ems")
                        c = mydb.cursor()
                        c.execute("update salary set final_sal=%s where emp_id=%s",(fs,eid,))
                        mydb.commit()
                        st.header("Fianl Salary Updated")
            if choice4=="Delete Salary":
                eid=st.text_input("Enter Employee ID ")
                btn=st.button("Delete Salary")
                if btn:
                    mydb = mysql.connector.connect(host="localhost", user="root", password="msdmsdmsd", database="ems")
                    c = mydb.cursor()
                    c.execute("delete from salary where emp_id=%s",(eid,))
                    mydb.commit()
                    st.subheader("Salary Deleted")
        if (choice3 == "Employee Details"):
            choice6 =st.selectbox("Features",("None","View All Employees","Add New Employee","Update Existing","Delete Employee"))
            if (choice6 == "View All Employees") :
                mydb = mysql.connector.connect(host="localhost", user="root", password="msdmsdmsd", database="ems")
                c = mydb.cursor()
                c.execute("select * from employee")
                x = []
                for row in c:
                    x.append(row)
                df5 = pd.DataFrame(x, columns=["Employee ID", "Name", "Gender", "DOB", "Mobile No.","Department Id","Role Name", "Monthly Salary"])
                st.dataframe(df5)
            if (choice6 == "Add New Employee"):
                eid2 = st.text_input("Enter Employee ID ")
                ename = st.text_input("Enter Employee Name ")
                egen = st.text_input("Enter Gender")
                dob = st.date_input("Enter Date of Birth ",datetime.date(1990,1,1))
                mno = st.text_input("Enter Contact details ")
                dep = st.text_input("Enter Department Id ")
                role = st.text_input("Enter Job role")
                msal = st.text_input("Enter Monthly Salary")
                btn4= st.button("Add Employee Details")
                if btn4:
                    mydb = mysql.connector.connect(host="localhost", user="root", password="msdmsdmsd", database="ems")
                    c = mydb.cursor()
                    c.execute("insert into employee values(%s,%s,%s,%s,%s,%s,%s,%s)",(eid2,ename,egen,dob,mno,dep,role,msal))
                    mydb.commit()
                    st.subheader("Employee Details added succesfully")
            if (choice6 == "Delete Employee"):
                eid3 = st.text_input("Enter Employee ID")
                btn5 = st.button("Delete")
                if btn5:
                    mydb = mysql.connector.connect(host="localhost", user="root", password="msdmsdmsd", database="ems")
                    c = mydb.cursor()
                    c.execute("delete from employee where emp_id = %s",(eid3,))
                    mydb.commit()
                    st.subheader("Employee Details deleted successfully")
            if (choice6 == "Update Existing"):
                choice7= st.selectbox("Update",("None","Employee Name","Gender","Date of Birth","Contact Details","Department ID","Job Role","Monthly Salary"))
                if choice7=="Employee Name":
                    eid4 = st.text_input("Enter Employee Id ")
                    ename1 = st.text_input("Enter Employee's name ")
                    btn6 = st.button("Update")
                    if btn6:
                        mydb = mysql.connector.connect(host="localhost", user="root", password="msdmsdmsd", database="ems")
                        c = mydb.cursor()
                        c.execute("update employee set name=%s where emp_id = %s", (ename1,eid4,))
                        mydb.commit()
                        st.subheader("Employee name updated successfully")
                if choice7 == "Gender":
                    eid4 = st.text_input("Enter Employee Id ")
                    gen = st.text_input("Enter Gender ")
                    btn6 = st.button("Update")
                    if btn6:
                        mydb = mysql.connector.connect(host="localhost", user="root", password="msdmsdmsd",database="ems")
                        c = mydb.cursor()
                        c.execute("update employee set gender=%s where emp_id = %s", (gen, eid4,))
                        mydb.commit()
                        st.subheader("Employee gender Updated")
                if choice7 == "Date of Birth":
                    eid4 = st.text_input("Enter Employee Id ")
                    dob1 = st.date_input("Enter Date of Birth ",datetime.date(1995,1,1))
                    btn6 = st.button("Update")
                    if btn6:
                        mydb = mysql.connector.connect(host="localhost", user="root", password="msdmsdmsd",database="ems")
                        c = mydb.cursor()
                        c.execute("update employee set dob=%s where emp_id = %s", (dob1, eid4,))
                        mydb.commit()
                        st.subheader("Employee's DOB Updated")
                if choice7 == "Contact Details":
                    eid4 = st.text_input("Enter Employee Id ")
                    con = st.text_input("Enter Contact Number")
                    btn6 = st.button("Update")
                    if btn6:
                        mydb = mysql.connector.connect(host="localhost", user="root", password="msdmsdmsd",database="ems")
                        c = mydb.cursor()
                        c.execute("update employee set Mob_no=%s where emp_id = %s", (con, eid4,))
                        mydb.commit()
                        st.subheader("Employee's contact number Updated")
                if choice7 == "Department ID":
                    eid4 = st.text_input("Enter Employee Id ")
                    did = st.text_input("Enter Department ID")
                    btn6 = st.button("Update")
                    if btn6:
                        mydb = mysql.connector.connect(host="localhost", user="root", password="msdmsdmsd",database="ems")
                        c = mydb.cursor()
                        c.execute("update employee set dept_id=%s where emp_id = %s", (did, eid4,))
                        mydb.commit()
                        st.subheader("Employee's dept. id Updated")
                if choice7 == "Job Role":
                    eid4 = st.text_input("Enter Employee Id ")
                    jb = st.text_input("Enter Job Role")
                    btn6 = st.button("Update")
                    if btn6:
                        mydb = mysql.connector.connect(host="localhost", user="root", password="msdmsdmsd",database="ems")
                        c = mydb.cursor()
                        c.execute("update employee set role_name=%s where emp_id = %s", (jb, eid4,))
                        mydb.commit()
                        st.subheader("Employee's Job Role Updated")
                if choice7 == "Monthly Salary":
                    eid4 = st.text_input("Enter Employee Id ")
                    ms1 = st.text_input("Enter Enter Monthly Salary")
                    btn6 = st.button("Update")
                    if btn6:
                        mydb = mysql.connector.connect(host="localhost", user="root", password="msdmsdmsd",database="ems")
                        c = mydb.cursor()
                        c.execute("update employee set month_sal=%s where emp_id = %s", (ms1, eid4,))
                        mydb.commit()
                        st.subheader("Employee's Salary Updated")


        if (choice3 == "Leaves"):
            choice8 = st.selectbox("Features", ("None", "View All Leaves", "Add New Leaves", "Update Existing Leaves", "Delete Leaves"))
            if choice8=="View All Leaves":
                mydb = mysql.connector.connect(host="localhost", user="root", password="msdmsdmsd", database="ems")
                c = mydb.cursor()
                c.execute("select * from leaves")
                l = []
                for row in c:
                    l.append(row)
                df7 = pd.DataFrame(l, columns=["Leave ID", "Employee ID", "Leave Date", "Leave Type", "Deduction","Amount Deducted"])
                st.dataframe(df7)
            if (choice8 == "Add New Leaves"):
                lid = st.text_input("Enter Leave ID ")
                eid = st.text_input("Enter Employee ID ")
                ldate = st.date_input("Enter Leave Date ",datetime.date(2023,1,1))
                ltype = st.text_input("Enter Leave Type ")
                ded = st.text_input("Enter Deduction (Y/N)")
                ad = st.text_input("Enter Deduction Amount ")
                btn = st.button("Add Leave")
                if btn:
                    mydb = mysql.connector.connect(host="localhost", user="root", password="msdmsdmsd", database="ems")
                    c = mydb.cursor()
                    c.execute("insert into leaves values( %s,%s,%s,%s,%s,%s)",(lid,eid,ldate,ltype,ded,ad,))
                    mydb.commit()
                    st.subheader("Leave Added Succesfully")
            if (choice8 == "Update Existing Leaves"):
                choice9=st.selectbox("Update",("Employee ID","Leave Date","Leave Type","Deduction (Y/N)","Amount Deducted"))
                if choice9 == "Employee ID":
                    lid= st.text_input("Enter Leave ID")
                    eid = st.text_input("Enter Employee ID")
                    btn=st.button("Update")
                    if btn:
                        mydb = mysql.connector.connect(host="localhost", user="root", password="msdmsdmsd",database="ems")
                        c = mydb.cursor()
                        c.execute("update leaves set emp_id=%s where leave_id=%s",(eid,lid,))
                        mydb.commit()
                        st.subheader("Employee ID Updated")
                if choice9 == "Leave Date":
                    lid = st.text_input("Enter Leave ID")
                    date = st.date_input("Enter Leave Date",datetime.date(2023,1,1))
                    btn = st.button("Update")
                    if btn:
                        mydb = mysql.connector.connect(host="localhost", user="root", password="msdmsdmsd", database="ems")
                        c = mydb.cursor()
                        c.execute("update leaves set leave_date=%s where leave_id=%s", (date, lid,))
                        mydb.commit()
                        st.subheader("Leave Date Updated")
                if choice9 == "Leave Type":
                    lid = st.text_input("Enter Leave ID")
                    lt = st.text_input("Enter Leave Type")
                    btn = st.button("Update")
                    if btn:
                        mydb = mysql.connector.connect(host="localhost", user="root", password="msdmsdmsd", database="ems")
                        c = mydb.cursor()
                        c.execute("update leaves set leave_type=%s where leave_id=%s", (lt, lid,))
                        mydb.commit()
                        st.subheader("Leave Type Updated")
                if choice9 == "Deduction (Y/N)":
                    lid = st.text_input("Enter Leave ID")
                    ded = st.text_input("Enter Leave Type")
                    btn = st.button("Update")
                    if btn:
                        mydb = mysql.connector.connect(host="localhost", user="root", password="msdmsdmsd", database="ems")
                        c = mydb.cursor()
                        c.execute("update leaves set deduction=%s where leave_id=%s", (ded, lid,))
                        mydb.commit()
                        st.subheader("Deduction Updated")
                if choice9 == "Amount Deducted":
                    lid = st.text_input("Enter Leave ID")
                    amt = st.text_input("Enter Amount to be deducted")
                    btn = st.button("Update")
                    if btn:
                        mydb = mysql.connector.connect(host="localhost", user="root", password="msdmsdmsd", database="ems")
                        c = mydb.cursor()
                        c.execute("update leaves set amount=%s where leave_id=%s", (amt, lid,))
                        mydb.commit()
                        st.subheader("Amount Updated")
            if choice8=="Delete Leaves":
                lid=st.text_input("Enter Leave ID")
                btn = st.button("Delete")
                if btn:
                    mydb = mysql.connector.connect(host="localhost", user="root", password="msdmsdmsd", database="ems")
                    c = mydb.cursor()
                    c.execute("delete from leaves where leave_id=%s",(lid,))
                    mydb.commit()
                    st.subheader("Leave Deleted")

        if (choice3 == "Job Roles"):
            choice10=st.selectbox("Features",("None","View all Job Roles","Add New Job Role"))
            if choice10=="View all Job Roles":
                mydb = mysql.connector.connect(host="localhost", user="root", password="msdmsdmsd", database="ems")
                c = mydb.cursor()
                c.execute("select * from role")
                m = []
                for row in c:
                    m.append(row)
                df8 = pd.DataFrame(m, columns=["Role ID", "Department ID", "Role Name", "Filled/Vacant", "Employee ID"])
                st.dataframe(df8)
            if (choice10 == "Add New Job Role"):
                rid = st.text_input("Enter Role ID ")
                did = st.text_input("Enter Department ID ")
                rname = st.text_input("Enter Role Name")
                fv = st.text_input("Enter if the Job role is Filled(fi) or Vacant(V)")
                ed = st.text_input("Enter Employee ID")
                btn = st.button("Add Job Role")
                if btn:
                    mydb = mysql.connector.connect(host="localhost", user="root", password="msdmsdmsd", database="ems")
                    c = mydb.cursor()
                    c.execute("insert into role values( %s,%s,%s,%s,%s)",(rid,did,rname,fv,ed,))
                    mydb.commit()
                    st.subheader("Job Role Added Succesfully")

        if (choice3 == "Departments"):
            mydb = mysql.connector.connect(host="localhost", user="root", password="msdmsdmsd", database="ems")
            c = mydb.cursor()
            c.execute("select * from dept")
            d = []
            for row in c:
                d.append(row)
            df9 = pd.DataFrame(d, columns=["Department ID","Department Name"])
            st.dataframe(df9)





        








