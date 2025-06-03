import urllib.request
import time

def test_download_speed(url, file_size_mb):
    print("Starting download test...")

    start_time = time.time()
    with urllib.request.urlopen(url) as response:
        while True:
            chunk = response.read(1024 * 1024)  # Read in 1MB chunks
            if not chunk:
                break
    end_time = time.time()

    elapsed_time = end_time - start_time
    speed_mbps = file_size_mb / elapsed_time

    print(f"Download speed: {speed_mbps:.2f} Mbps")
    print(f"Time taken: {elapsed_time:.2f} seconds")

if __name__ == "__main__":
    # ~100MB test file from Hetzner (Germany)
    test_url = "http://speed.hetzner.de/100MB.bin"
    test_download_speed(test_url, 100)
