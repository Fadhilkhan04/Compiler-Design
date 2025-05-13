%{
#include<stdio.h>
int positive=0;
int negative=0;
%}

%%
[-][0-9]+ {negative++; printf("negative number:%s\n",yytext);}
[0-9]+ {positive++; printf("postive number:%s\n,yytext);}
%%

int yywrap(){
  return 0;
}

int main(){
  yylex();
  printf("\n no of positive nos :%d",positive);
  printf("\n no of negative nos :%d",negative);
  return 0;
} 