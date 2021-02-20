from technologies import silicon_photonics
import ipkiss3.all as i3
from ipkiss.technology.technology import TechnologyTree, DelayedInitTechnologyTree
# LAYER DEFINITIONS
# -----------------
#
# lay_mesa = i3.Layer(number = 0, name = "mesa")
# lay_quantum_well = i3.Layer(number = 1, name = "quantum well")
# lay_n_contact = i3.Layer(number = 2, name = "n contact")
# lay_island = i3.Layer(number = 3, name = "island")
# lay_release = i3.Layer(number = 4, name = "release")
# lay_tether = i3.Layer(number = 5, name = "tether")
# lay_p_contact = i3.Layer(number = 6, name = "p contact")
# lay_BCB_etch = i3.Layer(number = 7, name = "BCB etch")
# lay_negative = i3.Layer(number = 8, name = "Boolean")
#
# # print lay_release
# # print lay_release.name
#
# TECH = i3.TECH
#
# from ipkiss.process.layer import PatternPurpose
# TECH.PURPOSE.DRAWETCH = PatternPurpose(name="Waveguide cladding", extension="DRAWETCH")
#
# TECH.PPLAYER.FULL = TechnologyTree()
# TECH.PROCESS.NONE = ProcessLayer("No specific process", "NONE")
#
# RWG_clad= i3.PPLayer(i3.TECH.PROCESS.FULL, i3.TECH.PURPOSE.PERF)
#
# # lay_release = i3.PPLayer(i3.ProcessLayer("waveguide", "WG"), i3.PatternPurpose("waveguide core", "CORE"), number = 4, name = "release")


from ipkiss.process import ProcessLayer, ProcessPurposeLayer, PatternPurpose

TECH = i3.TECH

# Create 1 new process and 2 new purposes and add them to the TECH tree
new_process = ProcessLayer(name="NEW_PROCESS", extension="NEWP")
new_purpose_1 = PatternPurpose(name="PATTERN_1", extension="PAT_1")
new_purpose_2 = PatternPurpose(name="PATTERN_2", extension="PAT_2")

TECH.PROCESS.NEW_PROCESS = new_process

TECH.PPLAYER.NEW_PROCESS = TechnologyTree()

# Combine the process and purposes into PPlayers and add them to the TECH tree.
TECH.PPLAYER.NEW_PROCESS.PP1 = ProcessPurposeLayer(process=new_process,
                                                   purpose=new_purpose_1,
                                                   name="PP1")

TECH.PPLAYER.NEW_PROCESS.PP2 = ProcessPurposeLayer(process=new_process,
                                                   purpose=new_purpose_2,
                                                   name="PP2")

# Add the layer to the GDSII import/export rules.
# These are the GDSII process and purpose numbers used in your existing gdsii files.
gdsii_maps = {(new_process, new_purpose_1) : (99, 1),
              (new_process, new_purpose_2) : (99, 2)}

TECH.GDSII.LAYERTABLE.update(gdsii_maps)
