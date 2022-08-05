import Molecules
import re
import os
from colorama import init
from termcolor import colored


torr = 760.0021
mmHG = 760.0021
PSI = 14.6959
Pa = 101325
Bar = 1.01325

orbital_name = ['1s', '2s', '2p', '3s', '3p', '3d', '4s', '4p', '4d', '4f', '5s', '5p', '5d', '5f', '6s', '6p', '6d', '7s', '7p', '8s']
orbital_num = [2, 2, 6, 2, 6, 10, 2, 6, 10, 16, 2, 6, 10, 16, 2, 6, 10, 2, 6, 2]

Periodic_Table = {
    'H': ['Hydrogen', 1, 1.008, 'Non Metal'],
    'He': ['Helium', 2, 4.003, 'Noble Gas'],
    'Li': ['Lithium', 3, 6.941, 'Alkali Metal'],
    'Be': ['Beryllium', 4, 9.012, 'Alkaline Earth Metal'],
    'B': ['Boron', 5, 10.811, 'Non Metal'],
    'C': ['Carbon', 6, 12.011, 'Non Metal'],
    'N': ['Nitrogen', 7, 14.007, 'Non Metal'],
    'O': ['Oxygen', 8, 15.999, 'Non Metal'],
    'F': ['Flourine', 9, 18.998, 'Halogen'],
    'Ne': ['Neon', 10, 20.180, 'Noble Gas'],
    'Na': ['Sodium', 11, 22.990, 'Alkali Metal'],
    'Mg': ['Magnesium', 12, 24.305, 'Alkaline Earth Metal'],
    'Al': ['Aluminum', 13, 26.982, 'Other Metal'],
    'Si': ['Silicon', 14, 32.066, 'Non Metal'],
    'P': ['Phosphorus', 15, 30.974, 'Non Metal'],
    'S': ['Sulfur', 16, 32.066, 'Non Metal'],
    'Cl': ['Chlorine', 17, 35.453, 'Halogen'],
    'Ar': ['Argon', 18, 39.948, 'Noble Gas'],
    'K': ['Potassium', 19, 30.098, 'Halogen'],
    'Ca': ['Calcium', 20, 40.078, 'Alkali Metal'],
    'Sc': ['Scandium', 21, 44.956, 'Transition Metal'],
    'Ti': ['Titanium', 22, 47.88, 'Transition Metal'],
    'V': ['Vanadium', 23, 50.942, 'Transition Metal'],
    'Cr': ['Chromium', 24, 51.996, 'Transition Metal'],
    'Mn': ['Manganese', 25, 54.938, 'Transition Metal'],
    'Fe': ['Iron', 26, 55.933, 'Transition Metal'],
    'Co': ['Cobalt', 27, 58.633, 'Transition Metal'],
    'Ni': ['Nickel', 28, 58.693, 'Transition Metal'],
    'Cu': ['Copper', 29, 63.546, 'Transition Metal'],
    'Zn': ['Zinc', 30, 65.39, 'Transition Metal'],
    'Ga': ['Gallium', 31, 69.732, 'Other Metal'],
    'Ge': ['Germanium', 32, 72.61, 'Other Metal'],
    'As': ['Arsenic', 33, 74.922, 'Non Metal'],
    'Se': ['Selenium', 34, 78.09, 'Non Metal'],
    'Br': ['Bromine', 35, 79.904, 'Halogen'],
    'Kr': ['Krypton', 36, 84.80, 'Noble Gas'],
    'Rb': ['Rubidium', 37, 84.468, 'Alkali Metal'],
    'Sr': ['Strontium', 38, 87.62, 'Alkaline Earth Metal'],
    'Y': ['Yttrium', 39, 88.906, 'Transition Metal'],
    'Zr': ['Zirconium', 40, 91.224, 'Transition Metal'],
    'Nb': ['Niobium', 41, 92.906, 'Transition Metal'],
    'Mo': ['Molybdenum', 42, 95.94, 'Transition Metal'],
    'Tc': ['Technetium', 43, 98.907, 'Transition Metal'],
    'Ru': ['Ruthenium', 44, 101.07, 'Transition Metal'],
    'Rh': ['Rhodium', 45, 102.906, 'Transition Metal'],
    'Pa': ['Palladium', 46, 106.42, 'Transition Metal'],
    'Ag': ['Silver', 47, 107.868, 'Transition Metal'],
    'Cd': ['Cadmium', 48, 112.411, 'Transition Metal'],
    'In': ['Indium', 49, 114,818, 'Other Metal'],
    'Sn': ['Tin', 50, 118.71, 'Other Metal'],
    'Sb': ['Antimony', 51, 121.760, 'Other Metal'],
    'Te': ['Tellurium', 52, 127.6, 'Non Metal'],
    'I': ['Iodine', 53, 126.904, 'Halogen'],
    'Xe': ['Xenon', 54, 131.29, 'Noble Gas'],
    'Cs': ['Cesium', 55, 132.905, 'Alkali Metal'],
    'Ba': ['Barium', 56, 137.327, 'Alkaline Earth Metal'],
    'La': ['Lanthanum', 57, 139.906, 'Lanthanide'],
    'Ce': ['Cerium', 58, 140.115, 'Lanthanide'],
    'Pr': ['Praseodymium', 59, 140.908, 'Lanthanide'],
    'Nd': ['Neodymium', 60, 144.24, 'Lanthanide'],
    'Pm': ['Promethium', 61, 144.913, 'Lanthanide'],
    'Sm': ['Samarium', 62, 150.36, 'Lanthanide'],
    'Eu': ['Europium', 63, 151.966, 'Lanthanide'],
    'Gd': ['Gadolinium', 64, 157.25, 'Lanthanide'],
    'Tb': ['Terbium', 65, 158.925, 'Lanthanide'],
    'Dy': ['Dysprosium', 66, 162.5, 'Lanthanide'],
    'Ho': ['Holmium', 67, 164.93, 'Lanthanide'],
    'Er': ['Erbium', 68, 167.26, 'Lanthanide'],
    'Tm': ['Thullium', 69, 168.934, 'Lanthanide'],
    'Yb': ['Yitterbium', 70, 173.04, 'Lanthanide'],
    'Lu': ['Lutetium', 71, 174.967, 'Lanthanide'],
    'Hf': ['Hafnium', 72, 178.49, 'Transition Metal'],
    'Ta':['Tantium', 73, 180.948, 'Transition Metal'],
    'W': ['Tungsten', 74, 180.85, 'Transition Metal'],
    'Re': ['Rhenium', 75, 168.207, 'Transition Metal'],
    'Os': ['Osmium', 76, 190.23, 'Transition Metal'],
    'Ir': ['Iridium', 77, 192.22, 'Transition Metal'],
    'Pt': ['Platinum', 78, 195.08, 'Transition Metal'],
    'Au': ['Gold', 79, 196.967, 'Transition Metal'],
    'Hg': ['Mercury', 80, 200.59, 'Transition Metal'],
    'Tl': ['Thallium', 81, 204.383, 'Basic Metal'],
    'Pb': ['Lead', 82, 207.2, 'Basic Metal'],
    'Bi': ['Bismuth', 83, 208.98, 'Basic Metal'],
    'Po': ['Polonium', 84, 208.982 ,'Non Metal'],
    'At': ['Astatine', 85, 209.987, 'Halogen'],
    'Rn': ['Radon', 86, 222.018, 'Noble Gas'],
    'Fr': ['Francium', 87, 223.02, 'Alkali Metal'],
    'Ra': ['Radium', 88, 226.025, 'Alkaline Metal'],
    'Ac': ['Actinium', 89, 226.028, 'Actinide'],
    'Th': ['Thorium', 90, 232.038, 'Actinide'],
    'Pa': ['Protactinium', 91, 231.036, 'Actinide'],
    'U': ['Uranium', 92, 231.036, 'Actinide'],
    'Np': ['Neptunium', 93, 237.048, 'Actinide'],
    'Pu': ['Plutonium', 94, 244.064, 'Actinide'],
    'Am': ['Americium', 95, 243.061, 'Actinide'],
    'Cm': ['Curium', 96, 247.061, 'Actinide'],
    'Bk': ['Berkelium', 97, 247.07, 'Actinide'],
    'Cf': ['Californium', 98, 251.080, 'Actinide'],
    'Es': ['Einteinium', 99, 254, 'Actinide'],
    'Fm': ['Fermium', 100, 257.095, 'Actinide'],
    'Md': ['Mendelevium', 101, 258.1, 'Actinide'],
    'No': ['Nobelium', 102, 259.101, 'Actinide'],
    'Lr': ['Lawerncium', 103, 262, 'Actinide'],
    'Rf': ['Rutherfordium', 104, 261, 'Transition Metal'],
    'Db': ['Dubium', 105, 262, 'Transition Metal'],
    'Sg': ['Seaborgium', 106, 266, 'Transition Metal'],
    'Bh': ['Bohrium', 107, 264, 'Transition Metal'],
    'Hs': ['Hassium', 108, 269, 'Transition Metal'],
    'Mt': ['Meitnerium', 109, 268, 'Transition Metal'],
    'Ds': ['Darmstadium', 110, 269, 'Transition Metal'],
    'Rg': ['Roentgenium', 111, 272, 'Transition Metal'],
    'Cn': ['Copernicium', 112, 277, 'Transition Metal'],
    'Uut': ['Ununtrium', 113, 'unknown', 'Basic Metal'],
    'Fl': ['Flerovium', 114, 289, 'Basic Metal'],
    'Uup': ['Ununopentium', 115, 'unknown', 'Basic Metal'],
    'Lv': ['Livermorium', 116, 298, 'Basic Metal'],
    'Uus': ['Ununseptium', 117, 'unknown', 'Halogen'],
    'Uuo': ['Ununoctium', 118, 'unknown', 'Noble Gas'],
}

