import subprocess
import time
import sys
import datetime

def log(msg):
    print(f"[{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] {msg}", flush=True)

def main():
    while True:
        log("启动 main.py ...")
        try:
            proc = subprocess.Popen([sys.executable, "main.py"])
            proc.wait()
            code = proc.returncode
            log(f"main.py 退出，返回码：{code}，5秒后重启")
        except Exception as e:
            log(f"守护进程异常：{e}，5秒后重试")
        time.sleep(5)

if __name__ == "__main__":
    main()