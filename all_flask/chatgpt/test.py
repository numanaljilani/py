from openai import OpenAI
# 

client = OpenAI(api_key='')

def GPTclone(prompt):
    response = client.chat.completions.create(
        model = 'gpt-4o-mini',
        messages=[
            {"role" : "system" , "content" : "You are a helpfull assistant."},
            {"role" : "user" , "content": prompt},
            
        ],
        max_tokens=50,
    )
    result = response.choices[0].message.content
    print(result)
    return result

def img(prompt):
    image = client.images.generate(
        model='dell-e-3',
        prompt=prompt,
        n=1,
        size='1024x1024',
    )
    print(image)