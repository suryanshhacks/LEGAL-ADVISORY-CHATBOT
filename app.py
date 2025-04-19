import streamlit as it
from main import index_legal_documents, setup_qa_chain

it.set_page_config(page_title = "LEGAL ADVISOR CHATBOT", layout = "centered")
it.title("LEGAL ADVISOR CHATBOT")
it.write("Ask questions based on live scraped legal content!")

default_urls = [
      "https://www.law.cornell.edu/wex/felony",
    "https://www.justia.com/criminal/offenses/",
    "https://www.indiacode.nic.in/handle/123456789/2263",   # Indian Penal Code (IPC)
    "https://indiankanoon.org/doc/1569259/",               # Example: IPC Section 302
    "https://www.bareactslive.com/ACA/ACT1296.HTM",        # The Information Technology Act, 2000
    "https://lawtimesjournal.in/murder-under-indian-penal-code/",
    "https://www.livelaw.in",
    "https://www.livelaw.in/news-updates",
    "https://www.barandbench.com",
    "https://www.barandbench.com/news",
    "https://www.barandbench.com/category/news/litigation-news",
    "https://lawtimesjournal.in/category/legal-news",
    "https://lawtimesjournal.in",
    "https://www.scconline.com/blog",
    "https://www.legalbites.in",
    "https://www.legalbites.in/legal-news"
]
   

urls = it.text_area("Enter URLs (one per line)", "\n".join(default_urls)).splitlines()


if it.button("Scrape and Index Content"): 
    with it.spinner("Scraping..."):
        vectordb = index_legal_documents(urls)
        it.session_state.qa_chain = setup_qa_chain(vectordb)
        it.session_state.chat_history = []
    it.success("Legal content scraped and indexed!")

if "qa_chain" in it.session_state:
    it.divider()
    it.subheader("🧠 Ask a Legal Question")
    question = it.text_input("Your question:", key="user_question")
    if question:
        with it.spinner("Thinking..."):
            response = it.session_state.qa_chain.run(question)
            it.session_state.chat_history.append((question, response))
if "chat_history" in it.session_state:
    it.divider()
    it.subheader("💬 Chat History")
    for q, a in it.session_state.chat_history:
        it.markdown(f"**🧑 You:** {q}")
        it.markdown(f"**🤖 Bot:** {a}")