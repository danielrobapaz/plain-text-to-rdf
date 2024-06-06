from KnowledgeExtractionLayer.EntityLinking import EntityLinking
entities = ['Berlin', 'Capital', 'City', 'Germany',
            'Area', 'Population', 'Inhibitants', 'December',
            'Union', 'Surrounded', 'Brandenburg', 'Contiguous',
            'Postdam', 'Metropolitan_Area', 'Rhine-Ruhr', 
            'Banks', 'Spree', 'Flows', 'Western', 'Lakes', 
            'Boroughs', 'Location', 'European', 'Temperature',
            'Forests', 'Parks', 'Gardens', 'Canals', 'Michael_Jordan',
            ]


for i in range(5):
    print(f'{i+1}: ', end='')
    el = EntityLinking(entities)