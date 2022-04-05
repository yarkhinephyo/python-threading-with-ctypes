FILENAMES = prime prime_pthread

compile:
	for filename in $(FILENAMES) ; do \
		gcc -c -fPIC $$filename.c -o $$filename.o && \
		gcc $$filename.o -shared -o lib$$filename.so; \
	done

clean:
	for filename in $(FILENAMES) ; do \
		rm lib$$filename.so && rm $$filename.o; \
	done