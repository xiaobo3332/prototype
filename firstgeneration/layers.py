############################################################################################
# Layer setting:
# 
# This file defines the process layer and purpose layers
# # Extra layers and purposes are defined for IPKISS, IPKISS.eda and PICAZZO usage (see comment)
############################################################################################

from ipkiss.technology.technology import ProcessTechnologyTree, TechnologyTree
from ipkiss.process.layer import ProcessLayer
from ipkiss.technology import get_technology

TECH = get_technology()

#################
# Process layers
#################

TECH.PROCESS = ProcessTechnologyTree()

# FEOL
# SOI/poly patterning
TECH.PROCESS.SHALL = ProcessLayer(name="SiN Waveguide (shallow half-depth etched SiN)", extension="SHALL")
TECH.PROCESS.FULL = ProcessLayer(name="SiN waveguide (full etched SiN)", extension="FULL")
TECH.PROCESS.CLROUT = ProcessLayer(name="", extension="CLROUT")
TECH.PROCESS.OPCLAD = ProcessLayer(name="Clad opening etch", extension="OPCLAD")
TECH.PROCESS.ELEC = ProcessLayer(name="elec", extension="electrode")
TECH.PROCESS.TRENCH = ProcessLayer(name="trench", extension="trench")

# Auxiliary
TECH.PROCESS.NO_DRC = ProcessLayer(name="", extension="NO_DRC")
TECH.PROCESS.DUMMY = ProcessLayer(name="", extension="DUMMY")
TECH.PROCESS.DOC = ProcessLayer(name="", extension="DOC")
TECH.PROCESS.TXTLAB = ProcessLayer(name="" , extension="TXTLAB")
TECH.PROCESS.ERRFLG = ProcessLayer(name="", extension="ERRFLG")
TECH.PROCESS.NO_SIZE = ProcessLayer(name="", extension="NO_SIZE")
TECH.PROCESS.NO_GEN = ProcessLayer(name="", extension="NO_GEN")
TECH.PROCESS.RED_FILL = ProcessLayer(name="", extension="RED_FILL")
TECH.PROCESS.NO_FILL = ProcessLayer(name="", extension="NO_FILL")
TECH.PROCESS.NO_DHOL = ProcessLayer(name="", extension="NO_DHOL")
TECH.PROCESS.COVER = ProcessLayer(name="" , extension="COVER")
TECH.PROCESS.CHIPEDGE = ProcessLayer(name="", extension="CHIPEDGE")
TECH.PROCESS.NO_INSP = ProcessLayer(name="", extension="NO_INSP")
TECH.PROCESS.MASKBRD = ProcessLayer(name="", extension="MASKBRD")
TECH.PROCESS.WAFERBRD = ProcessLayer(name="", extension="WAFERBRD")

#Required for IPKISS compatibility
TECH.PROCESS.NONE = ProcessLayer("No specific process", "NONE")
#Required for PICAZZO compatibility
TECH.PROCESS.SK = TECH.PROCESS.FC = TECH.PROCESS.SHALL
TECH.PROCESS.WG = TECH.PROCESS.FULL

###########################
# Drawing pattern purposes
###########################

