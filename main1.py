import streamlit as st
import pandas as pd

# Dummy user data for each role
users = {
    "student": {"username": "student", "password": "student123"},
    "company": {"username": "company", "password": "company123"},
    "admin": {"username": "admin", "password": "admin123"}
}
def landing_page():
    st.title("Welcome to Career Management Portal")

    # Display image (you can adjust the path based on your file location)
    st.image("career.jpg", caption="Career Management System")

    st.write("This is the landing page of the Career Management Portal. Explore different features to manage your career.")
    
    # You can continue with your existing login or other page elements here

# Call the landing page function
landing_page()
# Session state to track login
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
    st.session_state.role = None

def login_page(role):
    st.title(f"{role.capitalize()} Login")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        if username == users[role]["username"] and password == users[role]["password"]:
            st.session_state.logged_in = True
            st.session_state.role = role
            st.success("Login successful!")
            st.rerun()
        else:
            st.error("Invalid credentials!")

def student_page():
    st.title("Student Dashboard")
    menu = st.sidebar.selectbox("Student Menu", [
        "Apply for Job",
        "View Job Status",
        "Search Job",
        "Update Details",
        "Change Password"
    ])

    if menu == "Apply for Job":
        st.subheader("Apply for a Job")
        job_id = st.text_input("Enter Job ID")
        resume = st.file_uploader("Upload your Resume", type=["pdf", "docx"])
        if st.button("Submit Application"):
            if job_id and resume:
                st.success(f"Applied to job ID {job_id} successfully!")
            else:
                st.warning("Please enter job ID and upload resume.")

    elif menu == "View Job Status":
        st.subheader("Your Job Applications")
        # Dummy data
        st.table({
            "Job ID": ["101", "102"],
            "Company": ["ABC Corp", "XYZ Ltd"],
            "Status": ["Pending", "Accepted"]
        })

    elif menu == "Search Job":
        st.subheader("Search for Jobs")
        keyword = st.text_input("Search by keyword (e.g., developer, data)")
        location = st.text_input("Location")
        if st.button("Search"):
            st.info(f"Showing jobs for '{keyword}' in '{location}'")
            # Dummy results
            st.write("1. Frontend Developer - ABC Corp")
            st.write("2. Data Analyst - XYZ Ltd")

    elif menu == "Update Details":
        st.subheader("Update Your Details")
        name = st.text_input("Full Name")
        email = st.text_input("Email")
        phone = st.text_input("Phone Number")
        if st.button("Update"):
            st.success("Details updated successfully!")

    elif menu == "Change Password":
        st.subheader("Change Password")
        old_pwd = st.text_input("Old Password", type="password")
        new_pwd = st.text_input("New Password", type="password")
        confirm_pwd = st.text_input("Confirm New Password", type="password")
        if st.button("Change"):
            if new_pwd == confirm_pwd and old_pwd:
                st.success("Password changed successfully!")
            else:
                st.error("Passwords do not match or old password is empty.")


def company_page():
    st.title("🏢 Company Dashboard")

    menu = ["View Applications", "Post Job", "Update Details", "Change Password"]
    choice = st.sidebar.selectbox("Select Action", menu)

    if choice == "View Applications":
        st.subheader("📄 Applications Received")
        # Sample data
        applications = pd.DataFrame({
            "Student Name": ["Tanmay", "Aisha"],
            "Job ID": [101, 101],
            "Resume Link": ["link1.pdf", "link2.pdf"],
            "Status": ["Pending", "Reviewed"]
        })
        st.table(applications)

    elif choice == "Post Job":
        st.subheader("📝 Post a New Job")
        with st.form("post_job"):
            job_title = st.text_input("Job Title")
            description = st.text_area("Job Description")
            location = st.text_input("Location")
            last_date = st.date_input("Last Date to Apply")
            submit = st.form_submit_button("Post Job")

            if submit:
                # Here you can save to a database or CSV
                st.success(f"Job '{job_title}' posted successfully!")

    elif choice == "Update Details":
        st.subheader("🔧 Update Company Details")
        with st.form("update_details"):
            name = st.text_input("Company Name")
            email = st.text_input("Email")
            phone = st.text_input("Phone Number")
            submit = st.form_submit_button("Update")

            if submit:
                st.success("Details updated successfully!")

    elif choice == "Change Password":
        st.subheader("🔒 Change Password")
        with st.form("change_password"):
            current_pwd = st.text_input("Current Password", type="password")
            new_pwd = st.text_input("New Password", type="password")
            confirm_pwd = st.text_input("Confirm New Password", type="password")
            submit = st.form_submit_button("Change Password")

            if submit:
                if new_pwd == confirm_pwd:
                    st.success("Password changed successfully!")
                else:
                    st.error("Passwords do not match.")


