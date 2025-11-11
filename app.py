from dotenv import load_dotenv
load_dotenv()

import streamlit as st

from langchain.chat_models import ChatOpenAI
from langchain.schema import SystemMessage, HumanMessage

def get_llm_answer(input_text: str, selected_item: str) -> str:
    """
    input_text と selected_item を受け取り、LLM の応答文字列を返す。
    """
    if not input_text:
        return "テキストを入力してから実行ボタンを押してください"

    # 選択に応じたシステムプロンプト
    if selected_item == "旅行":
        sm_content = "You are an expert on tourist attractions.For questions unrelated to tourist attractions, respond with '専門外の質問です。'"
    else:
        sm_content = "You are an expert on education.For questions unrelated to education, respond with '専門外の質問です。'"

    # ボタン押下時にインスタンス化して呼び出す（互換性回避）
    llm = ChatOpenAI(model_name="gpt-4o-mini", temperature=0.5)
    messages = [
        SystemMessage(content=sm_content),
        HumanMessage(content=input_text)
    ]
    response = llm.predict_messages(messages)
    return response.content

st.title("いろいろ博士")

st.write("各ジャンルについての質問に答えます！")
st.write("質問したいジャンルを選択し、テキストボックスに質問内容を入力して「実行」ボタンを押してください。")


selected_item = st.radio(
    "何について質問したいですか？",
    ["旅行","教育"]
)

st.divider()

if selected_item == "旅行":
    input_message = st.text_input(label="旅行先や行きたい施設を教えてください。")
else:
    input_message = st.text_input(label="どんなことをお悩みですか？")

if st.button("実行"):
    st.divider()

    if input_message:
        answer = get_llm_answer(input_message, selected_item)
        st.write(answer)
    else:
        st.write("テキストを入力してから実行ボタンを押してください。")
