%{
#include "10.tab.h"
%}

%%

[0-9]+     { yylval = atoi(yytext); return NUMBER; }
[+\-*/()]  { return yytext[0]; }
[\t ]      { /* ignore whitespace */ }
\n         { return '\n';}
.          { return yytext[0]; }

%%

int yywrap() { return 1; }
