import gradio as gr
import hashlib

moldP_list = [
    "温和内敛",
    "热情奔放",
    "率真耿直",
    "沉着稳重",
    "古灵精怪"
]

moldN_list = [
    "暴躁易怒",
    "情感淡漠",
    "优柔寡断",
    "沉默寡言",
    "胆小怯懦",
    "敏感脆弱"
]

traitsP_list = [
    "富有想象力，擅长战略性规划",
    "富有创造力，且充满好奇心",
    "富有个人魅力，善于鼓舞、领导他人",
    "意志力强大，擅长解决问题",
    "聪明好奇，热衷于发现和挑战",
    "善于观察总结，能提出有效的建议",
    "生性浪漫，善良且乐于助人",
    "风趣幽默，乐于社交且自由自在",
    "重情重义，喜欢和家人、朋友在一起",
    "言出必行，十分可靠",
    "善于倾听，有化解冲突的能力",
    "直觉敏锐，且善于实践",
    "有独到的审美造诣，擅于用创作表达"
]

traitsN_list = [
    "无法独立生活，十分依赖于他人",
    "缺乏同理心，有较高犯罪天赋",
    "偏执任性、顽固不化",
    "意志力薄弱、难以保持原则",
    "生性多疑、难以信任他人",
    "不善于表达、时常会无意间伤害他人",
    "过分追求理念、时常苛责他人",
    "斤斤计较、患得患失，让人难以接近",
    "习惯性逃避，会把问题堆积到无可挽回的地步",
    "有很强的控制欲，时常会伤害到周围的人"
]

def get_mold_and_trait(name):
    # 计算name的sha256哈希值
    sha256_hash = hashlib.sha256(name.encode()).hexdigest()
    
    # 根据sha256第1个字符ascii的奇偶性选择mold列表
    mold_list = moldP_list if int(sha256_hash[0], 16) % 2 == 0 else moldN_list
    mold_polarity = 'P' if mold_list == moldP_list else 'N'
    
    # 根据sha256第2、3字符代表的hex转成十进制选择mold
    mold_index = int(sha256_hash[1:3], 16) % len(mold_list)
    mold = mold_list[mold_index]
    
    # 根据sha256第4个字符ascii的奇偶性选择traits列表
    traits_list = traitsP_list if int(sha256_hash[3], 16) % 2 == 0 else traitsN_list
    traits_polarity = 'P' if traits_list == traitsP_list else 'N'
    
    # 根据sha256第5、6字符代表的hex转成十进制选择traits
    traits_index = int(sha256_hash[4:6], 16) % len(traits_list)
    traits = traits_list[traits_index]
    
    # 根据mold和traits的极性拼接字符串
    if mold_polarity == traits_polarity:
        connector = "，且"
    else:
        connector = "，但"
    
    result = f"{mold}{connector}{traits}"
    
    return result

def select_story_type(name_A, name_B):
    # 拼接两个字符串
    concatenated_name = name_A + name_B
    
    # 计算SHA-256哈希值
    sha256_hash = hashlib.sha256(concatenated_name.encode()).hexdigest()
    
    # 将哈希值转换为十进制
    decimal_hash = int(sha256_hash, 16)
    
    # 定义故事类型列表
    story_types = [
        "相爱相杀冤家型",
        "青梅竹马养成型",
        "平平淡淡温情型",
        "一见倾心梦幻型",
        "轰轰烈烈激倩型",
        "青涩懵懂青春型",
        "互相讨厌培养型",
        "互相折磨病娇型",
        "又甜又真日常型",
        "催人泪下悲情型"
    ]
    
    # 使用mod操作符选择故事类型
    selected_story_type = story_types[decimal_hash % len(story_types)]
    
    return selected_story_type

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

def calculate_story(name_A,name_B):
    resultA = get_mold_and_trait(name_A)
    resultB = get_mold_and_trait(name_B)
    story = select_story_type(name_A, name_B)
    output_string = f"{name_A}:{resultA}\n{name_B}:{resultB}\n请根据他们的性格特点，写一个关于{story}的故事。"
    return output_string

with gr.Blocks() as demo:
    with gr.Row():
        gr.Markdown("# Cyber CP Demo")
    with gr.Row():
        with gr.Column(scale=1):
            name_A = gr.Textbox(label="A的名字")
            hash_A = gr.Textbox(label="Hash_A")
        with gr.Column(scale=1):
            name_B = gr.Textbox(label="B的名字")
            hash_B = gr.Textbox(label="Hash_B")
    with gr.Row():
        with gr.Column(scale=1):
            cp_button = gr.Button("计算cp值")
            story_button = gr.Button("生成故事Prompt")
    with gr.Row():
        with gr.Column(scale=1):
            cp_point = gr.Number(label="cp值")
            story_output = gr.Textbox(label="故事Prompt",show_label=True,show_copy_button=True)
            cp_button.click(calculate_cp_point, [name_A,name_B], [hash_A,hash_B,cp_point])
            story_button.click(calculate_story, [name_A,name_B], story_output)
            gr.Markdown("请将上述Prompt复制后交给Kimi生成故事：[Kimi.ai - 帮你看更大的世界](https://kimi.moonshot.cn/chat/)\nhttps://kimi.moonshot.cn/chat/")


demo.queue()
demo.launch(inbrowser=True)