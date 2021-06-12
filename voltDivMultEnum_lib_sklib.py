from skidl import Pin, Part, Alias, SchLib, SKIDL, TEMPLATE

SKIDL_lib_version = '0.0.1'

voltDivMultEnum_lib = SchLib(tool=SKIDL).add_parts(*[
        Part(**{ 'name':'R', 'dest':TEMPLATE, 'tool':SKIDL, 'keywords':'res resistor', 'description':'Resistor', '_match_pin_regex':False, 'pyspice':{'name': 'R', 'kw': {'value': 'resistance', 'resistance': 'resistance', 'ac': 'ac', 'multiplier': 'multiplier', 'm': 'multiplier', 'scale': 'scale', 'temp': 'temperature', 'temperature': 'temperature', 'dtemp': 'device_temperature', 'device_temperature': 'device_temperature', 'noisy': 'noisy', 'p': 'plus', 'n': 'minus'}, 'add': <function add_part_to_circuit at 0x10c8658b0>}, 'ref_prefix':'R', 'num_units':1, 'fplist':None, 'do_erc':True, 'aliases':Alias(), 'pin':None, 'footprint':None, 'pins':[
            Pin(num='1',name='p',func=Pin.types.PASSIVE,do_erc=True),
            Pin(num='2',name='n',func=Pin.types.PASSIVE,do_erc=True)] }),
        Part(**{ 'name':'V', 'dest':TEMPLATE, 'tool':SKIDL, '_match_pin_regex':False, 'keywords':'voltage source', 'description':'Voltage source', '_aliases':Alias({'v', 'vs', 'ammeter', 'AMMETER', 'VS'}), 'pyspice':{'name': 'V', 'kw': {'value': 'dc_value', 'dc_value': 'dc_value', 'p': 'plus', 'n': 'minus'}, 'add': <function add_part_to_circuit at 0x10c8658b0>}, 'dc_value':UnitValue(1 V), 'ref_prefix':'V', 'num_units':1, 'fplist':None, 'do_erc':True, 'aliases':Alias({'v', 'vs', 'ammeter', 'AMMETER', 'VS'}), 'pin':None, 'footprint':None, 'pins':[
            Pin(num='1',name='p',func=Pin.types.PASSIVE,do_erc=True),
            Pin(num='2',name='n',func=Pin.types.PASSIVE,do_erc=True)] })])