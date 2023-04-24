import numpy as np
import pickle
import streamlit as st

# Load the model
loaded_model = pickle.load(open('C:/Users/USER/Desktop/ML/Saving Model/SVMclassifier.pkl', 'rb'))

# Creating a function to predict the output
def pred(input_data):
    input_arr = np.asanyarray(input_data)
    input_arr = input_arr.reshape(1, -1)
    prediction = loaded_model.predict(input_arr)[0]
    return "StartTech Oscar prediction: " + str(prediction)

def main():
    # title 
    st.title("StartTech Oscar Prediction")

    # get input data - Marketing expense, Production expense, Multiplex coverage, Budget, Movie_length, Lead_ Actor_Rating, Lead_Actress_rating, Director_rating, Producer_rating, Critic_rating, Trailer_views, Time_taken, Twitter_hastags, Avg_age_actors, Num_multiplex, Collection, 3D_available_YES, Genre_Comedy, Genre_Drama, Genre_Thriller

    Marketing_expense = st.text_input("Marketing expense")
    Production_expense = st.text_input("Production expense")
    Multiplex_coverage = st.text_input("Multiplex coverage")
    Budget = st.text_input("Budget")
    Movie_length = st.text_input("Movie_length")
    Lead_Actor_Rating = st.text_input("Lead_Actor_Rating")
    Lead_Actress_rating = st.text_input("Lead_Actress_rating")
    Director_rating = st.text_input("Director_rating")
    Producer_rating = st.text_input("Producer_rating")
    Critic_rating = st.text_input("Critic_rating")
    Trailer_views = st.text_input("Trailer_views")
    Time_taken = st.text_input("Time_taken")
    Twitter_hastags = st.text_input("Twitter_hastags")
    Avg_age_actors = st.text_input("Avg_age_actors")
    Num_multiplex = st.text_input("Num_multiplex")
    Collection = st.text_input("Collection")
    _3D_available_YES = st.text_input("3D_available_YES")
    Genre_Comedy = st.text_input("Genre_Comedy")
    Genre_Drama = st.text_input("Genre_Drama")
    Genre_Thriller = st.text_input("Genre_Thriller")

    #code for prediction
    Star_oscar_prediction = ""

    #Create button to predict
    if st.button("Predict"):
        input_data = (Marketing_expense, Production_expense, Multiplex_coverage, Budget, Movie_length, Lead_Actor_Rating, Lead_Actress_rating, Director_rating, Producer_rating, Critic_rating, Trailer_views, Time_taken, Twitter_hastags, Avg_age_actors, Num_multiplex, Collection, _3D_available_YES, Genre_Comedy, Genre_Drama, Genre_Thriller)
        Star_oscar_prediction = pred(input_data)

    st.success(Star_oscar_prediction)

if __name__ == '__main__':
    main()