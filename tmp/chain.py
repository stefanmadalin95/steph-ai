from dotenv import load_dotenv
from langchain.chains import LLMChain
from langchain.chat_models import ChatOpenAI
from langchain.memory import ConversationBufferMemory
from langchain.prompts import PromptTemplate

load_dotenv()

def create_llm_chain():
    template = PromptTemplate(
        input_variables = ["chat_history", "human_input"],
        template = """You are a helpfull chatbot, having a conversation with a human.
        {chat_history}
        Human: {human_input}
        Chatbot:"""
    )
    memory = ConversationBufferMemory(memory_key="chat_history")
    llm_chain = LLMChain(
        llm=ChatOpenAI(model="gpt-4-turbo",temperature=0.7),
        memory=memory,
        prompt=template,
        verbose=True
    )
    return llm_chain
    