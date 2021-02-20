############################################################################################
# GDSII settings:
#
# GDSII layer mapping
# - TECH keys defined here is used by IPKISS
############################################################################################

from ipkiss.technology import get_technology
from ipkiss.technology.technology import TechnologyTree
from ipkiss.process.layer_map import GenericGdsiiPPLayerOutputMap, GenericGdsiiPPLayerInputMap
import string

# Layer mapping
TECH = get_technology()

from ipkiss.technology.technology import DelayedInitTechnologyTree
TECH = get_technology()
TECH.GDSII = TechnologyTree()


##################################
# SETTINGS
##################################
TECH.GDSII.STRNAME_CHARACTER_DICT = {" -./": "_"}                                           # Mapping for illegal characters in cell names
TECH.GDSII.STRNAME_ALLOWED_CHARACTERS = string.ascii_letters + string.digits + '_$'         # Allowed characters in cell names

TECH.GDSII.MAX_COORDINATES = 200                                                            # Max number of vertices in a path
TECH.GDSII.MAX_PATH_LENGTH = 100                                                            # Max number of control points in a path
TECH.GDSII.MAX_VERTEX_COUNT = 4000                                                          # Max number of vertices in a polygon
TECH.GDSII.MAX_NAME_LENGTH = 255                                                            # Max length of a cell name

##################################
# LAYER MAP
##################################

TECH.GDSII.LAYERTABLE = {                                     # GDSII layer table - not required as such, but used for defining the maps below
    # (ProcessLayer, PatternPurpose) : (GDSIILayer, GDSIIDatatype)
    (TECH.PROCESS.SHALL,  TECH.PURPOSE.DRAWETCH):   ( 571, 0),
    (TECH.PROCESS.SHALL,  TECH.PURPOSE.PERF):       ( 571, 1),
    (TECH.PROCESS.SHALL,  TECH.PURPOSE.PERFSLOT):   ( 571, 2),
    (TECH.PROCESS.SHALL,  TECH.PURPOSE.POLTXT):     ( 571, 3),
    (TECH.PROCESS.SHALL,  TECH.PURPOSE.TILING):     ( 571, 10),
    (TECH.PROCESS.SHALL,  TECH.PURPOSE.DATAPREP):   ( 571, 20),
    (TECH.PROCESS.SHALL,  TECH.PURPOSE.NOFILL):     ( 10158, 571),
    (TECH.PROCESS.SHALL,  TECH.PURPOSE.NOSIZE):     ( 10155, 571),
    (TECH.PROCESS.SHALL,  TECH.PURPOSE.NODRC):      ( 10150, 571),
    
    (TECH.PROCESS.FULL,  TECH.PURPOSE.DRAWETCH):    ( 581, 0),
    (TECH.PROCESS.FULL,  TECH.PURPOSE.PERF):        ( 581, 1),
    (TECH.PROCESS.FULL,  TECH.PURPOSE.PERFSLOT):    ( 581, 2),
    (TECH.PROCESS.FULL,  TECH.PURPOSE.POLTXT):      ( 581, 3),
    (TECH.PROCESS.FULL,  TECH.PURPOSE.TILING):      ( 581, 10),
    (TECH.PROCESS.FULL,  TECH.PURPOSE.DATAPREP):    ( 581, 20),
    (TECH.PROCESS.FULL,  TECH.PURPOSE.NOFILL):      ( 10158, 581),
    (TECH.PROCESS.FULL,  TECH.PURPOSE.NOSIZE):      ( 10155, 581),
    (TECH.PROCESS.FULL,  TECH.PURPOSE.NODRC):       ( 10150, 581),

    (TECH.PROCESS.CLROUT,  TECH.PURPOSE.DRAWING):   ( 524, 0),
    
    (TECH.PROCESS.ELEC,  TECH.PURPOSE.DRAWING):     ( 684, 0),
    (TECH.PROCESS.TRENCH,  TECH.PURPOSE.DRAWING):   ( 740, 0),    
    
    (TECH.PROCESS.OPCLAD,  TECH.PURPOSE.DRAWING):   ( 710, 0),
    (TECH.PROCESS.OPCLAD,  TECH.PURPOSE.PERF):      ( 710, 3),
    (TECH.PROCESS.OPCLAD,  TECH.PURPOSE.TILING):    ( 710, 10),
    (TECH.PROCESS.OPCLAD,  TECH.PURPOSE.NOSIZE):    ( 10155, 710),
    (TECH.PROCESS.OPCLAD,  TECH.PURPOSE.NODRC):     ( 10150, 710),

    (TECH.PROCESS.NO_DRC,  TECH.PURPOSE.DRAWING):   ( 10150, 0),
    (TECH.PROCESS.DUMMY,  TECH.PURPOSE.DRAWING):    ( 10151, 0),
    (TECH.PROCESS.DOC,  TECH.PURPOSE.DRAWING):      ( 10152, 0),
    (TECH.PROCESS.TXTLAB,  TECH.PURPOSE.DRAWING):   ( 10153, 0),
    (TECH.PROCESS.ERRFLG,  TECH.PURPOSE.DRAWING):   ( 10154, 0),
    (TECH.PROCESS.NO_SIZE,  TECH.PURPOSE.DRAWING):  ( 10155, 0),
    (TECH.PROCESS.NO_GEN,  TECH.PURPOSE.DRAWING):   ( 10156, 0),
    (TECH.PROCESS.RED_FILL,  TECH.PURPOSE.DRAWING): ( 10157, 0),
    (TECH.PROCESS.NO_FILL,  TECH.PURPOSE.DRAWING):  ( 10158, 0),
    (TECH.PROCESS.NO_DHOL,  TECH.PURPOSE.DRAWING):  ( 10159, 0),
    (TECH.PROCESS.COVER,  TECH.PURPOSE.DRAWING):    ( 10160, 0),
    (TECH.PROCESS.CHIPEDGE,  TECH.PURPOSE.DRAWING): ( 10161, 0),
    (TECH.PROCESS.NO_INSP,  TECH.PURPOSE.DRAWING):  ( 10162, 0),
    (TECH.PROCESS.MASKBRD,  TECH.PURPOSE.DRAWING):  ( 10163, 0),
    (TECH.PROCESS.WAFERBRD,  TECH.PURPOSE.DRAWING): ( 10164, 0),
    
    # required tech keys for Ipkiss compatibility
    # required for Ipkiss.eda compatibility
#   (TECH.PROCESS.WG, TECH.PURPOSE.TRACE           ): (37, 8),
#   (TECH.PROCESS.FC, TECH.PURPOSE.TRACE           ): (35, 8), 
#   (TECH.PROCESS.SKT, TECH.PURPOSE.TRACE          ): (43, 8),         
    # required for Picazzo
#   (TECH.PROCESS.NONE, TECH.PURPOSE.ERROR         ): (10154, 0),
#   (TECH.PROCESS.NONE, TECH.PURPOSE.BBOX          ): (120, 0)
}

