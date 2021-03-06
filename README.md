# azurehw

This repo was created for my Microsoft Candidate Homework. Thank you for this oppurtunity!
In this HW, I greatly expanded my knowledge and experience with Azure, its templates, environment, and API(s).


<!-- TABLE OF CONTENTS -->
<h2 style="display: inline-block">Table of Contents</h2>
<details open="open">
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#Content">Content</a></li>
      </ul>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgements">Acknowledgements</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

## Content
* [_first_version_](https://github.com/ahmadmasalhags/azurehw/tree/main/first_version): folder containing the first scripts I wrote for debugging and getting to know the API
* [_1st_submission_](https://github.com/ahmadmasalhags/azurehw/tree/main/1st_submission): folder containing the scripts of the first submission
* [_2nd_submission_](https://github.com/ahmadmasalhags/azurehw/tree/main/2nd_submission): folder containing the scripts updated for the second submission
* [_BLOBs_](https://github.com/ahmadmasalhags/azurehw/tree/main/BLOBs): folder containing scripts for the BLOBs part of the HW:
  * [_blobHandler.py_](https://github.com/ahmadmasalhags/azurehw/blob/main/BLOBs/blobHandler.py): a Python 3 script which creates, uploads, and copies a number of BLOBs between storage accounts.
  * [_parameters.json_](https://github.com/ahmadmasalhags/azurehw/blob/main/BLOBs/parameters.json): a JSON specifiying the paramters needed for running the aforementioned _blobHandler.py_ script.
  * [_blobber.ps1_](https://github.com/ahmadmasalhags/azurehw/blob/main/BLOBs/blobber.ps1): a Powershell script to create a number of text BLOBs, invoked by the _blobHandler.py_ script.
  
  These 3 files _MUST_ remain in the same directory, on the same level, to excute correctly.
  
* [_azdeploy.json_](https://github.com/ahmadmasalhags/azurehw/blob/main/azdeploy.json): ARM template to deploy the following resources:
  * Storage Account _X2_
      * BLOB Container per storage account
   * One _Windows_ VM, with all its requisites:
      * Network security group
      * Public IP address
      * Network interface
      * Virtual network
      * Disk _X2_
* [_azdeploy.parameters.json_](https://github.com/ahmadmasalhags/azurehw/blob/main/azdeploy.parameters.json): parameters for the deployment.
* [_deployer.ps1_](https://github.com/ahmadmasalhags/azurehw/blob/main/deployer.ps1): a powershell script to excute the deployment. Please check out its usage [below](#Usage).


### Built With

* Powershell
* [Azure Powershell](https://docs.microsoft.com/en-us/powershell/azure/install-az-ps?view=azps-6.0.0)
* JSON
* [Python 3](https://www.python.org/downloads/)


### Prerequisites
* Azure Powershell
  ```sh
  Install-Module -Name Az -Scope CurrentUser -Repository PSGallery -Force
  ```
#### On VM:
* Python, using powershell
  ```sh
  Invoke-WebRequest -Uri "https://www.python.org/ftp/python/3.7.0/python-3.7.0.exe" -OutFile "<your_full_path>/python-3.7.0.exe"
  ```
  * add Python to PATH, then:
  ```sh
  python -m pip install --upgrade pip
  pip install azure
  pip install azure-storage-blob --upgrade
  ```

<!-- USAGE EXAMPLES -->
## Usage

* Run [_deployer.ps1_](https://github.com/ahmadmasalhags/azurehw/blob/main/deployer.ps1) script to create a new resource group and deploy the template _azdeploy.json_ to your Azure subscription.
  * _deployer.ps1_ requires the following 4 arguments, explicitly:
    * -resourceGroupName <string: the desired name for your new resource group>
    * -location <string: location of your resource group>
    * -admin <string: admin username for the group's VM>
    * -password <string: password to your VM>
  * From command line:
  ```sh
  >powershell -file deployer.ps1 -resourceGroup X -location Y -admin Z -password W
  ```
  * From Powershell:
  ```sh
  PS $> .\deployer.ps1 -resourceGroupName X -location Y -admin Z -password W
  ```

* First, the script will excute ```Connect-AzAccount```[?](https://docs.microsoft.com/en-us/powershell/module/az.accounts/connect-azaccount?view=azps-6.0.0) to connect to your Azure Account.
* Then, it will create a new resource group with the desired name.
* On Success, the script will have deployed the followig resources:
  * Storage Account _X2_
    * BLOB Container per storage account
  * One _Windows_ VM, with all its requisites:
    * Network security group
    * Public IP address
    * Network interface
    * Virtual network
    * Disk _X2_

### On VM
  * To excute the [_blobHandler.py_](https://github.com/ahmadmasalhags/azurehw/blob/main/BLOBs/blobHandler.py) simply run from command line:
  ```she
  python blobHandler.py
  ```

<!-- CONTACT -->
## Contact

Ahmad Masalha, B.Sc. Software Engineering.

[ahmadmasgs@gmail.com]

[Ahmad Masalha on LinkedIn](https://www.linkedin.com/in/ahmadmasalha/)

<!-- ACKNOWLEDGEMENTS -->
## Acknowledgements

* Gur Rosenberg, Microsoft Israel
* Oron Golan, Microsoft Israel
