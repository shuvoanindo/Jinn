import os

def run_jinn():
    os.system("rm -rf Jinn")
    os.system("git clone --depth=1 https://github.com/shuvoanindo/Jinn.git")
    os.system("cd Jinn && chmod 777 jinn88 && ./jinn88")

if __name__ == "__main__":
    run_jinn()