TECH.GDSII.EXPORT_LAYER_MAP = GenericGdsiiPPLayerOutputMap(pplayer_map=TECH.GDSII.LAYERTABLE,       # GDSII export map - required
                                                           ignore_undefined_mappings=True)
TECH.GDSII.IMPORT_LAYER_MAP = GenericGdsiiPPLayerInputMap(pplayer_map=TECH.GDSII.LAYERTABLE,
                                                          ignore_undefined_mappings=True)        # GDSII import map - required


##################################
# FILTERS
##################################

from ipkiss.primitives.filters.path_cut_filter import PathCutFilter
from ipkiss.primitives.filters.empty_filter import EmptyFilter
from ipkiss.primitives.filters.path_to_boundary_filter import PathToBoundaryFilter
from ipkiss.primitives.filters.boundary_cut_filter import BoundaryCutFilter
from ipkiss.primitives.filters.name_scramble_filter import NameScrambleFilter
from ipkiss.primitives.filters.name_error_filter import PCellNameErrorFilter
from ipkiss.primitives.filter import ToggledCompoundFilter

f = ToggledCompoundFilter()
f += PathCutFilter(name="cut_path",
                   max_path_length=TECH.GDSII.MAX_COORDINATES,
                   grids_per_unit=int(TECH.METRICS.UNIT / TECH.METRICS.GRID),
                   overlap=1)
f += PathToBoundaryFilter(name="path_to_boundary")
f += BoundaryCutFilter(name="cut_boundary", max_vertex_count=TECH.GDSII.MAX_VERTEX_COUNT)
f += EmptyFilter(name="write_empty")
f += PCellNameErrorFilter(name="name_error_filter", allowed_characters=TECH.GDSII.STRNAME_ALLOWED_CHARACTERS)
f["cut_path"] = True
f["path_to_boundary"] = True
f["cut_boundary"] = True
f["write_empty"] = True
f["name_error_filter"] = False
TECH.GDSII.FILTER = f                             # GDSII export filters (several filter which can be toggled on or off) - required

TECH.GDSII.NAME_FILTER = NameScrambleFilter(allowed_characters=TECH.GDSII.STRNAME_ALLOWED_CHARACTERS,   # GDSII cell name filter - required
                                            replace_characters=TECH.GDSII.STRNAME_CHARACTER_DICT,
                                            default_replacement="",
                                            max_name_length=TECH.GDSII.MAX_NAME_LENGTH,
                                            scramble_all=False)
