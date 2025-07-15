import os
from difflib import unified_diff
from nltk.translate.bleu_score import sentence_bleu, SmoothingFunction
import textstat

# File paths
ai_output_path = "output/final_reviewed_chapter.txt"
human_edit_path = "output/human_edited_chapter.txt"
reward_log_path = "output/reward_log.txt"

def reward_bleu(ai_text, human_text):
    """Calculate BLEU score between AI and human-edited sentences."""
    ai_sentences = ai_text.split(". ")
    human_sentences = human_text.split(". ")
    smoothie = SmoothingFunction().method4
    scores = []

    for a, h in zip(ai_sentences, human_sentences):
        ref = [a.strip().split()]
        hyp = h.strip().split()
        if hyp:
            score = sentence_bleu(ref, hyp, smoothing_function=smoothie)
            scores.append(score)

    return sum(scores) / len(scores) if scores else 0.0

def readability_score(text):
    """Calculate Flesch Reading Ease score."""
    return textstat.flesch_reading_ease(text)

def evaluate_human_edit():
    """Main function to compare AI and human text, calculate reward scores, and show diffs."""
    if not os.path.exists(human_edit_path):
        print("[!] Please create 'output/human_edited_chapter.txt' with your changes before scoring.")
        return

    with open(ai_output_path, "r", encoding="utf-8") as f:
        ai_text = f.read()

    with open(human_edit_path, "r", encoding="utf-8") as f:
        human_text = f.read()

    # Calculate reward metrics
    bleu = reward_bleu(ai_text, human_text)
    readability = readability_score(human_text)

    # Save results
    with open(reward_log_path, "w", encoding="utf-8") as f:
        f.write(f"BLEU Similarity Score: {bleu:.4f}\n")
        f.write(f"Flesch Reading Ease (Higher is better): {readability:.2f}\n")

    # Print results
    diff = unified_diff(ai_text.splitlines(), human_text.splitlines(), lineterm='', fromfile='AI', tofile='Human')
    print("[✓] Differences:\n")
    print("\n".join(diff))
    print(f"\n[✓] BLEU Similarity Score: {bleu:.4f}")
    print(f"[✓] Flesch Reading Ease: {readability:.2f}")
    print(f"[✓] Reward scores saved to: {reward_log_path}")

# CLI entry point
if __name__ == "__main__":
    evaluate_human_edit()