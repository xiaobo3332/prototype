from technologies import silicon_photonics
import ipkiss3.all as i3
from picazzo3.routing.place_route import PlaceComponents
from MMI22_v2 import my_dc, my_dc2, my_dc3
from interface_mmi12 import NP_mmi12, Heater #AL_NP, SiN_NP
# from ipkiss3.pcell.gdscell import GDSCell

# class mmi_slots_cell_test(GDSCell):
#
#     def _default_filename(self):
#         return 'comb reference_v1.gds'  # flatten the original gds file will cause crash issue!!
#
#     def _default_cell_name(self):
#         return 'HYD_2'

# mmi_slots_cell_test().Layout.view.write_gdsii("via_test.gds")

class my_exe2(PlaceComponents):
    DC_list = i3.ChildCellListProperty(default=[])
    Recess_list = i3.ChildCellListProperty(default=[])

    def _default_DC_list(self):
        MMI22_list = []

        # new MMI
        dc_10 = my_dc(gap_inc_vec=[430, 430, 430], name="ring1")
        dc_15 = my_dc(gap_inc_vec=[430, 430, 430],  name="ring2")
        dc_20 = my_dc2(gap_inc_vec=[430], width=10.0, name="ring3")
        dc_25 = my_dc3(gap_inc_vec=[430], width=10.0, name="ring4")
        dc_25_2 = my_dc3(gap_inc_vec=[430], width=10.0, name="ring5")
        MMI22_list.append(dc_10)
        MMI22_list.append(dc_15)
        MMI22_list.append(dc_20)
        MMI22_list.append(dc_25)
        MMI22_list.append(dc_25_2)

        return MMI22_list

    def _default_Recess_list(self):
        temporary_list = []
        recess0 = NP_mmi12(pillar=True, pocket=False, tilt=False)
        recess1 = NP_mmi12(pillar=True, pocket=False, tilt=False)
        recess2 = NP_mmi12(pillar=True, pocket=True, tilt=True)
        recess3 = NP_mmi12(pillar=True, pocket=True, tilt=True)
        recess4 = NP_mmi12(pillar=True, pocket=True, tilt=False)
        recess5 = NP_mmi12(pillar=True, pocket=True, tilt=False)

        recess6 = NP_mmi12(pillar=True, pocket=False, tilt=False, double=False)
        recess7 = NP_mmi12(pillar=True, pocket=False, tilt=False, double=False)
        recess8 = NP_mmi12(pillar=True, pocket=False, tilt=False, double=False)
        recess9 = NP_mmi12(pillar=True, pocket=False, tilt=False, double=False)
        recess10 = NP_mmi12(pillar=True, pocket=False, tilt=True, double=False)
        recess11 = NP_mmi12(pillar=True, pocket=False, tilt=True, double=False)

        recess12 = NP_mmi12(pillar=True, pocket=False, tilt=False, double=False)
        recess13 = NP_mmi12(pillar=True, pocket=False, tilt=False, double=False)
        recess14 = NP_mmi12(pillar=True, pocket=False, tilt=True, double=False)
        recess15 = NP_mmi12(pillar=True, pocket=False, tilt=True, double=False)
        recess16 = NP_mmi12(pillar=True, pocket=False, tilt=False, double=False)
        recess17 = NP_mmi12(pillar=True, pocket=False, tilt=False, double=False)

        # recess18 = NP_mmi12(pillar=True, pocket=True, tilt=False, double=False)
        # recess19 = NP_mmi12(pillar=True, pocket=True, tilt=False, double=False)
        # recess20 = NP_mmi12(pillar=True, pocket=False, tilt=False, double=False)
        #
        # recess21 = NP_mmi12(pillar=True, pocket=False, tilt=False, double=False)
        # recess22 = NP_mmi12(pillar=True, pocket=False, tilt=False, double=False)
        # recess23 = NP_mmi12(pillar=True, pocket=False, tilt=False, double=False)
        # recess24 = NP_mmi12(pillar=True, pocket=False, tilt=False, double=False)
        # recess25 = NP_mmi12(pillar=True, pocket=True, tilt=True, double=False)
        # recess26 = NP_mmi12(pillar=True, pocket=True, tilt=True, double=False)
        # recess27 = NP_mmi12(pillar=True, pocket=True, tilt=False, double=False)

        for i in range(0, 18, 1):
            print(i)
            _inst = locals()['recess{}'.format(i)]
            temporary_list.append(_inst)


        Al0 = Heater()
        Al1 = Heater()
        Al2 = Heater()
        Al3 = Heater()
        Al4 = Heater()
        Al5 = Heater()

        Al6 = Heater(width=200)
        Al7 = Heater(width=200)
        Al8 = Heater(width=200)
        Al9 = Heater(width=200)
        Al10 = Heater(width=200)
        Al11 = Heater(width=200)
        Al12 = Heater(width=250)
        Al13 = Heater(width=250)
        Al14 = Heater(width=250)
        Al15 = Heater(width=250)
        Al16 = Heater(width=250)
        Al17 = Heater(width=250)
        # Al18 = AL_NP()
        # Al19 = AL_NP()
        # Al20 = AL_NP()
        #
        #
        # Al21 = AL_NP()
        # Al22 = AL_NP()
        # Al23 = AL_NP()
        # Al24 = AL_NP()
        # Al25 = AL_NP()
        # Al26 = AL_NP()
        # Al27 = AL_NP()
        #
        #
        for i in range(0, 18, 1):
            print(i)
            _inst = locals()['Al{}'.format(i)]
            temporary_list.append(_inst)
        #
        # SiN0 = SiN_NP(width=92, length=210)
        # SiN1 = SiN_NP(width=92, length=210)
        # SiN2 = SiN_NP()
        # SiN3 = SiN_NP()
        # SiN4 = SiN_NP()
        # SiN5 = SiN_NP()
        # SiN6 = SiN_NP()
        # SiN7 = SiN_NP()
        # SiN8 = SiN_NP()
        # SiN9 = SiN_NP()
        # SiN10 = SiN_NP()
        # SiN11 = SiN_NP(tilt=15)
        # SiN12 = SiN_NP(tilt=15)
        # SiN13 = SiN_NP()
        # SiN14 = SiN_NP(width=92, length=210, double=False)
        # SiN15 = SiN_NP(width=92, length=210, double=False)
        # SiN16 = SiN_NP(double=False)
        # SiN17= SiN_NP(double=False)
        # SiN18= SiN_NP(double=False)
        # SiN19= SiN_NP(double=False)
        # SiN20= SiN_NP(double=False)
        # SiN21= SiN_NP(double=False)
        # SiN22= SiN_NP(double=False)
        # SiN23= SiN_NP(double=False)
        # SiN24 = SiN_NP(double=False)
        # SiN25 = SiN_NP(double=False, tilt=15)
        # SiN26 = SiN_NP(double=False, tilt=15)
        # SiN27 = SiN_NP(double=False)
        # for i in range(0, 28, 1):
        #     print(i)
        #     _inst = locals()['SiN{}'.format(i)]
        #     MMI22_list.append(_inst)

        return temporary_list

    def _default_child_cells(self):
        child_cells = dict()
        for counter, child in enumerate(self.DC_list):
            print 'child number' + str(counter)
            child_cells['CHILD' + str(counter)] = child
            print 'child name ' + str(child.name)
            print child
        for counter, child in enumerate(self.Recess_list):
            print 'child number' + str(counter)
            child_cells['CHIL' + str(counter)] = child
            print 'child name ' + str(child.name)
            print child
        return child_cells

    class Layout(PlaceComponents.Layout):

        def _default_child_transformations(self):
            trans = dict()
            row = 5000
            trans["CHILD0"] = (0, 0)            #MMI
            trans["CHILD1"] = i3.HMirror(2500) - i3.Translation((5000, 0))      #MMI
            trans["CHILD2"] = i3.HMirror(0) + i3.Translation((20000, 0))  # MMI
            trans["CHILD3"] = i3.Translation((16000, 10000))  # MMI
            trans['CHILD4'] = i3.VMirror(0)+i3.Translation((16000, 20000)) #MMI

            trans['CHIL0'] = (-16000, -4000 + row * 0)
            trans['CHIL1'] = (-16000, -4000 + row * 1)
            trans['CHIL2'] = (-16000, -4000 + row * 2)
            trans['CHIL3'] = (-16000, -4000 + row * 3)
            trans['CHIL4'] = (-16000, -4000 + row * 4)
            trans['CHIL5'] = (-16000, -4000 + row * 5)
            trans['CHIL6'] = i3.Rotation(rotation=180) + i3.Translation((16000, -1000 + row * 0))
            trans['CHIL7'] = i3.Rotation(rotation=180) + i3.Translation((16000, -1000 + row * 1))
            trans['CHIL8'] = i3.Rotation(rotation=180) + i3.Translation((16000, -1000 + row * 2))
            trans['CHIL9'] = i3.Rotation(rotation=180) + i3.Translation((16000, -1000 + row * 3))
            trans['CHIL10'] = i3.Rotation(rotation=180) + i3.Translation((16000, -1000 + row * 4))
            trans['CHIL11'] = i3.Rotation(rotation=180) + i3.Translation((16000, -1000 + row * 5))
            trans['CHIL12'] = (4000, -4000 + row * 0)
            trans['CHIL13'] = (4000, -4000 + row * 1)
            trans['CHIL14'] = (4000, -4000 + row * 2)
            trans['CHIL15'] = (4000, -4000 + row * 3)
            trans['CHIL16'] = (4000, -4000 + row * 4)
            trans['CHIL17'] = (4000, -4000 + row * 5)

            trans['CHIL18'] = (-16000, -4000 + row * 0)
            trans['CHIL19'] = (-16000, -4000 + row * 1)
            trans['CHIL20'] = (-16000, -4000 + row * 2)
            trans['CHIL21'] = (-16000, -4000 + row * 3)
            trans['CHIL22'] = (-16000, -4000 + row * 4)
            trans['CHIL23'] = (-16000, -4000 + row * 5)
            trans['CHIL24'] = i3.Rotation(rotation=180) + i3.Translation((16000, -1000 + row * 0))
            trans['CHIL25'] = i3.Rotation(rotation=180) + i3.Translation((16000, -1000 + row * 1))
            trans['CHIL26'] = i3.Rotation(rotation=180) + i3.Translation((16000, -1000 + row * 2))
            trans['CHIL27'] = i3.Rotation(rotation=180) + i3.Translation((16000, -1000 + row * 3))
            trans['CHIL28'] = i3.Rotation(rotation=180) + i3.Translation((16000, -1000 + row * 4))
            trans['CHIL29'] = i3.Rotation(rotation=180) + i3.Translation((16000, -1000 + row * 5))

            # for _ in np.arange(10):
            #     trans['CHIL{}'.format(_)] = NotImplemented
            for _ in range(30,36,1):
                trans['CHIL{}'.format(_)] = (4000,-4000+ row *(_-30))
            # trans['CHIL30'] = (4000, -4000 + row * 0)
            # trans['CHIL31'] = (4000, -4000 + row * 1)
            # trans['CHIL32'] = (4000, -4000 + row * 2)
            # trans['CHIL33'] = (4000, -4000 + row * 3)
            # trans['CHIL34'] = (4000, -4000 + row * 4)
            # trans['CHIL35'] = (4000, -4000 + row * 5)
            # trans['CHILD23'] = i3.Rotation(rotation=180) + i3.Translation((26500, 0 + row * 0))
            # trans['CHILD24'] = i3.Rotation(rotation=180) + i3.Translation((26500, 0 + row * 1))
            # trans['CHILD25'] = i3.Rotation(rotation=180) + i3.Translation((26500, 0 + row * 2))
            # trans['CHILD26'] = i3.Rotation(rotation=180) + i3.Translation((26500, 0 + row * 3))
            # trans['CHILD27'] = i3.Rotation(rotation=180) + i3.Translation((26500, 0 + row * 4))
            # trans['CHILD28'] = i3.Rotation(rotation=180) + i3.Translation((26500, 0 + row * 5))
            # trans['CHILD29'] = i3.Rotation(rotation=180) + i3.Translation((26500, 0 + row * 6))



            # trans['CHILD32'] = (-14500, -3000 + row * 0)
            # trans['CHILD33'] = (-14500, -3000 + row * 1)
            # trans['CHILD34'] = (-14500, -3000 + row * 2)
            # trans['CHILD35'] = (-14500, -3000 + row * 3)
            # trans['CHILD36'] = (-14500, -3000 + row * 4)
            # trans['CHILD37'] = (-14500, -3000 + row * 5)
            # trans['CHILD38'] = (-14500, -3000 + row * 6)
            # trans['CHILD39'] = i3.Rotation(rotation=180) + i3.Translation((14500, 0 + row * 0))
            # trans['CHILD40'] = i3.Rotation(rotation=180) + i3.Translation((14500, 0 + row * 1))
            # trans['CHILD41'] = i3.Rotation(rotation=180) + i3.Translation((14500, 0 + row * 2))
            # trans['CHILD42'] = i3.Rotation(rotation=180) + i3.Translation((14500, 0 + row * 3))
            # trans['CHILD43'] = i3.Rotation(rotation=180) + i3.Translation((14500, 0 + row * 4))
            # trans['CHILD44'] = i3.Rotation(rotation=180) + i3.Translation((14500, 0 + row * 5))
            # trans['CHILD45'] = i3.Rotation(rotation=180) + i3.Translation((14500, 0 + row * 6))
            # trans['CHILD46'] = (-2500, -3000 + row * 0)
            # trans['CHILD47'] = (-2500, -3000 + row * 1)
            # trans['CHILD48'] = (-2500, -3000 + row * 2)
            # trans['CHILD49'] = (-2500, -3000 + row * 3)
            # trans['CHILD50'] = (-2500, -3000 + row * 4)
            # trans['CHILD51'] = (-2500, -3000 + row * 5)
            # trans['CHILD52'] = (-2500, -3000 + row * 6)
            # trans['CHILD53'] = i3.Rotation(rotation=180) + i3.Translation((26500, 0 + row * 0))
            # trans['CHILD54'] = i3.Rotation(rotation=180) + i3.Translation((26500, 0 + row * 1))
            # trans['CHILD55'] = i3.Rotation(rotation=180) + i3.Translation((26500, 0 + row * 2))
            # trans['CHILD56'] = i3.Rotation(rotation=180) + i3.Translation((26500, 0 + row * 3))
            # trans['CHILD57'] = i3.Rotation(rotation=180) + i3.Translation((26500, 0 + row * 4))
            # trans['CHILD58'] = i3.Rotation(rotation=180) + i3.Translation((26500, 0 + row * 5))
            # trans['CHILD59'] = i3.Rotation(rotation=180) + i3.Translation((26500, 0 + row * 6))
            #
            # trans['CHILD60'] = (-14500, -3000 + row * 0)
            # trans['CHILD61'] = (-14500, -3000 + row * 1)
            # trans['CHILD62'] = (-14500, -3000 + row * 2)
            # trans['CHILD63'] = (-14500, -3000 + row * 3)
            # trans['CHILD64'] = (-14500, -3000 + row * 4)
            # trans['CHILD65'] = (-14500, -3000 + row * 5)
            # trans['CHILD66'] = (-14500, -3000 + row * 6)
            # trans['CHILD67'] = i3.Rotation(rotation=180) + i3.Translation((14500, 0 + row * 0))
            # trans['CHILD68'] = i3.Rotation(rotation=180) + i3.Translation((14500, 0 + row * 1))
            # trans['CHILD69'] = i3.Rotation(rotation=180) + i3.Translation((14500, 0 + row * 2))
            # trans['CHILD70'] = i3.Rotation(rotation=180) + i3.Translation((14500, 0 + row * 3))
            # trans['CHILD71'] = i3.Rotation(rotation=180) + i3.Translation((14500, 0 + row * 4))
            # trans['CHILD72'] = i3.Rotation(rotation=180) + i3.Translation((14500, 0 + row * 5))
            # trans['CHILD73'] = i3.Rotation(rotation=180) + i3.Translation((14500, 0 + row * 6))
            # trans['CHILD74'] = (-2500, -3000 + row * 0)
            # trans['CHILD75'] = (-2500, -3000 + row * 1)
            # trans['CHILD76'] = (-2500, -3000 + row * 2)
            # trans['CHILD77'] = (-2500, -3000 + row * 3)
            # trans['CHILD78'] = (-2500, -3000 + row * 4)
            # trans['CHILD79'] = (-2500, -3000 + row * 5)
            # trans['CHILD80'] = (-2500, -3000 + row * 6)
            # trans['CHILD81'] = i3.Rotation(rotation=180) + i3.Translation((26500, 0 + row * 0))
            # trans['CHILD82'] = i3.Rotation(rotation=180) + i3.Translation((26500, 0 + row * 1))
            # trans['CHILD83'] = i3.Rotation(rotation=180) + i3.Translation((26500, 0 + row * 2))
            # trans['CHILD84'] = i3.Rotation(rotation=180) + i3.Translation((26500, 0 + row * 3))
            # trans['CHILD85'] = i3.Rotation(rotation=180) + i3.Translation((26500, 0 + row * 4))
            # trans['CHILD86'] = i3.Rotation(rotation=180) + i3.Translation((26500, 0 + row * 5))
            # trans['CHILD87'] = i3.Rotation(rotation=180) + i3.Translation((26500, 0 + row * 6))
            return trans


        def _generate_elements(self, elems):
            elems += i3.Rectangle(layer=i3.TECH.PPLAYER.PPLUS.LINE,
                                  center=(0, 10000),  # change
                                  box_size=(190, 30000))
            elems += i3.Rectangle(layer=i3.TECH.PPLAYER.PPLUS.LINE,
                                  center=(10000, 10000),  # change
                                  box_size=(190, 30000))
            elems += i3.Rectangle(layer=i3.TECH.PPLAYER.PPLUS.LINE,
                                  center=(6000+13905+190/2, 10000),  # change
                                  box_size=(190, 30000))
            elems += i3.Rectangle(layer=i3.TECH.PPLAYER.PPLUS.LINE,
                                  center=(5000, 15000),  # change
                                  box_size=(30000, 190))
            elems += i3.Rectangle(layer=i3.TECH.PPLAYER.SIL.LINE,
                                  center=(0, 10000),  # change
                                  box_size=(210, 30000))

            # Medphab = mmi_slots_cell_test()
            # elems += i3.ARef(n_o_periods=(2,6), period=(20000,5000), reference=Medphab, origin=(-21400,13625))

            return elems


# final = my_exe2(name="final")
# final_layout = final.Layout()
# final_layout.write_gdsii("execute_v8.gds")
