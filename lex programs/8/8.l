%{
#include "8.tab.h"
%}

%%
hello   { return HELLO; }
bye     { return BYE; }
.|\n    { return OTHER; }
%%

int yywrap() {
    return 1;
}
