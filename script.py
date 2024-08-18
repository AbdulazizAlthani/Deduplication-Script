import argparse
import sys
from tqdm import tqdm
import time

def remove_duplicates(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    unique_lines = list(set(lines))
    unique_lines.sort()

    with tqdm(total=len(unique_lines), desc="Processing", unit="line", ncols=100, leave=True) as pbar:
        with open(output_file, 'w', encoding='utf-8') as file:
            for line in unique_lines:
                file.write(line)
                time.sleep(0.01)  # Simulate work being done for the progress bar
                pbar.update(1)

    print(f"\nDuplicates removed. Filtered content saved to {output_file}")
    print("File processing complete.")

def display_banner():
    banner = r"""
  _____           _             _ _           _   _                _____           _       _   
 |  __ \         | |           | (_)         | | (_)              / ____|         (_)     | |  
 | |  | | ___  __| |_   _ _ __ | |_  ___ __ _| |_ _  ___  _ __   | (___   ___ _ __ _ _ __ | |_ 
 | |  | |/ _ \/ _` | | | | '_ \| | |/ __/ _` | __| |/ _ \| '_ \   \___ \ / __| '__| | '_ \| __|
 | |__| |  __/ (_| | |_| | |_) | | | (_| (_| | |_| | (_) | | | |  ____) | (__| |  | | |_) | |_ 
 |_____/ \___|\__,_|\__,_| .__/|_|_|\___\__,_|\__|_|\___/|_| |_| |_____/ \___|_|  |_| .__/ \__|
                         | |                                                        | |        
                         |_|                                                        |_|        
     Author: Abdulaziz S. Althani
     Version: 1.0
     Linkedin: https://www.linkedin.com/in/abdulaziz-al-thani

"""
    print("\033[91m")
    print(banner)
    print("\033[0m")

def display_instructions():
    instructions = """
1. Open a terminal or command prompt.
2. Navigate to the directory where the script is located.
3. If necessary, install the required libraries by running the following command:
   pip install -r requirements.txt
4. Run the script by entering the following command:
   python script.py -f <input_file>
   Replace <input_file> with the name or path of the text file you want to process.
5. The script will remove the duplicate lines and save the filtered content to the new filtered_<input_file> file.

### Please feel free to contact me on my Linkedin private messages: https://www.linkedin.com/in/abdulaziz-al-thani


"""
    print(instructions)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Remove duplicate lines from a text file.')
    parser.add_argument('-f', '--file', help='Input text file')

    if len(sys.argv) == 1:
        display_banner()
        display_instructions()
        sys.exit(1)

    args = parser.parse_args()

    if args.file:
        input_file = args.file
        output_file = f"filtered_{input_file}"

        remove_duplicates(input_file, output_file)
        display_banner()
        print("The file processing has finished successfully.### Please feel free to contact me on my Linkedin private messages: https://www.linkedin.com/in/abdulaziz-al-thani")
    else:
        display_banner()
        display_instructions()
