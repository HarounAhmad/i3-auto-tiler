# i3-auto-tiler

## Description
`i3-auto-tiler.py` is a Python script that automatically adjusts the layout of new windows in the i3 window manager based on their dimensions.

## Prerequisites
- Python 3.x
- i3ipc Python module
- i3 window manager

## Installation
1. Clone the repository or download the `i3-auto-tiler.py` file:
   ```shell
   git clone https://github.com/HarounAhmad/i3-auto-tiler.git
    ```
   
2. install the i3ipc Python module:
   ```shell
   pip install i3ipc
   ```
   or if you have arch linux
   ```shell
   sudo pacman -S python-i3ipc
   ```
3. add the following line to the top of `i3-auto-tiler.py`:
   ```
    #!/usr/bin/env python
    ```
4. change the name of the script to `i3-auto-tiler`:
   ```shell
   mv i3-auto-tiler.py i3-auto-tiler
   ```
5. make the script executable:
   ```shell
   chmod +x i3-auto-tiler
   ```
6. move the script to a directory in your `$PATH`:
   ```shell
    sudo mv i3-auto-tiler /usr/local/bin
    ```
7. add the following line to your i3 config file:
   ```s
    exec_always i3-auto-tiler
    ```
   
   
   
   
   