from technologies import silicon_photonics
import ipkiss3.all as i3
from picazzo3.routing.place_route import PlaceComponents
from MMI22 import my_dc
from interface_mmi12 import NP_mmi12, AL_NP, SiN_NP


class my_exe2(PlaceComponents):
    DC_list = i3.ChildCellListProperty(default=[])

    def _default_DC_list(self):
        MMI22_list = []

        dc1_15 = my_dc(gap_inc_vec2=[110.0, 110.0, 110.0], name="ring1")
        dc2_15 = my_dc(gap_inc_vec2=[110.0, 110.0, 110.0], name="ring2")
        MMI22_list.append(dc1_15)
        MMI22_list.append(dc2_15)
        dc1_20 = my_dc(gap_inc_vec2=[100.0, 110.0, 120.0], name="ring3", width=20, cleave=250)
        dc2_20 = my_dc(gap_inc_vec2=[100.0, 110.0, 120.0], name="ring4", width=20, cleave=250)

        recess0 = NP_mmi12(pillar=True, pocket=False, tilt=False, width=133.0, length=210)
        recess1 = NP_mmi12(pillar=True, pocket=False, tilt=False, width=133.0, length=210)
        recess2 = NP_mmi12(pillar=True, pocket=False, tilt=False)
        recess3 = NP_mmi12(pillar=True, pocket=False, tilt=False)
        recess4 = NP_mmi12(pillar=True, pocket=True, tilt=False)
        recess5 = NP_mmi12(pillar=True, pocket=True, tilt=False)
        recess6 = NP_mmi12(pillar=True, pocket=False, tilt=False)

        recess7 = NP_mmi12(pillar=True, pocket=False, tilt=False)
        recess8 = NP_mmi12(pillar=True, pocket=False, tilt=False)
        recess9 = NP_mmi12(pillar=True, pocket=False, tilt=False)
        recess10 = NP_mmi12(pillar=True, pocket=False, tilt=False)
        recess11 = NP_mmi12(pillar=True, pocket=True, tilt=True)
        recess12 = NP_mmi12(pillar=True, pocket=True, tilt=True)
        recess13 = NP_mmi12(pillar=True, pocket=True, tilt=False)

        recess14 = NP_mmi12(pillar=True, pocket=False, tilt=False, width=133.0, length=210, double=False)
        recess15 = NP_mmi12(pillar=True, pocket=False, tilt=False, width=133.0, length=210, double=False)
        recess16 = NP_mmi12(pillar=True, pocket=False, tilt=False, double=False)
        recess17 = NP_mmi12(pillar=True, pocket=False, tilt=False, double=False)
        recess18 = NP_mmi12(pillar=True, pocket=True, tilt=False, double=False)
        recess19 = NP_mmi12(pillar=True, pocket=True, tilt=False, double=False)
        recess20 = NP_mmi12(pillar=True, pocket=False, tilt=False, double=False)

        recess21 = NP_mmi12(pillar=True, pocket=False, tilt=False, double=False)
        recess22 = NP_mmi12(pillar=True, pocket=False, tilt=False, double=False)
        recess23 = NP_mmi12(pillar=True, pocket=False, tilt=False, double=False)
        recess24 = NP_mmi12(pillar=True, pocket=False, tilt=False, double=False)
        recess25 = NP_mmi12(pillar=True, pocket=True, tilt=True, double=False)
        recess26 = NP_mmi12(pillar=True, pocket=True, tilt=True, double=False)
        recess27 = NP_mmi12(pillar=True, pocket=True, tilt=False, double=False)

        for i in range(0, 28, 1):
            print(i)
            _inst = locals()['recess{}'.format(i)]
            MMI22_list.append(_inst)

        MMI22_list.append(dc1_20)
        MMI22_list.append(dc2_20)
        #
        #
        Al0 = AL_NP(offset=5)
        Al1 = AL_NP(offset=5)
        Al2 = AL_NP()
        Al3 = AL_NP()
        Al4 = AL_NP()
        Al5 = AL_NP()
        Al6 = AL_NP()

        Al7 = AL_NP()
        Al8 = AL_NP()
        Al9 = AL_NP()
        Al10 = AL_NP()
        Al11 = AL_NP()
        Al12 = AL_NP()
        Al13 = AL_NP()

        Al14 = AL_NP(offset=5)
        Al15 = AL_NP(offset=5)
        Al16 = AL_NP()
        Al17 = AL_NP()
        Al18 = AL_NP()
        Al19 = AL_NP()
        Al20 = AL_NP()


        Al21 = AL_NP()
        Al22 = AL_NP()
        Al23 = AL_NP()
        Al24 = AL_NP()
        Al25 = AL_NP()
        Al26 = AL_NP()
        Al27 = AL_NP()


        for i in range(0, 28, 1):
            print(i)
            _inst = locals()['Al{}'.format(i)]
            MMI22_list.append(_inst)

        SiN0 = SiN_NP(width=92, length=210)
        SiN1 = SiN_NP(width=92, length=210)
        SiN2 = SiN_NP()
        SiN3 = SiN_NP()
        SiN4 = SiN_NP()
        SiN5 = SiN_NP()
        SiN6 = SiN_NP()
        SiN7 = SiN_NP()
        SiN8 = SiN_NP()
        SiN9 = SiN_NP()
        SiN10 = SiN_NP()
        SiN11 = SiN_NP(tilt=15)
        SiN12 = SiN_NP(tilt=15)
        SiN13 = SiN_NP()
        SiN14 = SiN_NP(width=92, length=210, double=False)
        SiN15 = SiN_NP(width=92, length=210, double=False)
        SiN16 = SiN_NP(double=False)
        SiN17= SiN_NP(double=False)
        SiN18= SiN_NP(double=False)
        SiN19= SiN_NP(double=False)
        SiN20= SiN_NP(double=False)
        SiN21= SiN_NP(double=False)
        SiN22= SiN_NP(double=False)
        SiN23= SiN_NP(double=False)
        SiN24 = SiN_NP(double=False)
        SiN25 = SiN_NP(double=False, tilt=15)
        SiN26 = SiN_NP(double=False, tilt=15)
        SiN27 = SiN_NP(double=False)
        for i in range(0, 28, 1):
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
            row = 3000
            trans["CHILD0"] = (0, 0)            #MMI
            trans["CHILD1"] = i3.HMirror(1250) - i3.Translation((2500, 0))      #MMI

            trans['CHILD2'] = (-14500, -3000 + row * 0)
            trans['CHILD3'] = (-14500, -3000 + row * 1)
            trans['CHILD4'] = (-14500, -3000 + row * 2)
            trans['CHILD5'] = (-14500, -3000 + row * 3)
            trans['CHILD6'] = (-14500, -3000 + row * 4)
            trans['CHILD7'] = (-14500, -3000 + row * 5)
            trans['CHILD8'] = (-14500, -3000 + row * 6)
            trans['CHILD9'] = i3.Rotation(rotation=180) + i3.Translation((14500, 0 + row * 0))
            trans['CHILD10'] = i3.Rotation(rotation=180) + i3.Translation((14500, 0 + row * 1))
            trans['CHILD11'] = i3.Rotation(rotation=180) + i3.Translation((14500, 0 + row * 2))
            trans['CHILD12'] = i3.Rotation(rotation=180) + i3.Translation((14500, 0 + row * 3))
            trans['CHILD13'] = i3.Rotation(rotation=180) + i3.Translation((14500, 0 + row * 4))
            trans['CHILD14'] = i3.Rotation(rotation=180) + i3.Translation((14500, 0 + row * 5))
            trans['CHILD15'] = i3.Rotation(rotation=180) + i3.Translation((14500, 0 + row * 6))
            trans['CHILD16'] = (-2500, -3000 + row * 0)
            trans['CHILD17'] = (-2500, -3000 + row * 1)
            trans['CHILD18'] = (-2500, -3000 + row * 2)
            trans['CHILD19'] = (-2500, -3000 + row * 3)
            trans['CHILD20'] = (-2500, -3000 + row * 4)
            trans['CHILD21'] = (-2500, -3000 + row * 5)
            trans['CHILD22'] = (-2500, -3000 + row * 6)
            trans['CHILD23'] = i3.Rotation(rotation=180) + i3.Translation((26500, 0 + row * 0))
            trans['CHILD24'] = i3.Rotation(rotation=180) + i3.Translation((26500, 0 + row * 1))
            trans['CHILD25'] = i3.Rotation(rotation=180) + i3.Translation((26500, 0 + row * 2))
            trans['CHILD26'] = i3.Rotation(rotation=180) + i3.Translation((26500, 0 + row * 3))
            trans['CHILD27'] = i3.Rotation(rotation=180) + i3.Translation((26500, 0 + row * 4))
            trans['CHILD28'] = i3.Rotation(rotation=180) + i3.Translation((26500, 0 + row * 5))
            trans['CHILD29'] = i3.Rotation(rotation=180) + i3.Translation((26500, 0 + row * 6))

            trans["CHILD30"] = (12000, 0)       #MMI
            trans["CHILD31"] = i3.HMirror(1250) + i3.Translation((9500, 0))     #MMI

            trans['CHILD32'] = (-14500, -3000 + row * 0)
            trans['CHILD33'] = (-14500, -3000 + row * 1)
            trans['CHILD34'] = (-14500, -3000 + row * 2)
            trans['CHILD35'] = (-14500, -3000 + row * 3)
            trans['CHILD36'] = (-14500, -3000 + row * 4)
            trans['CHILD37'] = (-14500, -3000 + row * 5)
            trans['CHILD38'] = (-14500, -3000 + row * 6)
            trans['CHILD39'] = i3.Rotation(rotation=180) + i3.Translation((14500, 0 + row * 0))
            trans['CHILD40'] = i3.Rotation(rotation=180) + i3.Translation((14500, 0 + row * 1))
            trans['CHILD41'] = i3.Rotation(rotation=180) + i3.Translation((14500, 0 + row * 2))
            trans['CHILD42'] = i3.Rotation(rotation=180) + i3.Translation((14500, 0 + row * 3))
            trans['CHILD43'] = i3.Rotation(rotation=180) + i3.Translation((14500, 0 + row * 4))
            trans['CHILD44'] = i3.Rotation(rotation=180) + i3.Translation((14500, 0 + row * 5))
            trans['CHILD45'] = i3.Rotation(rotation=180) + i3.Translation((14500, 0 + row * 6))
            trans['CHILD46'] = (-2500, -3000 + row * 0)
            trans['CHILD47'] = (-2500, -3000 + row * 1)
            trans['CHILD48'] = (-2500, -3000 + row * 2)
            trans['CHILD49'] = (-2500, -3000 + row * 3)
            trans['CHILD50'] = (-2500, -3000 + row * 4)
            trans['CHILD51'] = (-2500, -3000 + row * 5)
            trans['CHILD52'] = (-2500, -3000 + row * 6)
            trans['CHILD53'] = i3.Rotation(rotation=180) + i3.Translation((26500, 0 + row * 0))
            trans['CHILD54'] = i3.Rotation(rotation=180) + i3.Translation((26500, 0 + row * 1))
            trans['CHILD55'] = i3.Rotation(rotation=180) + i3.Translation((26500, 0 + row * 2))
            trans['CHILD56'] = i3.Rotation(rotation=180) + i3.Translation((26500, 0 + row * 3))
            trans['CHILD57'] = i3.Rotation(rotation=180) + i3.Translation((26500, 0 + row * 4))
            trans['CHILD58'] = i3.Rotation(rotation=180) + i3.Translation((26500, 0 + row * 5))
            trans['CHILD59'] = i3.Rotation(rotation=180) + i3.Translation((26500, 0 + row * 6))

            trans['CHILD60'] = (-14500, -3000 + row * 0)
            trans['CHILD61'] = (-14500, -3000 + row * 1)
            trans['CHILD62'] = (-14500, -3000 + row * 2)
            trans['CHILD63'] = (-14500, -3000 + row * 3)
            trans['CHILD64'] = (-14500, -3000 + row * 4)
            trans['CHILD65'] = (-14500, -3000 + row * 5)
            trans['CHILD66'] = (-14500, -3000 + row * 6)
            trans['CHILD67'] = i3.Rotation(rotation=180) + i3.Translation((14500, 0 + row * 0))
            trans['CHILD68'] = i3.Rotation(rotation=180) + i3.Translation((14500, 0 + row * 1))
            trans['CHILD69'] = i3.Rotation(rotation=180) + i3.Translation((14500, 0 + row * 2))
            trans['CHILD70'] = i3.Rotation(rotation=180) + i3.Translation((14500, 0 + row * 3))
            trans['CHILD71'] = i3.Rotation(rotation=180) + i3.Translation((14500, 0 + row * 4))
            trans['CHILD72'] = i3.Rotation(rotation=180) + i3.Translation((14500, 0 + row * 5))
            trans['CHILD73'] = i3.Rotation(rotation=180) + i3.Translation((14500, 0 + row * 6))
            trans['CHILD74'] = (-2500, -3000 + row * 0)
            trans['CHILD75'] = (-2500, -3000 + row * 1)
            trans['CHILD76'] = (-2500, -3000 + row * 2)
            trans['CHILD77'] = (-2500, -3000 + row * 3)
            trans['CHILD78'] = (-2500, -3000 + row * 4)
            trans['CHILD79'] = (-2500, -3000 + row * 5)
            trans['CHILD80'] = (-2500, -3000 + row * 6)
            trans['CHILD81'] = i3.Rotation(rotation=180) + i3.Translation((26500, 0 + row * 0))
            trans['CHILD82'] = i3.Rotation(rotation=180) + i3.Translation((26500, 0 + row * 1))
            trans['CHILD83'] = i3.Rotation(rotation=180) + i3.Translation((26500, 0 + row * 2))
            trans['CHILD84'] = i3.Rotation(rotation=180) + i3.Translation((26500, 0 + row * 3))
            trans['CHILD85'] = i3.Rotation(rotation=180) + i3.Translation((26500, 0 + row * 4))
            trans['CHILD86'] = i3.Rotation(rotation=180) + i3.Translation((26500, 0 + row * 5))
            trans['CHILD87'] = i3.Rotation(rotation=180) + i3.Translation((26500, 0 + row * 6))
            return trans

        def _generate_elements(self, elems):
            elems += i3.Rectangle(layer=i3.TECH.PPLAYER.PPLUS.LINE,
                                  center=(0, 7500),  # change
                                  box_size=(190, 21000))
            elems += i3.Rectangle(layer=i3.TECH.PPLAYER.PPLUS.LINE,
                                  center=(6000, 7500),  # change
                                  box_size=(190, 21000))

            return elems


# final = my_exe2(name="final")
# final_layout = final.Layout()
# final_layout.write_gdsii("execute_v3.gds")
