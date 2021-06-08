from technologies import silicon_photonics
import ipkiss3.all as i3
from picazzo3.routing.place_route import PlaceComponents
from MMI22 import my_dc
from MMI2112 import my_MMI2112
from interface import NP, PI, AL_PI, AL_NP, SiN_NP, SiN_PI



# dc_10 = my_dc(gap_inc_vec=[390, 398, 406], name="ring1")
# # dc_10_layout = dc_10.Layout()
# # dc_10_layout.visualize(annotate=True)
# # dc_10_layout.write_gdsii("DC_V4.gds")
# #
# dc_15 = my_dc(gap_inc_vec=[390, 398, 406], name="ring2")
#
# recess0 = NP(width=338)
# recess1 = NP(width=338, pocket=True, tilt=False)
# recess2 = NP(width=338, pocket=True, tilt=True)
# recess3 = NP(pillar=True)
# recess4 = NP(pillar=True, pocket=True, tilt=False)
# recess5 = NP(pillar=True, pocket=True, tilt=True)
# recess6 = NP(pocket=False, tilt=False)
# recess7 = NP(pocket=False, tilt=False)
# recess8 = NP(pocket=False, tilt=False)
# recess9 = NP(pocket=False, tilt=False)
# recess10 = PI(pocket=False, tilt=False)
# recess11 = PI(pocket=False, tilt=False)


# pr = PlaceComponents(
#     child_cells={
#         "dc1": dc_10,
#         "dc2": dc_15,
#         "R0": recess0,
#         "R1": recess1,
#         "R2": recess2,
#         "R3": recess3,
#         "R4": recess4,
#         "R5": recess5
#     }
# )
# pr_layout = pr.Layout(child_transformations={"dc1": (0, 0),
#                                              "dc2": i3.HMirror(2500) - i3.Translation((5000, 0)),
#                                              "R0": (-15000, 0 + 5000 * -1),
#                                              "R1": (-15000, 0 + 5000 * 0),
#                                              "R2": (-15000, 0 + 5000 * 1),
#                                              "R3": (-15000, 0 + 5000 * 2),
#                                              "R4": (-15000, 0 + 5000 * 3),
#                                              "R5": (-15000, 0 + 5000 * 4),
#
#                                              })
# # pr_layout.visualize()
# pr_layout.write_gdsii("execute.gds")


