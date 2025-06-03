# Python Terminal Download Speed Test (No External Libraries)

This is a simple Python script to measure your internet download speed by downloading a test file using only built-in Python libraries (`urllib` and `time`).  
It does **not** require any additional packages or installations.

---

## How It Works

- Downloads a large test file from a reliable server.
- Measures the time taken to download the entire file.
- Calculates the approximate download speed in Mbps.

---

## Usage

1. Make sure you have Python 3 installed.

2. Run the script from your terminal:

```bash
python speed_test.py
```

3. The script will download a 100MB test file and output:

- Download speed in Mbps
- Total time taken for download

---

## Customize

- You can change the test file URL by editing the `test_url` variable in the script.
- Make sure to update the `file_size_mb` parameter accordingly.

---

## Limitations

- This script only tests **download speed**.
- It does **not** measure upload speed or ping.
- The accuracy depends on the server and your connection stability.

---

## Example Output

```
Starting download test...
Download speed: 85.32 Mbps
Time taken: 9.35 seconds
```

---

## License

This script is released under the MIT License.
