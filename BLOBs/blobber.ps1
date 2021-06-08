$blobsCount = $args[0]
$destDir = $args[1]

New-Item -ItemType Directory -Force -Path $destDir

For ($i = 1; $i -le $blobsCount; $i++) {
    $number = ($i).ToString('0000')
    $filename = "$destDir\text_$number.txt"
    New-Item  $filename -Force
    Set-Content $filename "This is text file number $i"
}
