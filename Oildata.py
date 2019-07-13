Olive=[
'olive1',
'olive2',
'olive3',
'olive4',
'olive5',
'olive6']

oil=[
'Regular',
'Premium',
'Super',
'Especial'
]

a={
('mix1'):0.45,
('mix2'):0.30,
('mix3'):0.60,
('mix4'):0.34,
('mix5'):0.38,
('mix6'):0.30
}

s={
('mix1'):0.02,
('mix2'):0.04,
('mix3'):0.01,
('mix4'):0.03,
('mix5'):0.05,
('mix6'):0.01
}

c={
('mix1'):75,
('mix2'):60,
('mix3'):115,
('mix4'):35,
('mix5'):40,
('mix6'):30
}

l={
('regular'):0.32,
('premium'):0.38,
('super'):0.45,
('especial'):0.50
}

u={
('regular'):0.05,
('premium'):0.04,
('super'):0.03,
('especial'):0.02
}

p={
('regular'):60,
('premium'):80,
('super'):90,
('especial'):110
}

d={
('regular'):3000,
('premium'):2000,
('super'):1500,
('especial'):600
}

import Oilmodel
Oilmodel.solve(Olive,oil,a,s,c,l,u,p,d)
