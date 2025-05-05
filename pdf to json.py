import json
import pdfplumber
import os
pdf_path=[r"C:\Users\Ali Com\OneDrive\Desktop\LLM_Django\creditfixrr_pdf\Creditfixrr Account Details.pdf",
            r"C:\Users\Ali Com\OneDrive\Desktop\LLM_Django\creditfixrr_pdf\Creditfixrr Account Statuses.pdf",
            r"C:\Users\Ali Com\OneDrive\Desktop\LLM_Django\creditfixrr_pdf\Creditfixrr Account Types.pdf",
            r"C:\Users\Ali Com\OneDrive\Desktop\LLM_Django\creditfixrr_pdf\Creditfixrr Bureau Codes.pdf",
            r"C:\Users\Ali Com\OneDrive\Desktop\LLM_Django\creditfixrr_pdf\Creditfixrr Late Statuses.pdf",
            r"C:\Users\Ali Com\OneDrive\Desktop\LLM_Django\creditfixrr_pdf\Creditfixrr Payment Statuses.pdf",
            r"C:\Users\Ali Com\OneDrive\Desktop\LLM_Django\creditfixrr_pdf\Creditfixrr Public Record Statuses.pdf",
            r"C:\Users\Ali Com\OneDrive\Desktop\LLM_Django\creditfixrr_pdf\Creditfixrr Public Record Type.pdf",
            r"C:\Users\Ali Com\OneDrive\Desktop\LLM_Django\creditfixrr_pdf\Creditfixrr Report CommentsRemarks.pdf",
            r"C:\Users\Ali Com\OneDrive\Desktop\LLM_Django\creditfixrr_pdf\Public Record Industry Types.pdf"]

def extract_headings_and_info(pdf_path):
    """
    Extract headings and corresponding information from a PDF file.
    Assumes headings are distinguishable by formatting (e.g., bold or larger font).
    """
    data = {}
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            text = page.extract_text()
            if text:
                lines = text.split("\n")
                current_heading = None
                for line in lines:
                    # Simple heuristic: Treat lines ending with a colon (:) as headings
                    if line.strip().endswith(":"):
                        current_heading = line.strip()
                        data[current_heading] = ""
                    elif current_heading:
                        # Append info to the last heading
                        data[current_heading] += f"{line.strip()} "
    # Clean up whitespace
    for key in data:
        data[key] = data[key].strip()
    return data

def process_pdfs(pdf_paths, output_json):
    """
    Process a list of PDFs, extracting headings and info, and save as JSON.
    """
    all_data = {}
    for pdf_path in pdf_paths:
        if not os.path.exists(pdf_path):
            print(f"File not found: {pdf_path}")
            continue
        print(f"Processing {pdf_path}...")
        file_name = os.path.basename(pdf_path)
        all_data[file_name] = extract_headings_and_info(pdf_path)
    
    # Save all data to JSON file
    with open(output_json, "w", encoding="utf-8") as json_file:
        json.dump(all_data, json_file, indent=4, ensure_ascii=False)
    print(f"Data saved to {output_json}")

# List of PDF files to process (corrected)
pdf_files = [
    r"C:\Users\Ali Com\OneDrive\Desktop\LLM_Django\creditfixrr_pdf\Creditfixrr Account Details.pdf",
    r"C:\Users\Ali Com\OneDrive\Desktop\LLM_Django\creditfixrr_pdf\Creditfixrr Account Statuses.pdf",
    r"C:\Users\Ali Com\OneDrive\Desktop\LLM_Django\creditfixrr_pdf\Creditfixrr Account Types.pdf",
    r"C:\Users\Ali Com\OneDrive\Desktop\LLM_Django\creditfixrr_pdf\Creditfixrr Bureau Codes.pdf",
    r"C:\Users\Ali Com\OneDrive\Desktop\LLM_Django\creditfixrr_pdf\Creditfixrr Late Statuses.pdf",
    r"C:\Users\Ali Com\OneDrive\Desktop\LLM_Django\creditfixrr_pdf\Creditfixrr Payment Statuses.pdf",
    r"C:\Users\Ali Com\OneDrive\Desktop\LLM_Django\creditfixrr_pdf\Creditfixrr Public Record Statuses.pdf",
    r"C:\Users\Ali Com\OneDrive\Desktop\LLM_Django\creditfixrr_pdf\Creditfixrr Public Record Type.pdf",
    r"C:\Users\Ali Com\OneDrive\Desktop\LLM_Django\creditfixrr_pdf\Creditfixrr Report CommentsRemarks.pdf",
    r"C:\Users\Ali Com\OneDrive\Desktop\LLM_Django\creditfixrr_pdf\Public Record Industry Types.pdf",
]

# Output JSON file
output_json_file = "output_data.json"

# Process the PDFs
process_pdfs(pdf_files, output_json_file)
