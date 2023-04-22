import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from PIL import Image
import joblib



def goblal_function():

    ############################ pour la connection multipage #########################
    st.set_page_config(
        page_title="Multipage",
        page_icon="©"
    )
    


    ############################ titre de l'application #############################
    st.title('PREDICTION DE RISQUE DES MALADIES CARDIO-VASCULAIRES/CORONARIENE')
    st.write(" ")

    # importation de l'image de l'application
    try:
        logo = Image.open("image_logo.png")
        st.image(logo, width=400)
    except Exception as e:
        st.error("Error loading image: {}".format(e))


    ########################### importation de donnee ########################
    @st.cache_data
    def load_data():
        # importation des donnees
        df = pd.read_csv('./heart_2020_cleaned.csv')
        # le pretraitement de donnees
        df['HeartDisease'] = df["HeartDisease"].map({"Yes":1, "No":0})
        df["Smoking"] = df["Smoking"].map({"Yes":1, "No":0})
        df["AlcoholDrinking"] = df["AlcoholDrinking"].map({"Yes":1, "No":0})
        df['DiffWalking'] = df['DiffWalking'].map({"Yes":1, "No":0})
        df['Diabetic'] = df['Diabetic'].map({"Yes":1, "No":0, 'No, borderline diabetes':2, 'Yes (during pregnancy)':3})
        df["KidneyDisease"] = df["KidneyDisease"].map({"Yes":1, "No":0})
        df["PhysicalActivity"] = df["PhysicalActivity"].map({"Yes":1, "No":0})
        df["Asthma"] = df["Asthma"].map({"Yes":1, "No":0})
        df['Sex'] = df["Sex"].map({'Female':0, 'Male':1})
        df["Stroke"] = df["Stroke"].map({"Yes":1, "No":0})
        df['AgeCategory'] = df['AgeCategory'].map({'18-24':13, "25-29":12, "30-34":11, '35-39':10,
                                                "40-44":9, "45-49":8, "50-54":7, "55-59":6, "60-64":5,
                                                "65-69":4, "70-74":3, "75-79":2, '80 or older':1})
        df['Race'] = df["Race"].map({'White':0, 'Black':1, 'Asian':3, 'American Indian/Alaskan Native':2,
            'Other':4, 'Hispanic':5})
        df["GenHealth"] = df["GenHealth"].map({'Very good':0, 'Fair':1, 'Good':2, 'Poor':3, 'Excellent':4})
        df["SkinCancer"] = df["SkinCancer"].map({"Yes":1, "No":0})
        return df
    

    from sklearn.model_selection import train_test_split
    from imblearn.over_sampling import SMOTE

    df = load_data()

    seed = 500
    # lecture du dataset

    df_copy = df.copy()

    #Surechantillonnage
    sm = SMOTE(k_neighbors=3, sampling_strategy=0.75)

    y = df_copy['HeartDisease']
    X = df_copy.drop('HeartDisease', axis=1)

    x_re, y_re = sm.fit_resample(X, y)

    X_train, x_test, y_train, y_test = train_test_split(x_re, y_re, test_size=0.3, random_state=seed)

    ########################################## La description de l'application ######################################
    st.write("    Notre application de prédiction des risques de maladies cardiovasculaires offre des fonctionnalités\
             avancées pour vous aider à comprendre et à gérer votre santé cardiaque. Cette application utilise des \
             algorithmes de pointe pour calculer votre risque de développer une maladie cardiovasculaire en se basant \
             sur vos antécédents médicaux, vos symptômes actuels et les facteurs de risque généraux tels que l'âge, le \
             sexe, le poids, le taux de cholestérol et la tension artérielle.")
    st.write("    Vous pouvez simplement entrer vos \
             informations personnelles, comme votre âge, votre sexe et vos habitudes de vie, pour créer un profil, et \
             l'application fournira une analyse complète de votre santé cardiaque.\
              Ceci inclut une estimation personnalisée \
             du risque de développer une maladie cardiovasculaire, ainsi que de précieux conseils et des recommandations pour\
              réduire ces risques. En utilisant cette application, vous pourrez prendre des mesures préventives dès maintenant \
             pour réduire votre risque de maladie cardiovasculaire à long terme. ")
    st.write("    En somme, notre application est un \
             outil essentiel pour améliorer votre santé cardiaque et réduire significativement le risque de maladies\
              cardiovasculaires. Essayez-la maintenant pour commencer votre voyage vers une meilleure santé cardiovasculaire !")
    st.write("")
    st.write("")
    st.write("")
    st.write("")

    st.write("Si vous voulez en savoir plus par rapport aux maladies cardio-vasculaires, je vous prie de cliquer sur ce \
             [lien](https://www.who.int/fr/news-room/fact-sheets/detail/cardiovascular-diseases-(cvds)) ")


    ########################################### les parametres du modele #################################################
    sex = st.radio(" De quel sexe etes vous?", ['Masculin', 'Feminin'])
    if sex == "Masculin" :
        sex = 1
    if sex=='Feminin':
        sex = 0       
    st.write(" ")

    imc = st.number_input("Indice de masse corporelle (IMC)")
    st.write("")

    smooking = st.radio("Avez-vous fumé au moins 100 cigarettes au cours de votre vie ?", ['Oui', 'Non'])
    if smooking == "Oui":
        smooking=1
    if smooking=='Non':
        smooking=0
    st.write("")

    drinking = st.radio("Hommes adultes ayant plus de 14 verres par semaine et femmes adultes ayant plus de 7 verres par semaine", ['Oui', 'Non'])
    if drinking=='Oui':
        drinking=1
    if drinking=='Non':
        drinking=0
    st.write(" ")

    stroke = st.radio("Avez vous deja eu une attaque de AVC?", ['Oui', 'Non'])
    if stroke=='Oui':
        stroke=1
    if stroke=='Non':
        stroke=0
    st.write(" ")

    physicalHealth = st.number_input(" pendant combien de jours au cours des 30 derniers jours votre santé physique n'était-elle pas bonne ? (0-30 jours)")
    st.write(" ")

    mentalhealth = st.number_input("pendant combien de jours au cours des 30 derniers jours votre santé mentale n'était-elle pas bonne ? (0-30 jours).")
    st.write(" ")

    diffwalking = st.radio(" Avez-vous de sérieuses difficultés à marcher ou à monter des escaliers ?", ['Oui', 'Non'])
    if diffwalking=='Oui':
        diffwalking=1
    if diffwalking=="Non":
        diffwalking=0
    st.write(" ")

    agecategory = st.selectbox("votre categorie d'age", ['18-24', '25-29', '30-34', '35-39', '40-44', '45-49', '50-54', '55-59', '60-64', '65-69', '70-74', '75-79', '80 et plus'])
    if agecategory=='18-24':    
        agecategory=13  
    elif agecategory=='25-29':  
        agecategory=12  
    elif agecategory=='30-34':  
        agecategory=11  
    elif agecategory=='35-39':  
        agecategory=10  
    elif agecategory=='40-44':  
        agecategory=9   
    elif agecategory=='45-49':  
        agecategory=8   
    elif agecategory=='50-54':  
        agecategory=7   
    elif agecategory=='55-59':  
        agecategory=6   
    elif agecategory=='60-64':  
        agecategory=5   
    elif agecategory=='65-69':  
        agecategory=4   
    elif agecategory=='70-74':       
        agecategory=3        
    elif agecategory=='75-79':   
        agecategory=2        
    elif agecategory=='80 et plus':      
        agecategory=1        
    st.write(" ")   

    race = st.selectbox('Quelle est votre race?', ['noire', 'blanche', 'hispanic', 'autre', 'asiatique', 'americaine']) 
    if race=='noire':    
        race=1   
    elif race=='blanche':    
        race=0   
    elif race=='hispanic':   
        race=5   
    elif race=='autre':  
        race =4  
    elif race=='asiatique':  
        race=3   
    elif race=='americaine':     
        race=2   
    st.write(" ")   
    diabete = st.radio("Souffrez-vous du diabete?", ['Oui', 'Non']) 
    if diabete=="Oui":   
        diabete=1    
    if diabete=='Non':   
        diabete=0    
    st.write(" ")   
    physicalactivity = st.radio("Avez vous pratiqué une activité physique ou un exercice au cours des 30 derniers jours en dehors de leur travail habituel.", ['Oui', "Non"])
    if physicalactivity=='Oui':
        physicalactivity=1
    if physicalactivity=='Non':
        physicalactivity=0
    st.write(" ")

    genthealth = st.selectbox(" Diriez-vous qu'en général votre santé est...", ['Very good', 'Fair', 'Good', 'Poor', 'Excellent'])
    if genthealth=='Very good': 
        genthealth=0    
    elif genthealth=='Fair':    
        genthealth=1    
    elif genthealth=='Good':    
        genthealth=2    
    elif genthealth=='Poor':    
        genthealth=3    
    elif genthealth=='Excellent':   
        genthealth=4    
    st.write(" ")   

    sleeptime = st.number_input("En moyenne, combien d'heures de sommeil avez-vous par période de 24 heures ?")
    st.write(" ")
    asthma = st.radio("Est-vous asmatique?", ['Oui', 'Non'])
    if asthma=='Oui':
        asthma=1
    if asthma=='Non':
        asthma=0
    st.write(" ")

    kidneydisease = st.radio("Avez-vous une maladie renale?", ['Oui', 'Non'])
    if kidneydisease=='Oui':
        kidneydisease=1
    if kidneydisease=='Non':
        kidneydisease=0
    st.write()

    cancer = st.radio("Avez-vous un cancer de la peau?", ['Oui', 'Non'])
    if cancer=='Oui':
        cancer=1
    if cancer=='Non':
        cancer=0

    # quelques espacement
    st.write("\n\n\n\n")
    st.write("\n\n\n\n")
    st.write("\n\n\n\n")
    st.write("\n\n\n\n")



    ########################################## Creation d'un boutton de prediction #####################################
    load_model = joblib.load(filename="RandomForest_model.pkl")
    if st.button("Predire")==True:
        
        dictionnaire = {
                         'BMI':[imc],
                         'Smoking':[smooking],
                         'AlcoholDrinking':[drinking],
                         'Stroke':[stroke],
                         'PhysicalHealth':[physicalHealth],
                         'MentalHealth':[mentalhealth],
                         'DiffWalking':[diffwalking],
                         'Sex':[sex],
                         'AgeCategory':[agecategory],
                         'Race':[race],
                         'Diabetic':[diabete],
                         'PhysicalActivity':[physicalactivity],
                         'GenHealth':[genthealth],
                         'SleepTime':[sleeptime],
                         'Asthma':[asthma],
                         'KidneyDisease':[kidneydisease],
                         'SkinCancer':[cancer]
                         }
        data = pd.DataFrame(dictionnaire)

        st.write(f"### Vous etes expose a {load_model.predict_proba(data)[0][0]*100}%  d'etre atteint par un maladie cardiovsculaire.")



    st.write("\n\n\n\n")
    st.write("\n\n\n\n")
    st.write("\n\n\n\n")
    st.write("\n\n\n\n")


    ##################################### espace de texte pour commantaire ##################################
    st.write("#### Laisser un commentaire 🗒️")
    st.text_area(" ")
    if st.button("Submit"):
        st.write("Nous vous remercions pour votre commentaire.")
    

    st.write("\n\n\n\n")
    st.write("\n\n\n\n")
    st.write("\n\n\n\n")
    st.write("\n\n\n\n")
    st.write("\n\n\n\n")
    st.write("\n\n\n\n")
    st.write("\n\n\n\n")
    st.write("\n\n\n\n")

    #######################################################################################################################

    # Contact section
    st.write("#### Contact")
    st.write("Email: contact@6-tech.com")
    st.write("Phone: +273 656280076 / +237 698076337")

   

    ####################################### page qui permet au utilisateur de laisser un commentaire ###################

    # creation d'un test erea pour les utilisateurs
    # ajouter le moyen de nous joindre
    # ajouter un bouton pour permettre aux utilisateur de mieux connaitre les informatiions par rapport aux variables
    # penser a metrre une teste qui permet d'assurer les utilisateur de la condidentialite de leurs information
    # ajouter une page pour la confidentialite
    
if __name__=='__main__':
    goblal_function()