constant = [\
  'V1',
  'Km1',
  'V2',
  'Km2',
  'V3',
  'Km3',
  'V4',
  'Km4',
  'V5',
  'Km5',
  'V6',
  'Km6',
  'KimERK',
  'KexERK',
  'KimpERK',
  'KexpERK',
  'KimppERK',
  'KexppERK',
  'V10',
  'Km10',
  'n10',
  'p11',
  'p12',
  'p13',
  'V14',
  'Km14',
  'V15',
  'Km15',
  'p16',
  'p17',
  'KimDUSP',
  'KexDUSP',
  'KimpDUSP',
  'KexpDUSP',
  'V20',
  'Km20',
  'V21',
  'Km21',
  'p22',
  'p23',
  'V24',
  'Km24',
  'V25',
  'Km25',
  'KimRSK',
  'KexRSK',
  'V27',
  'Km27',
  'V28',
  'Km28',
  'V29',
  'Km29',
  'V30',
  'Km30',
  'V31',
  'Km31',
  'n31',
  'p32',
  'p33',
  'p34',
  'V35',
  'Km35',
  'V36',
  'Km36',
  'V37',
  'Km37',
  'p38',
  'p39',
  'KimFOS',
  'KexFOS',
  'KimpcFOS',
  'KexpcFOS',
  'V42',
  'Km42',
  'V43',
  'Km43',
  'V44',
  'Km44',
  'p45',
  'p46',
  'p47',
  'm47',
  'p48',
  'p49',
  'm49',
  'p50',
  'p51',
  'm51',
  'p52',
  'm52',
  'p53',
  'p54',
  'm54',
  'p55',
  'p56',
  'm56',
  'V57',
  'Km57',
  'n57',
  'p58',
  'p59',
  'p60',
  'p61',
  'KimF',
  'KexF',
  'p63',
  'KF31',
  'nF31',
  #
  'a',
  'Vn',
  'Vc',
  ##
  'Ligand',
  'EGF',
  'HRG'\
]

#name2idx(constant)
for i,name in enumerate(constant):
  exec('%s=%d'%(name,i))

def setParamConst():
  x = [0]*len(constant)
  x[V1] = 0.34284837
  x[Km1] = 307.0415253
  x[V2] = 2.20e-01
  x[Km2] = 3.50e+02
  x[V3] = 7.20e-01
  x[Km3] = 1.60e+02
  x[V4] = 6.48e-01
  x[Km4] = 6.00e+01
  x[V5] = 19.49872346
  x[Km5]  =29.94073716
  x[V6] = x[V5]
  x[Km6] = x[Km5]
  x[KimERK] = 1.20e-02
  x[KexERK] = 1.80e-02
  x[KimpERK] = 1.20e-02
  x[KexpERK] = 1.80e-02
  x[KimppERK] = 1.10e-02
  x[KexppERK] = 1.30e-02
  x[V10] = 29.24109258
  x[Km10] = 169.0473748
  x[n10] = 3.970849295
  x[p11] = 0.000126129
  x[p12] = 0.007875765
  x[p13] = 0.001245747
  x[V14] = 5.636949216
  x[Km14] = 34180.48
  x[V15] = 2.992346912
  x[Km15] = 0.001172165
  x[p16] = 2.57e-04
  x[p17] = 9.63e-05
  x[KimDUSP] = 0.024269764
  x[KexDUSP] = 0.070467899
  x[KimpDUSP] = x[KimDUSP]
  x[KexpDUSP] = x[KexDUSP]
  x[V20] = 0.157678678
  x[Km20] = 735598.6967
  x[V21] = 0.005648117
  x[Km21] = 387.8377182
  x[p22] = 2.57e-04
  x[p23] = 9.63e-05
  x[V24] = 0.550346114
  x[Km24] = 29516.06587
  x[V25] = 10.09063736
  x[Km25] = 0.913939859
  x[KimRSK] = 0.025925065
  x[KexRSK] = 0.129803956
  x[V27] = 19.23118154
  x[Km27] = 441.5834425
  x[V28] = 6.574759504
  x[Km28] = 14.99180922
  x[V29] = 0.518529841
  x[Km29] = 21312.69109
  x[V30] = 13.79479021
  x[Km30] = 15.04396629
  x[V31] = 0.655214248
  x[Km31] = 185.9760682
  x[n31] = 1.988003164
  x[KF31] = 0.013844393
  x[nF31] = 2.800340453
  x[p32] = 0.003284434
  x[p33] = 0.000601234
  x[p34] = 7.65E-05
  x[V35] = 8.907637012
  x[Km35] = 8562.744184
  x[V36] = 0.000597315
  x[Km36] = 528.552427
  x[V37] = 1.745848179
  x[Km37] = 0.070379236
  x[p38] = 2.57e-04
  x[p39] = 9.63e-05
  x[KimFOS] = 0.54528521
  x[KexFOS] = 0.133249762
  x[KimpcFOS] = x[KimFOS]
  x[KexpcFOS] = x[KexFOS]
  x[V42] = 0.909968714
  x[Km42] = 3992.061328
  x[V43] = 0.076717457
  x[Km43] = 1157.116021
  x[V44] = 0.078344305
  x[Km44] = 0.051168202
  x[p45] = 2.57e-04
  x[p46] = 9.63e-05
  x[p47] = 0.001670815
  x[m47] = 15.80783969
  x[p48] = 0.686020478
  x[p49] = 0.314470502
  x[m49] = 2.335459127
  x[p50] = 26.59483436
  x[p51] = 0.01646825
  x[m51] = 9.544308421
  x[p52] = x[p47]
  x[m52] = x[m47]
  x[p53] = x[p48]
  x[p54] = x[p49]
  x[m54] = x[m49]
  x[p55] = x[p50]
  x[p56] = x[p51]
  x[m56] = x[m51]
  x[V57] = 1.026834758
  x[Km57] = 0.637490056
  x[n57] = 3.584464176
  x[p58] = 0.000270488
  x[p59] = 0.001443889
  x[p60] = 0.002448164
  x[p61] = 3.50E-05
  x[KimF] = 0.019898797
  x[KexF] = 0.396950616
  x[p63] = 4.13E-05

  x[a] = 218.6276381
  x[Vn] = 0.22
  x[Vc] = 0.94

  x[EGF]= 0
  x[HRG]= 1

  return x