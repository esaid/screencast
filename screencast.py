import streamlit as st
from streamlit.components.v1 import html

def runscreencast():

    selectmenu = '''<script>
           window.parent.document.getElementById("MainMenu").click();
           </script>
           '''
    selectscreencast = '''<script>
               window.parent.document.getElementsByClassName('css-1wud4gv e1pxm3bq4')[2].ariaSelected = "true";
               </script>
               '''
    clickscreencast = '''<script>
                   window.parent.document.getElementsByClassName('css-1wud4gv e1pxm3bq4')[2].click()
                   </script>
                   '''

    html(selectmenu)
    html(selectscreencast)
    html(clickscreencast)


st.write(""" # ScreenCast 
   ## press F5 to restart""")
st.button(' ScreenCast ', on_click=runscreencast)
