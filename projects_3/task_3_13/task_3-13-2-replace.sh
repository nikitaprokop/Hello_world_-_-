#!/bin/bash
cat > sequences.txt << 'SEQ'
>seq1 ATGCGTACGTTAG
>seq2 GGCATGCTAGCTA
>seq3 TTAGCGATCGTAC
>seq4 CCGTATGCTAGGA
SEQ
echo "Исходный файл sequences.txt"
cat sequences.txt
echo ""
sed -i 's/ /\t/g' sequences.txt
echo "=== Файл после замены (пробелы → табуляция) ==="
cat sequences.txt
