import streamlit as st
import spacy
import en_core_web_sm
from textblob import TextBlob
from gensim.summarization import summarize
# Sumy Summary Pkg
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lex_rank import LexRankSummarizer



# Function for Sumy Summarization
def sumy_summarizer(docx):
	parser = PlaintextParser.from_string(docx,Tokenizer("english"))
	lex_summarizer = LexRankSummarizer()
	summary = lex_summarizer(parser.document,3)
	summary_list = [str(sentence) for sentence in summary]
	result = ' '.join(summary_list)
	return result



def entity_analyzer(my_text):
    nlp = en_core_web_sm.load()
    docx = nlp(my_text)

    tokens = [token.text for token in docx]
    entities = [(entity.text, entity.label_) for entity in docx.ents]
    allData = [ '"Tokens":{}, \n"Entities":{}'.format(tokens, entities)]
    return allData


def text_analyzer(my_text):
    nlp = en_core_web_sm.load()
    docx = nlp(my_text)

    tokens = [token.text for token in docx]
    allData = [ ('"Tokens":{}, \n"Lemma":{}'.format(token.text, token.lemma_)) for token in docx ]
    return allData


def main():
    """ NLP App with Streamlit"""

    st.title('NLP app')
    st.subheader("Natural Language Processing on the go!")

    #Tokenizationç

    if st.checkbox("Show Tokens and Lemma"):
        st.subheader("Tokenize your text")
        message = st.text_area("Enter Your Text", "Type Here", key='a')
        if st.button("Analyze", key='a'):
            nlp_result = text_analyzer(message)
            st.json(nlp_result)

    if st.checkbox("Show Named Entities"):
        st.subheader("Extract Entities from your text")
        message = st.text_area("Enter Your Text", "Type Here", key='b')
        if st.button("Extract"):
            nlp_result = entity_analyzer(message)
            st.json(nlp_result)

    if st.checkbox("Show Sentiment"):
        st.subheader("Sentiment of your text")
        message = st.text_area("Enter Your Text", "Type Here", key='c')
        if st.button("Analyze", key='b'):
            blob = TextBlob(message)
            result_sentiment = blob.sentiment
            st.success(result_sentiment)

    if st.checkbox("Show Text Summarization"):
        st.subheader("Summarize Your Text")
        message = st.text_area("Enter Text","Type Here ..")
        summary_options = st.selectbox("Choose Summarizer",['sumy','gensim'])
        if st.button("Summarize"):
            if summary_options == 'sumy':
                st.text("Using Sumy Summarizer ..")
                summary_result = sumy_summarizer(message)
            elif summary_options == 'gensim':
                st.text("Using Gensim Summarizer ..")
                summary_result = summarize(message)
            else:
                st.warning("Using Default Summarizer")
                st.text("Using Gensim Summarizer ..")
                summary_result = summarize(message)
            st.success(summary_result)

    st.sidebar.subheader("About App")
    st.sidebar.text("NLPiffy App with Streamlit")
    st.sidebar.info("Cudos to the Streamlit Team")

    st.sidebar.subheader("By")
    st.sidebar.text("Jhan")
    st.sidebar.text("jhanettmillanmarcano@gmail.com")



if __name__ == '__main__':
    main()
