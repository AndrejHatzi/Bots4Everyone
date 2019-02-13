#with open('2017_2018/Belenenses')
import os
to_exclude : list = ['equipaID.link', 'jogadores.jfo', 'stats']
files : list = os.listdir('2017_2018/Belenenses')
print('@r', len(files))
i : int
gm : int = 0;
gs : int = 0;
for i in range(len(files)):
    if files[i] not in to_exclude:
        path_to_player : str = ('2017_2018/Belenenses/{}'.format(files[i]))
        with open(path_to_player, 'r', encoding='utf-8') as f:
            info : list = f.readlines()
            info = info[0].split(',')[-1]
            try:
                jpp : str = files[i].replace('.jg', '.sts')
                sts_path : str = ('2017_2018/Belenenses/stats/{}'.format(jpp))
                with open(sts_path, 'r') as f:
                    line : str
                    for line in f:
                        #print(line)
                        sts : list = line.split(',')
                        gm += int(sts[0])
                        #print(gm)
                        gs += int(sts[-1])
                    rgm: float = float(int(info) / int(gm))
                    rgs:float = float(int(info) / int(gs))
                    aosnoventagm : float = 90/rgm
                    aosnoventags : float = 90/rgs
                    with open('equipa.precompiled', 'a') as f:
                        f.write(('{},{},{},{},{},{},{},{}\n').format(files[i], info.replace('\n', ''), gm, gs, rgm, rgs, aosnoventagm, aosnoventags))
            except:
                print('@erro', files[i])
        print(files[i], info.replace('\n', ''), gm, gs, '|', rgm, rgs, '|', aosnoventagm, aosnoventags)
        gm, gs = 0,0
    
            
        
        