from ipkiss.process.layer import PatternPurpose
TECH.PURPOSE = TechnologyTree()
# actual mask drawings
TECH.PURPOSE.DRAWETCH = PatternPurpose(name="Waveguide cladding", extension="DRAWETCH")
TECH.PURPOSE.PERF = PatternPurpose(name="Waveguide core", extension="PERF")
TECH.PURPOSE.PERFSLOT = PatternPurpose(name="Slot etched on waveguide core", extension="PERFSLOT")
TECH.PURPOSE.DRAWING = PatternPurpose(name ="", extension = "DRAWING")
# auxiliary data
TECH.PURPOSE.POLTXT = PatternPurpose(name="", extension="POLTXT")
TECH.PURPOSE.TILING = PatternPurpose(name="", extension="TILING")
TECH.PURPOSE.DATAPREP = PatternPurpose(name ="", extension = "DATAPREP")
TECH.PURPOSE.NOFILL = PatternPurpose(name ="", extension = "NOFILL")
TECH.PURPOSE.NOSIZE = PatternPurpose(name ="", extension = "NOSIZE")
TECH.PURPOSE.NODRC = PatternPurpose(name ="", extension = "NODRC")
# ipkiss defined keys
TECH.PURPOSE.LF = TechnologyTree()
TECH.PURPOSE.DF = TechnologyTree()
TECH.PURPOSE.LF_AREA = PatternPurpose(name="Light-field area", extension="LFAREA")
TECH.PURPOSE.DF_AREA = PatternPurpose(name="Dark-field area", extension="DFAREA")
TECH.PURPOSE.LF.LINE = PatternPurpose(name="Light-field line", extension="LFLINE")
TECH.PURPOSE.DF.LINE = PatternPurpose(name="Dark-field line", extension="DFLINE")
TECH.PURPOSE.DF.POLYGON = PatternPurpose(name="Dark-field polygon", extension="POLYGON")
#Required by IPKISS compatibility
TECH.PURPOSE.ERROR = PatternPurpose(name="Error", extension="ERR", doc="Errors")
TECH.PURPOSE.PINREC = PatternPurpose(name="Pin recognition", extension="PIN", doc="Pin marker for extraction")
#required by PICAZZO
TECH.PURPOSE.TEXT = PatternPurpose(name = "Text", extension = "TEXT")
TECH.PURPOSE.TRACE = PatternPurpose(name = "Trace of waveguide template", extension = "TRACE")
TECH.PURPOSE.BBOX = PatternPurpose(name = "Bounding Box", extension = "BBOX")

########################
# Process-Purpose layers
########################

from ipkiss.process.layer import PPLayer
TECH.PPLAYER = TechnologyTree()

### shallow half-depth etched SiN ###
TECH.PPLAYER.SHALL = TechnologyTree()
TECH.PPLAYER.SHALL.DRAWETCH  = PPLayer(TECH.PROCESS.SHALL, TECH.PURPOSE.DRAWETCH, name="SHALL_DRAWETCH")
TECH.PPLAYER.SHALL.PERF      = PPLayer(TECH.PROCESS.SHALL, TECH.PURPOSE.PERF, name="SHALL_PERF")
TECH.PPLAYER.SHALL.PERFSLOT  = PPLayer(TECH.PROCESS.SHALL, TECH.PURPOSE.PERFSLOT, name="SHALL_PERFSLOT")
TECH.PPLAYER.SHALL.POLTXT    = PPLayer(TECH.PROCESS.SHALL, TECH.PURPOSE.POLTXT, name="SHALL_POLTXT")
TECH.PPLAYER.SHALL.TILING    = PPLayer(TECH.PROCESS.SHALL, TECH.PURPOSE.TILING, name="SHALL_TILING")
TECH.PPLAYER.SHALL.DATAPREP  = PPLayer(TECH.PROCESS.SHALL, TECH.PURPOSE.DATAPREP, name="SHALL_DATAPREP")
TECH.PPLAYER.SHALL.NOFILL    = PPLayer(TECH.PROCESS.SHALL, TECH.PURPOSE.NOFILL, name="SHALL_NOFILL")
TECH.PPLAYER.SHALL.NOSIZE    = PPLayer(TECH.PROCESS.SHALL, TECH.PURPOSE.NOSIZE, name="SHALL_NOSIZE")
TECH.PPLAYER.SHALL.NODRC     = PPLayer(TECH.PROCESS.SHALL, TECH.PURPOSE.NODRC, name="SHALL_NODRC")

