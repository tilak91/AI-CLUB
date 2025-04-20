import streamlit as st
import pandas as pd

# Page setup
st.set_page_config(page_title="AI Club Hub", layout="wide")

# Header Section
st.title("🤖 AI Club Platform")
st.markdown("""
    Welcome to the **AI Club Hub**! 🚀  
    Explore resources, learning paths, career opportunities, fun activities, and connect with our amazing members.  
    Let's innovate and grow together! 🌟
""")

# Tab navigation
tabs = st.tabs(["Resources", "Learning Paths", "Career Resources", "Fun Activities", "Members", "Events", "Contact Us"])

# Tab 1 - Resources
with tabs[0]:
    st.header("📚 AI Resources")
    st.markdown("""
        Discover some of the best resources to kickstart or advance your AI journey:
    """)
    st.markdown("- [Entire Resources](https://www.mltut.com/best-resources-to-learn-artificial-intelligence/?form=MG0AV3)")
    st.markdown("- [Intel Dataset Classification](https://github.com/Jean-BaptisteAC/Intel-Dataset-Classification/)")
    st.markdown("- [Deep Learning Basics (Colab)](https://colab.research.google.com/github/lexfridman/mit-deep-learning/blob/master/tutorial_deep_learning_basics/deep_learning_basics.ipynb#:~:text=At%20a%20high%2Dlevel%2C%20neural,useful%20infomation%20from%20those%20representations/)")

# Tab 2 - Learning Paths
with tabs[1]:
    st.header("🛣️ AI Learning Paths")
    st.markdown("Choose your learning path based on your experience level:")
    col1, col2, col3 = st.columns(3)

    with col1:
        st.subheader("👶 Beginner")
        st.markdown("- [Microsoft AI For Beginners](https://github.com/microsoft/AI-For-Beginners)")
        st.markdown("- [Machine Learning Fundamentals](https://github.com/amusi/awesome-ai-awesomeness)")

    with col2:
        st.subheader("🧑‍💻 Intermediate")
        st.markdown("- [Deep Learning Specialization](https://www.datakwery.com/post/fundamentals-of-nlp-guide/)")
        st.markdown("- [Computer Vision](https://www.geeksforgeeks.org/computer-vision//)")

    with col3:
        st.subheader("🧠 Advanced")
        st.markdown("- [Reinforcement Learning](https://github.com/AMAI-GmbH/AI-Expert-Roadmap)")
        st.markdown("- [Transfer Learning](https://www.tensorflow.org/tutorials/images/classification)")

# Tab 3 - Career Resources
with tabs[2]:
    st.header("💼 AI Career Resources")
    st.markdown("Find resources to build your career in AI:")
    st.subheader("📄 Resume Templates")
    st.markdown("- [Microsoft Resume Template](https://create.microsoft.com/en-us/templates/resumes)")
    st.markdown("- [Canva Resume Templates](https://www.canva.com/resumes/templates)")

    st.subheader("💬 Interview Preparation")
    with st.expander("Technical Interview Guide"):
        st.markdown("- [Download Guide (PDF)](https://drive.google.com/file/d/1ydiXGo1hU18YopMZ6vsu72v9omXpkvK5/view?usp=drive_link)")
        st.markdown("Covers: ML, DL, system design, coding questions.")
    with st.expander("Behavioral Interview Tips"):
        st.markdown("- [View Tips (PDF)](https://drive.google.com/file/d/1BjM3bDMYNuAGB2wcVFmGhQ8mG30O2CAE/view?usp=drive_link)")
        st.markdown("Includes: STAR method, common Qs, body language.")

    st.subheader("🧪 Internship Opportunities")
    st.markdown("- [Google Research Internship](https://careers.google.com/jobs)")
    st.markdown("- [OpenAI Internship Page](https://openai.com/careers)")

    st.subheader("💼 Job Portals")
    st.markdown("- [LinkedIn](https://www.linkedin.com) - Professional networking & job search")
    st.markdown("- [Indeed](https://www.indeed.com) - Jobs with AI filters")
    st.markdown("- [AngelList](https://angel.co) - Startup jobs & AI roles")

# Tab 4 - Fun Activities
with tabs[3]:
    st.header("🎮 Fun AI Activities")
    st.markdown("Explore fun AI projects, competitions, or games:")
    st.markdown("- [Quick, Draw! by Google](https://quickdraw.withgoogle.com/)")
    st.markdown("- [AI Dungeon](https://play.aidungeon.io/)")

