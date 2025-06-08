# What is it?
It's just a small project to Display (and maybe soon control) various Machines in Gregtech.

Possible upcoming features:
- Notification for maintenance issues
- More Reactor stats
- Information about backup battery buffers

# How to run
You need to run ControlPanel.lua on your Gregtech Computer, with your Lapotronic Supercapacitor, Fluid Reactor (with a MFU card) connected. 

The redstone (maintenance) functionality is implemented by another computer. The file just contains numbers, corrosponding to the current maintenance issues.

To make it work, create a config.py file, containing 4 variable definitions:

    frequency_path_name = "frequency_names.txt"
    lapo_sample_path = [your path to outputs\energy_sample.txt]
    redstone_sample_path = [your path to redstone.txt]
    reactor_sample_path = [your path to outputs\reactor_sample.txt]