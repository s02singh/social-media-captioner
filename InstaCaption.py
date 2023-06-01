#pip install openai
import openai

#OpenAI API credentials
openai.api_key = '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'

def generate_caption(prompt):
    #Create chat completion request
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ]
    )

    #Extract caption from the response
    caption = response['choices'][0]['message']['content']

    return caption

image_caption = 'a computer desk with a monitor and a keyboard.'
prompt = "Generate a short rhyming Instagram caption using the prompt: " + image_caption
caption = generate_caption(prompt)
print("Generated caption:", caption)
