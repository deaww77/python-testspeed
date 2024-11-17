import speedtest as st
from tqdm import tqdm
import time

def Speed_Test():
    print("Starting Speed Test...\n")

    for _ in tqdm(range(100), desc="Testing Internet Speed", ncols=80):
        time.sleep(0.03)

    test = st.Speedtest()
    down_speed = test.download()
    down_speed = round(down_speed / 10**6, 2)
    print("\nDowload Speed in Mbps: ", down_speed)

    up_speed = test.upload()
    up_speed = round(up_speed / 10**6, 2)
    print("Upload Speed n Mbps: ", up_speed)

    ping = test.results.ping
    print("Ping: ", ping)
Speed_Test()