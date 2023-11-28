import requests
import streamlit as st
from streamlit_option_menu import option_menu
from streamlit_lottie import st_lottie





# PAGE CONFIGURATION



st.set_page_config(
    page_title = "Portfolio | Saurabh Narwane",
    page_icon="https://i.imgur.com/DXz9exy.png",
    layout="wide"
)





# CUSTOM PAGE FORMATTING



font_center = """
<style>
.font_center {
    display: flex;
    justify-content: center;
    align-items: center;
    height: 135px; /* Adjust the height as needed */
}
</style>
"""



font_left = """
<style>
.font_left {
    display: flex;
    justify-content: left;
    align-items: left;
    height: 135px; /* Adjust the height as needed */
}
</style>
"""



hide_streamlit_style = """
<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
</style>
"""
st.markdown(hide_streamlit_style, unsafe_allow_html=True)



reduce_header_and_footer_height_style = """
    <style>
        div.block-container {padding-top:0rem;}
        div.block-container {padding-bottom:0rem;}
    </style>
"""
st.markdown(reduce_header_and_footer_height_style, unsafe_allow_html=True)



st.markdown(f"""
<style>
@import url("style/style.css");
</style>
""", unsafe_allow_html = True)





# DEFINING COLOURS



c1 = "#FFD580"

c2 = "#F5BD1F"

c3 = "#FFEECD"





# DEFINING FUNCTIONS



def gap(n):
    for i in range(n):
         st.write("")



def spaces(n):
    return "&nbsp;" * n



def gap_section(sec,n):
    for i in range(n):
        sec.write("")



def line():
    st.markdown("---")



def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()



def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

local_css("style/style.css")





### HEADER



col_h1_1, col_h1_2 = st.columns(spec = 2)



with col_h1_1.container():

    st.markdown("## Saurabh Narwane")

with col_h1_2.container():

    selected = option_menu(
            menu_title = None,
            options = ["Home", "Projects", "Credentials", "Achievements"],
            icons = ["house-fill", "laptop-fill", "person-badge-fill", "trophy-fill"],
            menu_icon = "cast",
            default_index = 0,
            orientation = "horizontal",
            styles={
            "container": {"font-family": "Poppins", "text-align": "left"},
            "nav-link": {"font-size": "15px", "text-align": "center"}
            }
        )



line()





# CREDNETIALS



gap(3)

st.markdown(f'<div class="font_left"><h2 style="color : {c2};">⚪ Credentials ⚪</h2></div>', unsafe_allow_html=True)

sec_1_1, sec_1_2, sec_1_3 = st.columns(spec = 3)



### FIRST SECTION



with sec_1_1.container():

    gap(3)

    st.markdown(f"<ul><li style='color : {c1}; font-size:40px; font-weight: bold'><h2 style='color : {c1};'>Microsoft </h2> <h3 style='color : {c3};'> Power BI <br> Data Analyst Associate. (PL-300)</h3></li></ul>",
                unsafe_allow_html = True)
    
    gap(3)

    st.image(image = "images/credentials/PL-300 Certificate.jpg")



### SECOND SECTION



with sec_1_2.container():

    gap(3)

    st.markdown(f"<ul><li style='color : {c1}; font-size:40px; font-weight: bold'><h2 style='color : {c1};'>Microsoft </h2> <h3 style='color : {c3};'>Azure Data Fundamentals. <br> (DP-900)</h3></li></ul>",
                    unsafe_allow_html = True)

    gap(3)

    st.image(image = "images/credentials/DP-900 Certificate.jpg")



### THIRD SECTION



with sec_1_3.container():

    gap(3)

    st.markdown(f"<ul><li style='color : {c1}; font-size:40px; font-weight: bold'><h2 style='color : {c1};'>Google </h2> <h3 style='color : {c3};'>Data Analytics <br> Professional Certification.</h3></li></ul>",
                    unsafe_allow_html = True)

    gap(3)

    st.image(image = "images/credentials/google_data_analytics.jpg")