### full etched SiN ###
TECH.PPLAYER.FULL = TechnologyTree()
TECH.PPLAYER.FULL.DRAWETCH   = PPLayer(TECH.PROCESS.FULL, TECH.PURPOSE.DRAWETCH, name="FULL_DRAWETCH")
TECH.PPLAYER.FULL.PERF       = PPLayer(TECH.PROCESS.FULL, TECH.PURPOSE.PERF, name="FULL_PERF")
TECH.PPLAYER.FULL.PERFSLOT   = PPLayer(TECH.PROCESS.FULL, TECH.PURPOSE.PERFSLOT, name="FULL_PERFSLOT")
TECH.PPLAYER.FULL.POLTXT     = PPLayer(TECH.PROCESS.FULL, TECH.PURPOSE.POLTXT, name="FULL_POLTXT")
TECH.PPLAYER.FULL.TILING     = PPLayer(TECH.PROCESS.FULL, TECH.PURPOSE.TILING, name="FULL_TILING")
TECH.PPLAYER.FULL.DATAPREP   = PPLayer(TECH.PROCESS.FULL, TECH.PURPOSE.DATAPREP, name="FULL_DATAPREP")
TECH.PPLAYER.FULL.NOFILL     = PPLayer(TECH.PROCESS.FULL, TECH.PURPOSE.NOFILL, name="FULL_NOFILL")
TECH.PPLAYER.FULL.NOSIZE     = PPLayer(TECH.PROCESS.FULL, TECH.PURPOSE.NOSIZE, name="FULL_NOSIZE")
TECH.PPLAYER.FULL.NODRC      = PPLayer(TECH.PROCESS.FULL, TECH.PURPOSE.NODRC, name="FULL_NODRC")

###  ###
TECH.PPLAYER.CLROUT = TechnologyTree()
TECH.PPLAYER.CLROUT.DRAWING = PPLayer(TECH.PROCESS.CLROUT, TECH.PURPOSE.DRAWING, name="CLROUT_DRAWING")

### Clad opening etch ###
TECH.PPLAYER.OPCLAD = TechnologyTree()
TECH.PPLAYER.OPCLAD.DRAWING  = PPLayer(process=TECH.PROCESS.OPCLAD, purpose=TECH.PURPOSE.DRAWING, name="OPCLAD_DRAWING")
TECH.PPLAYER.OPCLAD.PERF     = PPLayer(process=TECH.PROCESS.OPCLAD, purpose=TECH.PURPOSE.PERF, name="OPCLAD_PERF")
TECH.PPLAYER.OPCLAD.TILING   = PPLayer(process=TECH.PROCESS.OPCLAD, purpose=TECH.PURPOSE.TILING, name="OPCLAD_TILING")
TECH.PPLAYER.OPCLAD.NOSIZE   = PPLayer(process=TECH.PROCESS.OPCLAD, purpose=TECH.PURPOSE.NOSIZE, name="OPCLAD_NOSIZE")
TECH.PPLAYER.OPCLAD.NODRC    = PPLayer(process=TECH.PROCESS.OPCLAD, purpose=TECH.PURPOSE.NODRC, name="OPCLAD_NODRC")

