import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from PIL import Image


 

st.write("Cher utilisateur,")

st.write(" ")

st.write("Nous vous demandons de bien vouloir fournir votre nom et votre adresse e-mail pour \
         pouvoir utiliser notre application web. Ces informations seront utilisées pour vous \
         identifier et pour vous envoyer des mises à jour importantes.")

st.write(" ")

st.write("Nous vous assurons que vos informations personnelles ne seront pas partagées avec des\
          tiers sans votre consentement et qu'elles seront traitées conformément à \
         notre politique de confidentialité.")

st.write(" ")

st.write("Nous vous remercions de votre coopération.")

st.write("Cordialement, \
         Le nom de l'entreprise ou de l'équipe de développement de l'application")


#st.set_page_config(
#  page_title="Contact",
# page_icon="📞"
#)


# Get In Touch With Us section
st.write("## Get In Touch With Us")
name = st.text_input("Name")
email = st.text_input("Email")
message = st.text_area("Message")

if st.button("Submit"):
    st.write("Thank you for getting in touch, {}. We will contact you at {}.".format(name, email))
    # Here you can send the message to your email or save it to a database, etc.


##################################################################################

st.write("\n\n\n\n")
st.write("\n\n\n\n")
st.write("\n\n\n\n")
st.write("\n\n\n\n")
st.write("\n\n\n\n")
st.write("\n\n\n\n")
st.write("\n\n\n\n")
st.write("\n\n\n\n")

# Contact section
st.write("#### Contact")
st.write("Email: contact@6-tech.com")
st.write("Phone: +273 656280076 / +237 698076337")
