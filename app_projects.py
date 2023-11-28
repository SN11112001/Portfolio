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



# PROJECTS



gap(3)

st.markdown(f'<div class="font_left"><h2 style="color : {c2};">⚪ Projects ⚪</h2></div>', unsafe_allow_html=True)

gap(3)



### FIRST SECTION



sec_1_1, sec_1_2, sec_1_3, sec_1_4, sec_1_5 = st.columns(spec = 5)

with sec_1_1.container():

    st.markdown("<h2 style = 'color: #EEBA2C;'>• Power BI</h2>",
                unsafe_allow_html = True)
    
    gap(2)

    st.image(image = "images/projects/Power BI.png", width = 70)

    gap(2)
    
    st.markdown('''<div class="font_left">
        <ul>
        <li><h5><a style = "color: #FFFFFF; text-decoration: none;  width: 500px; height: 500px;" href = "https://www.novypro.com/project/supplychainanalytics">Supply Chain Analytics.</i></a></h5></li>
        <li><h5><a style = "color: #FFFFFF; text-decoration: none;  width: 500px; height: 500px;" href = "https://www.novypro.com/project/retailanalytics">Retail Analytics.</i></a></h5></li>
        <li><h5><a style = "color: #FFFFFF; text-decoration: none;  width: 500px; height: 500px;" href = "https://www.novypro.com/project/hospitalityanalytics">Hospitality Analytics.</i></a></h5></li>
        </ul>
        </div>'''
        ,unsafe_allow_html=True)



### SECOND SECTION



with sec_1_2.container():

    st.markdown("<h2  style = 'color: #FFA500;'>• Tableau</h2>",
                unsafe_allow_html = True)
    
    gap(2)
    
    st.image(image = "images/projects/Tableau.png", width = 70)
    
    gap(2)
    
    st.markdown('''<div class="font_left">
        <ul>
        <li><h5><a style = "color: #FFFFFF; text-decoration: none;  width: 500px; height: 500px;" href = "https://public.tableau.com/app/profile/saurabh.narwane/viz/WomeninSTEMFields_16869187544000/Dashboard">Women in STEM Fields.</i></a></h5></li>
        <li><h5><a style = "color: #FFFFFF; text-decoration: none;  width: 500px; height: 500px;" href = "https://public.tableau.com/app/profile/saurabh.narwane/viz/LiteracyRateinTamilNaduState/Dashboard">Literacy Rate in <br> Tamil Nadu State.</i></a></h5></li>
        </ul>
        </div>'''
        ,unsafe_allow_html=True)



### THIRD SECTION



with sec_1_3.container():

    st.markdown("<h2  style = 'color: #60849C;'>• SQL</h2>",
                unsafe_allow_html = True)
    
    gap(2)

    st.image(image = "images/projects/MySQL.png", width = 70)

    gap(2)
    
    st.markdown('''<div class="font_left">
        <ul>
        <li><h5><a style = "color: #FFFFFF; text-decoration: none;  width: 500px; height: 500px;" href = "https://github.com/SN11112001/8-Week-SQL-Challenge/blob/main/cs1_dannys_diner/cs1_dannys_diner.sql">Restaurant <br> Performance Analysis.</i></a></h5></li>
        </ul>
        </div>'''
        ,unsafe_allow_html=True)
    


### FOURTH SECTION



with sec_1_4.container():

    st.markdown("<h2  style = 'color: #2AAA8A;'>• Excel</h2>",
                unsafe_allow_html = True)
    
    gap(2)

    st.image(image = "images/projects/Excel.png", width = 70)

    gap(2)
    
    st.markdown('''<div class="font_left">
        <ul>
        <li><h5><a style = "color: #FFFFFF; text-decoration: none;  width: 500px; height: 500px;" href = "https://onedrive.live.com/embed?cid=D60D76CF9117A98C&resid=D60D76CF9117A98C%21283&authkey=AFZsH_5l7n95v7g&em=2">Banking Customers <br> Analysis.</i></a></h5></li>
        </ul>
        </div>'''
        ,unsafe_allow_html=True)



### FIFTH SECTION



with sec_1_5.container():

    st.markdown("<h2  style = 'color: #90EE90;'>• Machine Learning</h2>",
                unsafe_allow_html = True)
    
    gap(2)

    st.image(image = "images/projects/Python.png", width = 70)

    gap(2)
    
    st.markdown('''<div class="font_left">
        <ul>
        <li><h5><a style = "color: #FFFFFF; text-decoration: none;  width: 500px; height: 500px;" href = "https://github.com/SN11112001/E-Commerce-Data-Analysis-and-Modeling">E-Commerce Data <br> Modeling and Analysis.</i></a></h5></li>
        <li><h5><a style = "color: #FFFFFF; text-decoration: none;  width: 500px; height: 500px;" href = "https://sales-dashboard-by-sn11112001.streamlit.app/">Superstore Sales Dashboard.</i></a></h5></li>
        </ul>
        </div>'''
        ,unsafe_allow_html=True)

gap(1)




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