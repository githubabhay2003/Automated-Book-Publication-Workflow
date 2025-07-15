# run_pipeline.py

from human_editor import evaluate_human_edit  # updated function name
from voice_agent import speak_text
from chroma_manager import add_versioned_text, semantic_search
import os

def main():
    # Step 1: Generate AI-reviewed chapter (from updated ai_writer_chunked.py)
    print("[⚙️] Generating AI-reviewed chapter...")
    os.system("python ai_writer_chunked.py")  # calls the updated script that saves the reviewed chapter

    # Step 2: Voice output (read the reviewed chapter aloud)
    ai_output_path = "output/final_reviewed_chapter.txt"
    if os.path.exists(ai_output_path):
        with open(ai_output_path, "r", encoding="utf-8") as f:
            content = f.read()
        print("[🔊] Reading chapter aloud via voice agent...")
        speak_text(content)
    else:
        print("[❌] Missing AI output at:", ai_output_path)
        return

    # Step 3: Log version into ChromaDB
    print("[🧠] Logging version into ChromaDB...")
    add_versioned_text("v1_final_ai", content, {"stage": "AI Final", "version": 1})

    # Step 4: Evaluate human edit
    print("[📊] Evaluating human-edited version with reward scoring...")
    evaluate_human_edit()

    # Step 5: Semantic search example
    print("\n🔎 Example semantic search for 'Karolin':")
    result = semantic_search("Karolin")
    print(result)

if __name__ == "__main__":
    main()