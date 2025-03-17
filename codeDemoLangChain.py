from langchain.chat_models import ChatOpenAI
from langchain.schema import SystemMessage, HumanMessage
import os

# Đặt API Key của OpenAI (cần thay bằng API Key của bạn)
os.environ["OPENAI_API_KEY"] = ""

# Khởi tạo mô hình GPT từ OpenAI
chat_model = ChatOpenAI(model_name="gpt-3.5-turbo")

def chat_with_langchain():
    print("Chatbot LangChain - Nhập 'exit' để thoát")
    while True:
        user_input = input("Bạn: ")
        if user_input.lower() == "exit":
            break
        
        # Tạo lời nhắc cho mô hình
        messages = [
            SystemMessage(content="Bạn là một trợ lý AI hữu ích."),
            HumanMessage(content=user_input)
        ]
        
        # Gửi tin nhắn và nhận phản hồi
        response = chat_model(messages)
        print("Chatbot:", response.content)

if __name__ == "__main__":
    chat_with_langchain()
