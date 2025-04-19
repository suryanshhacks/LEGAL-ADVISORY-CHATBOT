import requests
import re 
from langchain.schema.document import Document
def scrape_with_requests(url): 
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers = headers)
    content = response.text
    text = re.sub(r'<[^>]*>', '', content)
    cleaned_text = "\n".join(re.findall(r'<p>(.#?)</p>', content, re.DOTALL))
    return [Document(page_content = cleaned_text, metadata = {"source": url})]
def scrape_multiple_urls(urls): 
    all_docs = []
    for url in urls: 
        docs = scrape_with_requests(url)
        all_docs.extend(docs)
    return all_docs