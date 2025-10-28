import re
import csv
import os

def analyze_log(file_path, output_path):
    """Analyze log file, count errors/warnings, and list active IPs."""
    
    if not os.path.exists(file_path):
        print(f"❌ File {file_path} not found!")
        return

    errors = 0
    warnings = 0
    ip_counts = {}

    with open(file_path, "r") as file:
        for line in file:
            if "ERROR" in line:
                errors += 1
            elif "WARNING" in line:
                warnings += 1

            match = re.search(r'(\d+\.\d+\.\d+\.\d+)', line)
            if match:
                ip = match.group(1)
                ip_counts[ip] = ip_counts.get(ip, 0) + 1

    # Save report
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w", newline="") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["IP Address", "Requests"])
        for ip, count in ip_counts.items():
            writer.writerow([ip, count])

    # Print results
    print("✅ Analysis completed successfully!")
    print(f"Total Errors: {errors}")
    print(f"Total Warnings: {warnings}")
    print(f"📁 Report saved at: {output_path}")

if __name__ == "__main__":
    input_file = "data/sample_log.txt"
    output_file = "output/report.csv"
    analyze_log(input_file, output_file)