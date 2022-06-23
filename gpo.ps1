Write-Host "Export GPO" -ForegroundColor Yellow 
cmd.exe /c "gpresult.exe /x gpreport.xml /F" 


[xml]$xml = Get-Content -Path .\backup\gpreport.xml 


$audit = '[{"name":"Audit Registry","value":1},{"name":"Audit Directory Service Changes","value":1},{"name":"Audit Security Group Management","value":1},{"name":"Audit Special Logon","value":1},{"name":"Audit Logon","value":3},{"name":"Audit Account Lockout","value":1},{"name":"Audit Other Account Management Events","value":1},{"name":"Audit Sensitive Privilege Use","value":1},{"name":"Audit Audit Policy Change","value":1},{"name":"Audit User Account Management","value":1},{"name":"Audit Process Creation","value":1}]' |ConvertFrom-Json

$policy = @("Include command line in process creation events","Turn on Module Logging","Turn on PowerShell Script Block Logging")


$gpoAudit = $xml.DocumentElement.ComputerResults.ExtensionData.Extension.AuditSetting
Write-Host "CHECK THE CONFIG GPO" -ForegroundColor Yellow 
Write-Host ""
Write-Host ""
$audit | ForEach-Object {
    $i =  $_

    if( $i.name -in $gpoAudit.SubcategoryName){
        $gpoAudit | Where-Object SubcategoryName -eq $i.name|ForEach-Object  {
            if($_.SettingValue -eq $i.value){
                Write-Host ($i.name,"is Enabled") -ForegroundColor Green
            }
            else{
                Write-Host ($i.name,"is not Enabled") -ForegroundColor Red
            }
        }
        # 
    }
    else{
        Write-Host ($i.name,"is not Enabled") -ForegroundColor Red
    }
}
Write-Host ""
Write-Host ""
Write-Host "CHECK THE CONFIG Policy" -ForegroundColor Yellow 
Write-Host ""
Write-Host ""
$policyConfig= $xml.DocumentElement.ComputerResults.ExtensionData.Extension.Policy
$policy |ForEach-Object {
    $i  = $_
    if($i -in $policyConfig.Name){
        $policyConfig | Where-Object Name -eq $i|ForEach-Object{
            if($policyConfig.State -eq "Enabled"){
                Write-Host ($i,"is Enabled") -ForegroundColor Green
            }
            else{
                Write-Host ($i,"is not Enabled") -ForegroundColor Red
            }
        }
    }
    else{
        Write-Host ($i,"is not Enabled") -ForegroundColor Red
    }

}
