from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
import os

app = FastAPI()

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://intellect7-ai.web.app"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def read_root():
    return {"message": "API is running"}

@app.get("/result.html")
async def get_result_page():
    return {"message": "Result page is not available in this version"}

@app.post("/analyze-resume")
async def analyze_resume(
    resume_file: UploadFile = File(...),
    job_description_file: UploadFile = File(None),
    job_description_text: str = File(None)
):
    # For now, ignore the file/text contents and return the mock response
    mock_response = {
        "Match Score": 0,
        "Key Matched Skills": [],
        "Gaps in Required Skills or Experience": [
            "python",
            "4 years of experience"
        ],
        "Brief Explanation": "The resume does not meet any of the explicitly stated requirements in the job description. The job description requires 3 years of experience with Python, which is not mentioned in the resume. Therefore, 0% of the required qualifications were met.",
        "Experience Analysis": {
            "Company-wise Experience Summary": [
                "Infosys Limited – Technology Analyst – From December 2021 to May 2025 – Duration: 3 years 6 months"
            ],
            "Total Work Experience": "3 years 6 months",
            "Experience Match": "No",
            "Is Fresher?": "No",
            "Date Issues": "None"
        },
        "LinkedIn Profile Check": "No LinkedIn URL found",
        "Email Check": "rkamalesh123@gmail.com",
        "Freelancer or Contractor Check": "No"
    }
    return mock_response

if __name__ == "__main__":
    import uvicorn
    port = int(os.environ.get("PORT", 10000))
    uvicorn.run(app, host="0.0.0.0", port=port)
