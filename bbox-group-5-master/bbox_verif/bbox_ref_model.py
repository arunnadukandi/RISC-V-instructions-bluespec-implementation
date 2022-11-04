#See LICENSE.iitm for license details
'''

Author   : Santhosh Pavan
Email id : santhosh@mindgrovetech.in
Details  : This file consists reference model which is used in verifying the bbox design (DUT).

--------------------------------------------------------------------------------------------------
'''
'''
TODO:
Task Description: Add logic for all instructions. One instruction is implemented as an example. 
                  Note - The value of instr (ANDN) is a temp value, it needed to be changed according to spec.

Note - if instr has single operand, take rs1 as an operand
'''

#Reference model
def bbox_rm(instr, rs1, rs2, XLEN):
    
    if instr == 1:
        res = rs1 & ~rs2 
        
        valid = '1'
    ## logic for all other instr starts 

    elif instr == 2:
        res = rs1 | (~rs2 + 2**64 ) 
        
        valid = '1'
    elif instr == 3:
        res = ~(rs1 ^ rs2) + 2**64
        #print(bin(res), bin(rs1) , bin(~rs2))
        valid = '1'

    elif instr == 4:
        bitcount = 0
        print("type ",type(rs1))
        #bin_rs1 = bin(rs1)
        bin_rs1 = ('{:64b}'.format(rs1)) # rs1 of type int , converting it to 64 bit binary
        # print(type(bin_rs1))
        # print(len(bin_rs1))
        # print("bin_rs1",bin_rs1)
        # print(bin_rs1[-1])
        for i in reversed(range(XLEN)):
            print(bin_rs1[i])
            if(bin_rs1[i] == '1'):
                # print(bin_rs1[i])
                bitcount+=1
            elif(bin_rs1[i] == " "):
                break
        res = bitcount  
        valid = '1'
        print("bitcount",bitcount)
        print("res ",type(res))

    ## logic for all other instr ends
    else:
        res = 0
        valid = '0'

    if XLEN == 32:
        result = '{:032b}'.format(res)
    elif XLEN == 64:
        result = '{:064b}'.format(res)
        print("R type",type(result))
    return valid+result

