#check path

$find_path = "C:\Users\huhl\Desktop\devops"


If (Test-path $find_path ) {
    robocopy C:\Users\huhl\Desktop\devops\pf\src_server C:\Users\huhl\Desktop\devops\pf\dest_server *.csv
  }

Else {Write-Host "No file at this location"}

{Write_Host "CVS File Copied Successfully"}
