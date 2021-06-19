from textblob import TextBlob
import csv
import tweepy
import matplotlib.pyplot as plt
import streamlit as st
import numpy as np
import pandas as pd
import plotly.express as px
from plotly.subplots import make_subplots
import plotly.graph_objects as go


new_title = '<p style="font-size: 50px;"><b>Sentiment Analyzer<b></p>'
st.markdown(new_title, unsafe_allow_html=True)


def percentage(part, whole):
    return 100 * float(part)/float(whole)


consumerKey = 'I4JIeJYX5PDmYRDp8D05uHTvw'
consumerSecret = '8E8YBZbg8q2CfdAB6VQLHPgGt0ApHWSbklars8CJePoTSJJRvH'
accessToken = '1262384577156460547-XcXM7lpaCp2um3IGVPw1mtUsCbH9as'
accessTokenSecret = 'CNxFNc3Hwncody61OX6YUAdmzCGC2wm1DWkOk9yMAABMs'

auth = tweepy.OAuthHandler(consumer_key=consumerKey,
                           consumer_secret=consumerSecret)

auth.set_access_token(accessToken, accessTokenSecret)

api = tweepy.API(auth)


new_title1 = '<p style="font-size: 20px;">This is a Review Analysis and Language Translator Web App</p>'
st.markdown(new_title1, unsafe_allow_html=True)

st.sidebar.title(
    "Welcome To The Web Dashboard:")


st.sidebar.header("Choose")
select = st.sidebar.selectbox('', ['Twitter Hashtags', 'Single Sentence',
                              'Language Translator', 'Multiple Reviews'], key='1')

st.sidebar.markdown("")
st.sidebar.markdown("")
st.sidebar.markdown("")
st.sidebar.markdown("")
st.sidebar.markdown("")
st.sidebar.markdown("")
st.sidebar.markdown("")

st.sidebar.image("PinClipart.com_tech-clip-art_784177.png",
                 use_column_width=True)


if select == 'Twitter Hashtags':

    searchTerm = st.text_input("Enter Keyword/ Hashtag to Search About:", )
    noOfSearchTerms = int(100)
    noOfSearchTerms = st.text_input(
        "Enter How Many Tweets to Analyze: (Inserting Large value may take longer time to process)", )
    if len(noOfSearchTerms) != 0:
        noOfSearchTerms = int(noOfSearchTerms)
    else:
        noOfSearchTerms = int(100)

    option = st.selectbox(
        'Analyze', ('Select', 'Review Statement', 'Detailed Analysis'))

    if (len(searchTerm) != 0):
        tweets = tweepy.Cursor(api.search, q=searchTerm).items(noOfSearchTerms)

        positive = 0
        negative = 0
        neutral = 0
        polarity = 0

        for tweet in tweets:

            analysis = TextBlob(tweet.text)

            polarity += analysis.sentiment.polarity

            if(analysis.sentiment.polarity == 0):
                neutral += 1

            elif(analysis.sentiment.polarity < 0.00):
                negative += 1

            elif(analysis.sentiment.polarity > 0.00):
                positive += 1

        positive = percentage(positive, noOfSearchTerms)

        negative = percentage(negative, noOfSearchTerms)

        neutral = percentage(neutral, noOfSearchTerms)

        polarity = percentage(polarity, noOfSearchTerms)

        positive = format(positive, '.2f')
        neutral = format(neutral, '.2f')
        negative = format(negative, '.2f')

        if(polarity == 0):
            s = "Neutral"
            s1 = "🙂"
        elif(polarity < 0.00):
            s = "Negative"
            s1 = "😔"
        elif(polarity > 0.00):
            s = "Positve"
            s1 = "😄"

        if option == 'Review Statement':

            st.header("People are Reacting " + s+" on " + searchTerm +
                      " by Analyzing "+str(noOfSearchTerms) + " Recent Tweets."+s1+"\n")

        if option == 'Detailed Analysis':

            st.header('Donut Chart of How People are Reacting on ' + searchTerm +
                      ' by Analyzing '+str(noOfSearchTerms) + ' Recent Tweets.')

            labels = ['Positive ['+str(positive)+'%]', 'Neutral [' +
                      str(neutral)+'%]', 'Negative['+str(negative)+'%]']

            sizes = [positive, neutral, negative]

            fig = go.Figure()

            x = ["Negative", "Positive", "Neutral"]
            y = [negative, positive,  neutral]
            colors = ['green', 'blue', 'red']

            layout = go.Layout(title='Donut Chart on How People are Reacting on ' + searchTerm +
                               ' by Analyzing '+str(noOfSearchTerms) + ' Recent Tweets.',)

            fig = go.Figure(
                data=[go.Pie(labels=labels, values=sizes, hole=.35, )])

            fig.update_traces(marker=dict(colors=colors))

            st.plotly_chart(fig, use_container_width=True)

        st.button("Run")

    else:
        new_title4 = '<p style="font-family:sans-serif; color:Red; font-size: 18px;">Enter Keyword Field is Mandatory</p>'
        st.markdown(new_title4, unsafe_allow_html=True)
        st.button("Re-run")


