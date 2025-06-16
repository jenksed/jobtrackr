# Step 1: Create and activate the virtual environment
python3 -m venv .venv
source .venv/bin/activate  # On Mac/Linux
# .venv\Scripts\activate   # On Windows

# Step 2: Upgrade pip (optional but recommended)
pip install --upgrade pip

# Step 3: Install the core dependencies
pip install streamlit sqlalchemy pandas plotly python-dotenv

# Step 4: Freeze requirements
pip freeze > requirements.txt

