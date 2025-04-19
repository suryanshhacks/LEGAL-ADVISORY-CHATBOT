from langchain.embeddings import OllamaEmbeddings
from langchain.vectorstores import Chroma
from langchain.chains import RetrievalQA
from langchain.llms import Ollama
from webscraper import scrape_multiple_urls
from langchain.chains import ConversationalRetrievalChain, LLMChain
from langchain.prompts import PromptTemplate
from langchain.memory import ConversationBufferMemory
from langchain.chains.question_answering import load_qa_chain

def index_legal_documents(urls, persist_dir = "db"):
    all_docs = scrape_multiple_urls(urls)
    embeddings = OllamaEmbeddings(model = "mistral")
    vectordb = Chroma.from_documents(all_docs, embeddings, persist_directory = persist_dir)
    vectordb.persist()
    return vectordb

def setup_qa_chain(vectordb):
    llm = Ollama(model="mistral")
    retriever = vectordb.as_retriever()
    memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)
    combine_docs_chain = load_qa_chain(llm, chain_type="stuff")
    question_prompt = PromptTemplate.from_template(
        "Given the following conversation and a follow-up question, rephrase the follow-up to be a standalone question.\n\nChat History:\n{chat_history}\nFollow-Up Question: {question}\nStandalone Question:"
    )
    question_generator = LLMChain(llm=llm, prompt=question_prompt)
    qa_chain = ConversationalRetrievalChain(
        retriever=retriever,
        combine_docs_chain=combine_docs_chain,
        question_generator=question_generator,
        memory=memory
    )
    return qa_chain

