import gradio as gr

def greet(name):
    return f"Hello, {name}!"

demo = gr.Interface(
    fn=greet,
    inputs=gr.Textbox(placeholder="Enter your name"),
    outputs="text",
    title="Greeting App",
    description="Enter your name and receive a personalized greeting."
)

if __name__ == "__main__":
    demo.launch()
