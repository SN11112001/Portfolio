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





# ACHIEVEMENTS



gap(3)

st.markdown(f'<div class="font_left"><h2 style="color : {c2};">⚪ Achievements ⚪</h2></div>', unsafe_allow_html=True)

gap(3)



### FIRST SECTION



sec_1_1, sec_1_2, sec_1_3, sec_1_4 = st.columns(spec = [3,1,2,1])

with sec_1_1.container():

    gap(6)

    st.markdown(f"<h3 style='color : {c1};'>○ NMIMS Datrimatrix Viz-a-Viz Competition</h3>",
                unsafe_allow_html = True)
    
    st.markdown(f'''<div class="font_left">
        <ul>
        <li><h5>Secured Runner-Up in NMIMS Mumbai's Annual Data Analytics Competition.</h5></li>
        <li><h5>Presented impactful visualizations and concise insights using Power BI to a panel of 3 esteemed judges.</h5></li>
        <li><h5>Utilized three distinct analyses to enhance business performance across the 6 critical retail metrics.</h5></li>
        <li><h5>Check the <a style = "color: #EEBA2C; text-decoration: none;  width: 500px; height: 500px;" href="https://www.linkedin.com/feed/update/urn:li:activity:7029302637254590465/">LinkedIn post</a> here.</h5></li>
        </ul>
        </div>'''
        ,unsafe_allow_html=True)

with sec_1_3.container():

    st.image(image = "images/achievements/nmims.jpg")

    gap(3)



### SECOND SECTION



sec_2_1, sec_2_2, sec_2_3, sec_2_4 = st.columns(spec = [3,1,2,1])

with sec_2_1.container():

    st.markdown(f"<h3 style='color : {c1};'>o Codebasics Analytics Challenge [Nov 2022]</h3>",
                unsafe_allow_html = True)
    
    st.markdown(f'''<div class="font_left">
        <ul>
        <li><h5>Honoured to be selected in the “Top 10” out of 372 submissions, in the Codebasics monthly challenge in the Supply Chain domain.</h5></li>
        <li><h5>Analyzed 6 dataset files with over 100000 rows and demonstrating proficiency in what-if analysis and data visualization.</h5></li>
        <li><h5>Appreciated for the super functional dashboard with amazing navigation for better storytelling and insights.</h5></li>
        <li><h5>Check the <a style = "color: #EEBA2C; text-decoration: none;  width: 500px; height: 500px;" href="https://www.youtube.com/watch?v=asOnUFHlvZw&t=1187s">Featured video</a> and <a style = "color: #EEBA2C; text-decoration: none;  width: 500px; height: 500px;" href="https://www.linkedin.com/feed/update/urn:li:activity:6996544615973564416/">LinkedIn post </a> here.</h5></li>
        </ul>
        </div>'''
        ,unsafe_allow_html=True)

with sec_2_3.container():

    st.image(image = "images/achievements/codebasics.jpg")

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