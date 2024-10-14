# DDLH API Examples
This repository has some DDLH Rest API examples. For now it just outlines how to get an access token and use it in requests.  
config.yaml file should include valid credentials for DDLH setup which is read by ddlh_api.py. 

### Requirements
- Credentials for a DDLH system user (i.e., dv-admin)
- Secret for the dv-amin-rest client (acquired from DDLH Keycloak IAM managent interface)
- Windows Server 2022, Windows 11 (might work with other Windows flavours and versions but untested)
- Python for Windows version 3.12.6 (might work with earlier versions but untested)

### Installation

1. Install [Python for Windows](https://www.python.org/downloads)
   - Select "Add Python to environment variables" in Advanced Options
   - Select "Disable Windows path limit" in the last step
2. Install [Git for Windows](https://git-scm.com/download/win)  
3. Switch into desired drive (i.e., "E"), create "programs" folder and clone this repository under "programs" directory
```console
E:  
mkdir programs  
cd programs  
git clone https://github.com/baris-saltik/ddlh-api-examples  
```
4. Switch into self-describing-media-archives directory, create a virtual Python environment named ".venv" and activate that environment.
```console
cd self-ddlh-api-examples  
python -m venv .venv  
.venv\Scripts\activate.bat  
```
5. Install required Python packages
```console
python -m pip install -r Requirements.txt
```
6. Launch the application
    -  Edit the "/config.yaml" configuration file with respective credentials
    -  Enable/Disable method calls in the main section of the "ddlh_api.py" file (section that starts "if __name__ == "__main__:")
    -  Run the following:
   ```console
   python ddlh_api.py
   ```