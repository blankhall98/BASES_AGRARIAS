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

    #DONT EDIT THIS#
    'ppb_route': './data/raw/PPB/',
    'nuc_route': './data/raw/NUC/',
    'processed_route': './data/processed/',

    'error_1_message': 'Error1',
    'error_2_message': 'Error2'
    ###############
}
# --------------

#application
def main():

    t = Tester()
    m = Matcher(inputs,t)

    m.match()
    m.report()
    m.save()
    

# run command
if __name__ == '__main__':
    main()