elif select == 'Single Sentence':
    sentence = st.text_input("Enter a Sentence to Analyze its Sentiment:", )
    ana = TextBlob(sentence)
    submit = st.button('Review Your Sentence')
    if submit:
        if(ana.sentiment.polarity < 0.0 and len(sentence) != 0):
            st.write(""" # Try To Improve! You got a Negative Review :worried:""")

        elif(ana.sentiment.polarity == 0.0 and len(sentence) != 0):
            st.write(
                """ # Good Work, But there's a room for improvement! You got a Neutral Review 🙂""")

        elif(ana.sentiment.polarity > 0.0 and len(sentence) != 0):
            st.write(""" # Great Work There! You got a Positive Review :smile:""")

        elif(len(sentence) == 0):
            new_title3 = '<p style="font-family:sans-serif; color:Red; font-size: 18px;">Enter a Sentence Field is Mandatory</p>'
            st.markdown(new_title3, unsafe_allow_html=True)

    st.markdown("")
    st.markdown("")

    st.image("performing-twitter-sentiment-analysis1-removebg-preview.png",
             use_column_width=True)


elif select == 'Language Translator':
    sentence = st.text_input("Enter a Sentence to Translate:", )
    if len(sentence) != 0:
        ana = TextBlob(sentence)

        option = st.selectbox(
            'Choose Language', ('Select', 'Arabic', 'Chinese', 'English', 'French', 'Hindi', 'Russian', 'Spanish'))

        if option == 'Arabic':
            if ana.detect_language() != 'ar':
                ana = ana.translate(to='ar')

        elif option == 'Chinese':
            if ana.detect_language() != 'zh-CN':
                ana = ana.translate(to='zh-CN')

        elif option == 'English':
            if ana.detect_language() != 'en':
                ana = ana.translate(to='en')

        elif option == 'French':
            if ana.detect_language() != 'fr':
                ana = ana.translate(to='fr')

        elif option == 'Hindi':
            if ana.detect_language() != 'hi':
                ana = ana.translate(to='hi')

        elif option == 'Russian':
            if ana.detect_language() != 'ru':
                ana = ana.translate(to='ru')

        elif option == 'Spanish':
            if ana.detect_language() != 'es':
                ana = ana.translate(to='es')

        st.success(ana)

    st.button('Run')

    st.markdown("")

    st.image("Language-Translator-2-600x280-removebg-preview.png", width=370)

elif select == 'Multiple Reviews':
    filename2 = st.file_uploader(
        "Select file", type=[".xlsx", ".xls", ".csv"],)

    if filename2 is not None:
        df = pd.read_csv(filename2)
        st.write(df)
    st.header("Sample CSV File:")
    df = pd.read_csv('file.csv')
    st.dataframe(df)

    positive = 0
    negative = 0
    neutral = 0
    polarity = 0
    noOfSearchTerms = 0

    with open('file.csv') as file:
        reader = csv.DictReader(file)

        for row in reader:
            analysis = TextBlob(row['Reviews'])

            polarity += analysis.sentiment.polarity

            if(analysis.sentiment.polarity == 0):
                neutral += 1

            elif(analysis.sentiment.polarity < 0.00):
                negative += 1

            elif(analysis.sentiment.polarity > 0.00):
                positive += 1

            noOfSearchTerms += 1

        positive = percentage(positive, noOfSearchTerms)

        negative = percentage(negative, noOfSearchTerms)

        neutral = percentage(neutral, noOfSearchTerms)

        polarity = percentage(polarity, noOfSearchTerms)

        positive = format(positive, '.2f')
        neutral = format(neutral, '.2f')
        negative = format(negative, '.2f')

        st.markdown("")
        st.header('Donut Chart of Sample CSV Data:')

        labels = ['Positive ['+str(positive)+'%]', 'Neutral [' +
                  str(neutral)+'%]', 'Negative['+str(negative)+'%]']

        sizes = [positive, neutral, negative]

        fig = go.Figure()

        x = ["Negative", "Positive", "Neutral"]
        y = [negative, positive,  neutral]

        colors = ['green', 'blue', 'red']

        layout = go.Layout(title='Donut Chart',)

        fig = go.Figure(
            data=[go.Pie(labels=labels, values=sizes, hole=.4, )])

        fig.update_traces(marker=dict(colors=colors))

        st.plotly_chart(fig, use_container_width=True)

    st.button("Re-run")
