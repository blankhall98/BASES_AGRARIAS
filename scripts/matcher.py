#imports 
import pandas as pd

# MATCHER
class Matcher:

    def __init__(self,inputs,tester):
        
        self.inputs = inputs
        self.tester = tester
        
        self.read_data()
        self.reduce_base()

        print(self.ppb.columns)
        print(self.nuc.columns)

        print(self.ppb.head())
        print(self.nuc.head())


    #Read PPB and NUC databases
    def read_data(self):
        #routes
        ppb_route = self.inputs['ppb_route']+self.inputs['ppb_filename']
        nuc_route = self.inputs['nuc_route']+self.inputs['nuc_filename']
        #read bases
        self.ppb = pd.read_excel(ppb_route)
        self.nuc = pd.read_excel(nuc_route)

    def reduce_base(self):
        #ppb significant columns
        ppb_sc = ['ESTADO','MUNICIPIO','NUCLEO_AGRARIO']
        self.ppb = self.ppb[ppb_sc]

    #Match 
    def match(self):
        self.mapping = []
        j = len(self.nuc)
        n = len(self.ppb)
        for i in range(len(self.ppb)):
            if i % 1000 == 0:
                print(f'Progress: {i/n}% ...')
            matched_lvl1 = False
            counter = 0
            #lets first enter the level 1 region
            while not matched_lvl1 and counter < j:
                matched_lvl1 = self.tester.test(self.ppb.loc[i]['MUNICIPIO'],self.nuc.loc[counter]['MUNICIPIO'])
                counter = counter + 1
            
            #decide what to do depending if we found lvl 1 match
            #no match
            if not matched_lvl1:
                self.mapping.append(self.inputs['error_1_message'])
            #match
            else:
                matched_lvl2 = False
                counter = 0
                #lvl2 region
                while not matched_lvl2 and counter < j:
                    matched_lvl2 = self.tester.test(self.ppb.loc[i]['NUCLEO_AGRARIO'],self.nuc.loc[counter]['NOM_NUC'])
                    counter = counter + 1
                #no match
                if not matched_lvl2:
                    self.mapping.append(self.inputs['error_2_message'])
                #match
                else:
                    cve = self.nuc.loc[counter-1]['CLAVE']
                    self.mapping.append(cve)

    def report(self):
        self.ppb['Merged'] = self.mapping
        print(self.ppb['Merged'].describe())

    def save(self):
        saving_route = self.inputs['processed_route'] + self.inputs['matched_filename']
        self.ppb.to_csv()