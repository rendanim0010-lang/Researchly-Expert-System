# Investigate Deployment
The web deployment for the Researchly research paper classification system is located in this folder.

## Documents
The Streamlit web application is called `app.py`.
The learned text classification pipeline is called `research_abstract_classifier.pkl`.
The Python dependencies needed to run the program are listed in `requirements.txt`.

## Conditions
It requires Python 3.x. ## Installation
Install the necessary packages by opening a terminal in this deployment folder:

## Launch the Application pip install -r requirements.txt
Launch the Streamlit program by using:
run app.py in streamlit.

Typically, the application will be accessible locally at:
http://localhost:8501

##Employing Researchly
1. Launch the Streamlit program.
2. In the **Research Abstract** field, paste a research abstract.
3. Choose **Classify Abstract**.
4. Either **AI Research** or **Classical Research** are returned by the trained model.

## Model
The final refined SGD classification pipeline created during the project is used in the deployed solution. Raw research abstracts can be supplied directly through the web interface thanks to the pipeline's TF-IDF text feature extraction and trained classifier.


