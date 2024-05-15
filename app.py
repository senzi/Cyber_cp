import gradio as gr
import hashlib

def calculate_cp_point(name_A,name_B):
    B = 1.7
    A = 3 * B
    hash1 = hashlib.sha256(name_A.encode()).hexdigest()
    hash2 = hashlib.sha256(name_B.encode()).hexdigest()
    hamming_distance = sum(bit1 != bit2 for bit1, bit2 in zip(hash1, hash2))
    hamming_point = 64 - hamming_distance
    distance_list = [abs(ord(bit1) - ord(bit2)) if bit1.isalpha() and bit2.isalpha() else 0
                     for bit1, bit2 in zip(hash1, hash2)]
    distance_sum = sum(distance_list)
    cp_point = A * hamming_point + B * distance_sum
    return [hash1,hash2,cp_point]   

with gr.Blocks() as demo:
    with gr.Row():
        gr.Markdown("#Cyber CP Demo")
    with gr.Row():
        with gr.Column(scale=1):
            name_A = gr.Textbox(label="A的名字")
            hash_A = gr.Textbox(label="Hash_A")
        with gr.Column(scale=1):
            name_B = gr.Textbox(label="B的名字")
            hash_B = gr.Textbox(label="Hash_B")
    with gr.Row():
        cp_button = gr.Button("计算cp值")
    with gr.Row():
        cp_point = gr.Number("cp值")
        cp_button.click(calculate_cp_point, [name_A,name_B], [hash_A,hash_B,cp_point])


demo.queue()
demo.launch(inbrowser=True)