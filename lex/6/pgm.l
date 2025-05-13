%{
#include<stdio.h>
int line=1;  
%}

%%
[6-9][0-9]{9} {if(line==1) printf("valid mobile");line++;}

[a-zA-Z0-9]+\@[a-zA-Z]+\.com {if(line==2) printf("valid email");line++;}

[0-3]{1}[0-9]{1}[-/][0-1]{1}[0-9]{1}[-/][0-9]{4} {if(line==3) printf("valid date"); return 0;}


. {printf("invalid");return 0;}


%%

int main() {
    printf("Enter Mobile Number (In First Line) & Email (In Second Line) % Date (In Third Line): \n");
    yylex();
    return 0;
}

int yywrap() {
    return 1;
}