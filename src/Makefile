JSLINT = jslint -process
SRC = .

all:	gae test

gae:
	python lib/web/template.py --compile templates

jslint:
	@find $(SRC) -name "*.js" -not -name "jQuery.*.js" -exec $(JSLINT) {} \;

test:	jslint

