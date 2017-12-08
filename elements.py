
def elements_choice():
    user_element = input("Element: ")
    
    element_list = {
    'Hydrogen': 1.00794,
    'Helium': 4.0026,
    'Lithium': 6.941,
    'Beryllium': 9.012182,
    'Boron': 10.811,
    'Carbon': 12.011,
    'Nitrogen': 14.00674,
    'Oxygen': 15.9994,
    'Fluorine':	18.9984,
    'Neon':	20.1797,
    'Sodium': 22.98977,
    'Magnesium': 24.305,
    'Aluminum':	26.981539,
    'Silicon': 28.0855,
    'Phosphorus': 30.9738,
    'Sulfur': 32.066,
    'Chlorine':	35.4527,
    'Argon': 39.948,
    'Potassium': 39.0983,
    'Calcium': 40.078,
    'Scandium':	44.9559,
    'Titanium':	47.88,
    'Vanadium':	50.9415,
    'Chromium':	51.9961,
    'Manganese': 54.938,
    'Iron':	55.847,
    'Cobalt': 58.9332,
    'Nickel': 58.6934,
    'Copper': 63.546,
    'Zinc':	65.39,
    'Gallium':	69.723,
    'Germanium': 72.59,
    'Arsenic': 74.59215,
    'Selenium':	78.96,
    'Bromine': 79.904,
    'Krypton': 83.8,
    'Rubidium':	85.4678,
    'Strontium': 87.92,
    'Yttrium': 88.90585,
    'Zirconium': 91.224,
    'Niobium': 92.90638,
    'Molybdenum': 95.94,
    'Technetium': 97.91,
    'Ruthenium': 101.07,
    'Rhodium': 102.9055,
    'Palladium': 106.42,
    'Silver': 107.8682,
    'Cadmium': 112.411,
    'Indium': 114.818,
    'Tin': 118.71,
    'Antimony':	121.76,
    'Tellurium': 127.6,
    'Iodine': 126.90447,
    'Xenon': 131.29,
    'Cesium': 132.9054,
    'Barium': 137.327,
    'Lanthanum': 138.9055,
    'Cerium': 140.115,
    'Praseodymium':	140.90765,
    'Neodymium':144.24,
    'Promethium':145,
    'Samarium':	150.36,
    'Europium':	151.965,
    'Gadolinium':157.25,
    'Terbium': 158.92534,
    'Dysprosium': 162.5,
    'Holmium': 164.9303,
    'Erbium': 167.26,
    'Thulium': 168.93421,
    'Ytterbium': 173.04,
    'Lutetium':	174.967,
    'Hafnium': 178.49,
    'Tantalum':	180.9479,
    'Tungsten':	183.34,
    'Rhenium': 186.207,
    'Osmium': 190.2,
    'Iridium': 192.217,
    'Platinum':	195.08,
    'Gold':	196.9665,
    'Mercury': 200.59,
    'Thallium':	204.3833,
    'Lead':	207.2,
    'Bismuth': 208.98,
    'Polonium':	209,
    'Astatine':	210,
    'Radon': 222,
    'Francium':	223,
    'Radium': 226.025,
    'Actinium':	227.028,
    'Thorium': 232.0381,
    'Protactinium':	231.03588,
    'Uranium': 238.0289,
    'Neptunium': 237.048,
    'Plutonium': 244,
    'Americium': 243,
    'Curium': 247,
    'Berkelium': 247,
    'Californium': 251,
    'Einsteinium': 252,
    'Fermium': 257,
    'Mendelevium': 258,
    'Nobelium':	259,
    'Lawrencium': 262,
    'Rutherfordium': 261,
    'Dubnium': 262,
    'Seaborgium': 266,
    'Bohrium': 264,
    'Hassium': 277,
    'Meitnerium': 268,
    'Darmstadtium':	271,
    'Roentgenium': 272,
    'Copernicium': 277,
    'Nihonium':	284,
    'Flerovium': 290,
    'Moscovium': 288,
    'Livermorium': 290,
    'Tennessine': 291,
    'Oganesson': 292,
    }
    
    abbreviation = {
    'H': 1.00794,
    'He': 4.0026,
    'Li': 6.941,
    'Be': 9.012182,
    'B': 10.811,
    'C': 12.011,
    'N': 14.00674,
    'O': 15.9994,
    'F': 18.9984,
    'Ne': 20.1797,
    'Na': 22.98977,
    'Mg': 24.305,
    'Al': 26.981539,
    'Si': 28.0855,
    'P': 30.9738,
    'S': 32.066,
    'Cl': 35.4527,
    'Ar': 39.948,
    'K': 39.0983,
    'Ca': 40.078,
    'Sc': 44.9559,
    'Ti': 47.88,
    'V': 50.9415,
    'Cr': 51.9961,
    'Mn': 54.938,
    'Fe': 55.847,
    'Co': 58.9332,
    'Ni': 58.6934,
    'Cu': 63.546,
    'Zn': 65.39,
    'Ga': 69.723,
    'Ge': 72.59,
    'As': 74.59215,
    'Se': 78.96,
    'Br': 79.904,
    'Kr': 83.8,
    'Rb': 85.4678,
    'Sr': 87.92,
    'Y': 88.90585,
    'Zr': 91.224,
    'Nb': 92.90638,
    'Mo': 95.94,
    'Tc': 97.91,
    'Ru': 101.07,
    'Rh': 102.9055,
    'Pd': 106.42,
    'Ag': 107.8682,
    'Cd': 112.411,
    'In': 114.818,
    'Sn': 118.71,
    'Sb': 121.76,
    'Te': 127.6,
    'I': 126.90447,
    'Xe': 131.29,
    'Cs': 132.9054,
    'Ba': 137.327,
    'La': 138.9055,
    'Ce': 140.115,
    'Pr': 140.90765,
    'Nd': 144.24,
    'Pm': 145,
    'Sm': 150.36,
    'Eu': 151.965,
    'Gd': 157.25,
    'Tb': 158.92534,
    'Dy': 162.5,
    'Ho': 164.9303,
    'Er': 167.26,
    'Tm': 168.93421,
    'Yb': 173.04,
    'Lu': 174.967,
    'Hf': 178.49,
    'Ta': 180.9479,
    'W': 183.34,
    'Re': 186.207,
    'Os': 190.2,
    'Ir': 192.217,
    'Pt': 195.08,
    'Au': 196.9665,
    'Hg': 200.59,
    'Tl': 204.3833,
    'Pb': 207.2,
    'Bi': 208.98,
    'Po': 209,
    'At': 210,
    'Rn': 222,
    'Fr': 223,
    'Ra': 226.025,
    'Ac': 227.028,
    'Th': 232.0381,
    'Pa': 231.03588,
    'U': 238.0289,
    'Np': 237.048,
    'Pu': 244,
    'Am': 243,
    'Cm': 247,
    'Bk': 247,
    'Cf': 251,
    'Es': 252,
    'Fm': 257,
    'Md': 258,
    'No': 259,
    'Lr': 262,
    'Rf': 261,
    'Db': 262,
    'Sg': 266,
    'Bh': 264,
    'Hs': 277,
    'Mt': 268,
    'Ds': 271,
    'Rg': 272,
    'Cn': 277,
    'Nh': 284,
    'Fl': 290,
    'Mc': 288,
    'Lv': 290,
    'Ts': 291,
    'Og': 292,
        
    }
    
    if user_element in (element_list):
        return(element_list[user_element])
    elif user_element in (abbreviation):
        return(abbreviation[user_element])
    else:
        return("Invalid Input")
        
def user_input_element(user_element):
    print(user_element)
        
