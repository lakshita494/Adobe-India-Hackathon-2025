import os
import json
import fitz  
from datetime import datetime

def process_collection(collection_path):
    """Process a single collection and generate output"""
    input_file = os.path.join(collection_path, "challenge1b_input.json")
    output_file = os.path.join(collection_path, "challenge1b_output.json")
    
    if not os.path.exists(input_file):
        print(f"[Warning] Input file not found: {input_file}")
        return
    
    # Read input data
    with open(input_file, "r") as f:
        input_data = json.load(f)
    
    persona = input_data.get("persona", "Unknown Persona")
    job = input_data.get("job", "Unknown Job")
    documents = input_data.get("documents", [])
    
    extracted_sections = []
    subsection_analysis = []
    
    # Process each document
    for doc_path in documents:
        full_doc_path = os.path.join(collection_path, doc_path)
        if not os.path.exists(full_doc_path):
            print(f"[Warning] File not found: {full_doc_path}")
            continue
        
        try:
            doc = fitz.open(full_doc_path)
            first_page = doc.load_page(0)
            text = first_page.get_text()
            
            extracted_sections.append({
                "document": doc_path,
                "page": 1,
                "section_title": "Auto Section Title",  
                "importance_rank": 1
            })
            
            subsection_analysis.append({
                "document": doc_path,
                "refined_text": text[:500],  
                "page": 1
            })
            
        except Exception as e:
            print(f"[Error] Failed to process {full_doc_path}: {str(e)}")
    
    # Create output data
    output_data = {
        "metadata": {
            "input_documents": documents,
            "persona": persona,
            "job": job,
            "timestamp": datetime.now().isoformat()
        },
        "extracted_sections": extracted_sections,
        "subsection_analysis": subsection_analysis
    }
    
    # Save output
    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(output_data, f, indent=2)
    
    print(f"✅ Processed {os.path.basename(collection_path)} - Output saved to: {output_file}")

def main():
    """Process all collections in Challenge_1b directory"""
    challenge_dir = "Challenge_1b"
    
    if not os.path.exists(challenge_dir):
        print(f"[Error] {challenge_dir} directory not found!")
        return
    
    collections = ["Collection_1", "Collection_2", "Collection_3"]
    
    for collection in collections:
        collection_path = os.path.join(challenge_dir, collection)
        if os.path.exists(collection_path):
            print(f"\n🔄 Processing {collection}...")
            process_collection(collection_path)
        else:
            print(f"[Warning] Collection directory not found: {collection_path}")

if __name__ == "__main__":
    main() 