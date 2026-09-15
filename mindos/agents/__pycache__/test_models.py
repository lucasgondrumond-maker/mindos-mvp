import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

models = client.models.list()
print("Modelos disponíveis:")
for m in models.data:
    print(f"- {m.id}")
    Set-Content -Path test_models.py -Encoding utf8 -Value 'import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

models = client.models.list()
print("Modelos disponiveis:")
for m in models.data:
    print(f"- {m.id}")'
    