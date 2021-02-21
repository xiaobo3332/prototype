from technologies import silicon_photonics
import ipkiss3.all as i3
from picazzo3.routing.place_route import PlaceComponents
from AlignmentMarker import AlignmentMarker


class AlignmentMarkerSet(i3.PCell):
    _name_prefix = "ALIGNMENT MARKER SET"

    # Center of the structure
    position = i3.Coord2Property(default=(0.0, 0.0))

    # Orientation
    horizontal = i3.BoolProperty(default=True)

    # Spacing
    v_spacing = i3.PositiveNumberProperty(default=320.0)
    h_spacing = i3.PositiveNumberProperty(default=300.0)

    class Layout(i3.LayoutView):

        def _generate_elements(self, elems):

            # Center of the structure
            (x0, y0) = self.position

            if self.horizontal == False:

                # ADD RELEASE
                elems += i3.SRef(reference=AlignmentMarker(layer=i3.TECH.PPLAYER.WG.TEXT, layer_text="Release"),
                                 transformation=i3.Translation((x0 + 0.0 * self.h_spacing, y0)))
                elems += i3.SRef(reference=AlignmentMarker(layer=i3.TECH.PPLAYER.HFW, complement=True),
                                 transformation=i3.Translation((x0 + 0.0 * self.h_spacing, y0)))

                # # ADD TETHER
                # elems += i3.SRef(reference=AlignmentMarker(layer=lay_island, layer_text="Tether"),
                #                  transformation=i3.Translation((x0 + 1.0 * self.h_spacing, y0)))
                # elems += i3.SRef(reference=AlignmentMarker(layer=lay_release, protection=True),
                #                  transformation=i3.Translation((x0 + 1.0 * self.h_spacing, y0)))
                # elems += i3.SRef(reference=AlignmentMarker(layer=lay_tether, complement=True),
                #                  transformation=i3.Translation((x0 + 1.0 * self.h_spacing, y0)))
                #
                # # ADD Dongbomesa
                # elems += i3.SRef(reference=AlignmentMarker(layer=lay_island, layer_text="Dongbomesa"),
                #                  transformation=i3.Translation((x0 + 2.0 * self.h_spacing, y0)))
                # elems += i3.SRef(reference=AlignmentMarker(layer=lay_release, protection=True),
                #                  transformation=i3.Translation((x0 + 2.0 * self.h_spacing, y0)))
                # elems += i3.SRef(reference=AlignmentMarker(layer=lay_tether, protection=True),
                #                  transformation=i3.Translation((x0 + 2.0 * self.h_spacing, y0)))
                # elems += i3.SRef(reference=AlignmentMarker(layer=lay_mesa, complement=True),
                #                  transformation=i3.Translation((x0 + 2.0 * self.h_spacing, y0)))

            else:

                # ADD RECESS
                elems += i3.SRef(reference=AlignmentMarker(layer=i3.TECH.PPLAYER.WG.TEXT, layer_text="RECESS"),
                                 transformation=i3.Translation((x0 + 0.0 * self.h_spacing, y0)))
                elems += i3.SRef(reference=AlignmentMarker(layer=i3.TECH.PPLAYER.HFW, complement=True),
                                 transformation=i3.Translation((x0 + 0.0 * self.h_spacing, y0)))

                # ADD AL
                elems += i3.SRef(reference=AlignmentMarker(layer=i3.TECH.PPLAYER.WG.TEXT, layer_text="AL"),
                                 transformation=i3.Translation((x0, y0 - 1.0 * self.v_spacing)))
                elems += i3.SRef(reference=AlignmentMarker(layer=i3.TECH.PPLAYER.HFW, protection=True),
                                 transformation=i3.Translation((x0, y0 - 1.0 * self.v_spacing)))
                elems += i3.SRef(reference=AlignmentMarker(layer=i3.TECH.PPLAYER.CONTACT.PILLAR, complement=True),
                                 transformation=i3.Translation((x0, y0 - 1.0 * self.v_spacing)))

                # ADD SiN
                elems += i3.SRef(reference=AlignmentMarker(layer=i3.TECH.PPLAYER.WG.TEXT, layer_text="SiN"),
                                 transformation=i3.Translation((x0, y0 - 2.0 * self.v_spacing)))
                elems += i3.SRef(reference=AlignmentMarker(layer=i3.TECH.PPLAYER.HFW, protection=True),
                                 transformation=i3.Translation((x0, y0 - 2.0 * self.v_spacing)))
                elems += i3.SRef(reference=AlignmentMarker(layer=i3.TECH.PPLAYER.SIL.LINE, complement=True),
                                 transformation=i3.Translation((x0, y0 - 2.0 * self.v_spacing)))

                # ADD BackUp
                elems += i3.SRef(reference=AlignmentMarker(layer=i3.TECH.PPLAYER.WG.TEXT, layer_text="BackUp"),
                                 transformation=i3.Translation((x0, y0 - 3.0 * self.v_spacing)))
                elems += i3.SRef(reference=AlignmentMarker(layer=i3.TECH.PPLAYER.HFW, protection=True),
                                 transformation=i3.Translation((x0, y0 - 3.0 * self.v_spacing)))
                # elems += i3.SRef(reference=AlignmentMarker(layer=lay_tether, complement=True),
                #                  transformation=i3.Translation((x0, y0 - 3.0 * self.v_spacing)))

                # RECESS adjustment according to the mask
                elems += i3.SRef(reference=AlignmentMarker(layer=i3.TECH.PPLAYER.NONE.DOC, protection=True),
                                 transformation=i3.Translation((x0, y0 - 0.0 * self.v_spacing)))
                generated1 = i3.TECH.PPLAYER.NONE.DOC - i3.TECH.PPLAYER.HFW
                mapping = {generated1: i3.TECH.PPLAYER.V12.PILLAR}
                elems += i3.get_elements_for_generated_layers(elems, mapping)

            return elems


