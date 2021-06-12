param([ValidateNotNullOrEmpty()][string] $resourceGroupName,
      [ValidateNotNullOrEmpty()][string] $location,
      [ValidateNotNullOrEmpty()][string] $admin,
      [ValidateNotNullOrEmpty()][string] $password)

if ($PSBoundParameters.Count -ne 4){
    Write-Error "Please explicitly pass the following 4 parameters:
    -resourceGroupName <string> -location <string> -admin <string> -password <string>
    "
    exit
}

Connect-AzAccount

New-AzResourceGroup -Name $resourceGroupName -Location $location

$spswrd = ConvertTo-SecureString $password -AsPlainText -Force

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
