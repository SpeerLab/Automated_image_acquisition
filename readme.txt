The master_xml_generator will generate a complete master_run.xml file for use in serial section imaging experiments. 

The script requires the presence of a "bead_positions.txt" file (three positions), a "positions.txt" file (N positions), and a "master_xml.xml" file that
specifies the loop parameters for each sequence of actions to be written to the output xml. The master_xml is built using 
component elements that are located in the "xmls" folder. 

The script requires access to a "python" code directory containing several files related to bead generation, xml appending, and
converting XML formats. These are titled: "append_pauses", "nodeToDict", "daveActions", "bead_position_generator". 


The master_xml also references power progressions for STORM movies which are located in a "powertest" folder and should be 
named "750storm_0001" and "647_storm_0001".


The master_xml_generator currently takes the bead file and position file and generates two rounds of 36 tiled sparse bead fields, 
9 tiled flat-field correction dense bead fields, N conventional movies, and N STORM movies in three colors (750/647/488).  

The parameters established in the current master_xml relate to settings for a 600x600 image field specified in the acquisition/settings folder.
Subfolders here each contain settings and shutter files for different parameter settings, here sorted by active imaging area.

On 2018.7.17, 561nm channel is added to master_xml_hcam.xml. Backup file can be found in C:\Users\Sperry\Desktop\acquisition\BackUp

On 1/24/2019£¬ all .xml moved to xml folder. 