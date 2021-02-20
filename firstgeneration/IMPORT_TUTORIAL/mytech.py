# Technology example which starts from the demolib PDK in IPKISS.
# As the layers existing in your GDSII files may not be in the demolib TECH - we will add
# them to the technology here. Each layer needs to be a ProcessPurpose layer.
# Here we will add two layers that use the 1 process.
# In the long run it is best to create your own TECH file for your process. demolib is a good example but Luceda can do it for you as service.

import demolib.all as pdk
# from technologies import silicon_photonics
import ipkiss3.all as i3
TECH = i3.TECH
# print TECH
TECH.name = "CUSTOMIZED TECHNOLOGY SAMPLE"

from ipkiss.process import ProcessLayer, ProcessPurposeLayer, PatternPurpose
from ipkiss.technology.technology import TechnologyTree
from ipkiss.visualisation.display_style import DisplayStyle, DisplayStyleSet
from ipkiss.visualisation import color

# We create 1 new process and 2 new purposes and add them to the TECH tree
new_process = ProcessLayer(name="NEW_PROCESS", extension="NEWP")
new_purpose_1 = PatternPurpose(name="PATTERN_1", extension="PAT_1")
new_purpose_2 = PatternPurpose(name="PATTERN_2", extension="PAT_2")

TECH.PROCESS.NEW_PROCESS = new_process
TECH.PPLAYER.NEW_PROCESS = TechnologyTree()

# We combine the process and purposes into PPlayers and add them to the TECH tree.
TECH.PPLAYER.NEW_PROCESS.PP1 = ProcessPurposeLayer(process=new_process,
                                                   purpose=new_purpose_1,
                                                   name="PP1")

TECH.PPLAYER.NEW_PROCESS.PP2 = ProcessPurposeLayer(process=new_process,
                                                   purpose=new_purpose_2,
                                                   name="PP2")

# Add the layer to the GDSII import/export rules. These are the GDSII process and purpose numbers used in your existing gdsii files.
gdsii_maps = {(new_process, new_purpose_1): (99, 1),
              (new_process, new_purpose_2): (99, 2)}

TECH.GDSII.LAYERTABLE.update(gdsii_maps)

# Add the layer to the visualization styleset
DISPLAY_PP1 = DisplayStyle(color=color.COLOR_YELLOW, alpha=0.5, edgewidth=1.0)
DISPLAY_PP2 = DisplayStyle(color=color.COLOR_YELLOW, alpha=0.2, edgewidth=1.0)

TECH.DISPLAY.DEFAULT_DISPLAY_STYLE_SET.append((TECH.PPLAYER.NEW_PROCESS.PP1, DISPLAY_PP1))
TECH.DISPLAY.DEFAULT_DISPLAY_STYLE_SET.append((TECH.PPLAYER.NEW_PROCESS.PP2, DISPLAY_PP2))