sec_2_1, sec_2_2, sec_2_3 = st.columns(spec = 3)



### FOURTH SECTION



with sec_2_1.container():

    gap(3)

    st.markdown(f"<ul><li style='color : {c1}; font-size:40px; font-weight: bold'><h2 style='color : {c1};'>HackerRank </h2> <h3 style='color : {c3};'>Intermediate SQL <br> Certification.</h3></li></ul>",
                    unsafe_allow_html = True)

    gap(3)

    st.image(image = "images/credentials/hackerrank_sql.jpg")


    
### FIFTH SECTION



with sec_2_2.container():

    gap(3)

    st.markdown(f"<ul><li style='color : {c1}; font-size:40px; font-weight: bold'><h2 style='color : {c1};'>Coursera </h2> <h3 style='color : {c3};'>Mathematics and Statistics <br> for Data Science.</h3></li></ul>",
                    unsafe_allow_html = True)

    gap(3)

    st.image(image = "images/credentials/data_science_math_skills.jpg")



### SIXTH SECTION



with sec_2_3.container():

    gap(3)

    st.markdown(f"<ul><li style='color : {c1}; font-size:40px; font-weight: bold'><h2 style='color : {c1};'>Coursera </h2> <h3 style='color : {c3};'>Data Analysis and <br> Visualisation with Excel.</h3></li></ul>",
                    unsafe_allow_html = True)

    gap(3)

    st.image(image = "images/credentials/data_visualisation_with_excel.jpg")



gap(3)




### FOOTER



line()

footer_1, footer_2, footer_3 = st.columns(spec = 3)

footer_1.markdown('''<b>Let's Connect: &nbsp;&nbsp;&nbsp;</b> <a style = "color: #FFFFFF; text-decoration: none;  width: 500px; height: 500px;" href = "https://www.linkedin.com/in/saurabh-narwane/"> <i class="fa-brands fa-linkedin"></i></a>
                <a style = "color: #FFFFFF; text-decoration: none;  width: 500px; height: 500px;" href = "https://twitter.com/saurabhnarwane"> <i class="fa-brands fa-twitter"></i></a>
                <a style = "color: #FFFFFF; text-decoration: none;  width: 500px; height: 500px;" href = "https://www.instagram.com/saurabh.narwane/"> <i class="fa-brands fa-instagram"></i></a>
                <a style = "color: #FFFFFF; text-decoration: none;  width: 500px; height: 500px;" href = "https://www.youtube.com/channel/UCnDX94mNIcHTHKScgBFzkbQ"> <i class="fa-brands fa-youtube"></i></a>''',
                unsafe_allow_html = True)

st.markdown(
    """
    <style>
    .center-align {
        text-align: center;
    }
    </style>
    """,
    unsafe_allow_html=True
)

footer_2.markdown('''<div class="center-align">
                <a href="https://www.novypro.com/profile_projects/saurabhnarwane">
                <img border="0" alt="Novy Pro" src="https://i.imgur.com/6Zoa2mR.png" width="25" height="25">
                </a>
                &nbsp;&nbsp;&nbsp;
                <a href="https://github.com/SN11112001">
                <img border="0" alt="GitHub" src="https://i.imgur.com/ytYEVVv.png" width="25" height="25">
                </a>
                &nbsp;&nbsp;&nbsp;
                <a href="https://public.tableau.com/app/profile/saurabh.narwane">
                <img border="0" alt="Tableau Public" src="https://i.imgur.com/4DXzz7F.png" width="25" height="25">
                </a>''',
                unsafe_allow_html = True)

st.markdown(
    """
    <style>
    .right-align {
        text-align: right;
    }
    </style>
    """,
    unsafe_allow_html=True
)

footer_3.markdown('''<div class="right-align"><b style = "text-alignment:right;">© 2023 Saurabh Narwane. All Rights Reserved.</b></div>''',
                unsafe_allow_html = True)