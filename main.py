import subprocess

def main():
    subprocess.run([".venv/bin/python3", "-m", "app.main"])
    print("bye.." ) 
    
if __name__ == "__main__":
    main() 
