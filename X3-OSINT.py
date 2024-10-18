import requests
import time
import random
import pandas as pd
from datetime import datetime
import os

# Simple banner without fancy alignment
BANNER = """
================================================================

██╗  ██╗██████╗        ██████╗ ███████╗██╗███╗   ██╗████████╗
╚██╗██╔╝╚════██╗      ██╔═══██╗██╔════╝██║████╗  ██║╚══██╔══╝
 ╚███╔╝  █████╔╝█████╗██║   ██║███████╗██║██╔██╗ ██║   ██║   
 ██╔██╗  ╚═══██╗╚════╝██║   ██║╚════██║██║██║╚██╗██║   ██║   
██╔╝ ██╗██████╔╝      ╚██████╔╝███████║██║██║ ╚████║   ██║   
╚═╝  ╚═╝╚═════╝        ╚═════╝ ╚══════╝╚═╝╚═╝  ╚═══╝   ╚═╝   
                                                             
Developed by X3NIDE
Github: https://github.com/mubbashirulislam

================================================================
"""

# List of user agents - kept simple
USER_AGENTS = [
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0'
]

def clear_screen():
    # Simple screen clear
    if os.name == 'nt':  # for windows
        os.system('cls')
    else:  # for mac and linux
        os.system('clear')

class SocialMediaChecker:
    def __init__(self):
        # Basic session setup
        self.session = requests.Session()
        self.session.headers['User-Agent'] = random.choice(USER_AGENTS)
        
        # Dictionary of social media sites with simple checks
        self.sites = {
            'Twitter': {
                'url': 'https://twitter.com/{}',
                'not_found_message': "This account doesn't exist"
            },
            'Instagram': {
                'url': 'https://instagram.com/{}',
                'not_found_message': 'Page Not Found'
            },
            'GitHub': {
                'url': 'https://github.com/{}',
                'not_found_message': 'Not Found'
            },
            'Facebook': {
                'url': 'https://facebook.com/{}',
                'not_found_message': 'Page Not Found'
            },
            'Linkedin': {
                'url': 'https://linkedin.com/{}',
                'not_found_message': 'Page Not Found'
            },
            'TikTok': {
                'url': 'https://tiktok.com/@{}',
                'not_found_message': "Couldn't find this account"
            },
            'Reddit': {
                'url': 'https://reddit.com/user/{}',
                'not_found_message': 'Sorry, nobody on Reddit goes by that name'
            },
            'Twitch': {
                'url': 'https://twitch.tv/{}',
                'not_found_message': "Sorry. Unless you've got a time machine"
            },
    
        }

    def check_username(self, username):
        print(f"\nStarting search for username: {username}")
        results = {}
        
        for site_name, site_info in self.sites.items():
            try:
                print(f"Checking {site_name}...", end='', flush=True)
                
                # Make the request
                url = site_info['url'].format(username)
                response = self.session.get(url, timeout=10)
                
                # Simple check if account exists
                if response.status_code == 200 and site_info['not_found_message'] not in response.text:
                    print(" Found!")
                    results[site_name] = {
                        'url': url,
                        'status': 'Active',
                        'checked_on': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                    }
                else:
                    print(" Not found")
                
                # Add delay between requests
                time.sleep(random.uniform(1, 2))
                
            except Exception as e:
                print(f" Error: {str(e)}")
                continue
        
        return results

    def save_results(self, results, username):
        try:
            # Create results folder if it doesn't exist
            if not os.path.exists('results'):
                os.mkdir('results')
            
            # Save to Excel file
            filename = f"results/social_media_{username}_{datetime.now().strftime('%Y%m%d_%H%M')}.xlsx"
            
            # Convert results to DataFrame
            df = pd.DataFrame.from_dict(results, orient='index')
            df.to_excel(filename)
            
            print(f"\nResults saved to {filename}")
            
        except Exception as e:
            print(f"Couldn't save results: {str(e)}")

def main():
    clear_screen()
    print(BANNER)
    
    checker = SocialMediaChecker()
    
    while True:
        print("\nOptions:")
        print("1. Search username")
        print("2. Exit")
        
        choice = input("\nWhat do you want to do? (1 or 2): ")
        
        if choice == '1':
            username = input("\nEnter username to search: ").strip()
            
            if username:
                results = checker.check_username(username)
                
                if results:
                    print("\nFound accounts:")
                    for site, data in results.items():
                        print(f"{site}: {data['url']}")
                    
                    checker.save_results(results, username)
                else:
                    print("\nNo active accounts found!")
                    
            else:
                print("Please enter a valid username!")
                
        elif choice == '2':
            print("\nBye!")
            break
            
        else:
            print("\nPlease choose 1 or 2!")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nProgram stopped!")
    except Exception as e:
        print(f"\nSomething went wrong: {e}")