%{
int wc=0,lc=0,ch=0;
%}

%%
[\n] {lc++;ch+=yyleng;}
[^\t\n]+ {wc++;ch+=yyleng;}
%%

int yywrap(){
  return 1;
}
int main(){
  yylex();
  printf("line count : %d",lc);
  printf("word count : %d",wc);
  printf("char count : %d",ch);
  return 0;
}