from lambdas import string_to_lambda_expression as l

PAIR = l("&&&2!3!1")
CLASSIC_FIRST = l("&(&&2)!1")
CLASSIC_SECOND = l("&(&&1)!1")
POLISH_FIRST, POLISH_SECOND = CLASSIC_SECOND, CLASSIC_FIRST
FIRST, SECOND = POLISH_FIRST, POLISH_SECOND