function Bit#(XLEN) fn_andn(Bit#(XLEN) rs1, Bit#(XLEN) rs2);
  return rs1 & ~rs2;
endfunction

function Bit#(XLEN) fn_orn(Bit#(XLEN) rs1, Bit#(XLEN) rs2);
  return rs1 | ~rs2;
endfunction

function Bit#(XLEN) fn_xnor(Bit#(XLEN) rs1, Bit#(XLEN) rs2);
  return ~(rs1 ^ rs2);
endfunction

function Bit#(XLEN) fn_cpop(Bit#(XLEN) rs1);
  //provisos(Bits#(Bit,szTD));
  Bit#(XLEN) bitcount = 0;
  /* valueof(or valueOf()) -  convert a numeric type into the corresponding 
  Integer value.
  fromInteger - Converts from an Integer type to any type defined in the
Literal type class */

  for (Integer i = 0 ; i < fromInteger(valueof(XLEN)) ; i = i+1)
    if(rs1[i] == 1) begin
      bitcount = bitcount +1;
    end

  return bitcount;
endfunction
