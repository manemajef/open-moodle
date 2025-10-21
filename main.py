import os, subprocess

def main():
    base = os.path.dirname(os.path.abspath(__file__))
    python_path = os.path.join(base, ".venv/bin/python3")
    subprocess.run([python_path, "-m", "app.main"], cwd=base)

if __name__ == "__main__":
    main()
