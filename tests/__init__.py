import subprocess

def start_app():
    return subprocess.Popen(['python3', 'run.py'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

def stop_app(process):
    process.terminate()
