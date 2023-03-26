# pip install openai
# pip install gpt_index
# pip install PyPDF2
# pip install gradio

from gpt_index import SimpleDirectoryReader, GPTListIndex, GPTSimpleVectorIndex, LLMPredictor, PromptHelper
from langchain import OpenAI
import gradio as gr
import os

os.environ["OPENAI_API_KEY"] = "API_KEY" #Replace AP_KEY with the 

#Setting directory path
path1="direcctory" #Folder "docs" where the scraped data is saved
os.chdir(path1) #Directory path1 is set

def construct_index(directory_path):
    max_input_size = 4096
    num_outputs = 1024
    max_chunk_overlap = 20
    chunk_size_limit = 600

    prompt_helper = PromptHelper(max_input_size, num_outputs, max_chunk_overlap, chunk_size_limit=chunk_size_limit)

    llm_predictor = LLMPredictor(llm=OpenAI(temperature=0.7, model_name="text-davinci-003", max_tokens=num_outputs))

    documents = SimpleDirectoryReader(directory_path).load_data()

    index = GPTSimpleVectorIndex(documents, llm_predictor=llm_predictor, prompt_helper=prompt_helper)

    index.save_to_disk('index.json')

    return index

def chatbot(input_text):
    index = GPTSimpleVectorIndex.load_from_disk('index.json')
    response = index.query(input_text, response_mode="compact")
    return response.response

iface = gr.Interface(fn=chatbot,
                     inputs=gr.inputs.Textbox(lines=7, label="Enter your text"),
                     outputs="text",
                     title="Custom-trained AI Chatbot")

#the files saved in scraped_data folder is used to tune GPT-3
index = construct_index("docs")
iface.launch(share=True)