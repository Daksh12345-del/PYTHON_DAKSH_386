#curl is a command line utility for transferring data with URLs. It supports various protocols, including HTTP, HTTPS, FTP, and more. With curl, you can perform a wide range of tasks such as downloading files, sending HTTP requests, and interacting with APIs.
#command line utility for curl is a utility used in pythin at terminal

import argparse
import requests
# Source - https://stackoverflow.com/a/16696317
# Posted by Roman Podlinov, modified by community. See post 'Timeline' for change history
# Retrieved 2026-03-17, License - CC BY-SA 4.0

def download_file(url,local_filename):
    local_filename = url.split('/')[-1]
    # NOTE the stream=True parameter below
    with requests.get(url, stream=True) as r:
        r.raise_for_status()
        with open(local_filename, 'wb') as f:
            for chunk in r.iter_content(chunk_size=8192): 
                # If you have chunk encoded response uncomment if
                # and set chunk_size parameter to None.
                #if chunk: 
                f.write(chunk)
    return local_filename

parser = argparse.ArgumentParser()

#Add command line arguments
parser.add_argument("arg1", help="Description of argument 1")
# parser.add_argument("-o", "--optional", help="Description of argument 2",default=None)
parser.add_argument("-o", "--output", help="Description of argument 2",default=None)
#Parse the command line arguments
args = parser.parse_args()

#Access the arguments
print("Argument 1:", args.arg1)
print("Argument 2:", args.arg2)
download_file(args.arg1, args.output)