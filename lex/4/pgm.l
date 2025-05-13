%{
#include<stdio.h>
int i;    
%}

%%

[0-9]+ {i = atoi(yytext);
if(i%2==0)printf("even");
else printf("odd");}

%%

int yywrap(){
  return 0;
}
int main(){
  yylex();
  return 0;
}