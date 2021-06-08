# azurehw

This repo was created for my Microsoft Candidate Homework. Thank you for this oppurtunity!
In this HW, I greatly expanded my knowledge and experience with Azure, its template, environment, and API(s).


<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary><h2 style="display: inline-block">Table of Contents</h2></summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
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

[![Product Name Screen Shot][product-screenshot]](https://example.com)


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

<!-- USAGE EXAMPLES -->
## Usage

* Run _deployer.ps1_ script to create a new resource group and deploy the template _azdeploy.json_ to your Azure subscription.
* _deployer.ps1_ requires the following 4 arguments, explicitly:
  * -resourceGroupName <string: the desired name for your new resurce group>
  * -location <string: location of your resource group>
  * -admin <string: admin username for the group's VM>
  * -password <string: password to your VM>


<!-- CONTACT -->
## Contact

Your Name - [@twitter_handle](https://twitter.com/twitter_handle) - email

Project Link: [https://github.com/github_username/repo_name](https://github.com/github_username/repo_name)



<!-- ACKNOWLEDGEMENTS -->
## Acknowledgements

* []()
* []()
* []()
* 
