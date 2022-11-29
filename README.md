Klipper Clear M73 Plugin
========================

Reset progress bar to return control to virtual_sdcard.

Why this exists
---------------

By default the `display_status` module uses `virtual_sdcard` to manage updating the progress bar during a print. However, the progress bar can be manually set to any value using the `M73` command. I use this in my print start macro to show progress during probing, etc. Unfortunately once an `M73` command is issued there is no way to release control back to `virtual_sdcard` when the actual print begins. This plugin provides a command to do this.


Installation
------------

To install, clone repo into your rpi home folder and run `install.sh`.

Then, add `[clear_m73]` somewhere in your klipper configuration to enable the plugin.


Usage
-----

Use `CLEAR_M73` in your gcode macros or execute from the klipper console.
