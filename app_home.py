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





# HOME



def home():



    ### FIRST SECTION



    col_1, col_2 = st.columns(spec = 2)

    with col_1.container():

        gap(10)

        st.markdown(f"<h3 style='color : {c1};'>Hello 🙋‍♂️,</h3>", unsafe_allow_html = True)
        st.markdown("<h1>Welcome to my portfolio.</h1>", unsafe_allow_html = True)

        gap(2)

        st.markdown(f"<h5 style='color : {c2};'>Please scroll down to know more about me, my work, skills, and education!</h5>", unsafe_allow_html = True)
        st.markdown("<h4>Feel free to contact me and connect with me.</h4>", unsafe_allow_html = True)

        gap(10)

    with col_2.container():
        
        gap(12)

        st.image(f"images/skills/Desktop_Logos.png", use_column_width  = True)

    st.markdown("---")



    ### SECOND SECTION



    col_b_1, col_b_2 = st.columns(spec = 2)

    with col_b_1.container():

        gap(3)
        
        st.markdown(f"<div class='font_left'><h2 style='color : {c2};'>⚪ About Me ⚪</h2></div>", unsafe_allow_html=True)

        gap(3)
        
        st.markdown('''<div class="font_left">
            <ul>
            <li><h5>I'm a data analyst by day, a music producer by evening and a hustler, always.</h5></li>
            <li><h5>If you can't find me, it's because either I'm playing basketball, off on a hike, or cheering for my favourite teams!</h5></li>
            <li><h5>I am passionate about Business Intelligence and Machine Learning (though I never studied them formally) and a die-hard fan of Andrew Ng.</h5></li>
            <li><h5>I love how the concept of "work" has evolved over the past years, and I enjoy travelling and working together whenever possible.</h5></li>
            </ul>
            </div>'''
            ,unsafe_allow_html=True)

    with col_b_2.container():

        lottie_coding = load_lottieurl("https://assets3.lottiefiles.com/packages/lf20_8efd9doz.json")

        gap(8)

        st_lottie(lottie_coding, height = 300, key = "coding")
    


    gap(3)



    line()



    ### THIRD SECTION



    gap(3)
        
    st.markdown(f"<div class='font_left'><h2 style='color : {c2};'>⚪ Work Experience ⚪</h2></div>", unsafe_allow_html=True)

    gap(3)

    col_c_1, col_c_2, col_c_3, col_c_4 = st.columns(spec = 4)

    with col_c_1.container():

        st.markdown(f'''<div class="font_left">
                <left>
                <h4 style='color : {c1};'>• Wiggles India (a D2C Pet Care brand)</h4>
                </left>
                </div>'''
                    , unsafe_allow_html=True)

        gap(1)
        
        st.image(image = f"images/work/Wiggles.png")

        gap(1)

        st.markdown(f'''<div class="font_left">
                <left>
                <h5>- Data Analyst.</h5>
                <h5>- December 2022 - Present.</h5>
                </left>
                </div>'''
                    , unsafe_allow_html=True)

    with col_c_2.container():

        st.markdown(f'''<div class="font_left">
                <left>
                <h4 style='color : {c1};'>• Urban Company</h4>
                </left>
                </div>'''
                    , unsafe_allow_html=True)

        gap(1)
        
        st.image(image = f"images/work/Urban Company.png")

        gap(1)

        st.markdown(f'''<div class="font_left">
                <left>
                <h5>- Business Development Associate.</h5>
                <h5>- July 2022 - September 2022.</h5>
                </left>
                </div>'''
                    , unsafe_allow_html=True)
    
    with col_c_3.container():

        st.markdown(f'''<div class="font_left">
                <left>
                <h4 style='color : {c1};'>• Stockarea</h4>
                </left>
                </div>'''
                    , unsafe_allow_html=True)

        gap(1)
        
        st.image(image = f"images/work/Stockarea.png")

        gap(1)

        st.markdown(f'''<div class="font_left">
                <left>
                <h5>- Supply Chain Intern.</h5>
                <h5>- April 2022 - June 2022.</h5>
                </left>
                </div>'''
                    , unsafe_allow_html=True)

    with col_c_4.container():
        
        st.markdown(f'''<div class="font_left">
                <left>
                <h4 style='color : {c1};'>• Centre For Railway Information Systems</h4>
                </left>
                </div>'''
                    , unsafe_allow_html=True)

        gap(1)
        
        st.image(image = f"images/work/CRIS.png")

        gap(1)

        st.markdown(f'''<div class="font_left">
                <left>
                <h5>- Web Designer Intern.</h5>
                <h5>- April 2021 - July 2022.</h5>
                </left>
                </div>'''
                    , unsafe_allow_html=True)

    gap(3)

    line()



    ### FOURTH SECTION



    gap(3)

    st.markdown(f'<div class="font_left"><h2 style="color : {c2};">⚪ My Skills ⚪</h2></div>', unsafe_allow_html=True)

    gap(3)

    d1, d2, d3, d4, d5, d6, d7, d8, d9, d10, d11, d12 = st.columns(spec = 12)

    ray = [d1, d2, d3, d4, d5, d6, d7, d8, d9, d10]

    skills_logos = ["Excel", "MySQL", "Power BI", "Tableau", "Python", "Numpy", "Pandas", "Matplotlib", "Scikit Learn", "Streamlit"]

    for k in range(len(skills_logos)):
        
        col = ray[k]

        logo = skills_logos[k]

        col.image(f"images/skills/{logo}.png", width = 75, caption = f'{logo}')

    gap(3)

    line()



    ### FIFTH SECTION



    gap(3)

    st.markdown(f'<div class="font_left"><h2 style="color : {c2};">⚪ My Education ⚪</h2></div>', unsafe_allow_html=True)

    gap(3)

    col_f_1, col_f_2, col_f_3, col_f_4 = st.columns(spec = 4)

    with col_f_1.container():

        st.markdown(f'''<div class="font_left">
                <left>
                <h4 style='color : {c1};'>• Secondary School (X)</h4>
                </left>
                </div>'''
                    , unsafe_allow_html=True)

        gap(1)
        
        st.image(image = f"images/education/kv.png")

        gap(1)

        st.markdown(f'''<div class="font_left">
                <left>
                <h5>- Kednriya Vidyalaya, Sambhajinagar.</h5>
                <h6>- 2007-2017</h6>
                <h5>- CGPA: 9.8</h5>
                </left>
                </div>'''
                    , unsafe_allow_html=True)
    
    with col_f_2.container():

        st.markdown(f'''<div class="font_left">
                <left>
                <h4 style='color : {c1};'>• Higher Secondary School (XII)</h4>
                </left>
                </div>'''
                    , unsafe_allow_html=True)

        gap(1)
        
        st.image(image = f"images/education/spi.png")

        gap(1)

        st.markdown(f'''<div class="font_left">
                <left>
                <h5>- Services Preparatory Institute, Sambhajinagar.</h5>
                <h6>- 2017-2019</h6>
                <h5>- CGPA: 8.4</h5>
                </left>
                </div>'''
                    , unsafe_allow_html=True)
    
    with col_f_3.container():

        st.markdown(f'''<div class="font_left">
                <left>
                <h4 style='color : {c1};'>• Bachelor of Science</h4>
                </left>
                </div>'''
                    , unsafe_allow_html=True)

        gap(1)
        
        st.image(image = f"images/education/nrti.png")

        gap(1)

        st.markdown(f'''<div class="font_left">
                <left>
                <h5>- Gati Shakti Vishwavidyalaya, Vadodara.</h5>
                <h6>- 2019-2022</h6>
                <h5>- CGPA: 8.52</h5>
                </left>
                </div>'''
                    , unsafe_allow_html=True)
        
    gap(3)

    line()



    ### SIXTH SECTION



    gap(3)

    st.markdown(f'<div class="font_left"><h2 style="color : {c2};">⚪ Contact Me ⚪</h2></div>', unsafe_allow_html=True)

    gap(3)

    contact_form = """
    <form action="https://formsubmit.co/saurabhnarwane11@gmail.com" method="POST">
        <input type="hidden" name="_captcha" value="false">
        <input type="text" name="name" placeholder="Your Name" required>
        <input type="email" name="email" placeholder="Your Email" required>
        <textarea name="message" placeholder="Your Message Here"></textarea>
        <button type="submit">Send</button>
    </form>
    """

    col_d_1, col_d_2, col_d_3 = st.columns(spec = 3)

    col_d_1.markdown('''<h5>As a data analyst, I know exactly how you can <br>
                    use data optimally within your business. <br>
                    Based on your objectives, I will make a plan to <br>
                    reach the proper insight.</h5>''' ,
                    unsafe_allow_html = True)

    gap_section(col_d_1, 3)

    col_d_1.markdown('''##### :envelope: E-mail: saurabhnarwane11@gmail.com''')

    gap_section(col_d_1, 1)

    col_d_1.markdown('''##### :telephone_receiver: Phone: +91 - 7875112487''')

    gap_section(col_d_1, 1)

    col_d_1.markdown('''##### :house: Address: Pune, Maharashtra''')

    col_d_2.markdown(contact_form, unsafe_allow_html=True)


    gap(3)





# PROJECTS



def projects():

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






# CREDNETIALS



def credentials():

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





# ACHIEVEMENTS



def achievements():



    ### FIRST SECTION



    gap(3)

    st.markdown(f'<div class="font_left"><h2 style="color : {c2};">⚪ Achievements ⚪</h2></div>', unsafe_allow_html=True)

    gap(3)

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





### PAGE NAVIGATION



if selected == "Home":

    home()

elif selected == "Projects":

    projects()

elif selected == "Achievements":

    achievements()

elif selected == "Credentials":

    credentials()





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