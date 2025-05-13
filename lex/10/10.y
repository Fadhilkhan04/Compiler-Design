%{
#include <stdio.h>
#include <stdlib.h>
void yyerror(const char *s);
int yylex(void);
%}

%token NUMBER

%%

calc:
    expr '\n'   { printf("= %d\n", $1); }
;

expr:
      expr '+' term   { $$ = $1 + $3; }
    | expr '-' term   { $$ = $1 - $3; }
    | term
;

term:
      term '*' factor { $$ = $1 * $3; }
    | term '/' factor { $$ = $1 / $3; }
    | factor
;

factor:
      '(' expr ')'    { $$ = $2; }
    | NUMBER
;

%%

int main() {
    printf("Enter an expression (e.g., 3+4*2):\n");
    yyparse();
    return 0;
}

void yyerror(const char *s) {
    fprintf(stderr, "Error: %s\n", s);
}
