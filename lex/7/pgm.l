%{
#include<stdio.h>
#include<stdlib.h>  
%}

%%

"int"|"if"|"else"|"return"|"while" {printf("keywords :%s",yytext);}
[0-9]+ {printf("number :%s",yytext);}
[a-z|A-Z]{1} {printf("Identifier: %s\n",yytext);}
"="|"=="|"+"|"-"|"/"|"*" {printf("Operator: %s\n",yytext);}
";"|"," {printf("Delimiter: %s\n",yytext);}
[ \t\n] {}
. { printf("Unknown Character: %s\n",yytext);}   

%%

int main() {
    printf("Enter Source Code: \n");
    yylex();
    return 0;
}

int yywrap() {
    return 1;
}