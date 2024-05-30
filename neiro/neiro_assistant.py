import requests
async def get_response(message_text):
    prompt = {
  "modelUri": "gpt://b1gi5u5svdb4thh7hkdk/yandexgpt-lite",
  "completionOptions": {
    "stream": False,
    "temperature": 0.9,
    "maxTokens": "2000"
  },
  "messages": [
    {
      "role": "system",
      "text": "Ты - проффесионально умеешь улучшать запросы пользователя, он пишет запрос, ты его улучшаешь и передаешь в нейронную сеть для генерации картинки"
    },
    {
      "role": "user",
      "text": message_text
    }
  ]
}

    url = "https://llm.api.cloud.yandex.net/foundationModels/v1/completion"
    headers = {
        "Content-Type": "application/json",
        "Authorization": "Api-Key AQVNxSbP7DyphtPgoEjPSEA3cd9MJWGM6NRPpDyJ"
    }

    response = requests.post(url, headers=headers, json=prompt)
    result = response.json()
    return result['result']['alternatives'][0]['message']['text']
