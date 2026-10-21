from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv

load_dotenv() 

embedding = OpenAIEmbeddings(model='text-embedding-3-large',  dimensions=32)

docs = [
  "hiiiii", 
  "hello world",
  "anacondaaaaa"]

result = embedding.embed_documents(docs)

print(str(result))

# but this needs openai api key which is paid and i dont have it