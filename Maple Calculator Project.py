from math import *

def is_int(s):
    try:
        int(s)
        return True
    except ValueError:
        return False

    
def input_it(prompt):
    while True:
        stat = input(prompt)
        if is_int(stat) == True or stat == "nil":
            stat = int(stat)
            return stat
            break
        else:
            print ("That is not a number!\n")

def printerror():
    print ("Error in Value Inputted.  Please Try Again! \n")
        
    
   
while True:      
    choice = input_it("Choose what you want to calculate. 1,2,3, or 4.  \n1) Att vs Stat \n2) Att% vs Boss Dmg% \n3) Crit Dmg% vs Stat% \n4) Dpm increase for each point of Stat & Stat% / Att / Att% / Crit Dmg & Crit% / Dmg% / Boss Dmg% \n \n")
    if choice == 1:
        print ("\nEnsure there is 2 free grids in your Primary Stat and Att each in Legion, and also an unassigned 'A' character block (2 squares) before proceeding \n")
        while True:
            stat_b4 = input_it("Current Stat in Stat Window: ")
            range_b4 = input_it("Current Max Range in Stat Window: ")
            range_stat = input_it("Max Range AFTER placing the 'A' character block in your Primary Stat grid: ")
            print ("Remove the 'A' chracter block from your Primary Stat")
            range_att = input_it("Max Range AFTER placing the 'A' character block in ATT: ")
            if (range_att - range_b4) <=0 or (range_stat - range_b4) <=0 or stat_b4 <= 0 or range_b4 <= 0 or range_stat <= 0:
                printerror()
            else:
                ratio = (range_stat - range_b4)/(range_att - range_b4)/5
                print ("\n1 Att is equals to %.2f Stat \n" %(ratio))
                break


            
    elif choice == 2:
        while True:
            boss_dmg = input_it("\nBoss Dmg in stat window: ")
            boss_dmg += input_it("Dmg in stat window: ")
            total_att = input_it("Add up all sources of Att% (Weapon, Secondary, Emblem, Skills, Buffs): ")
            if (total_att+100) <= 100 or (total_att+100)<=100:
                printerror()
            else:
                ratio = (boss_dmg+100)/(total_att+100)
                print ("\n1%% Att is equals to %.2f%% Boss Dmg \n" %(ratio))
                break
            

        
    elif choice == 3:
        while True:
            print ("\nEnsure there is 2 free grids in your Primary Stat grid in Legion, and also an unassigned 'A' character block (2 squares) before proceeding \n")
            crit_dmg = input_it("Crit Dmg in Stat Window: ")
            stat_b4 = input_it("Current Stat in Stat Window: ")
            stat_aft = input_it("Stat in Stat Window AFTER placing the 'A' character block in your Primary Stat Grid")
            stat_per = (stat_aft - stat_b4)*10
            crit_dmg_total = crit_dmg + 35
            if crit_dmg_total <35 or stat_per <=0 or (stat_aft - stat_b4)<=0:
                printerror()
            else:
                ratio = stat_per/crit_dmg_total
                print("\n 1%% Crit Dmg is equals to %.2f%% Stat \n" %(ratio))
                break


            
        
    elif choice == 4:
        while True:
            print("\nPlease enter a number from 1 to 6 according to your choice. \n")
            choice2 = input_it("1) Stat & Stat% \n2) Att \n3) Att% \n4) Crit% & Crit Dmg% \n5) Dmg% \n6) Boss Dmg% \n or Press 7 to return \n \n")
            
            if choice2 == 1:
                while True:
                    print ("\nEnsure there is 2 free grids in your Primary Stat grid in Legion, and also an unassigned 'A' character block (2 squares) before proceeding \n")
                    stat_b4 = input_it("Current Stat in Stat Window: ")
                    stat_aft = input_it("Stat in Stat Window AFTER placing the 'A' character block in your Primary Stat grid: ")
                    stat_per = (stat_aft - stat_b4)*10
                    if stat_b4 <=0 or (stat_aft - stat_b4)<=0 or stat_per<=0:
                        printerror()
                    else:
                        stat_ratio = (1/stat_b4) * stat_per
                        per_ratio = 1/stat_per
                        print ("Your DPM increases by %.4f%% for every 1 Primary Stat (from sources scalable with %%stat) \n" %(stat_ratio))
                        print ("Your DPM increases by %.4f%% for every 1%% Stat \n" %(per_ratio))
                    break

                    

            elif choice2 == 2:
                while True:
                    print ("\nEnsure there is 2 free grids in your ATT grid in Legion, and also an unassigned 'A' character block (2 squares) before proceeding \n")
                    range_b4 = input_it("Current Max Range in Stat Window: ")
                    range_att = input_it("Max Range AFTER placing the 'A' character block in ATT: ")
                    if range_att <= 0 or range_b4 <= 0 or (range_att - range_b4) <=0:
                        printerror()
                    else:
                        ratio = (range_att/range_b4)/2
                        print ("Your DPM increases by %.4f%% for every 1 ATT \n" %(ratio))
                    break
                    
                

            elif choice2 == 3:
                while True:
                    att = input_it("\nAdd up all sources of ATT%(Weap, Secondary, Emblem, Skills, Buffs): ")
                    if att <=0:
                        printerror()
                    else:
                        ratio = (1/att)*100
                        print ("Your DPM increases by %.4f%% for every 1%% ATT \n" %(ratio))
                    break
                    
                    
                        

            elif choice2 == 4:
                while True:
                    x = 135+input_it("\nCrit Dmg as shown in Stat Window: ")
                    y = input_it("Crit Rate as shown in Stat Window: ")
                    if x<135 or y <= 0 or y>100:
                        print_error()
                    else:
                        z = (100-y)*100
                        dmg_ratio = (((x+1)*y+z)/((x)*y+z)-1)*100
                        print ("Your DPM increases by %.4f%% for 1%% additional Crit Dmg \n" %(dmg_ratio))
                        if 99<y<=100:
                            rate_ratio = ((100*x)/(y*x+z)-1)*100
                            print ("Your DPM increases by %.4f%% for 1%% additional Crit Rate \n" %(rate_ratio))
                        
                        else:
                            rate_ratio = ((((y+1)*x+(99-y)*100)/x*y+z)-1)*100
                            print ("Your DPM increases by %.4f%% for 1%% additional Crit Rate \n" %(rate_ratio))
                    break

                    

            elif choice2 == 5:
                while True:
                    dmg = input_it("\nDmg as shown in Stat Window: ")
                    boss_dmg = input_it("Boss Dmg as shown in Stat Window: ")
                    if dmg<0 or boss_dmg <0:
                        printerror()
                    else:
                        dmg_ratio = (1/dmg)*100
                        dmg_ratio2 = (1/(boss_dmg+dmg))*100
                        print("Your DMG increases by %.4f%% for 1%% additional DMG (Against normal mobs) \n" %(dmg_ratio))
                        print("Your DMG increase by %.4f%% for 1%% additional DMG (Against Bosses) \n" %(dmg_ratio2))
                    break
                        
            elif choice2 == 6:
                while True:
                    boss_dmg = input_it("\nBoss Dmg as shown in Stat Window: ")
                    dmg = 100 + input_it("Dmg as shown in Stat Window: ")
                    if dmg<100 or boss_dmg <0:
                        printerror()
                    else:
                        dmg_ratio = (1/(boss_dmg+dmg))*100
                        print("Your DMG increase by %.4f%% for 1%% additional DMG \n" %(dmg_ratio))
                    break
                        

            elif choice2 == 7:
                break
                

            else:
                print("\nPlease Enter a Number from 1 to 7 \n")
                
            
                

 
    else:
        print ("\nPlease Enter a Number from 1 to 4 \n")

        
    
'''crit_rate = input_it("Crit Rate: ")
#print(crit_rate)
crit_dmg = input_it("Crit Dmg (As shown in stat window): ")
#print(crit_dmg)
print ("(Remove 10 stat from Legion). %stat = Actual Stat lost * 10.  \nRmb not to remove a character with base primary stat on the card")
per_stat = input_it("%stat: ")
#print(per_stat)
total_stat = input_it("Total Stat (As shown in stat window): ")
#print(total_stat)


raw_stat = total_stat/per_stat*100
#print (raw_stat)'''

#------------------------------------------

'''stat:att ratio,
boss dmg : att % ratio
crit dmg% vs stat%
dpm increase for each point of stat/stat%/dmg/crit dmg/crit/attack%/att
total att/stat/crit%
'''






            
        
          
