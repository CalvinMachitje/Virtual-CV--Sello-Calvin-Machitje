import subprocess

file = "app_cv.py"


subprocess.Popen(
    ["streamlit", "run", file], shell=True
)