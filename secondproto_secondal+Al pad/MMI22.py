from technologies import silicon_photonics
from picazzo3.traces.wire_wg.trace import WireWaveguideTemplate
from picazzo3.routing.place_route import PlaceAndAutoRoute
import ipkiss3.all as i3
from picazzo3.container.transition_ports import AutoTransitionPorts
from picazzo3.filters.mmi.cell import MMI2x2Tapered
from MMI12 import MMI2112


class my_dc(PlaceAndAutoRoute):
    DC_list = i3.ChildCellListProperty(default=[])
    # gap_inc_vec = i3.ListProperty(default=[], doc="Length of MMI")
    gap_inc_vec2 = i3.ListProperty(default=[], doc="length of 12mmi")
    WG1 = i3.ChildCellProperty(doc="", locked=True)
    WG2 = i3.ChildCellProperty()
    wg_t1 = i3.WaveguideTemplateProperty(doc="board WG")
    mmi_trace_template = i3.WaveguideTemplateProperty()
    mmi_access_template = i3.WaveguideTemplateProperty()
    width = i3.PositiveNumberProperty(doc="width of ports", default=15)
    cleave = i3.PositiveNumberProperty(doc="tolerance", default=150)

    def _default_wg_t1(self):
        wg_t1 = WireWaveguideTemplate(name="port_{}".format(str(self.width)))
        wg_t1.Layout(core_width=self.width,
                     cladding_width=self.width + 2 * 12.0,
                     )
        return wg_t1

    def _default_trace_template(self):
        wg_sm = WireWaveguideTemplate(name="sm_template")
        wg_sm.Layout(core_width=3.8, cladding_width=3.8 + 2 * 12.0)
        return wg_sm

    def _default_WG1(self):
        WG1 = i3.Waveguide(name="straight{}_{}".format(str(self.width), str(self.cleave)), trace_template=self.wg_t1)
        WG1.Layout(shape=[(0.0, 0.0), (self.cleave, 0.0)])
        return WG1

    def _default_WG2(self):
        Port = AutoTransitionPorts(
            name="ports{}_{}".format(str(self.width), str(self.cleave)),
            contents=self.WG1,
            port_labels=["out"],
            trace_template=self.trace_template)
        Port.Layout(transition_length=300)  # .visualize(annotate=True)
        return Port

    def _default_mmi_trace_template(self):
        mmi_trace_template = WireWaveguideTemplate(name="MMI_tt")
        mmi_trace_template.Layout(core_width=20.0, cladding_width=20.0 + 2 * 12)  # MMI_width
        return mmi_trace_template

    def _default_mmi_access_template(self):
        mmi_access_template = WireWaveguideTemplate(name="MMI_at")
        mmi_access_template.Layout(core_width=9.0, cladding_width=9.0 + 2 * 12)
        return mmi_access_template

    def _default_DC_list(self):
        print '____________ MMI 2x2 ______________'
        MMI22_list = []

        # cell = MMI2x2Tapered(mmi_trace_template=self.mmi_trace_template,
        #                      input_trace_template=self.mmi_access_template,
        #                      output_trace_template=self.mmi_access_template,
        #                      trace_template=self.trace_template,
        #                      )
        #
        # cell.Layout(name="MMI22_l_430", transition_length=200.0,
        #             length=430, trace_spacing=11.0
        #             )
        #
        # MMI22_list.append(cell)
        #
        # print 'cell name ' + str(cell.name)
        # print '__________________________'

        for l, dl in enumerate(self.gap_inc_vec2):
            print 'length number ' + str(l)
            print 'dl ' + str(dl)

            cell = MMI2112()

            cell.Layout(name="MMI2112_l_{}".format(str(self.gap_inc_vec2[l])),
                        length=self.gap_inc_vec2[l]
                        )

            MMI22_list.append(cell)

            print 'cell name ' + str(cell.name)
            print '__________________________'

        return MMI22_list


    def _default_child_cells(self):
        child_cells = dict()
        for counter in range(0, 11, 1):
            print counter
            # child_cells['straight' + str(counter)] = self.WG1
            child_cells['taper' + str(counter)] = self.WG2

        for counter, child in enumerate(self.DC_list):
            print 'child number' + str(counter)
            child_cells['ring' + str(counter)] = child
            print 'child name ' + str(child.name)
            print child
        return child_cells


    def _default_links(self):
        links = [
            # ("taper0:out", "ring0:in2"),
            # ("taper1:out", "ring0:in1"),
            # ("taper2:out", "ring0:out2"),
            # ("taper3:out", "ring0:out1"),

            ("taper0:out", "ring0:narrow_in"),
            ("taper1:out", "ring0:MMI1a_out1"),
            ("taper2:out", "ring0:MMI1a_out2"),


            ("taper3:out", "ring1:narrow_in"),
            ("taper4:out", "ring1:MMI1a_out1"),
            ("taper5:out", "ring1:MMI1a_out2"),
            ("taper6:out", "ring2:narrow_in"),
            ("taper7:out", "ring2:MMI1a_out1"),
            ("taper8:out", "ring2:MMI1a_out2"),

            ("taper9:out", "taper10:out")

        ]
        return links


    class Layout(PlaceAndAutoRoute.Layout):

        def _default_child_transformations(self):
            trans = dict()
            column = 6000
            trans['ring0'] = (600, 0)
            trans['ring1'] = (600, 1 * column)
            trans['ring2'] = (600, 2 * column )
            # trans['ring3'] = (1300, 8000 + 2 * column )

            trans["taper0"] = (0, 0)
            trans["taper1"] = i3.HMirror(0) + i3.Translation((2500, -1500))
            trans["taper2"] = i3.HMirror(0) + i3.Translation((2500, 1500))

            trans["taper3"] = (0, 1* column)
            trans["taper4"] = i3.HMirror(0) + i3.Translation((2500, -1500+1*column))
            trans["taper5"] = i3.HMirror(0) + i3.Translation((2500, 1500+1*column))

            trans["taper6"] = (0, 2* column)
            trans["taper7"] = i3.HMirror(0) + i3.Translation((2500, -1500+2*column))
            trans["taper8"] = i3.HMirror(0) + i3.Translation((2500, 1500+2*column))

            trans["taper9"] = (0,  3800+2 * column)

            trans["taper10"] = i3.HMirror(0) + i3.Translation((2500, -1500+3*column))
            # trans["taper11"] = i3.HMirror(0) + i3.Translation((3000, 6500+ 2 * column))
            # trans["taper12"] = i3.HMirror(0) + i3.Translation((3000, 9500+ 2 * column))


            return trans

        def _default_bend_radius(self):
            bend_radius = 300
            return bend_radius

        def _generate_elements(self, elems):
            for counter, child in enumerate(self.DC_list):
                name = child.name

                elems += i3.PolygonText(layer=i3.TECH.PPLAYER.WG.TEXT,
                                        text="{}_{}".format(name, self.cell.wg_t1.name),
                                        # coordinate=(1300.0, 100.0),
                                        alignment=(i3.TEXT_ALIGN_LEFT, i3.TEXT_ALIGN_LEFT),
                                        font=2,
                                        height=30.0,
                                        transformation=i3.Translation((600, 100 + 6000 * counter))
                                        )
                for i in range(1,8,1):
                    elems += i3.PolygonText(layer=i3.TECH.PPLAYER.WG.TEXT,
                                            text="{}".format(i),
                                            coordinate=(400, -4400+3000*i),
                                            font=2,
                                            height=200.0,
                                            )
                for j in range (-1,2,1):
                    for i in range(0,4,1):
                        elems += i3.Rectangle(layer=i3.TECH.PPLAYER.WG.TEXT, center=(
                                    100+j*6000, -3000+100+6000*i),box_size=(100, 100))
                        elems += i3.Rectangle(layer=i3.TECH.PPLAYER.WG.TEXT, center=(
                            100+j*6000, -3000 - 100 + 6000 * i), box_size=(100, 100))
                    elems += i3.Rectangle(layer=i3.TECH.PPLAYER.WG.TEXT, center=(
                        100+j*6000, -3000 + 100 + 6000 * 3+3000), box_size=(100, 100))
                    elems += i3.Rectangle(layer=i3.TECH.PPLAYER.WG.TEXT, center=(
                        100+j*6000, -3000 - 100 + 6000 * 3+3000), box_size=(100, 100))
                elems += i3.Rectangle(layer=i3.TECH.PPLAYER.WG.TEXT, center=(
                    300, -3000 + 100 + 6000 * 3 + 3000), box_size=(100, 100))
                elems += i3.Rectangle(layer=i3.TECH.PPLAYER.WG.TEXT, center=(
                    300, -3000 - 100 ), box_size=(100, 100))

            return elems


# dc_10 = my_dc(gap_inc_vec2=[110.0, 110.0, 110.0], name="ring1", cleave=200)
# dc_10_layout = dc_10.Layout()
# # dc_10_layout.visualize(annotate=True)
# # dc_10_layout.write_gdsii("MMI22.gds")
#
#
# dc_15 = my_dc(gap_inc_vec2=[110.0, 120.0, 130.0], name="ring2")
# dc_15_layout = dc_15.Layout()
#
# pr = PlaceAndAutoRoute(
#     child_cells={
#         "dc1": dc_10,
#         "dc2": dc_15,
#     }
# )
# pr_layout = pr.Layout(child_transformations={"dc1": (0, 0),
#                                              "dc2": i3.HMirror(1250) - i3.Translation((2500, 0)),
#
#                                              })
# # pr_layout.visualize()
# pr_layout.write_gdsii("MMI22.gds")