### Auxiliary ###
TECH.PPLAYER.NO_DRC = TechnologyTree()
TECH.PPLAYER.NO_DRC.DRAWING  = PPLayer(TECH.PROCESS.NO_DRC, TECH.PURPOSE.DRAWING, name="NO_DRC_DRAWING")
TECH.PPLAYER.DUMMY = TechnologyTree()
TECH.PPLAYER.DUMMY.DRAWING   = PPLayer(TECH.PROCESS.DUMMY, TECH.PURPOSE.DRAWING, name="DUMMY_DRAWING")
TECH.PPLAYER.DOC = TechnologyTree()
TECH.PPLAYER.DOC.DRAWING     = PPLayer(TECH.PROCESS.DOC, TECH.PURPOSE.DRAWING, name="DOC_DRAWING")
TECH.PPLAYER.TXTLAB = TechnologyTree()
TECH.PPLAYER.TXTLAB.DRAWING  = PPLayer(TECH.PROCESS.TXTLAB, TECH.PURPOSE.DRAWING, name="TXTLAB_DRAWING")
TECH.PPLAYER.ERRFLG = TechnologyTree()
TECH.PPLAYER.ERRFLG.DRAWING  = PPLayer(TECH.PROCESS.ERRFLG, TECH.PURPOSE.DRAWING, name="ERRFLG_DRAWING")
TECH.PPLAYER.NO_SIZE = TechnologyTree()
TECH.PPLAYER.NO_SIZE.DRAWING = PPLayer(TECH.PROCESS.NO_SIZE, TECH.PURPOSE.DRAWING, name="NO_SIZE_DRAWING")
TECH.PPLAYER.NO_GEN = TechnologyTree()
TECH.PPLAYER.NO_GEN.DRAWING  = PPLayer(TECH.PROCESS.NO_GEN, TECH.PURPOSE.DRAWING, name="NO_GEN_DRAWING")
TECH.PPLAYER.RED_FILL = TechnologyTree()
TECH.PPLAYER.RED_FILL.DRAWING= PPLayer(TECH.PROCESS.RED_FILL, TECH.PURPOSE.DRAWING, name="RED_FILL_DRAWING")
TECH.PPLAYER.NO_FILL = TechnologyTree()
TECH.PPLAYER.NO_FILL.DRAWING = PPLayer(TECH.PROCESS.NO_FILL, TECH.PURPOSE.DRAWING, name="NO_FILL_DRAWING")
TECH.PPLAYER.NO_DHOL = TechnologyTree()
TECH.PPLAYER.NO_DHOL.DRAWING = PPLayer(TECH.PROCESS.NO_DHOL, TECH.PURPOSE.DRAWING, name="DHOL_DRAWING")
TECH.PPLAYER.COVER = TechnologyTree()
TECH.PPLAYER.COVER.DRAWING   = PPLayer(TECH.PROCESS.COVER, TECH.PURPOSE.DRAWING, name="COVER_DRAWING")
TECH.PPLAYER.CHIPEDGE = TechnologyTree()
TECH.PPLAYER.CHIPEDGE.DRAWING= PPLayer(TECH.PROCESS.CHIPEDGE, TECH.PURPOSE.DRAWING, name="CHIPEDGE_DRAWING")
TECH.PPLAYER.NO_INSP = TechnologyTree()
TECH.PPLAYER.NO_INSP.DRAWING = PPLayer(TECH.PROCESS.NO_INSP, TECH.PURPOSE.DRAWING, name="NO_INSP_DRAWING")
TECH.PPLAYER.MASKBRD = TechnologyTree()
TECH.PPLAYER.MASKBRD.DRAWING = PPLayer(TECH.PROCESS.MASKBRD, TECH.PURPOSE.DRAWING, name="MASKBRD_DRAWING")
TECH.PPLAYER.WAFERBRD = TechnologyTree()
TECH.PPLAYER.WAFERBRD.DRAWING= PPLayer(TECH.PROCESS.WAFERBRD, TECH.PURPOSE.DRAWING, name="WAFERBRD_DRAWING")

# required tech keys for Ipkiss compatibility
TECH.PPLAYER.WG = TechnologyTree()
TECH.PPLAYER.WG.TEXT         = TECH.PPLAYER.FULL.POLTXT
TECH.PPLAYER.PINREC          = PPLayer(TECH.PROCESS.NONE, TECH.PURPOSE.PINREC, name="PINREC")    # Used in ports

# required for Ipkiss.eda compatibility
TECH.PPLAYER.WIRE_TRACE      = PPLayer(TECH.PROCESS.FULL, TECH.PURPOSE.TRACE, name="WIRE_TRC")
TECH.PPLAYER.RIB_TRACE       = PPLayer(TECH.PROCESS.SHALL, TECH.PURPOSE.TRACE, name="RIB_TRC")

# required for Picazzo
TECH.PPLAYER.ERROR  = TechnologyTree()
TECH.PPLAYER.ERROR.GENERIC   = PPLayer(TECH.PROCESS.NONE, TECH.PURPOSE.ERROR, name="ERROR")
TECH.PPLAYER.ERROR.CROSSING  = TECH.PPLAYER.ERROR.GENERIC

#TECH.PPLAYER.NONE.BBOX = PPLayer(process=TECH.PROCESS.NONE, purpose = TECH.PURPOSE.BBOX,name="BBOX")
