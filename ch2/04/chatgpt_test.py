from openai import OpenAI
client = OpenAI()
# Window settings에 미리 환경변수를 setting해 놓았더니 - 실제로 바로 구할 수 있어 매우매우 다행이라고 생각한다.
response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "user", "content": "Python에 대해 알려주세요"},
    ],
)
print(response.choices[0].message.content)
