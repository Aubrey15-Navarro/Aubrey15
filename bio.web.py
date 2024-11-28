import streamlit as st
from PIL import Image
from streamlit_option_menu import option_menu

st.set_page_config(page_title="Biography Manager", layout="wide")

if "biographies" not in st.session_state:
    st.session_state["biographies"] = []

default_biography = {
    "name": "Aubrey Sarah B. Navarro",
    "age": 19,
    "sex": "Female",
    "intro": "Hello! My name is Aubrey Sarah B. Navarro, and I am a first-year student currently pursuing my studies in Bachelor of Science in Computer Engineering at Surigao del Norte State University. I am passionate about improving programming skills and problem-solving, and I am eager to explore and grow both academically and personally during this exciting phase of my education. I enjoy participating in activities and practicing pronunciation, like doing tongue twisters, and I look forward to contributing to my school community while learning as much as I can.",
    "bio": "Just live up your life.",
    "hobby/s": ["Reading, Listening to Music"],
    "mother_name": "Ennelene B. Navarro",
    "mother_occupation": "Housewife",
    "father_name": "Bonifacio L. Navarro",
    "father_occupation": "Driver",
    "elementary_school": "San Jose Elementary School",
    "high_school": "San Jose National High School",
    "college": "Surigao del Norte State University",
    "course": "Bachelor of Science in Computer Engineering (BSCpE)",
    "other_schools": ["STI College Surigao"],
    "activities": ["Interactive Technology", "Reading and Writing Activities"],
    "accomplishments": ["With Honors in Elementary", "With Honors in High Schhol", "Youth Member in Catholic Church", "SSG President in Elementary", "Classroom Secretary Officer", "Winning in Suduko", "2nd Place in Microscope Contest during Science Month in Elementary"],
    "contact_no": "09120646240",
    "email_address": "aubreysarahbullonavarro35@gmail.com",
    "address": "Barangay San Jose, Surigao City",
    "image": None,
}

if not st.session_state["biographies"]:
    st.session_state["biographies"].append(default_biography)

with st.sidebar:
    selected = option_menu(
        "Main Menu",
        ["Add Biography", "View Biographies"],
        icons=["person-plus", "list-task"],
        menu_icon="menu-app",
        default_index=0,
    )

def display_biography(bio):
    st.subheader(f"👤 {bio['name']} ({bio['age']} years old)")
    if bio.get("image"):
        st.image(bio["image"], caption="Profile Picture", width=150)
    st.write(f"**Sex:** {bio['sex']}")
    st.write(f"**Introduction:** {bio['intro']}")
    st.write(f"**Bio:** {bio['bio']}")
    st.write(f"**Hobby/s:** {bio['hobby/s']}")
    st.write("### 👨‍👩‍👧 Parents Information")
    st.write(f"**Mother:** {bio['mother_name']} ({bio['mother_occupation']})")
    st.write(f"**Father:** {bio['father_name']} ({bio['father_occupation']})")
    st.write("### 🎓 Educational Background")
    st.write(f"**Elementary School:** {bio['elementary_school']}")
    st.write(f"**High School:** {bio['high_school']}")
    st.write(f"**College:** {bio['college']}")
    st.write(f"**Course:** {bio['course']}")
    st.write(f"**Other Schools:** {', '.join(bio.get('other_schools', []))}")
    st.write("### 📝 Educational Activities")
    for activity in bio.get("activities", []):
        st.write(f"- {activity}")
    st.write(f"**Accomplishments:** {bio['accomplishments']}")
    st.write("### 📞 Contact Information")
    st.write(f"**Phone:** {bio['contact_no']}")
    st.write(f"**Email Address:** {bio['email_address']}")
    st.write(f"**Address:** {bio['address']}")

if selected == "Add Biography":
    st.title("📖 Add a New Biography")
    with st.form("bio_form"):
        st.header("👤 Personal Information")
        uploaded_image = st.file_uploader("Upload Profile Picture", type=["jpg", "jpeg", "png"])
        name = st.text_input("Full Name *")
        age = st.number_input("Age *", min_value=0, step=1)
        sex = st.selectbox("Sex", ["Male", "Female", "Other"])
        intro = st.text_area("Introduction About Yourself")
        bio = st.text_area("Bio")
        hobby = st.text_input("Hobby/s")

        st.header("👨‍👩‍👧 Parents' Information")
        mother_name = st.text_input("Mother's Name")
        mother_occupation = st.text_input("Mother's Occupation")
        father_name = st.text_input("Father's Name")
        father_occupation = st.text_input("Father's Occupation")

        st.header("🎓 Educational Background")
        elementary_school = st.text_input("Elementary School")
        high_school = st.text_input("High School")
        college = st.text_input("College")
        course = st.text_input("Course")
        other_schools = st.text_area("Other Schools (comma-separated)").split(",")

        st.header("📝 Educational Activities")
        activities = st.text_area("Educational Activities (one per line)").split("\n")
        accomplishments = st.text_input("Accomplishments")

        st.header("📞 Contact Information")
        contact_no = st.text_input("Contact No.")
        email_address = st.text_input("Email Address")
        address = st.text_input("Address")

        submitted = st.form_submit_button("Add Biography")
        if submitted:
            if not name or not age:
                st.error("Full Name and Age are required!")
            else:
                bio_entry = {
                    "name": name,
                    "age": age,
                    "sex": sex,
                    "intro": intro,
                    "bio": bio,
                    "mother_name": mother_name,
                    "mother_occupation": mother_occupation,
                    "father_name": father_name,
                    "father_occupation": father_occupation,
                    "elementary_school": elementary_school,
                    "high_school": high_school,
                    "college": college,
                    "course": course,
                    "other_schools": [school.strip() for school in other_schools if school.strip()],
                    "activities": [activity.strip() for activity in activities if activity.strip()],
                    "accomplishments": accomplishments,
                    "contact_no": contact_no,
                    "email_address": email_address,
                    "address": address,
                    "image": Image.open(uploaded_image) if uploaded_image else None,
                }
                st.session_state["biographies"].append(bio_entry)
                st.success(f"Biography for {name} added successfully!")

elif selected == "View Biographies":
    st.title("📜 View Biographies")
    if st.session_state["biographies"]:
        for i, bio in enumerate(st.session_state["biographies"]):
            with st.expander(f"Biography {i + 1}: {bio['name']}"):
                display_biography(bio)
    else:
        st.write("No biographies available. Please add one!")
