$rg = 'ahmadmasgroup'
New-AzResourceGroup -Name $rg -Location 'East US'


$password = "adminus1706Sus"
$spswrd = ConvertTo-SecureString $password -AsPlainText -Force

$Deployment = @{
    Name                  = 'AhmadMasHW';
    ResourceGroupName     = $rg;
    TemplateFile          = "$PSScriptRoot\azdep.json";
    TemplateParameterFile = "$PSScriptRoot\azdep.parameters.json";
    adminUsername         = 'adminus';
    adminPassword         = $spswrd;
    storageName           = 'asm17';
}

New-AzResourceGroupDeployment @Deployment
