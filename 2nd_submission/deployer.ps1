param([ValidateNotNullOrEmpty()][string] $resourceGroupName,
      [ValidateNotNullOrEmpty()][string] $location)

if ($PSBoundParameters.Count -ne 2){
    Write-Error "Please explicitly pass the following 2 parameters:
    -resourceGroupName <string> -location <string>
    "
    exit
}

Connect-AzAccount

try {
    [ValidateNotNullOrEmpty()][string]$admin = Read-Host "Choose a Username for your VM" 
    [ValidateNotNullOrEmpty()][string]$spswrd = Read-Host "Choose a Password for your VM" -AsSecureString
} catch {
    Write-Error -Message "Invalid Username or password - Please enter valid credentials"
    exit 255
}

New-AzResourceGroup -Name $resourceGroupName -Location $location

$Deployment = @{
    Name                  = 'AhmadMasDeployer';
    ResourceGroupName     = $resourceGroupName;
    TemplateFile          = "$PSScriptRoot\azdeploy.json";
    TemplateParameterFile = "$PSScriptRoot\azdeploy.parameters.json";
    adminUsername         = $admin;
    adminPassword         = $spswrd;
    storageName           = 'asm17';
}

New-AzResourceGroupDeployment @Deployment
