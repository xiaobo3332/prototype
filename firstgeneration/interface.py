from technologies import silicon_photonics


import ipkiss3.all as i3

#
# # from ipkiss.technology import get_technology
from ipkiss.technology.technology import TechnologyTree, DelayedInitTechnologyTree
# from ipkiss.geometry.shapes.basic import ShapeRectangle
#
# # TECH = get_technology()
#
# import LayerDefinitions


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



class Interface(i3.PCell):
    _name_prefix = "INTERFACE"

    # Center of the structure
    position = i3.Coord2Property(default=(0.0, 0.0))

    # Layer
    layer = i3.LayerProperty(default=i3.TECH.PPLAYER.NEW_PROCESS.PP1)
    layer_bool = i3.LayerProperty(default=i3.TECH.PPLAYER.NEW_PROCESS.PP2)

    # Mesa parameters
    length = i3.PositiveNumberProperty(default=5000.0)
    width = i3.PositiveNumberProperty(default=3000.0)

    pocket = i3.BoolProperty(default=False)
    tilt = i3.BoolProperty(default=False)

    class Layout(i3.LayoutView):

        def _generate_elements(self, elems):

            # Center of the structure
            (x0, y0) = self.position

            elems += i3.Rectangle(layer=self.layer, center=(x0 + 7500, y0 + 4500),
                                  box_size=(15000, 1000))

            # elems += i3.Rectangle(layer=i3.TECH.PPLAYER.NONE.DOC, center=(x0 + 7500, y0 + 4500),
            #                       box_size=(15000, 1000))


            elems += i3.Rectangle(layer=self.layer, center=(x0 + 7500, y0 + 500),
                                  box_size=(15000, 1000))
            elems += i3.Rectangle(layer=self.layer, center=(x0 + 12500, y0 + 2500),
                                  box_size=(self.length, self.width))


            if self.pocket:
                PO = i3.Rectangle(layer=self.layer_bool, center=(10001, 2500), box_size=(2, 160))
                elems += PO
                generated1 = self.layer - self.layer_bool
                mapping = {generated1: self.layer}
                elems = i3.get_elements_for_generated_layers(elems, mapping)


            if self.tilt:
                # TI = i3.Rectangle(layer=self.layer_bool, center=(10001, 2500), box_size=(2, 160))
                # elems += TI
                TI_shape = i3.Shape(points=[(10000.0, 2470.0), (10010.58, 2530.0), (10000.0, 2530.0)], closed=True)
                TI = i3.Boundary(layer=self.layer_bool, shape=TI_shape)
                elems += TI

            generated1 = self.layer - self.layer_bool
            mapping = {generated1: self.layer}
            elems = i3.get_elements_for_generated_layers(elems, mapping)


            return elems


# GDS-file generation for debugging
Interface(pocket= False, tilt=False).Layout.view.write_gdsii("interface1.gds")
print("Done writing Release.gds!")
Interface(pocket= True, tilt=False).Layout.view.write_gdsii("interface2.gds")
print("Done writing Release.gds!")
Interface(pocket= False, tilt=True).Layout.view.write_gdsii("interface3.gds")
print("Done writing Release.gds!")
Interface(pocket= True, tilt=True).Layout.view.write_gdsii("interface4.gds")
print("Done writing Release.gds!")
