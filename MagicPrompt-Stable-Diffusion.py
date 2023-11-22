import torch
from transformers import AutoTokenizer, AutoModelForCausalLM

model_name = "Gustavosta/MagicPrompt-Stable-Diffusion"

temperature = 0.9              # A higher temperature will produce more diverse results, but with a higher risk of less coherent text
top_k = 8                      # the number of tokens to sample from at each step
max_length = 200               # the maximum number of tokens for the output of the model
repetition_penalty = 1.2       # the penalty value for each repetition of a token
num_return_sequences = 5       # the number of results to generate

tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)

prompt = r"a dog, color cool"  # the beginning of the prompt

input_ids = tokenizer(prompt, return_tensors='pt').input_ids
output = model.generate(
    input_ids,
    do_sample=True,
    temperature=temperature,
    top_k=top_k,
    max_length=max_length,
    num_return_sequences=num_return_sequences,
    repetition_penalty=repetition_penalty,
    early_stopping=True
)

print('\033[96m' + prompt + '\033[0m')
for i in range(len(output)):
    print(tokenizer.decode(output[i], skip_special_tokens=True) + '\n')
