import plugins.gpt4free.writesonic as openai_api


def chat_init(history):
    # history_data  = [
    #     {
    #         'is_sent': True,
    #         'message': 'my name is Tekky'
    #     },
    #     {
    #         'is_sent': False,
    #         'message': 'hello Tekky'
    #     }
    # ]
    history_data = []
    if history is not None:
        history_data = []
        for i, old_chat in enumerate(history):
            if  old_chat['role'] == "user":
                history_data.append({
                    'is_sent': True,
                    'message': old_chat['content']
                })
            elif old_chat['role'] == "AI" or old_chat['role'] == 'assistant':
                history_data.append({
                    'is_sent': False,
                    'message': old_chat['content']
                })
    return history_data


def chat_one(prompt, history_formatted, max_length, top_p, temperature, zhishiku=False):
    response = openai_api.Completion.create(
    api_key = account.key,
    prompt  = prompt,
    enable_memory = True,
    history_data  = history_formatted
)
    yield response.completion.choices[0].text


account = None


def load_model():
    global account
    print("create account (3-4s)")
    account = openai_api.Account.create(logging=True)

    # simple completion
    response = openai_api.Completion.create(
        api_key=account.key,
        prompt='hello world'
    )

    # Hello! How may I assist you today?
    print("apitest:", response.completion.choices[0].text)