Periodic_Table_Visual = [
    ['H', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', 'He'],
    ['Li', 'Be', '', '', '', '', '', '', '', '', '', '', 'B', 'C', 'N', 'O', 'F', 'Ne'],
    ['Na', 'Mg', '', '', '', '', '', '', '', '', '', '', 'Al', 'Si', 'P', 'S', 'Cl', 'Ar'],
    ['K', 'Ca', 'Sc', 'Ti', 'V', 'Cr', 'Mn', 'Fe', 'Co', 'Ni', 'Cu', 'Zn', 'Ga', 'Ge', 'As', 'Se', 'Br', 'Kr'],
    ['Rb', 'Sr', 'Y', 'Ze', 'Nb', 'Mo', 'Tc', 'Ru', 'Rh', 'Pd', 'Ag', 'Cd', 'In', 'Sn', 'Sb', 'Te', 'I', 'Xe'],
    ['Cs', 'Ba', '[]', 'Hf', 'Ta', 'W', 'Re', 'Os', 'Ir', 'Pt', 'Au', 'Hg', 'Tl', 'Pb', 'Bi', 'Po', 'At ', 'Rn '],
    ['Fr', 'Ra', '[]', 'Rf', 'Db', 'Sg', 'Bh', 'Hs', 'Mt', 'Ds', 'Rg', 'Cn', 'Uut', 'Fl', 'Uup', 'Lv', 'Uus','Uuo'],
    ['', '--->>','La', 'Ce', 'Pr', 'Nd', 'Pm', 'Sm', 'Eu', 'Gd', 'Tb', 'Dy', 'Ho', 'Er', 'Tm', 'Yb', 'Lu'],
    ['', '--->>','Ac', 'Th', 'Pa', 'U', 'Np', 'Pu', 'Am', 'Cm', 'Bk', 'Cf', 'Es', 'Fm', 'Md', 'No', 'Lr']
]


def show_element(input): 
    os.system('cls' if os.name == 'nt' else 'clear') 
    if len(input) == 1:
        input = input[0]
    else:
        input = ''
    x = input
    if x in Periodic_Table:
        for element in Periodic_Table_Visual:
                
                for i in element:
                    while len(i) < 3:
                        i += ' '
                    while len(x) < 3:
                        x += ' '
                    if i == x:
                        print(colored(i, 'white', 'on_red'), end=' ')
                    else:
                        print(colored(i, 'green'), end=' ')
                print()
        print('name:                                    ' + Periodic_Table[input][0])
        print('atomic number:                           ' + str(Periodic_Table[input][1]))
        print('molecular weight:                        ' + str(Periodic_Table[input][2]))
        print('type:                                    ' + Periodic_Table[input][3])
    elif x == '':
        for element in Periodic_Table_Visual:
                for i in element:
                    while len(i) < 3:
                        i += ' '
                    print(colored(i, 'green'), end=' ')
                print()
    else:
        for element in Periodic_Table_Visual:
                for i in element:    
                    while len(i) < 3:
                            i += ' '
                    print(colored(i, 'red'), end=' ')
                print()
        print(colored('not found!', 'red'))
        

def get_type(Element):
    try:
        return Periodic_Table[Element][3]
    except:
        return 

def get_keys_from_value(d, val):
    a = []
    for i in d:
        if d[i][0] == val:
            a.append(i)
    if len(a) == 1:
        return a[0]
    return a

def get_name(Element):
    Element = Element[0]
    print(Element)
    if Element in Periodic_Table:
        return Periodic_Table[Element][0]
    
    d = Periodic_Table
    keys = get_keys_from_value(d, Element)
    if not keys:
        pass
    else:
        return keys
    # If the program doesn't find the Element in the periodic table, it looks for 
    # Molecule names. 
    d = Molecules.molecules
    keys = get_keys_from_value(d,Element)
    if not keys:
        return 'Element not found!'
    return keys
    
    

def get_atomic_number(Element):
    try:
        return Periodic_Table[Element[0]][1]
    except:
        return 'Element not found!'

def check_molecules(input):

    pass
def get_molecular_mass(input, Unit = True):
    Elements = re.findall('[A-Z][^A-Z]*', input[0])
    result = 0
    unit = ' g/mol '
    nunit = ''
    for Element in Elements:
        nElement = Element 
        match = re.match(r'([a-z]+)([0-9]+)', Element, re.I)
        if match:
            items = match.groups()
            if items[0] in Molecules.molecules:
                result += Molecules.molecules[items[0]][1] * float(items[1])
                nunit += f"({Molecules.molecules[items[0]][0]}){items[1]}"
                continue
            if items[0] in Periodic_Table:
                result += Periodic_Table[items[0]][2] * float(items[1])
                nunit += nElement
                
                continue
            print( Element + " Not in table")
            continue
        
        if Element in Molecules.molecules:
                result += Molecules.molecules[Element][1]
                nunit += f"({Molecules.molecules[Element][0]})"
                continue

        if Element in Periodic_Table:              
                result += Periodic_Table[Element][2]
                nunit += nElement
                continue
        print( Element + " Not in table")
        continue


    if Unit == True:
        return str(result) + ' ' + nunit + unit
    elif Unit == False:
        return [result, nunit]




def splice(input, type = 1):
    if type == 1:
        x = input.split(' ')
        if x[1] == 'moles' or x[1] == 'n':
            x[1] = 'mol'
        if x[1] == 'gram' or x[1] == 'grams':
            x[1] = 'g'
        try:
            x.remove('of')
            return x
        except:
            return x
    elif type == 2:
        x = input.split(' ')
        return x
    elif type == 3:
        x = input.split(' ')
        try:
            x.remove('to')
        except:
            pass
        return x



def unit_conversion(x, specific = False,  Unit = True):
        molar_ratio = [0, 0]
        amount = float(x[0])
        molecule = x[2]
        r = 3
        if specific == True:
            r = 7
        mol = ['n', 'mol', 'moles', 'mols']
        g = ['g', 'gram', 'grams']
        molar_ratio = get_molecular_mass(x[2:], False)
        if x[1] in mol:
            out = round(amount * molar_ratio[0], r)
            a = 'g '
        elif x[1] in g:
            out = round(amount / molar_ratio[0], r)
            a = 'mol '
        if Unit == True:
            return str(out) + ' ' + a + molar_ratio[1]
        return out





def to_atm(input, show_unit = True):
    amount = input[0]
    unit = input[1].lower()
    result = 'null'
    if unit == 'torr':
        result = amount / torr
    elif unit == 'mmhg':
        result = amount / mmHG
    elif unit == 'psi':
        result = amount / PSI
    elif unit == 'pa':
        result = amount / Pa
    elif unit == 'kpa':
        result = amount / Pa / 1000
    elif unit == 'bar':
        result = amount / Bar
    elif unit == 'atm':
        result = amount
    unit = ' atm'

    if show_unit == True:
        result = round(result, 5)
        out = str(result) + unit
        return out
    return result

def preassure_unit_conversion(input, specific = False,show_unit = True):
    try: #fix this
        r = 2
        if specific == True:
            r = 7
        amount = float(input[0])
        unit = input[1]
        unit2 = input[2].lower()
        atm = float(to_atm([amount, unit], False))
        result = 'null'
        if unit2 == 'torr':
            result = atm * torr
            unit2 = ' torr'
        elif unit2 == 'mmhg':
            result = atm * mmHG
            unit2 = ' mmHg'
        elif unit2 == 'pa':
            result = atm / Pa
            unit2 = ' Pa'
        elif unit2 == 'kpa':
            result = atm * Pa / 1000
            unit2 = ' kPa'
        elif unit2 == 'psi':
            result = atm * PSI
            unit2 = ' PSI'
        elif unit2 == 'bar':
            result = atm * Bar
            unit2 = 'Bar'
        else:
            result = atm
            unit2 = ' atm'    
        if show_unit == True:
            result = round(result, r)
            out = str(result) + ' ' + unit2
            return out
        return result
    except:
        return 'Error'

def energy_conversion(input, specific = False, show_unit = True):
    amount = float(input[0])
    unit = input[1].lower()
    unit2 = input[2].lower()
    if unit == 'cal':
        if unit2 == 'kcal':
            result = amount / 1000
            unit3='KCal'
        elif unit2 == 'joule'.casefold():
            result = amount * 4.184
            unit3='Joule'
        elif unit2 == 'kjoule'.casefold():
            result = amount * 0.004184
            unit3='KJoule'
        else:
            return str(amount) + ' Cal'
    elif unit == 'kcal'.casefold():
        if unit2 == 'cal'.casefold():
            result = amount * 1000
            unit3='Cal'
        elif unit2 == 'joule'.casefold():
            result = amount * 4184
            unit3='Joule'
        elif unit2 == 'kjoule'.casefold():
            result = amount * 4.184
            unit3='KJoule'
        else:
            return str(amount) + ' Cal'
    elif unit == 'joule'.casefold(): 
        if unit2 == 'kjoule':
            result = amount / 1000
            unit3='KJoule'
        elif unit2 == 'kcal':
            result = amount / 4184
            unit3='KCal'
        elif unit2 == 'cal':
            result = amount / 4.184
            unit3='Cal'
        else:
            return str(amount) + ' Joule'
    elif unit == 'kjoule':
        if unit2 == 'joule':
            result = amount * 1000
            unit3='Joule'
        elif unit2 == 'kcal':
            result = amount / 4184
            unit3='KCal'
        elif unit2 == 'cal':
            result = amount / 0.04184
            unit3='Cal'
        else:
            return str(amount) + ' KJoule'
    if show_unit == True:
        if specific == True:
            return str(round(result, 7)) + ' ' + unit3
        return str(result) + ' ' + unit3
    return result

def to_kelvin(input, target):
    amount = input
    unit = target.upper()
    result = amount
    if unit == 'C':
        result = amount + 273.15
    elif unit == 'F':
        result = (amount - 32) *  5/9 + (273.15)
    return result

def temp_change(input, specific = False, show_element = True):
    try: #fix this
        amount = input[0]
        unit = input[1]
        unit2 = input[2].upper()
        amount = float(amount)
        namount = to_kelvin(amount,  unit)
        unit = unit.upper()
        result = namount
        if unit2 == 'C': 
            result = namount - 273.15
        elif unit2 == 'F':
            result = ((namount - 273.15) * (9/5)) + 32
        else:
            unit2 = 'K'
        if show_element == True:
            if specific == True:
                return str(round(result, 7)) + unit2
            return str(round(result, 2)) + unit2
        return result
    except:
        return 'Error!'



def ect():
    i = 0
    for e in orbital_num:
        print(orbital_name[i] + str(e), end='  ')
        i += 1
    print()

def econfig(input):
    i = 0
    element = get_atomic_number(input[0])
    for e in orbital_num:
        element -= e
        remain = e
        if element <= 0:
            remain = e + element
            print(orbital_name[i] + str(remain), end='  ')
            break
        print(orbital_name[i] + str(remain), end='  ')
        i += 1

    return ''