# # GDS-file generation for debugging
# AlignmentMarkerSet(horizontal=False).Layout.view.write_gdsii("AlignmentMarkerSet.gds")
# print("Done writing AlignmentMarkerSet.gds!")

class PlaceMarkers(PlaceComponents):
    DC_list = i3.ChildCellListProperty(default=[])

    def _default_DC_list(self):
        MMI22_list = []

        for i in range(0, 3, 1):
            for j in range(0, 3, 1):
                cell = AlignmentMarkerSet(position=(1500 + i * 8500, 0 + j * 10000))
                MMI22_list.append(cell)
        return MMI22_list

    def _default_child_cells(self):
        child_cells = dict()
        for counter, child in enumerate(self.DC_list):
            child_cells['marker' + str(counter)] = child
            print 'child name ' + str(child.name)
            print child
        return child_cells

    # class Layout(PlaceComponents.Layout):
    #
    #     def _default_child_transformations(self):
    #         trans = dict()
    #         row = 5000
    #         trans["CHILD0"] = (0, 0)
    #         trans["CHILD1"] = i3.HMirror(2500) - i3.Translation((5000, 0))
    #         trans['CHILD2'] = (-15000, 0 + row * -1)
    #         trans['CHILD3'] = (-15000, 0 + row * 0)
    #         trans['CHILD4'] = (-15000, 0 + row * 1)
    #         trans['CHILD5'] = (-15000, 0 + row * 2)
    #         trans['CHILD6'] = (-15000, 0 + row * 3)
    #         trans['CHILD7'] = (-15000, 0 + row * 4)
    #         trans['CHILD8'] = i3.Rotation(rotation=180) + i3.Translation((15000, 0 + row * 0))
    #         trans['CHILD9'] = i3.Rotation(rotation=180) + i3.Translation((15000, 0 + row * 1))
    #         trans['CHILD10'] = i3.Rotation(rotation=180) + i3.Translation((15000, 0 + row * 2))
    #         trans['CHILD11'] = i3.Rotation(rotation=180) + i3.Translation((15000, 0 + row * 3))
    #         trans['CHILD12'] = i3.Rotation(rotation=180) + i3.Translation((15000, 0 + row * 4))
    #         trans['CHILD13'] = i3.Rotation(rotation=180) + i3.Translation((15000, 0 + row * 5))
    #         trans['CHILD14'] = (-15000, 0 + row * -1)
    #         trans['CHILD15'] = (-15000, 0 + row * 0)
    #         trans['CHILD16'] = (-15000, 0 + row * 1)
    #         trans['CHILD17'] = (-15000, 0 + row * 2)
    #         trans['CHILD18'] = (-15000, 0 + row * 3)
    #         trans['CHILD19'] = (-15000, 0 + row * 4)
    #         trans['CHILD20'] = i3.Rotation(rotation=180) + i3.Translation((15000, 0 + row * 0))
    #         trans['CHILD21'] = i3.Rotation(rotation=180) + i3.Translation((15000, 0 + row * 1))
    #         trans['CHILD22'] = i3.Rotation(rotation=180) + i3.Translation((15000, 0 + row * 2))
    #         trans['CHILD23'] = i3.Rotation(rotation=180) + i3.Translation((15000, 0 + row * 3))
    #         trans['CHILD24'] = i3.Rotation(rotation=180) + i3.Translation((15000, 0 + row * 4))
    #         trans['CHILD25'] = i3.Rotation(rotation=180) + i3.Translation((15000, 0 + row * 5))
    #         trans['CHILD26'] = (-15000, 0 + row * -1)
    #         trans['CHILD27'] = (-15000, 0 + row * 0)
    #         trans['CHILD28'] = (-15000, 0 + row * 1)
    #         trans['CHILD29'] = (-15000, 0 + row * 2)
    #         trans['CHILD30'] = (-15000, 0 + row * 3)
    #         trans['CHILD31'] = (-15000, 0 + row * 4)
    #         trans['CHILD32'] = i3.Rotation(rotation=180) + i3.Translation((15000, 0 + row * 0))
    #         trans['CHILD33'] = i3.Rotation(rotation=180) + i3.Translation((15000, 0 + row * 1))
    #         trans['CHILD34'] = i3.Rotation(rotation=180) + i3.Translation((15000, 0 + row * 2))
    #         trans['CHILD35'] = i3.Rotation(rotation=180) + i3.Translation((15000, 0 + row * 3))
    #         trans['CHILD36'] = i3.Rotation(rotation=180) + i3.Translation((15000, 0 + row * 4))
    #         trans['CHILD37'] = i3.Rotation(rotation=180) + i3.Translation((15000, 0 + row * 5))
    #
    #         return trans


final = PlaceMarkers()
final_layout = final.Layout()
final_layout.write_gdsii("AlignmentMarkerSet.gds")
