#imports 
import pandas as pd

# MATCHER
class Matcher:

    def __init__(self,inputs,tester):
        print('matcher working')
        
        self.inputs = inputs
        self.tester = tester
        
        self.read_data()
        self.reduce_base()

    #Read PPB and NUC databases
    def read_data(self):
        #routes
        ppb_route = self.inputs['ppb_route']+self.inputs['ppb_filename']
        nuc_route = self.inputs['nuc_route']+self.inputs['nuc_filename']
        #read bases
        self.ppb = pd.read_excel(ppb_route)
        self.nuc = pd.read_excel(nuc_route)

        #### simulation####
        if self.inputs['simulation']:
            self.ppb = self.ppb.head(self.inputs['n_sim'])

    def reduce_base(self):
        #ppb significant columns
        ppb_sc = ['ESTADO','MUNICIPIO','NUCLEO_AGRARIO']
        self.ppb = self.ppb[ppb_sc]

    #Match 
    def match(self):
        self.mapping = []
        j = len(self.nuc)
        N = len(self.ppb)
        for i in range(len(self.ppb)):
            if i % 10 == 0:
                print(f'Progress: {i/N}% ...')

            #eliminate null and verbotten values
            verbotten = False
            for n in self.inputs['nulos']:
                if self.ppb.loc[i]['MUNICIPIO'].startswith(n) or self.ppb.loc[i]['MUNICIPIO']==n:
                    self.mapping.append['0']
                    verbotten = True
                    break
            
            #if the value is allowed, we search for the match:
            if not verbotten:
                matched_lvl1 = False
                counter = 0
                #lets first enter the level 1 region
                while not matched_lvl1 and counter < j:
                    a = self.ppb.loc[i]['MUNICIPIO']
                    b = self.nuc.loc[counter]['MUNICIPIO']
                    matched_lvl1 = self.tester.test(a,b)
                    counter = counter + 1
                
                #decide what to do depending if we found lvl 1 match
                #no match
                if not matched_lvl1:
                    self.mapping.append(self.inputs['error_1_message'])
                #match
                else:
                    reduced_nuc = self.nuc[self.nuc['MUNICIPIO'] == b].reset_index(drop=True)
                    jj = len(reduced_nuc)
                    matched_lvl2 = False
                    counter = 0
                    #lvl2 region
                    while not matched_lvl2 and counter < jj:
                        a = self.ppb.loc[i]['NUCLEO_AGRARIO']
                        b = reduced_nuc.loc[counter]['NOM_NUC']
                        matched_lvl2 = self.tester.test(a,b)
                        counter = counter + 1
                    #no match
                    if not matched_lvl2:
                        self.mapping.append(self.inputs['error_2_message'])
                    #match
                    else:
                        cve = reduced_nuc.loc[counter-1]['CLAVE']
                        self.mapping.append(cve)

    def report(self):
        self.ppb['Merged'] = self.mapping
        print(self.ppb['Merged'].describe())

    def save(self):
        saving_route = self.inputs['processed_route'] + self.inputs['matched_filename']
        self.ppb.to_csv(saving_route,index=False)