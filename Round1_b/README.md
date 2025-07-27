# Round 1b - Document Intelligence Challenge

This project implements a document intelligence system that processes PDF documents and extracts structured information based on user personas and job requirements.

## 🏗️ Project Structure

```
Round1_b/
├── Challenge_1b/                    # Main challenge directory
│   ├── Collection_1/                # Drug Discovery Research
│   │   ├── PDFs/                    # Drug discovery papers
│   │   ├── challenge1b_input.json   # Input configuration
│   │   └── challenge1b_output.json  # Analysis results
│   ├── Collection_2/                # Financial Analysis
│   │   ├── PDFs/                    # Annual reports
│   │   ├── challenge1b_input.json   # Input configuration
│   │   └── challenge1b_output.json  # Analysis results
│   ├── Collection_3/                # Organic Chemistry Study
│   │   ├── PDFs/                    # Chemistry textbooks
│   │   ├── challenge1b_input.json   # Input configuration
│   │   └── challenge1b_output.json  # Analysis results
│   └── README.md                    # Challenge-specific documentation
├── process_collections.py           # Main processing script
├── Dockerfile                       # Docker configuration
├── requirements.txt                 # Python dependencies
└── README.md                        # This file
```

## 🚀 Quick Start

### Option 1: Direct Python Execution (Recommended)

1. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Process All Collections:**
   ```bash
   python process_collections.py
   ```

3. **Process Individual Collection:**
   ```bash
   # Navigate to specific collection
   cd Challenge_1b/Collection_1
   
   # Run processing (from collection directory)
   python ../../process_collections.py
   ```

### Option 2: Docker Execution

1. **Build Docker Image:**
   ```bash
   docker build -t document-intelligence .
   ```

2. **Run with Docker:**
   ```bash
   # Process all collections
   docker run -v $(pwd)/Challenge_1b:/app/Challenge_1b document-intelligence python process_collections.py
   ```

3. **Interactive Docker Session:**
   ```bash
   docker run -it -v $(pwd)/Challenge_1b:/app/Challenge_1b document-intelligence bash
   ```

## 📋 Prerequisites

- Python 3.9 or higher
- pip (Python package manager)
- Docker (optional, for containerized execution)

## 📦 Dependencies

The following Python packages are required:
- `pymupdf` - PDF processing and text extraction
- `sentence-transformers` - Text analysis and processing

## 🔧 Configuration

### Input Format

Each collection has a `challenge1b_input.json` file with the following structure:

```json
{
  "persona": "User Persona Description",
  "job": "Job to be done",
  "documents": [
    "PDFs/document1.pdf",
    "PDFs/document2.pdf",
    "PDFs/document3.pdf"
  ]
}
```

### Output Format

The system generates a `challenge1b_output.json` file containing:

```json
{
  "metadata": {
    "input_documents": ["list of processed documents"],
    "persona": "User persona",
    "job": "Job description",
    "timestamp": "ISO timestamp"
  },
  "extracted_sections": [
    {
      "document": "document path",
      "page": 1,
      "section_title": "Auto Section Title",
      "importance_rank": 1
    }
  ],
  "subsection_analysis": [
    {
      "document": "document path",
      "refined_text": "extracted text (first 500 chars)",
      "page": 1
    }
  ]
}
```

## 📊 Collections Overview

### Collection 1: Drug Discovery Research
- **Persona**: Pharmaceutical Researcher
- **Job**: Research and analyze drug discovery methodologies and processes
- **Documents**: Drug discovery research papers and methodologies

### Collection 2: Financial Analysis
- **Persona**: Financial Analyst
- **Job**: Analyze annual reports and financial performance data
- **Documents**: Annual report PDFs

### Collection 3: Organic Chemistry Study
- **Persona**: Chemistry Student
- **Job**: Study and understand organic chemistry concepts and reactions
- **Documents**: Organic chemistry textbooks and study materials

## 🐳 Docker Information

**Yes, this project supports Docker!** 

The `Dockerfile` is configured to:
- Use Python 3.9 slim image as base
- Install dependencies from `requirements.txt`
- Set working directory to `/app`
- Copy all project files
- Default command runs `main.py`

### Docker Commands Summary

```bash
# Build image
docker build -t document-intelligence .

# Run processing
docker run -v $(pwd)/Challenge_1b:/app/Challenge_1b document-intelligence python process_collections.py

# Interactive shell
docker run -it -v $(pwd)/Challenge_1b:/app/Challenge_1b document-intelligence bash

# Check running containers
docker ps

# Remove containers
docker rm $(docker ps -aq)

# Remove images
docker rmi document-intelligence
```

## 🔍 Troubleshooting

### Common Issues

1. **PDF Processing Errors:**
   - Ensure PDFs are not corrupted
   - Check file permissions
   - Verify PDFs are text-based (not scanned images)

2. **Docker Volume Mount Issues:**
   - Use absolute paths for volume mounting
   - Ensure proper file permissions

3. **Missing Dependencies:**
   - Run `pip install -r requirements.txt`
   - Check Python version compatibility

### Debug Mode

To run with verbose output:
```bash
python process_collections.py --debug
```

## 📝 Development

### Adding New Collections

1. Create new collection directory in `Challenge_1b/`
2. Add PDFs to `PDFs/` subdirectory
3. Create `challenge1b_input.json` with proper configuration
4. Update `process_collections.py` if needed

### Modifying Processing Logic

The main processing logic is in `process_collections.py`. Key functions:
- `process_collection()` - Processes individual collections
- `main()` - Orchestrates processing of all collections

## 📄 License

This project is part of the Adobe India Hackathon 2025.

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

---

**Note**: This project is designed for educational and hackathon purposes. Ensure you have proper permissions for any PDF documents you process. 