cd $env:APPDATA;
cd .minecraft;
new-item ./mods/old-mods;
move-item -Path ./mods/* -destination ./mods/old-mods;
Invoke-WebRequest -Uri https://raw.githubusercontent.com/tec-fox/repos-gfs/main/mods.zip -OutFile mods.zip;
Expand-Archive ./mods.zip;
Remove-Item –path ./mods.zip
