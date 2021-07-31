from technologies import silicon_photonics
import ipkiss3.all as i3
from picazzo3.routing.place_route import PlaceComponents
from MMI22 import my_dc
from interface import NP, PI, AL_PI, AL_NP, SiN_NP, SiN_PI
from interface_mmi12 import NP_mmi12

class my_exe2(PlaceComponents):
    DC_list = i3.ChildCellListProperty(default=[])

    def _default_DC_list(self):
        MMI22_list = []

        dc_10 = my_dc( gap_inc_vec2=[110.0, 110.0, 110], name="ring1")
        # dc_10_layout = dc_10.Layout()
        # dc_10_layout.visualize(annotate=True)
        # dc_10_layout.write_gdsii("DC_V4.gds")
        #
        dc_15 = my_dc(gap_inc_vec2=[110.0, 110.0, 110], name="ring2")
        MMI22_list.append(dc_10)
        MMI22_list.append(dc_15)

        recess0 = NP(width=338, pocket=True, tilt=True)
        recess1 = NP(pillar=True)
        recess2 = NP_mmi12(width=330, pillar=True, pocket=False, tilt=False)
        recess3 = NP_mmi12(width=330, pillar=True, pocket=False, tilt=False)
        recess4 = NP_mmi12(width=330, pillar=True, pocket=True, tilt=False)
        recess5 = NP_mmi12(width=330, pillar=True, pocket=True, tilt=False)
        recess6 = NP_mmi12(width=330, pillar=True, pocket=True, tilt=True)
        recess7 = NP_mmi12(width=330, pillar=True, pocket=True, tilt=True)

        recess8 = NP(width=338, pillar=True, pocket=False, tilt=False)
        recess9 = NP(width=338, pillar=True, pocket=True, tilt=False)
        recess10 = NP_mmi12(width=338, pillar=True, pocket=False, tilt=False)
        recess11 = NP_mmi12(width=338, pillar=True, pocket=False, tilt=False)
        recess12 = NP_mmi12(width=338, pillar=True, pocket=True, tilt=False)
        recess13 = NP_mmi12(width=338, pillar=True, pocket=True, tilt=False)
        recess14 = NP_mmi12(width=338, pillar=True, pocket=True, tilt=True)
        recess15 = NP_mmi12(width=338, pillar=True, pocket=True, tilt=True)


        for i in range(0, 16, 1):
            print(i)
            _inst = locals()['recess{}'.format(i)]
            MMI22_list.append(_inst)

        #
        #
        # Al0 = AL_NP(width=338)
        # Al1 = AL_NP(width=338)
        # Al2 = AL_NP(width=338)
        # Al3 = AL_NP(pillar=True)
        # Al4 = AL_NP(pillar=True)
        # Al5 = AL_NP(pillar=True)
        # Al6 = AL_NP()
        # Al7 = AL_NP()
        # Al8 = AL_NP(width=338, pillar=True)
        # Al9 = AL_NP(width=338, pillar=True)
        # Al10 = AL_PI()
        # Al11 = AL_PI()
        #
        # for i in range(0, 12, 1):
        #     print(i)
        #     _inst = locals()['Al{}'.format(i)]
        #     MMI22_list.append(_inst)

        # SiN0 = SiN_NP(width=338)
        # SiN1 = SiN_NP(width=338)
        # SiN2 = SiN_NP(width=338, tilt_0=True)
        # SiN3 = SiN_NP(pillar=True)
        # SiN4 = SiN_NP(pillar=True)
        # SiN5 = SiN_NP(pillar=True, tilt_0=True)
        # SiN6 = SiN_NP()
        # SiN7 = SiN_NP()
        # SiN8 = SiN_NP(width=338, pillar=True)
        # SiN9 = SiN_NP(width=338, pillar=True)
        # SiN10 = SiN_PI()
        # SiN11 = SiN_PI()
        # for i in range(0, 12, 1):
        #     print(i)
        #     _inst = locals()['SiN{}'.format(i)]
        #     MMI22_list.append(_inst)




        return MMI22_list

    def _default_child_cells(self):
        child_cells = dict()
        for counter, child in enumerate(self.DC_list):
            print 'child number' + str(counter)
            child_cells['CHILD' + str(counter)] = child
            print 'child name ' + str(child.name)
            print child
        return child_cells

    class Layout(PlaceComponents.Layout):

        def _default_child_transformations(self):
            trans = dict()
            row = 3000
            trans["CHILD0"] = (0, 0)
            trans["CHILD1"] = i3.HMirror(2500) - i3.Translation((5000, 0))
            trans['CHILD2'] = (-15000, -5000)
            trans['CHILD3'] = (-15000, 0)
            trans['CHILD4'] = (-15000, 2000 + row * 1)
            trans['CHILD5'] = (-15000, 2000 + row * 2)
            trans['CHILD6'] = (-15000, 2000 + row * 3)
            trans['CHILD7'] = (-15000, 2000 + row * 4)
            trans['CHILD8'] = (-15000, 2000 + row * 5)
            trans['CHILD9'] = (-15000, 2000 + row * 6)
            trans['CHILD10'] = i3.Rotation(rotation=180) + i3.Translation((15000, 0))
            trans['CHILD11'] = i3.Rotation(rotation=180) + i3.Translation((15000, 5000))
            trans['CHILD12'] = i3.Rotation(rotation=180) + i3.Translation((15000, 5000 + row * 1))
            trans['CHILD13'] = i3.Rotation(rotation=180) + i3.Translation((15000, 5000 + row * 2))
            trans['CHILD14'] = i3.Rotation(rotation=180) + i3.Translation((15000, 5000 + row * 3))
            trans['CHILD15'] = i3.Rotation(rotation=180) + i3.Translation((15000, 5000 + row * 4))
            trans['CHILD16'] = i3.Rotation(rotation=180) + i3.Translation((15000, 5000 + row * 5))
            trans['CHILD17'] = i3.Rotation(rotation=180) + i3.Translation((15000, 5000 + row * 6))

            # trans['CHILD14'] = (-15000, 0 + row * -1)
            # trans['CHILD15'] = (-15000, 0 + row * 0)
            # trans['CHILD16'] = (-15000, 0 + row * 1)
            # trans['CHILD17'] = (-15000, 0 + row * 2)
            # trans['CHILD18'] = (-15000, 0 + row * 3)
            # trans['CHILD19'] = (-15000, 0 + row * 4)
            # trans['CHILD20'] = i3.Rotation(rotation=180) + i3.Translation((15000, 0 + row * 0))
            # trans['CHILD21'] = i3.Rotation(rotation=180) + i3.Translation((15000, 0 + row * 1))
            # trans['CHILD22'] = i3.Rotation(rotation=180) + i3.Translation((15000, 0 + row * 2))
            # trans['CHILD23'] = i3.Rotation(rotation=180) + i3.Translation((15000, 0 + row * 3))
            # trans['CHILD24'] = i3.Rotation(rotation=180) + i3.Translation((15000, 0 + row * 4))
            # trans['CHILD25'] = i3.Rotation(rotation=180) + i3.Translation((15000, 0 + row * 5))


            return trans

        def _generate_elements(self, elems):
            elems += i3.Rectangle(layer=i3.TECH.PPLAYER.NONE.DOC,
                                  center=(0,9000),  # change
                                  box_size=(200, 28000))


            # generated1 = i3.TECH.PPLAYER.HFW - i3.TECH.PPLAYER.NONE.DOC
            # mapping = {generated1: i3.TECH.PPLAYER.HFW}
            # elems = i3.get_elements_for_generated_layers(elems, mapping)
            return elems


final = my_exe2(name="final")
final_layout = final.Layout()
final_layout.write_gdsii("execute2.gds")
