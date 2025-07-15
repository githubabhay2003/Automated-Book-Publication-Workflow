from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
import os
import textwrap

# Load FLAN-T5
model_name = "google/flan-t5-base"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSeq2SeqLM.from_pretrained(model_name)

# Chunking utility
def chunk_text(text, max_words=200):
    words = text.split()
    for i in range(0, len(words), max_words):
        yield " ".join(words[i:i + max_words])

# Define prompts
def writer_prompt(chunk):
    return f"Rephrase and enrich the following story content with a modern and dramatic tone:\n\n{chunk}"

def reviewer_prompt(chunk):
    return f"Polish the following for clarity, grammar, and tone in narrative fiction style:\n\n{chunk}"

# Generation utility
def generate_text(prompt):
    inputs = tokenizer(prompt, return_tensors="pt", truncation=True, max_length=512)
    output = model.generate(
        **inputs,
        max_new_tokens=512,
        do_sample=True,
        temperature=0.7,
        top_p=0.9
    )
    return tokenizer.decode(output[0], skip_special_tokens=True)

# ✅ MAIN FUNCTION TO EXPORT
def generate_ai_review():
    # Load the raw chapter
    with open("output/chapter_text.txt", "r", encoding="utf-8") as f:
        raw_text = f.read()

    final_output = []
    for chunk in chunk_text(raw_text, max_words=200):
        written = generate_text(writer_prompt(chunk))
        reviewed = generate_text(reviewer_prompt(written))
        final_output.append(reviewed)

    # Combine and save
    full_text = "\n\n".join(final_output)
    output_path = "output/final_reviewed_chapter.txt"
    os.makedirs("output", exist_ok=True)

    with open(output_path, "w", encoding="utf-8") as f:
        f.write(full_text)

    print(f"[✓] Final AI-reviewed chapter saved to: {output_path}")