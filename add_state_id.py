import geopandas
import sys

shp = geopandas.read_file(sys.argv[1])

# drop fid and cat columns
del shp['fid']
del shp['cat']

ST_ID = {
    'Puducherry': 'IN-PY',
    'Lakshadweep': 'IN-LD',
    'Ladakh': 'IN-LA',
    'Jammu and Kashmir': 'IN-JK',
    'Jammu & Kashmir': 'IN-JK',
    'Delhi': 'IN-DL',
    'NCT of Delhi': 'IN-DL',
    'Daman and Diu': 'IN-DD',
    'Daman & Diu': 'IN-DD',
    'Dadra and Nagar Haveli': 'IN-DN',
    'Dadara & Nagar Havelli': 'IN-DN',
    'Chandigarh': 'IN-CH',
    'Andaman and Nicobar Islands': 'IN-AN',
    'Andaman & Nicobar Island': 'IN-AN',
    'West Bengal': 'IN-WB',
    'Uttar Pradesh': 'IN-UP',
    'Uttarakhand': 'IN-UT',
    'Tripura': 'IN-TR',
    'Telangana': 'IN-TG',
    'Tamil Nadu': 'IN-TN',
    'Sikkim': 'IN-SK',
    'Rajasthan': 'IN-RJ',
    'Punjab': 'IN-PB',
    'Odisha': 'IN-OR',
    'Nagaland': 'IN-NL',
    'Mizoram': 'IN-MZ',
    'Meghalaya': 'IN-ML',
    'Manipur': 'IN-MN',
    'Maharashtra': 'IN-MH',
    'Madhya Pradesh': 'IN-MP',
    'Kerala': 'IN-KL',
    'Karnataka': 'IN-KA',
    'Jharkhand': 'IN-JH',
    'Himachal Pradesh': 'IN-HP',
    'Haryana': 'IN-HR',
    'Gujarat': 'IN-GJ',
    'Goa': 'IN-GA',
    'Chhattisgarh': 'IN-CT',
    'Bihar': 'IN-BR',
    'Assam': 'IN-AS',
    'Arunachal Pradesh': 'IN-AR',
    'Andhra Pradesh': 'IN-AP'
}

ids = []
ids_ = []
for st_nm in shp['ST_NM']:
    ids.append(ST_ID[st_nm])
    ids_.append(ST_ID[st_nm].replace('IN-', ''))

shp['ST_ID'] = ids
shp['ID'] = ids_

shp.to_file("india_states.shp")
        