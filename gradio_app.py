import gradio as gr
from clearml import Task

def greet(name):
    return "Hallo " + name + "!"

Task.init(project_name='gradio test',take_name='gradio_erez')
demo = gr.Interface(fn=greet, inputs="text", outputs="text")

demo.launch()