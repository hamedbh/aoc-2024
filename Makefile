.PHONY: all all_answer_files update clean lint format requirements environment test help

PROJECT_DIR := $(shell dirname $(realpath $(lastword $(MAKEFILE_LIST))))

###############################################################################
# COMMANDS                                                                    #
###############################################################################

## Update the data inputs and Python scripts
update:
	./update_aoc

SOURCE_DATA_FILES=$(wildcard data/day_*.txt)
ANSWER_FILES=$(patsubst data/day_%.txt,answers/day_%.txt,$(SOURCE_DATA_FILES))
all_answer_files: $(ANSWER_FILES)

answers/day_%.txt: aoc2024/day_%.py data/day_%.txt
	uv run python3 -m aoc2024.day_$* > $@

## Build the answers into the README
README.md: $(ANSWER_FILES)
	echo "# Advent of Code 2024" > $@
	echo "" >> $@
	echo "I'm trying this in Python for the first time. Usually I get distracted by life at some point, let's see how far I get this year." >> $@
	echo "" >> $@
	cat $^ >> $@

## Delete all compiled Python files
clean:
	find . -type f -name "*.py[co]" -delete
	find . -type d -name "__pycache__" -delete

## Lint using ruff
lint:
	uv run ruff check

## Format source code with ruff
format:
	uv run ruff format

## Install required packages, including local/project source code	
requirements:
	uv lock
	uv sync --all-extras

###############################################################################
# Self Documenting Commands                                                   #
###############################################################################

.DEFAULT_GOAL := help

# Inspired by 
# <http://marmelab.com/blog/2016/02/29/auto-documented-makefile.html>
# sed script explained:
# /^##/:
# 	* save line in hold space
# 	* purge line
# 	* Loop:
# 		* append newline + line to hold space
# 		* go to next line
# 		* if line starts with doc comment, strip comment character off and loop
# 	* remove target prerequisites
# 	* append hold space (+ newline) to line
# 	* replace newline plus comments by `---`
# 	* print line
# Separate expressions are necessary because labels cannot be delimited by
# semicolon; see <http://stackoverflow.com/a/11799865/1968>
help:
	@echo "$$(tput bold)Available rules:$$(tput sgr0)"
	@echo
	@sed -n -e "/^## / { \
		h; \
		s/.*//; \
		:doc" \
		-e "H; \
		n; \
		s/^## //; \
		t doc" \
		-e "s/:.*//; \
		G; \
		s/\\n## /---/; \
		s/\\n/ /g; \
		p; \
	}" ${MAKEFILE_LIST} \
	| awk -F '---' \
		-v ncol=$$(tput cols) \
		-v indent=19 \
		-v col_on="$$(tput setaf 6)" \
		-v col_off="$$(tput sgr0)" \
	'{ \
		printf "%s%*s%s ", col_on, -indent, $$1, col_off; \
		n = split($$2, words, " "); \
		line_length = ncol - indent; \
		for (i = 1; i <= n; i++) { \
			line_length -= length(words[i]) + 1; \
			if (line_length <= 0) { \
				line_length = ncol - indent - length(words[i]) - 1; \
				printf "\n%*s ", -indent, " "; \
			} \
			printf "%s ", words[i]; \
		} \
		printf "\n"; \
	}' \
	| more $(shell test $(shell uname) = Darwin && echo '--no-init --raw-control-chars')

