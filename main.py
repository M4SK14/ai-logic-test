# Simple script to simulate a prompt analysis
def evaluate_prompt(prompt):
    if len(prompt) < 5:
        return "Prompt too short"
    return "Valid prompt for AI processing"

user_prompt = "Explique o que é aprendizado de máquina."
print(f"Testing prompt: '{user_prompt}'")
print(f"Result: {evaluate_prompt(user_prompt)}")
