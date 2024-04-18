from prompt_templates import memory_prompt_template
from langchain.chains import LLMChain
from langchain.memory import ConversationBufferWindowMemory
from langchain.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from utils import load_config
from dotenv import load_dotenv

config = load_config()
load_dotenv()

def create_llm():
    llm = ChatOpenAI(model="gpt-4-turbo",temperature=0.7)
    return llm

def create_embeddings():
    ...
    
def create_chat_memory(chat_history):
    return ConversationBufferWindowMemory(memory_key="history", chat_memory=chat_history, k=3)

def create_prompt_from_template(template):
    return PromptTemplate.from_template(template)

def create_llm_chain(llm, chat_prompt, memory):
    return LLMChain(llm=llm, prompt=chat_prompt, memory = memory)
    
def load_normal_chain(chat_history):
    return chatChain(chat_history)


class chatChain:

    def __init__(self, chat_history):
        self.memory = create_chat_memory(chat_history)
        llm = create_llm()
        chat_prompt = create_prompt_from_template(memory_prompt_template)
        self.llm_chain = create_llm_chain(llm, chat_prompt, self.memory)

    def run(self, user_input):
        return self.llm_chain.run(human_input = user_input, history = self.memory.chat_memory.messages, stop = ['Human:'] )