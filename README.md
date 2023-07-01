# i3-auto-tiler

basic python script to automatically decide how to tile a window based on its size

## Install instructions

### Install dependencies
```
sudo pacman -S python-pip
sudo pacman -S python-i3ipc
```


### Install the script
```
chmod a+x i3-auto-tiler
sudo cp i3-auto-tiler /usr/local/bin/
or
sudo cp i3-auto-tiler /usr/bin/
```

### Add the script to your i3 config
```
exec_always i3-auto-tiler
```
### reload or restart i3
```
i3-msg reload
i3-msg restart
```