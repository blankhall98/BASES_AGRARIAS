#Import matcher and tester
from scripts.matcher import Matcher
from scripts.tester import Tester

# --- INPUTS ---
inputs = {
    #EDIT THIS#
    'ppb_filename': 'chiapas.xlsx',
    'nuc_filename': 'NA_chiapas.xlsx',

    'matched_filename': 'match_chiapas.csv',
    ###########

    #ONLY EDIT THIS IF SIMULATION#
    'simulation': True,
    'n_sim': 100,

    ##############################

    #DONT EDIT THIS#
    'ppb_route': './data/raw/PPB/',
    'nuc_route': './data/raw/NUC/',
    'processed_route': './data/processed/',

    'error_1_message': 'Error1',
    'error_2_message': 'Error2',

    'nulos': ['0','NO DEFINIDO','NO ESPECIFICADO','PEQUEÑA PROPIEDAD','PEQUENA PROPIEDAD'],
    'cabeceras': ['CAB, MPAL,','CAB, MUNICIPAL','CABECERA MUNICIPAL'],
    'remover': ['N,C,P,E,','N,C,P,','B,C,','P,P,','RANCH,','POB,','C,A,G,','COOP,','COL',
                'AMP,','AMPL,','COPROP,','COOPRO,','RIA,','PP','RIA','RIB,','SPR','COL,']

    ###############
}
# --------------

#application
def main():

    t = Tester(inputs)
    m = Matcher(inputs,t)

    m.match()
    m.report()
    m.save()
    

# run command
if __name__ == '__main__':
    main()