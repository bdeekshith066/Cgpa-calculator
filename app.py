import streamlit as st
st.set_page_config(layout="wide")



st.markdown("""
<style>

.block-container
{
    padding-top: 1rem;
    padding-bottom: 0rem;
    margin-top: 1rem;
}

.gradient-text-container {
    display: flex;
    justify-content: center;
}

</style>
""", unsafe_allow_html=True)

gradient_text_html = """
        <style>
        .gradient-text {
            font-weight: bold;
            background: -webkit-linear-gradient(left, #07539e, #4fc3f7, #ffffff);
            background: linear-gradient(to right, #07539e, #4fc3f7, #ffffff);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            display: inline;
            font-size: 3em;
        }
        </style>
        <div class="gradient-text-container">
            <div class="gradient-text">Exam Tips</div>
        </div>
        """

# Display the gradient text HTML
st.markdown(gradient_text_html, unsafe_allow_html=True)
st.write('---')
st.write(' Carry your ID card, hall ticket with photo, and calculator to the exam hall.')
st.write('Inviligation during SEE is strict with high chances of squads checking pockets, pouches. Strict actions will be taken for malpractice.')
st.write('Dont be late to cie, for SEE max 5-10 mins u can be late. Makesure you are on time')
st.write('Say u have got 43/50 in CIE consoliated week , if will have to get 47(94 in SEE) for O or 37(74 in SEE) for A+ even if u get 46 or any makrs between 37 to 46 u will get A+ so plan accordingly and study')
st.write('Labs is where you need to maximise the marks , becuase 1 marks u get in lab = 4 marks you get in cie. Subjects having labs 25 is for lab 20 for cie and quiz is for 5 marks. Cie is (cie 1+ cie 2)/4')
st.write('Subject is not having labs then Your cie marks will be divided by 2 , so here cie marks is more affecting your cgpa . Even if u get 33/40 in both cies and 9 in quiz...Your marks in 42/50.')
st.write('Quiz is one thing where u have to score really well its ypur marks booster ')
st.write('Make sure you have a better score in cies always u will have a boost. SEE its comparitively hard to study ')
gradient_text_html = """
        <style>
        .gradient-text {
            font-weight: bold;
            background: -webkit-linear-gradient(left, #07539e, #4fc3f7, #ffffff);
            background: linear-gradient(to right, #07539e, #4fc3f7, #ffffff);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            display: inline;
            font-size: 3em;
        }
        </style>
        <div class="gradient-text-container">
            <div class="gradient-text">CGPA Calculator</div>
        </div>
        """

# Display the gradient text HTML
st.markdown(gradient_text_html, unsafe_allow_html=True)

st.write('')
st.write('')

col1, col2, col3 = st.columns([0.8, 0.1, 0.9])

with col1:
    st.image('f1cgpa.png', width=480 , caption='Result Sheet of First Sem')
    st.write('')
    st.image('calculator.jpg', width = 490, caption='Grade points Table')
  

with col2:  
    st.write() 

with col3:
    st.header('Steps to :orange[Calculate]')
    st.write('')
    st.write('')
    st.write('1. Know the :orange[credit] value of each subject. If you are unsure refer to syllabus copy.')
    st.write('2. Refer to the :orange[grading points table] provided and examine the uploaded :orange[results sheet] image.')
    st.write('   - For instance,the :orange[math] score is :orange[80],which falls within the range of :orange[>=80 and <90], which is graded 9 points.Math is a :orange[ 4-credit] course.')
    st.write('   - Hence, the grade points for math are calculated as 4 * 9 = 36.')
    st.write('4. Repeat the process for all subjects according to the uploaded result image.')
    st.write('5. The total grade points are calculated as follows:')
    st.write('      Total Grade Points = 4*9 + 4*9 + 3*8 + 3*8 + 4*10 + 1*9 + 1*9 + 1*10 = :orange[188]')
    st.write('6. Determine the total credits:')
    st.write('      Total Credits = 4 + 4 + 3 + 3 + 3 + 1 + 1 + 1 = :orange[20]')
    st.write('7. Calculate the Semester Grade Point Average (SGPA):')
    st.write('      SGPA = Total Grade Points / Total Credits = :orange[8.9]')
    st.write('8. Calculate the Cumulative Grade Point Average (CGPA):')

st.write('      CGPA is the cumulative GPA. Calculate the SGPA for the second semester, add both semesters\' grade points, add both semesters\' credit scores, and then divide.')
st.write('')
st.write('')
st.write('')
