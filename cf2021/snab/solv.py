from Crypto.Util.number import *
from math import *

e = 65537
s = 518521484172073259043145502034694599512935443283076107003494840643504150663248402410462928864122818999731280619095755616648044687630285476363367234348295346345048643618601901838740100
n = 121789376487960809489253386587170686658768726657045553214623415992384832614485249137256874454267032401365173859563210814953487893574413409932117585950570225259024509903129746392143101
a = 14910
b = 1443061772954701335732136128869248910288995712185482317126411260349775148932784597588115548780067761993841192961205698418501468762734686695975550561598140253475710348439640002745286347562
c_list = [95844532553991737600355244654272099305361975575150371319709729091243030203575898742071987199800250922501746626433985253038713853151746857514762678605619742310839669559545627531098676, 42098262117872607180245376226279234844537189667792611290978137770131205295202393318329675438677406769928295941768074280915365884838027414974072838410934952571392616562898636004189303, 8604504123043858588289398284978073629384165878986588408956445422750740896636700840713408309772547146776823067482307495576552057400894861616123713400577813256614795674220942022738198, 66896916235028791010554130879834163456721897024453929564151545727202320039792487273512943832159287883050106923587075192390665897004465138382234040927275478139131450371794658563343368, 88176130128782413821390318550151008388570132120182664342566671328546119423517817326934034720909238554168653863093116429325532932401977519369212892117707167802400008407395125896733332, 42250039274640778630603717605163827961176577828564055370588929192401015587247485151024369147022833032549004175634147831360114651662490704138925606397505368573040950634048151235675964, 106267843822546752528780879737401351948170741446817769684516569656816005147897267321452764634553751488085440938706773625287154372645991244141121226180609731226228509942129690482744498, 7344462713592491879813960159075800353984094813742489003735150623847056840460595091048879286634691169764793649426176975158414555454778075430233699780146900520609629142406422725693811, 68155732896092345896827379516624133280166986984023541993085330906321960888421556683672078055376548346464764100036149614632795220030187229733989823788323988946361921828069707823065198, 2456638129741631242062051214133833843357605035108383884677777076160879939756985403557604264648903511528401478876871578775440101482814072714355366084122429853207060638683606389504551, 99671982271645788903414016384550975165361965345980177928115018027271173062935625698434769263846972984813377601618481025600240081090732166957299336765744471217496851539810214590361856]

sroot = sqrt(s)

print(sroot)
"""
n = p*(sroot-p)
p = n/(sroot-p)
"""