class my_exe2(PlaceComponents):
    DC_list = i3.ChildCellListProperty(default=[])

    def _default_DC_list(self):
        MMI22_list = []

        dc_10 = my_dc(gap_inc_vec=[382, 398, 414], name="ring1")
        # dc_10_layout = dc_10.Layout()
        # dc_10_layout.visualize(annotate=True)
        # dc_10_layout.write_gdsii("DC_V4.gds")
        #
        dc_15 = my_MMI2112(gap_inc_vec=[92, 97, 102], name="ring2")
        MMI22_list.append(dc_10)
        MMI22_list.append(dc_15)

        recess0 = NP(width=338)
        recess1 = NP(width=338, pocket=True, tilt=False)
        recess2 = NP(width=338, pocket=True, tilt=True)
        recess3 = NP(pillar=True)
        recess4 = NP(pillar=True, pocket=True, tilt=False)
        recess5 = NP(pillar=True, pocket=True, tilt=True)
        recess6 = NP()
        recess7 = NP(pocket=True, tilt=False)
        recess8 = NP(width=338, pillar=True, pocket=False, tilt=False)
        recess9 = NP(width=338, pillar=True, pocket=True, tilt=False)
        recess10 = PI(pocket=False, tilt=False)
        recess11 = PI(pocket=True, tilt=False)

        for i in range(0, 12, 1):
            print(i)
            _inst = locals()['recess{}'.format(i)]
            MMI22_list.append(_inst)

        # MMI22_list.append(recess0)
        # MMI22_list.append(recess1)
        # MMI22_list.append(recess2)
        # MMI22_list.append(recess3)
        # MMI22_list.append(recess4)
        # MMI22_list.append(recess5)
        # MMI22_list.append(recess6)
        # MMI22_list.append(recess7)
        # MMI22_list.append(recess8)
        # MMI22_list.append(recess9)
        # MMI22_list.append(recess10)
        # MMI22_list.append(recess11)

        Al0 = AL_NP(width=338)
        Al1 = AL_NP(width=338)
        Al2 = AL_NP(width=338)
        Al3 = AL_NP(pillar=True)
        Al4 = AL_NP(pillar=True)
        Al5 = AL_NP(pillar=True)
        Al6 = AL_NP()
        Al7 = AL_NP()
        Al8 = AL_NP(width=338, pillar=True)
        Al9 = AL_NP(width=338, pillar=True)
        Al10 = AL_PI()
        Al11 = AL_PI()
        # _ = [Al0, Al1, Al2, Al3, Al4, Al5, Al6, Al7, Al8, Al9, Al10, Al11]
        #
        # for i in range(0,12,1):
        #     # _[i].append(i)
        #     MMI22_list.append(_[i])
        for i in range(0, 12, 1):
            print(i)
            _inst = locals()['Al{}'.format(i)]
            MMI22_list.append(_inst)

        SiN0 = SiN_NP(width=338)
        SiN1 = SiN_NP(width=338)
        SiN2 = SiN_NP(width=338, tilt_0=True)
        SiN3 = SiN_NP(pillar=True)
        SiN4 = SiN_NP(pillar=True)
        SiN5 = SiN_NP(pillar=True, tilt_0=True)
        SiN6 = SiN_NP()
        SiN7 = SiN_NP()
        SiN8 = SiN_NP(width=338, pillar=True)
        SiN9 = SiN_NP(width=338, pillar=True)
        SiN10 = SiN_PI()
        SiN11 = SiN_PI()
        for i in range(0, 12, 1):
            print(i)
            _inst = locals()['SiN{}'.format(i)]
            MMI22_list.append(_inst)

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
            row = 5000
            trans["CHILD0"] = (0, 0)
            trans["CHILD1"] = i3.HMirror(2500) - i3.Translation((5000, 0))
            trans['CHILD2'] = (-15000, 0 + row * -1)
            trans['CHILD3'] = (-15000, 0 + row * 0)
            trans['CHILD4'] = (-15000, 0 + row * 1)
            trans['CHILD5'] = (-15000, 0 + row * 2)
            trans['CHILD6'] = (-15000, 0 + row * 3)
            trans['CHILD7'] = (-15000, 0 + row * 4)
            trans['CHILD8'] = i3.Rotation(rotation=180) + i3.Translation((15000, 0 + row * 0))
            trans['CHILD9'] = i3.Rotation(rotation=180) + i3.Translation((15000, 0 + row * 1))
            trans['CHILD10'] = i3.Rotation(rotation=180) + i3.Translation((15000, 0 + row * 2))
            trans['CHILD11'] = i3.Rotation(rotation=180) + i3.Translation((15000, 0 + row * 3))
            trans['CHILD12'] = i3.Rotation(rotation=180) + i3.Translation((15000, 0 + row * 4))
            trans['CHILD13'] = i3.Rotation(rotation=180) + i3.Translation((15000, 0 + row * 5))
            trans['CHILD14'] = (-15000, 0 + row * -1)
            trans['CHILD15'] = (-15000, 0 + row * 0)
            trans['CHILD16'] = (-15000, 0 + row * 1)
            trans['CHILD17'] = (-15000, 0 + row * 2)
            trans['CHILD18'] = (-15000, 0 + row * 3)
            trans['CHILD19'] = (-15000, 0 + row * 4)
            trans['CHILD20'] = i3.Rotation(rotation=180) + i3.Translation((15000, 0 + row * 0))
            trans['CHILD21'] = i3.Rotation(rotation=180) + i3.Translation((15000, 0 + row * 1))
            trans['CHILD22'] = i3.Rotation(rotation=180) + i3.Translation((15000, 0 + row * 2))
            trans['CHILD23'] = i3.Rotation(rotation=180) + i3.Translation((15000, 0 + row * 3))
            trans['CHILD24'] = i3.Rotation(rotation=180) + i3.Translation((15000, 0 + row * 4))
            trans['CHILD25'] = i3.Rotation(rotation=180) + i3.Translation((15000, 0 + row * 5))
            trans['CHILD26'] = (-15000, 0 + row * -1)
            trans['CHILD27'] = (-15000, 0 + row * 0)
            trans['CHILD28'] = (-15000, 0 + row * 1)
            trans['CHILD29'] = (-15000, 0 + row * 2)
            trans['CHILD30'] = (-15000, 0 + row * 3)
            trans['CHILD31'] = (-15000, 0 + row * 4)
            trans['CHILD32'] = i3.Rotation(rotation=180) + i3.Translation((15000, 0 + row * 0))
            trans['CHILD33'] = i3.Rotation(rotation=180) + i3.Translation((15000, 0 + row * 1))
            trans['CHILD34'] = i3.Rotation(rotation=180) + i3.Translation((15000, 0 + row * 2))
            trans['CHILD35'] = i3.Rotation(rotation=180) + i3.Translation((15000, 0 + row * 3))
            trans['CHILD36'] = i3.Rotation(rotation=180) + i3.Translation((15000, 0 + row * 4))
            trans['CHILD37'] = i3.Rotation(rotation=180) + i3.Translation((15000, 0 + row * 5))

            return trans


# final = my_exe(name="final")
# final_layout = final.Layout()
# final_layout.write_gdsii("execute.gds")
