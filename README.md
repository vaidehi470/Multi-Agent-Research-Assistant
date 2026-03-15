# Multi-Agent-Research-Assistant

This project implements a multi-agent AI system that autonomously researches and generates a structured report on emerging Generative AI (GenAI) use cases in FMCG supply chains.

The system uses a collaborative agent architecture where each agent performs a specialized role such as planning the research, retrieving information, generating insights, and reviewing the final output.

The workflow follows a structured pipeline:

Planner → Researcher → Analyst → Critic → Final Report

The Critic Agent introduces a reflection stage that reviews and improves the generated report before producing the final output

## Setup Instructions
1. Clone the Repository
git clone <repository_url>
cd <repository_name>
2. Create a Virtual Environment
python -m venv venv

#### Activate the environment:

Windows:
venv\Scripts\activate

Mac/Linux:
source venv/bin/activate

#### Install Dependencies
pip install -r requirements.txt

#### Setup Environment Variables
This project requires API keys.
Create a .env file in the project root directory.
Example:
GOOGLE_API_KEY=your_gemini_api_key
SERPER_API_KEY=your_serper_api_key

###### Run the Project
After setting up the environment variables, run:
python main.py

The system will execute the multi-agent pipeline and generate a structured report on GenAI use cases in FMCG supply chains.
