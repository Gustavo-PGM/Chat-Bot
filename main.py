import openai

openai.api_key = "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"

teste =[
    {"role": "system", "content": "Seja um bom assistente"},
  ]

usuario = input(" Digite Sua Mensagem: ")
teste.append({"role": "user", "content": usuario})

while usuario != 'Acabou':
    armazem = openai.ChatCompletion.create(
        model = 'gpt-3.5-turbo',
        messages = teste,
        temperature = 0.8,
        max_tokens = 300
    )

    resposta = armazem[0]['message']['content']