COMPILER := gcc
FLAGS := 	-O2 -Wall -Werror -Wformat-security -Wignored-qualifiers -Winit-self -Wswitch-default \
			-Wfloat-equal -Wpointer-arith -Wtype-limits -Wempty-body -Wno-logical-op \
			-Wstrict-prototypes -Wold-style-declaration -Wold-style-definition \
			-Wmissing-parameter-type -Wmissing-field-initializers -Wnested-externs \
			-Wno-pointer-sign -Wno-unused-result -std=gnu99 -lm

compile:
	$(COMPILER) $(FLAGS) $(DIR)/$(FILE) -o $(DIR)/$(COMPILED_FILE)
run:
	$(DIR)/$(COMPILED_FILE) > $(DIR)/$(OUTPUT_FILE)
format:
	clang-format --style=file:$(FORMAT_CONFIG) $(DIR)/$(FILE) > $(DIR)/$(FORMATTED_FILE)
clear:
	rm $(DIR)/$(COMPILED_FILE) $(DIR)/$(OUTPUT_FILE)