def admin_page():
    st.title("🛠️ Admin Dashboard")

    menu = ["Manage Students", "Manage Companies", "Update Details", "Feedback", "Reports"]
    choice = st.sidebar.selectbox("Select Action", menu)

    # Manage Students
    if choice == "Manage Students":
        st.subheader("👨‍🎓 Manage Students")
        # Sample data for students
        students = pd.DataFrame({
            "Student Name": ["Tanmay", "Aisha"],
            "Roll Number": ["S101", "S102"],
            "Email": ["tanmay@example.com", "aisha@example.com"],
            "Status": ["Active", "Inactive"]
        })
        st.table(students)

        # Options to manage student data
        action = st.selectbox("Select Action", ["Add Student", "Remove Student", "Update Student"])
        if action == "Add Student":
            with st.form("add_student"):
                name = st.text_input("Student Name")
                email = st.text_input("Email")
                status = st.selectbox("Status", ["Active", "Inactive"])
                submit = st.form_submit_button("Add Student")
                if submit:
                    st.success(f"Student '{name}' added successfully!")
        elif action == "Remove Student":
            student_name = st.selectbox("Select Student to Remove", students["Student Name"])
            if st.button("Remove"):
                st.success(f"Student '{student_name}' removed successfully!")
        elif action == "Update Student":
            student_name = st.selectbox("Select Student to Update", students["Student Name"])
            with st.form("update_student"):
                new_name = st.text_input("New Student Name")
                new_email = st.text_input("New Email")
                new_status = st.selectbox("New Status", ["Active", "Inactive"])
                submit = st.form_submit_button("Update Student")
                if submit:
                    st.success(f"Student '{student_name}' updated successfully!")

    # Manage Companies
    elif choice == "Manage Companies":
        st.subheader("🏢 Manage Companies")
        # Sample data for companies
        companies = pd.DataFrame({
            "Company Name": ["ABC Corp", "XYZ Ltd"],
            "Email": ["abc@example.com", "xyz@example.com"],
            "Location": ["New York", "San Francisco"],
            "Status": ["Active", "Inactive"]
        })
        st.table(companies)

        # Options to manage company data
        action = st.selectbox("Select Action", ["Add Company", "Remove Company", "Update Company"])
        if action == "Add Company":
            with st.form("add_company"):
                name = st.text_input("Company Name")
                email = st.text_input("Email")
                location = st.text_input("Location")
                status = st.selectbox("Status", ["Active", "Inactive"])
                submit = st.form_submit_button("Add Company")
                if submit:
                    st.success(f"Company '{name}' added successfully!")
        elif action == "Remove Company":
            company_name = st.selectbox("Select Company to Remove", companies["Company Name"])
            if st.button("Remove"):
                st.success(f"Company '{company_name}' removed successfully!")
        elif action == "Update Company":
            company_name = st.selectbox("Select Company to Update", companies["Company Name"])
            with st.form("update_company"):
                new_name = st.text_input("New Company Name")
                new_email = st.text_input("New Email")
                new_location = st.text_input("New Location")
                new_status = st.selectbox("New Status", ["Active", "Inactive"])
                submit = st.form_submit_button("Update Company")
                if submit:
                    st.success(f"Company '{company_name}' updated successfully!")

    # Update Admin Details
    elif choice == "Update Details":
        st.subheader("🔧 Update Admin Details")
        with st.form("update_details"):
            admin_name = st.text_input("Admin Name")
            admin_email = st.text_input("Admin Email")
            admin_phone = st.text_input("Admin Phone")
            submit = st.form_submit_button("Update Admin Details")
            if submit:
                st.success("Admin details updated successfully!")

    # Feedback Section
    elif choice == "Feedback":
        st.subheader("📢 Feedback")
        feedback = st.text_area("Provide your feedback")
        if st.button("Submit Feedback"):
            st.success("Feedback submitted successfully!")

    # Reports Section
    elif choice == "Reports":
        st.subheader("📊 Generate Reports")
        report_type = st.selectbox("Select Report Type", ["Student Report", "Company Report"])
        if report_type == "Student Report":
            # Placeholder for student report data
            st.write("Generating Student Report...")
            st.table(pd.DataFrame({
                "Student Name": ["Tanmay", "Aisha"],
                "Roll Number": ["S101", "S102"],
                "Status": ["Active", "Inactive"]
            }))
        elif report_type == "Company Report":
            # Placeholder for company report data
            st.write("Generating Company Report...")
            st.table(pd.DataFrame({
                "Company Name": ["ABC Corp", "XYZ Ltd"],
                "Location": ["New York", "San Francisco"],
                "Status": ["Active", "Inactive"]
            }))

# Sidebar selection for login role
if not st.session_state.logged_in:
    role = st.sidebar.selectbox("Login as", ["Select", "student", "company", "admin"])
    if role != "Select":
        login_page(role)
else:
    if st.session_state.role == "student":
        student_page()
    elif st.session_state.role == "company":
        company_page()
    elif st.session_state.role == "admin":
        admin_page()

    if st.button("Logout"):
        st.session_state.logged_in = False
        st.session_state.role = None
        st.rerun()

