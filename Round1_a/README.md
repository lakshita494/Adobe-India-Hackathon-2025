# Challenge 1a: PDF Processing Solution

## Overview
This is a **solution** for Challenge 1a of the Adobe India Hackathon 2025. The challenge requires implementing a PDF processing solution that extracts structured data (title and outline/headings) from PDF documents and outputs JSON files. The solution is containerized using Docker and meets the specified performance and resource constraints.

## Official Challenge Guidelines

### Submission Requirements
- **GitHub Project**: Complete code repository with working solution
- **Dockerfile**: Must be present in the root directory and functional
- **README.md**: Documentation explaining the solution, models, and libraries used

### Build Command
```bash
docker build --platform linux/amd64 -t mysolutionname:test .
```

### Run Command
```bash
docker run --rm -v ${PWD}/app/input:/app/input -v ${PWD}/app/output:/app/output --network none mysolutionname
```

### Critical Constraints
- **Execution Time**: ≤ 10 seconds for a 50-page PDF
- **Model Size**: ≤ 200MB (if using ML models)
- **Network**: No internet access allowed during runtime execution
- **Runtime**: Must run on CPU (amd64) with 8 CPUs and 16 GB RAM
- **Architecture**: Must work on AMD64, not ARM-specific

### Key Requirements
- **Automatic Processing**: Process all PDFs from `/app/input` directory
- **Output Format**: Generate `filename.json` for each `filename.pdf`
- **Input Directory**: Read-only access only
- **Open Source**: All libraries, models, and tools must be open source
- **Cross-Platform**: Test on both simple and complex PDFs

## Solution Structure
```
Round1_a/
├── app/
│   ├── input/           # Input PDF files directory
│   │   ├── Introduction_to_Cybersecurity_and_Screen_Readers.pdf
│   │   ├── Introduction_to_Cybersecurity_and_Keyboard_Navigation.pdf
│   │   └── sequential circuit.pdf
│   └── output/          # Generated JSON output files directory
│       ├── Introduction_to_Cybersecurity_and_Screen_Readers.json
│       ├── Introduction_to_Cybersecurity_and_Keyboard_Navigation.json
│       └── sequential circuit.json
├── Dockerfile           # Docker container configuration
├── main.py              # PDF processing script
├── requirements.txt     # Python dependencies
└── README.md            # This file
```

## Implementation Details

### Main Processing Script (`main.py`)
- Scans all PDF files in `/app/input`.
- For each PDF:
  - Extracts the document title (from metadata or largest text on first page).
  - Detects headings (H1, H2, H3) using font size, boldness, capitalization, and numbering heuristics.
  - Outputs a JSON file with the extracted structure to `/app/output/filename.json`.
- Handles errors gracefully and prints processing status for each file.

### Libraries Used
- **PyMuPDF (fitz)**: For fast, accurate, and offline PDF parsing ([PyMuPDF documentation](https://pymupdf.readthedocs.io/)).

### Docker Configuration
- Uses `python:3.10-slim` base image for AMD64.
- Installs dependencies from `requirements.txt`.
- Sets up `/app/input` and `/app/output` directories.
- Entry point runs `main.py`.

#### Sample Dockerfile
```dockerfile
FROM --platform=linux/amd64 python:3.10-slim
WORKDIR /app
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
COPY main.py ./
RUN mkdir -p /app/input /app/output
ENTRYPOINT ["python", "main.py"]
```

## Expected Output Format
Each PDF generates a corresponding JSON file with the following structure:
```json
{
  "title": "Document Title",
  "outline": [
    { "level": "H1", "text": "Heading 1", "page": 1 },
    { "level": "H2", "text": "Subheading", "page": 2 },
    ...
  ]
}
```

## Implementation Guidelines
- **Memory Management**: Efficient handling of large PDFs
- **Processing Speed**: Optimized for sub-10-second execution
- **Resource Usage**: Stays within 16GB RAM constraint
- **CPU Utilization**: Efficient use of 8 CPU cores

## Testing Your Solution

### Local Testing
```bash
# Build the Docker image
docker build --platform linux/amd64 -t mysolutionname:test .

# Prepare input/output directories
mkdir -p app/input app/output
# Place your PDFs in app/input

# Run the solution
docker run --rm -v ${PWD}/app/input:/app/input -v ${PWD}/app/output:/app/output --network none mysolutionname
```

### Validation Checklist
- [ ] All PDFs in input directory are processed
- [ ] JSON output files are generated for each PDF
- [ ] Output format matches required structure
- [ ] Processing completes within 10 seconds for 50-page PDFs
- [ ] Solution works without internet access
- [ ] Memory usage stays within 16GB limit
- [ ] Compatible with AMD64 architecture

---

**Note**: This implementation is designed to meet all official challenge requirements and constraints. For any queries, please refer to the challenge documentation or contact the team lead. 