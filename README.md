# i3-auto-tiler

## Description
`i3-auto-tiler.py` is a Python script that automatically adjusts the layout of new windows in the i3 window manager based on their dimensions.

## Installation
1. download the script from the releases page using one of the following commands:
   ```shell
   curl -LO https://github.com/HarounAhmad/i3-auto-tiler/releases/download/v1.0.0/i3-auto-tiler
    ```
     ```shell
   wget https://github.com/HarounAhmad/i3-auto-tiler/releases/download/v1.0.0/i3-auto-tiler
    ```
     ```shell
   fetch -o i3-auto-tiler https://github.com/HarounAhmad/i3-auto-tiler/releases/download/v1.0.0/i3-auto-tiler
    ```
2. move the script to a directory in your `$PATH`:
   ```shell
    mv i3-auto-tiler /usr/local/bin
    ```
3. add the following line to your i3 config file:
   ```shell
    exec_always i3-auto-tiler
    ```
4. restart or reload i3:
    ```shell
     i3-msg restart
     i3-msg reload
     ```