import streamlit as st
import pandas as pd
from load_css import local_css


st.set_page_config(
    page_title='Python for Accounting workshops',
    page_icon='👨‍🏫'
)

local_css("css/style.css")

st.title("Sign up for the workshops")

st.markdown("""
            
All workshops are help in one of the PC teaching rooms on campous. Please see details on the booking page, which is linked below.
            
&nbsp;

<div class="highlight red">
Sign ups for the Python for Accounting workshops will be available for bookings from 18-Nov 2024.
<br>
<br>
There are a limited number of spaces available for each session!
<br>
<br> 
<b>Please use one of the links below to sign up for the first workshop in week 8 and the second workshop in week 9.
<ul>
    <li><a href="https://apps.lse.ac.uk/training-system/userBooking/course/9301744">this link</a> to secure your spot for the first workshop in week 8. You only need to attend one of the sessions!</b></li>
    <li><a href="https://apps.lse.ac.uk/training-system/userBooking/course/9301749">this link</a> to secure your spot for the second workshop in week 9. You only need to attend one of the sessions!</b></li>   
</ul>


If you can no longer attend, please cancel your booking so another student can book.</div>


""",
            unsafe_allow_html=True
            )