# Tab 5 - Members
with tabs[4]:
    st.header("👥 AI Club Members")
    st.markdown("Meet our amazing members:")
    members_data = [
        ("A. Vaishnavi", "Member", "First Year", "Active", "April 9, 2025"),
        ("Akumalla Venkata Lakshmi Pranathi", "Member", "First Year", "Active", "April 9, 2025"),
        ("B Pranay", "Core Team", "Second Year", "Active", "April 9, 2025"),
        ("Balling Harini Sai", "Member", "First Year", "Active", "April 9, 2025"),
        ("Busa Uma Maheshwar", "Member", "First Year", "Active", "April 9, 2025"),
        ("Challa Bhavana", "Member", "First Year", "Active", "April 9, 2025"),
        ("Chathelli Sambaraju", "Member", "First Year", "Active", "April 9, 2025"),
        ("Chiluvuri Hasika Vimal", "Member", "First Year", "Active", "April 9, 2025"),
        ("D. Pavani", "Member", "First Year", "Active", "April 9, 2025"),
        ("Damarla Jyothi Naga Subhashini", "Member", "First Year", "Active", "April 9, 2025"),
        ("Deepika", "Member", "First Year", "Active", "April 9, 2025"),
        ("Faizan Khan", "Member", "First Year", "Active", "April 9, 2025"),
        ("G. Akshitha", "Member", "First Year", "Active", "April 9, 2025"),
        ("Gaddameedi Bhargavi", "Member", "Second Year", "Active", "April 9, 2025"),
        ("Ganti Lalitha Meenakshi", "Member", "First Year", "Active", "April 9, 2025"),
        ("Gopi Chand Kamma", "Member", "Third Year", "Active", "April 9, 2025"),
        ("Gudi Akhila", "Member", "First Year", "Active", "April 9, 2025"),
        ("Gudisela Harika", "Member", "First Year", "Active", "April 9, 2025"),
        ("K. Vaishnavi", "Member", "First Year", "Active", "April 9, 2025"),
        ("Kakani Durga Srinidhi", "Member", "First Year", "Active", "April 9, 2025"),
        ("Kalakoti Rishith Kumar Reddy", "Member", "First Year", "Active", "April 9, 2025"),
        ("Kodali Rupa Sri", "Member", "Second Year", "Active", "April 9, 2025"),
        ("Kommanaboyina Venkata Rohith", "Member", "Second Year", "Active", "April 9, 2025"),
        ("Kotagiri Padmini Goud", "Member", "Second Year", "Active", "April 9, 2025"),
        ("Kunapareddy Jaideep", "Member", "Second Year", "Active", "April 9, 2025"),
        ("Lakshmi Praharsha Reddy", "Member", "First Year", "Active", "April 9, 2025"),
        ("Maidhili", "Member", "First Year", "Active", "April 9, 2025"),
        ("Mann Sharma", "Member", "First Year", "Active", "April 9, 2025"),
        ("Markalashmi Praharsha", "Member", "First Year", "Active", "April 9, 2025"),
        ("Murali Krishna", "Member", "First Year", "Active", "April 9, 2025"),
        ("Neerathesh ARV", "Member", "First Year", "Active", "April 9, 2025"),
        ("Oleti Anusha", "Member", "First Year", "Active", "April 9, 2025"),
        ("Pattri Raghavendra Saideep", "VICE PRESIDENT", "Second Year", "Active", "April 9, 2025"),
        ("Peddabai Bhavana", "Member", "First Year", "Active", "April 9, 2025"),
        ("Pranathipotluri", "Member", "First Year", "Active", "April 9, 2025"),
        ("Priya Kumari", "Member", "Second Year", "Active", "April 9, 2025"),
        ("Punjala Niharika", "Member", "Second Year", "Active", "April 9, 2025"),
        ("Raja Shekar Patha", "Member", "Second Year", "Active", "April 9, 2025"),
        ("Ramayanam Prabhakar", "Member", "First Year", "Active", "April 9, 2025"),
        ("Rangineni Sathvik", "Member", "First Year", "Active", "April 9, 2025"),
        ("Ravula Nandha Kishor Reddy", "Member", "Third Year", "Active", "April 9, 2025"),
        ("Sidigiddi Vaishnavi", "Member", "First Year", "Active", "April 9, 2025"),
        ("Sneha Gupta", "Member", "First Year", "Active", "April 9, 2025"),
        ("Sriram Kruthika", "Member", "First Year", "Active", "April 9, 2025"),
        ("Vadla Saicharan", "Member", "First Year", "Active", "April 9, 2025"),
        ("Vallamdas Saicharan", "Member", "First Year", "Active", "April 9, 2025"),
        ("Vanapalli Lova Kumar", "Member", "First Year", "Active", "April 9, 2025"),
        ("Veerayya Gari Manisha", "Member", "Second Year", "Active", "April 9, 2025"),
        ("Vishal Dubey", "Member", "Second Year", "Active", "April 9, 2025"),
        ("Yaswanth Naidu Yalla", "Member", "First Year", "Active", "April 9, 2025"),
    ]
    df = pd.DataFrame(members_data, columns=["Name", "Role", "Year", "Status", "Join Date"])
    st.dataframe(df, use_container_width=True)

# Tab 6 - Events
with tabs[5]:
    st.header("📅 Upcoming Events")
    st.markdown("- **Guest Lecture**: Learn from industry experts.")
    st.markdown("- **AI Chatbot Creation**: Build your own chatbot.")
    st.markdown("- **AI Quiz**: Test your AI knowledge.")

# Tab 7 - Contact Us
with tabs[6]:
    st.header("📞 Contact Us")
    st.markdown("Get in touch with our team for any queries or collaborations!")
    members = [
        {
            "name": "Tilak",
            "role": "President",
            "bio": "Leading the AI Club to new heights with a passion for ML and innovation.",
            "contact": "9182330751"
        },
        {
            "name": "Raghav",
            "role": "Vice President",
            "bio": "Data enthusiast and co-leader of our exciting AI projects.",
            "contact": "8639342772"
        },
        {
            "name": "Priyanshu",
            "role": "Joint Secretary",
            "bio": "Loves to bring creative ideas into AI projects and club management.",
            "contact": "7396363147"
        },
        {
            "name": "Sadvik Kumar",
            "role": "Technical Lead",
            "bio": "Tech wizard driving innovation in AI projects and mentoring the team.",
            "contact": "8919597568"
        },
        {
            "name": "Pranay",
            "role": "Member Management",
            "bio": "Ensures smooth coordination and management of club members.",
            "contact": "9059315079"
        }
    ]
    for member in members:
        with st.expander(f"{member['name']} - {member['role']}"):
            st.markdown(f"**Bio:** {member['bio']}")
            st.markdown(f"**Contact Number:** {member['contact']}")