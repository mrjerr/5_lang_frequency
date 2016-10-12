#5_lang_frequency task

**Description**
--------
Calculates and displays a list of the most frequently used words in a text file. The default is 10 words

**Examples**
--------
```sh
$ ./lang_frequency.py

No such file or directory, check path
usage:             ./lang_frequency.py [-h] [-file FILEPATH] [-n NUMBER]
```
```sh
$ ./lang_frequency.py -file Vojna_i_mir.Tom1.txt
10 most_frequent_words:
                        и: 4915
                        в: 2349
                       не: 1972
                       он: 1809
                      что: 1780
                       на: 1617
                        с: 1387
                      как: 1078
                        к: 871
                        я: 862
```
```sh
$ ./lang_frequency.py -file Vojna_i_mir.Tom1.txt -n15
15 most_frequent_words:
                        и: 4915
                        в: 2349
                       не: 1972
                       он: 1809
                      что: 1780
                       на: 1617
                        с: 1387
                      как: 1078
                        к: 871
                        я: 862
                      его: 848
                       то: 780
                    князь: 625
                       но: 602
                      это: 584
```

