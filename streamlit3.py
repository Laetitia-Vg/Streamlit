import streamlit as st
from streamlit_authenticator import Authenticate
from streamlit_option_menu import option_menu

# Nos données utilisateurs doivent respecter ce format

lesDonneesDesComptes = {'usernames': {'utilisateur': {'name': 'utilisateur',
   'password': 'utilisateurMDP',
   'email': 'utilisateur@gmail.com',
   'failed_login_attemps': 0, # Sera géré automatiquement
   'logged_in': False, # Sera géré automatiquement
   'role': 'utilisateur'},
  'root': {'name': 'root',
   'password': 'rootMDP',
   'email': 'admin@gmail.com',
   'failed_login_attemps': 0, # Sera géré automatiquement
   'logged_in': False, # Sera géré automatiquement
   'role': 'administrateur'}}}

authenticator = Authenticate(
    lesDonneesDesComptes, # Les données des comptes
    "cookie name", # Le nom du cookie, un str quelconque
    "cookie key", # La clé du cookie, un str quelconque
    30, # Le nombre de jours avant que le cookie expire 
)

authenticator.login()

#def accueil():
 #     st.title("Bienvenue sur le site officiel du Uno")
        # Création du menu qui va afficher les choix qui se trouvent dans la variable options

 # Ajout d'une barre latérale
with st.sidebar:
    st.button("Déconnexion")

    selection = option_menu(
            menu_title=None,
            options = ["Accueil", "Photos"]
        )

# On indique au programme quoi faire en fonction du choix
if selection == "Accueil":
    st.title("Bienvenue sur le site officiel du Uno")
    st.write("Et si on jouait au Uno?")
    choice = st.selectbox("Choisissez une version ?", ['Classique','Flip','No mercy'])

    if choice == 'Classique':
        st.image("uno_classique.jpg", caption="Uno classique")
    elif choice == 'Flip':
        st.image("uno_flip.jpg", caption = "Uno flip")
    elif choice == 'No mercy':
        st.image("uno_no_mercy.jpg", caption = "Uno No Mercy")



elif selection == "Photos":
    st.write("Venez découvrir l'existence d'autres Uno")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.header("Uno Barbie")
        st.image("uno_barbie.jpg", caption="Très girly", use_container_width=True)

    with col2:
        st.header("Uno Super Mario")
        st.image("uno_SP.jpg", caption="Pour retrouver votre âme d'enfant", use_container_width=True)

    with col3:
        st.header("Uno Harry Potter")
        st.image("uno_HP.jpg", caption="Pour faire ressortir la magie qui est en vous", use_container_width=True)

# if st.session_state["authentication_status"]:
#   accueil()
#   # Le bouton de déconnexion
#   authenticator.logout("Déconnexion")

# elif st.session_state["authentication_status"] is False:
#     st.error("L'username ou le password est/sont incorrect")
# elif st.session_state["authentication_status"] is None:
#     st.warning('Les champs username et mot de passe doivent être remplie')