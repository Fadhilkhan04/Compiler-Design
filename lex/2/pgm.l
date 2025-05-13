%{
#include<stdio.h>
#include<string.h>
%}

%%

[aA][a-zA-Z0-9]+ {printf("word : %s\n",yytext);}
[a-zA-Z0-9]+ {}

%%

int yywrap(){
  return 0;
}
int main(){
  yylex();
  return 0;
}