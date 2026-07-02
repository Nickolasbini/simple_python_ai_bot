import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=os.getenv("OPENROUTER_API_KEY"),
)

print("Assistente iniciado! Digite 'sair' para encerrar.\n")

while True:
    pergunta = input("Você: ")

    if pergunta.lower() == "sair":
        print("Até a próxima!")
        break

    resposta = client.chat.completions.create(
        model="cohere/north-mini-code:free",
        messages=[
            {"role": "user", "content": pergunta}
        ]
    )

    print(f"IA: {resposta.choices[0].message.content}\n")