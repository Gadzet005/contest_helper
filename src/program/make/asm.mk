COMPILER := nasm
FLAGS := -DUNIX -f elf -Werror

compile:
	$(COMPILER) $(FLAGS) $(DIR)/$(FILE) -o $(DIR)/$(COMPILED_FILE)
run:
	$(DIR)/$(COMPILED_FILE) > $(DIR)/$(OUTPUT_FILE)
clear:
	rm $(DIR)/$(COMPILED_FILE) $(DIR)/$(OUTPUT_FILE)
