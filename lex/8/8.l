%{
#include "8.tab.h"  
%}

%%

hello { return hello;}
bye { return bye;}
.|\n {return other;}

%%

int yywrap(){
  return 1;
}