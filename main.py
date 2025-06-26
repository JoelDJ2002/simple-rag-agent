from langchain_ollama.llms import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate
from vector import retirever

model = OllamaLLM(model="llama3.2")

template = '''
You are an expert in answering questions about a pizza restraunt.
Here are some relevant reviews : {reviews}
Here is the question to answer: {question}
'''

prompt = ChatPromptTemplate.from_template(template)

chain = prompt | model

while True:
    print("\n\n----------------------------------------")
    user_quesiton = input("Enter your question (or 'exit' to quit): ")
    print("\n\n")
    if user_quesiton.lower() == 'exit':
        break
    reviews = retirever.invoke(user_quesiton)
    result = chain.invoke({
    "reviews": reviews,
    "question": user_quesiton})
    print(result)