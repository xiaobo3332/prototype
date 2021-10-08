from technologies import silicon_photonics
import ipkiss3.all as i3
from picazzo3.routing.place_route import PlaceComponents
from execute2 import my_exe2
from AlignmentMarkerSet import PlaceMarkers
# from import2 import ImportRik


class Merge(i3.PCell):
    _name_prefix = "Merge"

    class Layout(i3.LayoutView):

        def _generate_elements(self, elems):
            elems += i3.SRef(reference=PlaceMarkers())

            elems += i3.SRef(reference=my_exe2(name="final"))

            generated1 = i3.TECH.PPLAYER.HFW - i3.TECH.PPLAYER.V12.PILLAR
            mapping = {generated1: i3.TECH.PPLAYER.M2.LINE}
            elems += i3.get_elements_for_generated_layers(elems, mapping)

            generated2 = i3.TECH.PPLAYER.WG.CLADDING - i3.TECH.PPLAYER.WG.CORE
            mapping = {generated2: i3.TECH.PPLAYER.WG.TEXT}
            elems += i3.get_elements_for_generated_layers(elems, mapping)

            # elems += i3.SRef(reference=ImportRik())
            return elems


Merge().Layout.view.write_gdsii("merge_test7.gds")
