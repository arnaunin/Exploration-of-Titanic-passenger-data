import streamlit as st
import pandas as pd

def clean_data(df):

    survived_dict = {1: "Yes", 0: "No"}
    pclass_dict = {1: "1st", 2: "2nd", 3: "3rd"}
    embarkment_dict = {"C": "Cherbourg", "Q": "Queenstown", "S": "Southhampton"}

    df.replace({"Survived": survived_dict}, inplace = True)
    df.replace({"Pclass": pclass_dict}, inplace = True)
    df.replace({"Embarked": embarkment_dict}, inplace = True)

    # dropna elimina cada fila en la que haya un Na o un None en la columna indicada
    df.dropna(subset = ["Fare"], inplace = True)
    df.dropna(subset = ["Age"], inplace = True)
    df.dropna(subset = ["Embarked"], inplace = True)

    df["count"] = 1

    return df

@st.cache_data
def get_data(url_s3):

    df = pd.read_csv(url_s3)
    df = clean_data(df)

    return df

@st.cache_data
def get_values(col):

    return sorted(st.session_state['df'][col].unique())

def update_df():
     
     st.session_state['df_fil'] = st.session_state['df'][
        (st.session_state["df"]["Survived"].isin(st.session_state["Survived"])) &
        (st.session_state["df"]["Pclass"].isin(st.session_state["Pclass"])) &
        (st.session_state["df"]["Sex"].isin(st.session_state["Sex"])) &
        (st.session_state["df"]["Embarked"].isin(st.session_state["Embarked"])) & 
        ((st.session_state["df"]["Age"] >= st.session_state["Age"][0]) & (st.session_state["df"]["Age"] <= st.session_state["Age"][1])) &
        ((st.session_state["df"]["SibSp"] >= st.session_state["SibSp"][0]) & (st.session_state["df"]["SibSp"] <= st.session_state["SibSp"][1])) &
        ((st.session_state["df"]["Parch"] >= st.session_state["Parch"][0]) & (st.session_state["df"]["Parch"] <= st.session_state["Parch"][1])) &
        ((st.session_state["df"]["Fare"] >= st.session_state["Fare"][0]) & (st.session_state["df"]["Fare"] <= st.session_state["Fare"][1]))
     ]

st.set_page_config(
    page_title = "Titanic - data",
    page_icon = "🚢",
    layout = "wide",
    initial_sidebar_state = "collapsed"
)

if 'df' in st.session_state:
    st.session_state['df'] = pd.DataFrame()

if 'df_fil' in st.session_state:
    st.session_state['df_fil'] = pd.DataFrame()

st.header("Titanic passenger data")

# Url alojada en un s3 de amazon (archivo publico)
url_s3 =r"https://conquerblocksbucket.s3.eu-north-1.amazonaws.com/train.csv"
st.session_state["df"] = get_data(url_s3)


def page_1():
    st.subheader("Data description📜")
    st.markdown(
        open(r"./html_titanic_table.html").read(), # Texto html
        unsafe_allow_html=True
    )
    with st.expander("Dataframe"):
        st.write(st.session_state['df'])

    with st.expander("Describe"):
        st.write(st.session_state['df'].describe())

def page_2():
    st.subheader("Data analitiscs📈")

    with st.expander("Filters"):
            
        with st.form(key = "filter_form"):

            col_fil_1, col_fil_2 = st.columns([1,1])

            with col_fil_1:

                surv_values = get_values("Survived")
                sel_survived = st.multiselect(
                    'Survived',
                    options = surv_values,
                    help = "Survived yes or no",
                    default = surv_values,
                    key = "Survived"
                )

                pclass_values = get_values("Pclass")
                sel_pclass = st.multiselect(
                    'Pclass',
                    options = pclass_values,
                    help = "1st, 2nd or 3rd class",
                    default = pclass_values,
                    key = "Pclass"
                )

                sex_values = get_values("Sex")
                sel_pclass = st.multiselect(
                    'Sex',
                    options = sex_values,
                    help = "Male or female",
                    default = sex_values,
                    key = "Sex"
                )

                embark_values = get_values("Embarked")
                sel_pclass = st.multiselect(
                    'Embarked',
                    options = embark_values,
                    help = "Southhampton, Cherboutg or Queenstone",
                    default = embark_values,
                    key = "Embarked"
                )

            with col_fil_2:

                age_values = get_values("Age")
                sel_age = st.slider(
                    "Age",
                    min_value = min(age_values),
                    max_value = max(age_values),
                    value = [min(age_values), max(age_values)],
                    key = "Age"
                )
                
                SibSp_values = get_values("SibSp")
                sel_sibs = st.slider(
                    "SibSp",
                    min_value = min(SibSp_values),
                    max_value = max(SibSp_values),
                    value = [min(SibSp_values), max(SibSp_values)],
                    key = "SibSp"
                )

                parch_values = get_values("Parch")
                sel_parhc = st.slider(
                    "Parch",
                    min_value = min(parch_values),
                    max_value = max(parch_values),
                    value = [min(parch_values), max(parch_values)],
                    key = "Parch"
                )

                fare_values = get_values("Fare")
                sel_fare= st.slider(
                    "Fare",
                    min_value = min(fare_values),
                    max_value = max(fare_values),
                    value = [min(fare_values), max(fare_values)],
                    key = "Fare"
                )

                submit = st.form_submit_button("Update")

        if submit:
            update_df()

        st.write(st.session_state['df_fil'])


def page_3():
    st.subheader("Artificial inteligence🤖")

pg = st.navigation(
    {"D&A": [
        st.Page(page_1, title = "Data description", icon = "📜"),
        st.Page(page_2, title = "Data analitiscs", icon = "📈")
    ],
    "AI": [
        st.Page(page_3, title = "Artificial inteligence", icon = "🤖")

    ]

    }
)

pg.run()



