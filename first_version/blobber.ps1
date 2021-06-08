$storage = "C:"
$dirName= "blobs"

$dirFullPath = "$storage\$dirName"

New-Item -ItemType Directory -Force -Path $dirFullPath

For ($i = 1; $i -le 100; $i++) {
    $filename = "$dirFullPath\text_$i.txt"
    New-Item  $filename
    Set-Content $filename "This is text file number $i"
}

