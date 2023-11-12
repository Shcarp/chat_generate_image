from openai import OpenAI

api_key = f"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"

client = OpenAI(api_key=api_key)

print(client.fine_tuning.jobs.list(limit=10))

# res = client.fine_tuning.jobs.retrieve("ftjob-ehp5EjOjanxTWTZ52oc0q8Ld")

# print(res)
