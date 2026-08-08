import requests
import json
import csv

# Configuration - PASTE YOUR ABUSEIPDB API KEY HERE
API_KEY = 'YOUR_ABUSEIPDB_API_KEY_HERE'
OUTPUT_FILE = 'threat_intel_report.csv'

# Sample list of malicious IPs collected from your lab network or firewalls
suspicious_ips = [
    '185.220.101.5',   # Known Tor Exit Node
    '45.142.120.21',   # Known Scanner IP
    '192.168.1.1',     # Internal Safe IP (Control test)
    '8.8.8.8'          # Safe Google DNS (Control test)
]

def check_ip(ip_address):
    url = 'https://abuseipdb.com'
    querystring = {
        'ipAddress': ip_address,
        'maxAgeInDays': '90'
    }
    headers = {
        'Accept': 'application/json',
        'Key': API_KEY
    }
    
    try:
        response = requests.get(url, headers=headers, params=querystring)
        if response.status_code == 200:
            return response.json()['data']
        else:
            print(f"Error checking {ip_address}: Status code {response.status_code}")
            return None
    except Exception as e:
        print(f"Connection failed for {ip_address}: {e}")
        return None

def main():
    print("[*] Launching Automated Threat Intelligence Lookup...")
    
    with open(OUTPUT_FILE, mode='w', newline='') as file:
        writer = csv.writer(file)
        # Define clean column layout for the final report
        writer.writerow(['IP Address', 'Is Public', 'Abuse Score (%)', 'Total Reports', 'Country', 'Usage Type'])
        
        for ip in suspicious_ips:
            print(f"[*] Processing Indicator: {ip}")
            data = check_ip(ip)
            
            if data:
                writer.writerow([
                    data.get('ipAddress'),
                    data.get('isPublic'),
                    data.get('abuseConfidenceScore'),
                    data.get('totalReports'),
                    data.get('countryCode'),
                    data.get('usageType')
                ])
                
    print(f"[+] Enrichment Complete! Output saved to: {OUTPUT_FILE}")

if __name__ == '__main__':
    main()
